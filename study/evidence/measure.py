#!/usr/bin/env python3
"""Measure the MOOLLM corpus: pyramid conformance, token economics, index drift.

Read-only. Never writes to the moollm tree.

Usage:
    python measure.py [path-to-moollm]     # defaults to ../../moollm
"""

import os
import statistics
import sys

# Rough bytes-per-token for English prose + YAML. Real tokenizers vary 3.5-4.5;
# every figure derived from this is an estimate, and labelled as one.
BYTES_PER_TOKEN = 4

TIERS = ["GLANCE.yml", "CARD.yml", "SKILL.md", "README.md"]


def skill_dirs(skills_root):
    return sorted(
        d for d in os.listdir(skills_root)
        if os.path.isdir(os.path.join(skills_root, d))
    )


def measure(root):
    skills_root = os.path.join(root, "skills")
    if not os.path.isdir(skills_root):
        sys.exit(f"no skills/ under {root}")

    dirs = skill_dirs(skills_root)
    sizes = {t: [] for t in TIERS}
    missing = {t: [] for t in TIERS}

    for d in dirs:
        for t in TIERS:
            p = os.path.join(skills_root, d, t)
            if os.path.exists(p):
                sizes[t].append(os.path.getsize(p))
            else:
                missing[t].append(d)

    print(f"skill directories: {len(dirs)}\n")

    print("PYRAMID CONFORMANCE")
    for t in TIERS:
        n = len(sizes[t])
        print(f"  {t:<12} {n:>4}/{len(dirs)}  missing: {', '.join(missing[t]) or '-'}")
    full = sum(
        1 for d in dirs
        if all(os.path.exists(os.path.join(skills_root, d, t)) for t in TIERS)
    )
    print(f"  full 4-tier pyramid: {full}/{len(dirs)}\n")

    print("TOKEN ECONOMICS (estimated)")
    hdr = f"  {'tier':<12}{'n':>5}{'total KB':>10}{'mean B':>9}{'median B':>10}{'~tokens':>11}"
    print(hdr)
    for t in TIERS:
        v = sizes[t]
        print(
            f"  {t:<12}{len(v):>5}{sum(v)/1024:>10.0f}"
            f"{statistics.mean(v):>9.0f}{statistics.median(v):>10.0f}"
            f"{sum(v)/BYTES_PER_TOKEN:>11,.0f}"
        )

    total = sum(sum(v) for v in sizes.values())
    glance = sum(sizes["GLANCE.yml"])
    print(f"\n  entire skill corpus : {total/1024:>7.0f} KB  ~{total/BYTES_PER_TOKEN:>9,.0f} tokens")
    print(f"  GLANCE-only sweep   : {glance/1024:>7.0f} KB  ~{glance/BYTES_PER_TOKEN:>9,.0f} tokens")
    print(f"  compression ratio   : {total/glance:>7.1f}x")

    idx = os.path.join(skills_root, "INDEX.yml")
    if os.path.exists(idx):
        b = os.path.getsize(idx)
        print(f"  INDEX.yml           : {b/1024:>7.1f} KB  ~{b/BYTES_PER_TOKEN:>9,.0f} tokens"
              f"  ({total/b:.0f}x smaller than corpus)")

    # Cost of loading N skills at full depth vs the whole corpus.
    per_skill = total / len(dirs)
    print("\n  cost of full-depth loading:")
    for n in (1, 3, 5, 10):
        c = per_skill * n
        print(f"    {n:>2} skills ~{c/BYTES_PER_TOKEN:>7,.0f} tokens "
              f"({100*c/total:>4.1f}% of corpus)")

    print("\nINDEX DRIFT")
    if os.path.exists(idx):
        import re
        txt = open(idx, encoding="utf-8").read()
        m = re.search(r"skill_count:\s*(\d+)", txt)
        if m:
            claimed = int(m.group(1))
            print(f"  INDEX.yml skill_count : {claimed}")
            print(f"  actual directories    : {len(dirs)}")
            print(f"  drift                 : {len(dirs)-claimed:+d}")

    print("\nBOOT ARTIFACT VALIDITY")
    cr = os.path.join(root, ".cursorrules")
    if os.path.exists(cr):
        try:
            import yaml
            yaml.safe_load(open(cr, encoding="utf-8"))
            print("  .cursorrules parses as YAML: yes")
        except ImportError:
            print("  .cursorrules: pyyaml not installed, skipped")
        except Exception as e:
            first = str(e).strip().splitlines()[-1]
            print(f"  .cursorrules parses as YAML: NO -> {first}")
            print("  (works anyway: an LLM reads it, not a parser)")


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "moollm"
    )
    measure(os.path.abspath(root))
