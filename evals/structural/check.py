#!/usr/bin/env python3
"""Structural invariant checks for the zhizhi skills.

These are the deterministic layer of the eval suite: cross-file invariants the
three skills rely on to hand off to each other. They run in seconds with no
model calls, so they belong in CI. The behavioral layer (evals/evals.json)
verifies the skills' conduct; this layer verifies the contract surface they
share stays consistent as the files evolve.

Usage: python3 evals/structural/check.py [repo-root]
Exit code 0 = all invariants hold.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]

FAILURES = []
CHECKS = 0


def check(name: str, ok: bool, evidence: str = ""):
    global CHECKS
    CHECKS += 1
    mark = "ok" if ok else "FAIL"
    line = f"[{mark:>4}] {name}"
    if not ok and evidence:
        line += f"\n       {evidence}"
    print(line)
    if not ok:
        FAILURES.append(name)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def prose(rel: str) -> str:
    """Whitespace-normalized text, for phrases that may wrap across lines."""
    return re.sub(r"\s+", " ", read(rel))


# ---------------------------------------------------------------- frontmatter

SKILLS = ["kickoff", "wrapup", "quiz-me"]

for skill in SKILLS:
    text = read(f"skills/{skill}/SKILL.md")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    check(f"{skill}: SKILL.md has YAML frontmatter", bool(m))
    if not m:
        continue
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.MULTILINE)
    desc = re.search(r"^description:\s*(.+)", fm, re.MULTILINE)
    check(f"{skill}: frontmatter name matches directory",
          bool(name) and name.group(1) == skill,
          f"name field: {name.group(1) if name else 'missing'}")
    check(f"{skill}: frontmatter description is substantial",
          bool(desc) and len(desc.group(1)) > 100,
          "description missing or too short to drive triggering")

# ------------------------------------------------------- reference integrity

for skill in SKILLS:
    skill_md = read(f"skills/{skill}/SKILL.md")
    ref_dir = ROOT / f"skills/{skill}/references"
    mentioned = set(re.findall(r"references/([\w-]+\.md)", skill_md))
    on_disk = {p.name for p in ref_dir.glob("*.md")} if ref_dir.is_dir() else set()
    check(f"{skill}: every reference mentioned in SKILL.md exists on disk",
          mentioned <= on_disk,
          f"missing: {sorted(mentioned - on_disk)}")
    check(f"{skill}: no orphan reference files (on disk but never mentioned)",
          on_disk <= mentioned,
          f"orphans: {sorted(on_disk - mentioned)}")

# --------------------------------------------------- anchor-token consistency
# Verdict keywords are the trust anchors: every file that renders one must
# agree on the exact token. A token drifting in one file breaks the handoff
# between plan -> notes -> audit -> gate.

PLAN = "skills/kickoff/references/plan.md"
AUDIT = "skills/wrapup/references/audit.md"
WRAPUP = "skills/wrapup/SKILL.md"
QUIZME = "skills/quiz-me/SKILL.md"
RULES = "rules/unknowns-rules.md"

ANCHOR_SETS = {
    "VERIFIED": [PLAN, AUDIT, WRAPUP],
    "FAILED": [PLAN, AUDIT, WRAPUP],
    "NOT RUN": [PLAN, AUDIT, WRAPUP],
    "DEFERRED": [PLAN, AUDIT, WRAPUP],
    "AMENDMENT PENDING": [PLAN, AUDIT, WRAPUP],
    "CONFIRMED": [PLAN, AUDIT],
    "UNVERIFIABLE": [PLAN, AUDIT],
    "NOT YET": [PLAN, AUDIT, WRAPUP, QUIZME],
    "(self-audited)": [AUDIT, WRAPUP],
    "NO CONTRACT — verified by inspection": [AUDIT, WRAPUP],
}

for token, files in ANCHOR_SETS.items():
    for rel in files:
        check(f"anchor '{token}' present in {rel}", token in prose(rel))

# The two-axis vocabulary must exist on both sides of the handoff.
check("wrapup gate names the merge axis", "merge axis" in prose(WRAPUP))
check("wrapup gate names the understanding axis", "understanding axis" in prose(WRAPUP))
check("quiz-me scopes itself to one axis", "one axis" in prose(QUIZME))
check("quiz-me hands merge-worthiness to wrapup",
      re.search(r"merge[\w-]*.{0,60}wrapup", prose(QUIZME), re.IGNORECASE) is not None,
      "quiz-me must direct the merge question to wrapup's audit")

# ------------------------------------------- five-item stop-and-ask base set
# The permanent base lives in two places that must agree: plan.md section 3
# (the contract the implementer works under) and the always-on rules.

BASE_STEMS = ["intent", "value tradeoff", "irreversible", "security surface",
              "outward promises"]
for rel in (PLAN, RULES):
    text = prose(rel).lower()
    missing = [s for s in BASE_STEMS if s not in text]
    check(f"five stop-and-ask base items present in {rel}",
          not missing, f"missing stems: {missing}")

# ------------------------------------------------------- cross-skill handoff

check("plan.md has a section 5 verification contract heading",
      re.search(r"^### 5\..*[Vv]erification contract", read(PLAN), re.MULTILINE) is not None)
check("plan.md has a section 3 deviation policy heading",
      re.search(r"^### 3\..*[Dd]eviation policy", read(PLAN), re.MULTILINE) is not None)
check("plan.md commits pass bars before results exist",
      "committed now" in prose(PLAN).lower())
check("plan.md separates author from verdict",
      "never the author of its verdict" in prose(PLAN))
check("audit.md forbids fabricating criteria after the fact",
      "never fabricate acceptance criteria" in prose(AUDIT))
check("audit.md orders evidence before narrative",
      re.search(r"narrative.{0,80}last", prose(AUDIT), re.IGNORECASE) is not None)
check("wrapup audits before narrating",
      "Audit before you narrate" in prose(WRAPUP))
check("wrapup reads audit.md for the audit",
      "references/audit.md" in read(WRAPUP))
check("kickoff plan embeds the verification contract for wrapup",
      "verification contract" in prose("skills/kickoff/SKILL.md"))
check("wrapup two-axis gate refuses to collapse the axes",
      "Never collapse the axes" in prose(WRAPUP))
check("quiz-me PASS verdict promises understanding, not merge",
      "PASS — you understand this change" in prose(QUIZME))
check("wrapup understanding axis uses the same PASS phrasing as quiz-me",
      "PASS — you understand this change" in prose(WRAPUP))

# --------------------------------------------------------- language contract
# Every user-facing skill file carries a Language spec so translated output
# keeps the English anchor tokens.

lang_files = [f"skills/{s}/SKILL.md" for s in SKILLS] + [
    f"skills/kickoff/references/{n}.md"
    for n in ["blindspot", "brainstorm", "challenge", "impl-notes",
              "interview", "plan", "use-reference"]
] + [f"skills/wrapup/references/{n}.md" for n in ["audit", "pitch", "quiz"]]

for rel in lang_files:
    check(f"language spec present in {rel}", "**Language:**" in read(rel))

# ------------------------------------------------------------ README parity

for rel in ("README.md", "README.zh-CN.md"):
    text = read(rel)
    missing = [s for s in SKILLS if s not in text]
    check(f"{rel} documents all three skills", not missing,
          f"missing: {missing}")

# --------------------------------------------------------------- valid JSON

for rel in ("hooks/hooks.json", ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json"):
    try:
        json.loads(read(rel))
        check(f"{rel} is valid JSON", True)
    except (OSError, json.JSONDecodeError) as e:
        check(f"{rel} is valid JSON", False, str(e))

# --------------------------------------------------------------------- exit

print(f"\n{CHECKS - len(FAILURES)}/{CHECKS} invariants hold")
if FAILURES:
    print("failed:")
    for name in FAILURES:
        print(f"  - {name}")
    sys.exit(1)
