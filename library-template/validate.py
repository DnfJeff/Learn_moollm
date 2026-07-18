#!/usr/bin/env python3
"""Validate the Legible Library: card-stack conformance, ledger sync, index drift.

Postel's law is about protocol peers. It does not mean be liberal with your own filing.
Be liberal in what you accept into inbox/; be strict about what you filed yourself.

Checks:
  - Free channel (AGENT.md) is prepaid and small
  - Session state (.agent/) is present and sane
  - Host drivers declare a fallback for every capability they lack
  - Capabilities: index count matches, each unit has GLANCE+CARD
  - Library: every card-stack directory is complete (GLANCE/CARD/SKILL/README),
    every unit's SKILL.md carries provenance frontmatter, every unit is registered
    in its section ledger, and the catalog + ontology + change log exist

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

REQUIRED_TIERS = ["GLANCE.yml", "CARD.yml"]
CARD_STACK = ["GLANCE.yml", "CARD.yml", "SKILL.md", "README.md"]
SKILL_FRONTMATTER = ["status", "created", "provenance"]

BUDGETS = {
    "GLANCE.yml": 2500,    # ~600 tokens  — "is this relevant?"
    "CARD.yml": 8000,      # ~2,000       — "where does it route / how do I use it?"
    "SKILL.md": 40000,     # ~10,000      — "the knowledge / the ledger"
    "README.md": 20000,    # ~5,000       — "why is it like this?"
}
FREE_CHANNEL_BUDGET = 8000  # ~2,000 tokens, taxed every call


class Report:
    def __init__(self):
        self.errors, self.warnings, self.notes = [], [], []

    def error(self, m): self.errors.append(m)
    def warn(self, m): self.warnings.append(m)
    def note(self, m): self.notes.append(m)

    def print(self, strict=False):
        for m in self.notes:    print(f"  note  {m}")
        for m in self.warnings: print(f"  WARN  {m}")
        for m in self.errors:   print(f"  ERROR {m}")
        n_err = len(self.errors) + (len(self.warnings) if strict else 0)
        print()
        print(f"{len(self.errors)} errors, {len(self.warnings)} warnings")
        return n_err


def check_yaml(path, rep):
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


def read_frontmatter(path, rep):
    """Parse leading --- ... --- YAML block of a Markdown file. None if absent."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as e:
        rep.error(f"{path}: unreadable - {e}")
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        rep.error(f"{path}: invalid frontmatter YAML")
        return None


def rel(root, path):
    return os.path.relpath(path, root)


# ---- workspace-level checks (shared with the base template) -----------------

def validate_free_channel(root, rep):
    for name in ("AGENT.md", "CLAUDE.md", ".cursorrules"):
        p = os.path.join(root, name)
        if not os.path.exists(p):
            continue
        size = os.path.getsize(p)
        if size > FREE_CHANNEL_BUDGET:
            rep.warn(f"{name}: {size}B over {FREE_CHANNEL_BUDGET}B "
                     f"(~{size//4} tokens taxed every call) - cut it")
        else:
            rep.note(f"{name}: {size}B (~{size//4} tokens/session)")


def validate_state(root, rep):
    d = os.path.join(root, ".agent")
    if not os.path.isdir(d):
        rep.warn(".agent/: missing - no externalized session state")
        return
    ws = os.path.join(d, "working-set.yml")
    if os.path.exists(ws):
        if check_yaml(ws, rep) is not None:
            lines = sum(1 for _ in open(ws, encoding="utf-8"))
            if lines > 30:
                rep.warn(f".agent/working-set.yml: {lines} lines - that's a filing "
                         f"cabinet, not a working set")
    gi = os.path.join(root, ".gitignore")
    if os.path.exists(gi) and ".agent" not in open(gi, encoding="utf-8").read():
        rep.warn(".gitignore: does not ignore .agent/ - session state is not source")


def validate_drivers(root, rep):
    d = os.path.join(root, "policy", "drivers")
    if not os.path.isdir(d):
        return
    names = [f for f in os.listdir(d) if f.endswith(".yml")]
    if "generic.yml" not in names:
        rep.warn("policy/drivers/: no generic.yml - nothing handles an unknown host")
    for f in names:
        data = check_yaml(os.path.join(d, f), rep)
        if not data:
            continue
        if "driver" not in data:
            rep.error(f"policy/drivers/{f}: no 'driver' block")
        caps = data.get("capabilities", {}) or {}
        fallbacks = data.get("fallbacks", {}) or {}
        for cap, val in caps.items():
            if val is False and cap not in fallbacks:
                rep.warn(f"policy/drivers/{f}: '{cap}' unsupported with no fallback")


def validate_capabilities(root, rep):
    capdir = os.path.join(root, "capabilities")
    if not os.path.isdir(capdir):
        return
    idx = os.path.join(capdir, "INDEX.yml")
    listed = set()
    if os.path.exists(idx):
        data = check_yaml(idx, rep) or {}
        for group in data.values():
            if isinstance(group, list):
                for e in group:
                    if isinstance(e, dict) and "id" in e:
                        listed.add(e["id"])
        actual = {d for d in os.listdir(capdir)
                  if os.path.isdir(os.path.join(capdir, d)) and not d.startswith(".")}
        for miss in sorted(actual - listed):
            rep.error(f"capabilities/INDEX.yml: '{miss}' exists but is not indexed")
        for ghost in sorted(listed - actual):
            rep.error(f"capabilities/INDEX.yml: '{ghost}' indexed but has no directory")
        if "count" in data and data["count"] != len(actual):
            rep.error(f"capabilities/INDEX.yml: count says {data['count']}, found {len(actual)}")
    else:
        rep.warn("capabilities/INDEX.yml: missing - the entry point")
    for name in sorted(os.listdir(capdir)):
        d = os.path.join(capdir, name)
        if not os.path.isdir(d) or name.startswith("."):
            continue
        for tier in REQUIRED_TIERS:
            if not os.path.exists(os.path.join(d, tier)):
                rep.error(f"capabilities/{name}: missing {tier}")


# ---- library-level checks (the new layer) -----------------------------------

def is_card_unit(d):
    return os.path.exists(os.path.join(d, "CARD.yml"))


def skipped(path):
    """Skip dotfiles and _templates / _-prefixed scaffolding anywhere in the path."""
    return any(part.startswith((".", "_")) for part in path.split(os.sep))


def validate_library(root, rep):
    lib = os.path.join(root, "library")
    if not os.path.isdir(lib):
        rep.note("no library/ - nothing to catalog yet")
        return

    # Finding aids that must exist for the collection to be navigable.
    for req, kind in [("INDEX.md", "error"), ("meta/ontology.md", "error"),
                      ("meta/structure-log.md", "warn")]:
        p = os.path.join(lib, req)
        if not os.path.exists(p):
            (rep.error if kind == "error" else rep.warn)(f"library/{req}: missing")
    idx = os.path.join(lib, "INDEX.md")
    if os.path.exists(idx) and "reading protocol" not in open(idx, encoding="utf-8").read().lower():
        rep.warn("library/INDEX.md: no reading protocol printed at top")

    # Every card-stack directory must be complete, and its SKILL.md must carry provenance.
    units = 0
    for cur, dirs, files in os.walk(lib):
        dirs[:] = [d for d in dirs if not d.startswith((".", "_"))]
        if skipped(rel(root, cur)) or not is_card_unit(cur):
            continue
        units += 1
        name = rel(lib, cur)
        for tier in CARD_STACK:
            if not os.path.exists(os.path.join(cur, tier)):
                rep.error(f"library/{name}: card stack missing {tier}")
        for y in ("GLANCE.yml", "CARD.yml"):
            yp = os.path.join(cur, y)
            if os.path.exists(yp):
                check_yaml(yp, rep)
        skill = os.path.join(cur, "SKILL.md")
        if os.path.exists(skill):
            fm = read_frontmatter(skill, rep)
            if fm is None:
                rep.error(f"library/{name}/SKILL.md: no frontmatter "
                          f"(need {', '.join(SKILL_FRONTMATTER)})")
            else:
                for field in SKILL_FRONTMATTER:
                    if field not in fm:
                        rep.warn(f"library/{name}/SKILL.md: frontmatter missing '{field}'")
        for tier, budget in BUDGETS.items():
            tp = os.path.join(cur, tier)
            if os.path.exists(tp) and os.path.getsize(tp) > budget:
                rep.warn(f"library/{name}/{tier}: over {budget}B budget "
                         f"- probably answering the next tier's question")

    # Ledger sync: a unit nested under a section must appear in that section's SKILL.md.
    domains = os.path.join(lib, "domains")
    if os.path.isdir(domains):
        for section in sorted(os.listdir(domains)):
            sdir = os.path.join(domains, section)
            if not os.path.isdir(sdir) or section.startswith((".", "_")) or not is_card_unit(sdir):
                continue
            ledger = ""
            sp = os.path.join(sdir, "SKILL.md")
            if os.path.exists(sp):
                ledger = open(sp, encoding="utf-8").read()
            for child in sorted(os.listdir(sdir)):
                cdir = os.path.join(sdir, child)
                if (os.path.isdir(cdir) and not child.startswith((".", "_"))
                        and is_card_unit(cdir) and child not in ledger):
                    rep.warn(f"library/domains/{section}: unit '{child}' not in the "
                             f"section ledger (SKILL.md) - a ghost unit, invisible to readers")

    rep.note(f"{units} card-stack units in the library")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    root = os.path.abspath(args[0] if args else ".")

    print(f"validating {root}\n")
    rep = Report()
    validate_free_channel(root, rep)
    validate_state(root, rep)
    validate_drivers(root, rep)
    validate_capabilities(root, rep)
    validate_library(root, rep)
    sys.exit(1 if rep.print(strict) else 0)


if __name__ == "__main__":
    main()
