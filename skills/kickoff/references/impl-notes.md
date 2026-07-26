# Implementation Notes

No matter how much planning happened, unknown unknowns lurk in the code. Notes turn them
from silent improvisation into a record. Embed these instructions in the plan's handoff
so the implementing session follows them.

**Language:** headings in the template below stay in English — wrapup locates them by
name. Write the entries themselves in the user's language; code identifiers, file
paths, and the evidence tokens RUN / NOT RUN / FAILED stay in English.

## Setup

At the start of implementation, create `implementation-notes.md` in the repo root (or
`docs/` if the project keeps working documents there):

```markdown
# Implementation notes — <task name>
Plan: <link/path to the plan>

## Contract
<verbatim copy of the plan's §5 — the audit compares this against the plan's copy>

## Decisions
## Deviations
## Amendments
## Surprises
## Verification evidence
## Questions for review
```

The Contract section is copied **verbatim** from the plan, never paraphrased — the two
copies are the lock (see plan.md's handoff). No plan §5? Omit Contract, Amendments, and
Verification evidence; the rest still applies.

## Rules during implementation

1. **Log as you go, not at the end.** An entry written two hours later loses the reason.
2. Every entry gets a file/line reference where applicable.
3. **On an edge case that forces deviating from the plan: pick the conservative option,
   log it under Deviations, keep going.** Conservative = reversible, minimal blast
   radius, closest to the plan's intent. Don't stall the task on a judgment call the
   notes can carry to review.
4. Stop and ask only for what the plan's deviation policy reserved — its five-item base
   (intent, value tradeoffs, irreversible actions, security surface, outward promises)
   plus the task-specific list — or a discovery that invalidates the plan's premise.
5. **Re-diagnosis trigger:** when the third entry lands under Deviations or Amendments,
   or a single Surprise contradicts one of the plan's premises, stop patching. Say: "the
   map has drifted from the territory — recommend re-running kickoff on the affected
   area before continuing." A plan whose premises broke doesn't need more deviations
   logged against it; it needs a new diagnosis.
6. **The recorder does not judge.** For each contract line marked implementer-run: log
   the command, where its output lives, and RUN / NOT RUN / FAILED under Verification
   evidence — never the word "passes"; the audit judges evidence against the bar. Keep
   raw output inline only for checks that can't be cheaply re-run later (time-dependent,
   destructive, external systems). A NOT RUN logged honestly is worth more than a
   "passes" nobody can audit.
7. **When a contract line itself is wrong** — its bar rests on a falsified premise, its
   command can't exist here — don't game the check and don't silently skip it. File an
   entry under Amendments (old line / new line / evidence why) and keep working against
   the **stricter** of the two readings; the human countersigns at wrapup. The third
   amendment is the re-diagnosis trigger (rule 5), not a fourth entry.

What goes where: **Decisions** — choices the plan left open, and what you picked.
**Deviations** — what the plan said, what you did, why, and the alternative.
**Amendments** — contract lines that turned out wrong, with evidence.
**Surprises** — hidden coupling, dead code that isn't, tests asserting the wrong thing.
**Verification evidence** — command, output location, RUN / NOT RUN / FAILED.
**Questions for review** — anything needing human judgment.

## At the end of the session

Summarize at the top: what shipped versus what the plan promised, three sentences max.
Point at the two or three entries most worth attention. The summary points at evidence;
it never contains a correctness verdict — "contract lines run, outputs under
Verification evidence" is the recorder's ceiling, and "it works" belongs to the audit.
The wrapup skill consumes this file.
