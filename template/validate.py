#!/usr/bin/env python3
"""Validate the capability library: YAML validity, pyramid conformance, index drift.

This is the piece MOOLLM never built, and the reason its .cursorrules has been invalid
YAML with two standing constraints silently dropped, and its index is 8 skills out of sync.

Postel's law is about protocol peers. It does not mean be liberal with your own config.
Be liberal in what you accept from users; be strict about what you wrote yourself.

Usage:
    python validate.py            # validate ./
    python validate.py --strict   # warnings become errors
    python validate.py <path>

Exit code 0 = clean, 1 = errors. Wire it into CI.
"""

import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml:  pip install pyyaml")

# Tiers, cheapest first. Each answers a different question; each is a rewrite, not a
# truncation of the one below it.
REQUIRED_TIERS = ["GLANCE.yml", "CARD.yml"]
OPTIONAL_TIERS = ["SKILL.md", "README.md"]

# Soft ceilings. A tier that outgrows its budget has stopped answering its own question
# and started answering the next one down.
BUDGETS = {
    "GLANCE.yml": 2500,    # ~600 tokens  — "is this relevant?"
    "CARD.yml": 8000,      # ~2,000       — "how do I call it?"
    "SKILL.md": 40000,     # ~10,000      — "how does it work?"
    "README.md": 20000,    # ~5,000       — "why is it like this?"
}

FREE_CHANNEL_BUDGET = 8000  # ~2,000 tokens. Everything here is taxed on every call.


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.notes = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def print(self, strict=False):
        for m in self.notes:
            print(f"  note  {m}")
        for m in self.warnings:
            print(f"  WARN  {m}")
        for m in self.errors:
            print(f"  ERROR {m}")
        n_err = len(self.errors) + (len(self.warnings) if strict else 0)
        print()
        print(f"{len(self.errors)} errors, {len(self.warnings)} warnings")
        return n_err


def check_yaml(path, rep):
    """Every YAML file we authored must actually parse. This is the check MOOLLM lacks."""
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        line = getattr(getattr(e, "problem_mark", None), "line", None)
        where = f" (line {line + 1})" if line is not None else ""
        rep.error(f"{path}: invalid YAML{where}")
        return None
    except OSError as e:
        rep.error(f"{path}: unreadable - {e}")
        return None


def validate_capability(root, name, rep):
    d = os.path.join(root, "capabilities", name)

    for tier in REQUIRED_TIERS:
        p = os.path.join(d, tier)
        if not os.path.exists(p):
            rep.error(f"capabilities/{name}: missing {tier}")
            continue
        if tier.endswith(".yml"):
            data = check_yaml(p, rep)
            if data is None:
                continue
            if tier == "GLANCE.yml":
                for field in ("what", "key_insight"):
                    if field not in data:
                        rep.warn(f"capabilities/{name}/GLANCE.yml: no '{field}' - "
                                 f"a glance without one is a truncation, not a rewrite")

    # Tier ordering: you cannot have a deeper tier without the shallower one above it.
    # That rule is what stops the ladder collapsing into "just read SKILL.md".
    for i, tier in enumerate(OPTIONAL_TIERS):
        if os.path.exists(os.path.join(d, tier)):
            above = (REQUIRED_TIERS + OPTIONAL_TIERS)[: len(REQUIRED_TIERS) + i]
            for a in above:
                if not os.path.exists(os.path.join(d, a)):
                    rep.error(f"capabilities/{name}: has {tier} but no {a} "
                              f"- every tier needs the tier above it")

    for tier, budget in BUDGETS.items():
        p = os.path.join(d, tier)
        if os.path.exists(p):
            size = os.path.getsize(p)
            if size > budget:
                rep.warn(f"capabilities/{name}/{tier}: {size}B over {budget}B budget "
                         f"- probably answering the next tier's question")


def validate_index(root, rep):
    p = os.path.join(root, "capabilities", "INDEX.yml")
    if not os.path.exists(p):
        rep.error("capabilities/INDEX.yml: missing - this is the entry point")
        return

    data = check_yaml(p, rep)
    if not data:
        return

    listed = set()
    for group in data.values():
        if isinstance(group, list):
            for entry in group:
                if isinstance(entry, dict) and "id" in entry:
                    listed.add(entry["id"])

    capdir = os.path.join(root, "capabilities")
    actual = {
        d for d in os.listdir(capdir)
        if os.path.isdir(os.path.join(capdir, d)) and not d.startswith(".")
    }

    # This is the drift MOOLLM has: INDEX.yml says 133, there are 141 directories.
    for missing in sorted(actual - listed):
        rep.error(f"INDEX.yml: '{missing}' exists but is not indexed - invisible to the agent")
    for ghost in sorted(listed - actual):
        rep.error(f"INDEX.yml: '{ghost}' is indexed but has no directory")

    if "count" in data and data["count"] != len(actual):
        rep.error(f"INDEX.yml: count says {data['count']}, found {len(actual)}")

    rep.note(f"{len(actual)} capabilities indexed")


def validate_free_channel(root, rep):
    """The free channel is prepaid but small. Everything in it is taxed every call."""
    for name in ("AGENT.md", "CLAUDE.md", ".cursorrules"):
        p = os.path.join(root, name)
        if not os.path.exists(p):
            continue
        size = os.path.getsize(p)
        if size > FREE_CHANNEL_BUDGET:
            rep.warn(f"{name}: {size}B over {FREE_CHANNEL_BUDGET}B "
                     f"(~{size//4} tokens taxed on every call) - cut it")
        else:
            rep.note(f"{name}: {size}B (~{size//4} tokens/session)")
        # .cursorrules is YAML-ish; CLAUDE.md/AGENT.md are markdown. Only parse the former.
        if name == ".cursorrules":
            check_yaml(p, rep)


def validate_drivers(root, rep):
    d = os.path.join(root, "policy", "drivers")
    if not os.path.isdir(d):
        return
    names = [f for f in os.listdir(d) if f.endswith(".yml")]
    if not names:
        return

    if "generic.yml" not in names:
        rep.warn("policy/drivers/: no generic.yml - nothing handles an unknown host")

    for f in names:
        data = check_yaml(os.path.join(d, f), rep)
        if not data:
            continue
        if "driver" not in data:
            rep.error(f"policy/drivers/{f}: no 'driver' block")
        caps = data.get("capabilities", {})
        fallbacks = data.get("fallbacks", {})
        # A capability you lack without a declared fallback is a crash waiting for the
        # right host. The fallback table IS graceful degradation.
        for cap, val in caps.items():
            if val is False and cap not in fallbacks:
                rep.warn(f"policy/drivers/{f}: '{cap}' unsupported with no fallback")

    if len(names) == 1:
        rep.note("only one driver - the driver layer costs more than it gives until "
                 "you have a second host")


def validate_state(root, rep):
    d = os.path.join(root, ".agent")
    if not os.path.isdir(d):
        rep.warn(".agent/: missing - no externalized state")
        return

    ws = os.path.join(d, "working-set.yml")
    if os.path.exists(ws):
        data = check_yaml(ws, rep)
        if data is not None:
            lines = sum(1 for _ in open(ws, encoding="utf-8"))
            if lines > 30:
                rep.warn(f".agent/working-set.yml: {lines} lines - that's a filing "
                         f"cabinet, not a working set")

    hot = os.path.join(d, "hot.yml")
    if os.path.exists(hot):
        data = check_yaml(hot, rep)
        if isinstance(data, dict):
            for entry in data.get("keep", []) or []:
                if isinstance(entry, dict) and "why" not in entry:
                    rep.warn(f".agent/hot.yml: '{entry.get('path','?')}' has no 'why' "
                             f"- it will become permanent by inertia")

    gi = os.path.join(root, ".gitignore")
    if os.path.exists(gi):
        if ".agent" not in open(gi, encoding="utf-8").read():
            rep.warn(".gitignore: does not ignore .agent/ - runtime state is not source")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    root = os.path.abspath(args[0] if args else ".")

    print(f"validating {root}\n")
    rep = Report()

    validate_free_channel(root, rep)
    validate_state(root, rep)
    validate_drivers(root, rep)

    capdir = os.path.join(root, "capabilities")
    if os.path.isdir(capdir):
        validate_index(root, rep)
        for name in sorted(os.listdir(capdir)):
            if os.path.isdir(os.path.join(capdir, name)) and not name.startswith("."):
                validate_capability(root, name, rep)
    else:
        rep.note("no capabilities/ - fine below ~10 capabilities; the ladder is overhead")

    sys.exit(1 if rep.print(strict) else 0)


if __name__ == "__main__":
    main()
