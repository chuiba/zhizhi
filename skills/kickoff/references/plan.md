# Unknowns-First Implementation Plan

A plan's job is not to list steps — it's to put the user's review time where decisions
might actually flip. Lead with what they're most likely to tweak; bury what they'd
rubber-stamp.

Fold in whatever this kickoff produced: criteria list, decision log, blindspot briefing,
semantics checklist.

**Language:** templates and section names in this file are the spec, not literal output —
render everything user-facing in the user's language. Code identifiers, file paths, and
anchor tokens (CONFIRMED / FALSE / UNVERIFIABLE, VERIFIED / FAILED / NOT RUN, DEFERRED,
AMENDMENT PENDING, PASS / NOT YET, notes headings) stay in English.

## Write the plan in this exact order

### 1. Decisions you'll most likely tweak (top of the document)

Data model changes, new type interfaces, API shapes, anything user-facing. For each:

- The decision, concretely (show the actual schema / interface / flow, not a description)
- **Confidence: high / medium / low**
- **What would flip it** — the specific evidence or answer that would change the decision

This section is the review surface. Readable in five minutes.

For diagnostic tasks ("why does X keep failing?"), this section holds **ranked
hypotheses** instead — each with confidence and the cheapest experiment that would
flip it.

### 2. Assumptions

Everything taken as given, each with confidence and source (user said it / found in
code / industry default). Industry-default assumptions get flagged loudest — they're the
ones most likely to be wrong for this codebase.

### 3. Deviation policy

Pre-authorize the implementer:

- **When an edge case forces a deviation: pick the conservative option, log it, keep
  going.** Define "conservative" for this task explicitly.
- List what must **stop and ask** instead. Five items are the permanent base — they
  belong to the human at any level of trust and are never delegated: **a change of
  intent or scope**, **a value tradeoff** (what counts as better), **irreversible
  actions** (destructive migrations, data deletion), **security surface**, and
  **outward promises** (API contracts, commitments to people outside the task). Add
  task-specific items on top; never remove from the base. A discovery that invalidates
  the plan's premise also stops.
- For inherently destructive work (production migrations, data deletion), invert the
  default: enumerate the few places where keep-going is safe; everything else stops
  and asks.
- **Contract amendments:** when a §5 line itself turns out wrong — its bar rests on a
  premise the territory falsified, its command cannot exist here — the implementer
  neither games the check nor silently skips it. They file a proposed amendment in the
  notes (old line / new line / evidence) and keep working against the **stricter** of
  the two readings; the human countersigns at wrapup. A third amendment means the
  contract's premises broke — that is the re-diagnosis trigger, not a fourth amendment.

### 4. Mechanical work (bottom)

Refactoring, plumbing, boilerplate. One line each. Mark the section "low review value —
trust the implementer."

### 5. Verification contract

The correctness contract — wrapup's audit executes this section, so write it for a
reader with no memory of this plan. One line per "it works" claim, each with:

- **The check.** Either **runnable** — the exact command, against real data where
  possible — or **inspection** — the criterion, where to look, and who confirms — for
  deliverables that can't be executed (a runbook, a design doc). Never invent a fake
  runnable check for a document.
- **The pass bar, committed now.** Decided before any results exist — the spike rule
  from brainstorm.md, promoted to the whole task. A bar decided after seeing output
  gets shaped by the output.
- **Who runs it.** The implementer (runs it, records raw evidence), the audit (re-runs
  and judges), or a named human for territory only they can reach.

Scale: roughly one line per §1 decision plus one smoke check — about five lines, not
twenty. A mechanical-only plan gets a one-line contract and no ceremony around it. The
boundary the contract enforces: **the author of a change is never the author of its
verdict** — the implementer records evidence; the audit judges it against the bar.

## Review loop

Walk the user through **section 1 and the contract's pass bars — nothing else**, in one
pass. Adjust until they stop tweaking. Their approval locks the contract: after this,
changing a §5 line is an amendment (see §3), not an edit. Don't burn their attention on
the mechanical section.

## Handoff

Recommend executing in a **fresh session**: write the plan and kickoff artifacts to
stable repo paths first, then pass them along with the implementation-notes setup (see
`impl-notes.md`) so deviations get logged instead of silently improvised. The setup
copies §5 **verbatim** to the top of `implementation-notes.md` — two copies are the
lock: wrapup's audit compares them, and divergence without a logged amendment is a
finding. (This deters drift, not adversaries — a session that controls the disk can
rewrite both copies. Honest drift is the common failure, and it's the one this
catches.) Scale the handoff to the plan — if the mechanical section is essentially the
whole plan, skip the fresh session and the notes file. If humans, not an agent session,
will execute (a prod cutover, an ops runbook), replace the fresh-session/notes
instructions with a named log owner and the same Decisions/Deviations/Surprises
checklist inside the document; §5 lines they run after handoff name their runner and
due moment, and the audit marks them DEFERRED rather than pretending to run them. What
the execution learns becomes the map for next time.
