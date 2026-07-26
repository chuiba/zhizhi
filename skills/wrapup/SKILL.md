---
name: wrapup
description: Wrapup (收工) — run after implementation work is done, before merging or sharing. Audits the change against the plan's verification contract (re-running checks, reconciling the diff against the logged deviations), then produces what the moment needs — a buy-in document that leads with the demo, demo steps and a spot-check menu for the user, and a quiz that verifies they understand what changed. Recommends merge only when the contract is green and the quiz passes. Ends by promoting session learnings into permanent context. Use when the user says "wrapup", "收工", "干完了", "I'm done", "package this up", "ready to merge", "get buy-in", or finishes a long working session.
---

# Wrapup

After a long session, more happened than the user realizes — and the session's own
story of what happened is a map, not the territory. Wrapup audits that story against
the diff and the contract, closes the gap between the user and the people they need
buy-in from, then banks what was learned. Audit first, narrate second, quiz last: a
claim checked after it has been written up is a claim you'll rationalize.

**Language:** write everything user-facing — the report, quiz questions, verdicts — in
the language the user is speaking. The pitch doc follows its *audience*: match the
repo's PR/doc convention, ask if unclear. Verdict keywords — PASS / NOT YET, VERIFIED /
FAILED / NOT RUN, DEFERRED, AMENDMENT PENDING, "(self-audited)" — stay in English in
every language. File names and code identifiers stay in English.

## Step 1 — Collect what happened

Gather whatever exists: the diff against the base branch, the plan, `implementation-notes.md`
(deviations and surprises are the most valuable material), and demo evidence (screenshots,
GIF, runnable link). For user-facing work whose review depends on *seeing* it, make demo
evidence first — a terminal transcript or test run counts for non-visual work; if the
host can't capture it, write the exact steps for the user and leave a placeholder. When
the diff is the demo (copy fixes, renames), skip this.

No `implementation-notes.md`? Reconstruct the deviations and surprises from the session
history and the diff — or state that there were none — and write the result to a file at
once; Steps 2 and 5 read it from disk, not from chat. Tag each item **witnessed** (you saw it
happen) or **inferred** (guessed from the diff): after compaction, "reconstruction" is
generation, and an inference presented as a memory poisons everything downstream. If the
history is already compacted, say so, salvage what the summary still holds into a
retroactive notes file, and work from that. When the reconstruction surfaced something
notes would have caught, mention once — not more — that zhizhi's three always-on rules
(`rules/unknowns-rules.md` in its repository) capture these automatically; if the repo
isn't on this machine, name the project and stop — never guess install commands.

**Mind the context budget — and the audit boundary.** Wrapup runs when the session is
at its fullest. Everything it consumes can live on disk (diff, plan, notes), so with
notes on disk it runs fine in a fresh session — and for Step 2's audit, better than
fine: the implementing session can only re-read its own map, while a fresh session
reads nothing but artifacts and territory. Recommend a fresh session whenever the notes
hold Deviations or the change is large. Without notes, the session's memory *is* the
evidence: **salvage precedes audit** — run this step's reconstruction and write it to
disk first, then audit from disk. Either way, write what you produce to files, not only
chat.

## Step 2 — Audit before you narrate

A trivial change — one a reader of the diff alone fully understands, no hidden code
paths — needs no audit and no products: say "nothing here needs a wrapup — safe to
merge" and stop. That verdict is a first-class outcome, exempt from Step 4's two-axis
formula, and it is wrapup succeeding, not failing.

For everything else, read `references/audit.md` and run the audit **before writing a
word of pitch or report**. The audit re-runs the plan's verification contract (§5),
reconstructs the real deviation set from the diff and reconciles it with the notes, and
grades the implementation's own claims the way kickoff's premise challenge grades the
user's. Prefer a fresh session (see the context-budget note above); a same-session
audit tags its verdict "(self-audited)". No contract exists? The audit says so and
downgrades honestly — it never fabricates criteria after the fact; audit.md has the
protocol.

A FAILED contract line or a FALSE claim stops the parade: surface it and recommend
fix-and-re-audit. Don't proceed to quiz a user on a change that doesn't work.

## Step 3 — Produce what the moment needs

Decide from context, confirm with one short question only if genuinely unclear:

- **Pitch doc** (read `references/pitch.md`) — when the work needs review, approval, or
  an audience: a single document that leads with the demo, walks the decisions that
  matter, and answers the reviewer's first three questions before they ask. Skip when
  there is no reviewer or audience — work only the author will ever read needs no pitch.
- **The human's gate materials** — the steps for the user to run the demo *themselves*
  (minutes proportional to blast radius — a config rename doesn't earn fifteen), and a
  **spot-check menu**: the 2–3 places most worth a deep read, picked by the audit — not
  the implementer — each with what to look at and how it could be proven wrong. Honest
  exit: "nothing here rewards a deep read." The audit's verdict table, the deviation
  reconciliation, the spot-check scope, and the rollback path together form a
  one-screen certificate. When a pitch doc exists the certificate is not a second
  document — the pitch's Risks & rollback section links it, and each "it works" claim
  cites the evidence behind an audit row. Solo path, no reviewer: the certificate is a
  record kept for yourself; no signing ceremony.
- **Understanding quiz** (read `references/quiz.md`) — a report explaining the change
  including the pre-existing code paths the diff never shows, then a quiz. **Don't skip
  this for any non-trivial change**; it's the only step that verifies the user can
  actually stand behind the merge.

Order: pitch doc first (its material feeds the report), quiz last.

## Step 4 — The gate

Two axes, one final line:

- **The merge axis** is the audit's contract tally: "contract: 6/6 VERIFIED —
  mergeable", or "4/6 VERIFIED, 1 DEFERRED, 1 FAILED — not mergeable yet". DEFERRED
  lines name their runner; AMENDMENT PENDING lines name the countersign they wait for;
  no contract → `NO CONTRACT — verified by inspection`. A self-audited tally carries
  its "(self-audited)" tag into this line.
- **The understanding axis** is the quiz verdict:
  - **PASS — you understand this change.**
  - **NOT YET — misses on: <topics>. Re-quiz when ready.**

"Safe to merge" may only follow a fully green contract **and** PASS. Every other
combination names what's missing — "you understand it, but two contract lines never
ran; that is not a merge recommendation." Never collapse the axes: a comprehension PASS
is not evidence the code works, and a green contract is not evidence the user can stand
behind it. Never soften either verdict. Everything after a dash is written in the
user's language; the verdict keywords stay English — they are the trust anchor.

## Step 5 — Bank the learnings

From the Surprises, Deviations, and audit findings (the notes', or the ones
reconstructed in Step 1), propose which learnings should be **promoted to permanent
context** (CLAUDE.md, AGENTS.md, or team docs) — a surprise that will surprise the next
person too is a documentation bug. Draft the exact lines to add; let the user say yes
or no. Only **witnessed** items get pre-drafted lines; **inferred** ones are posed as
questions for the user to confirm from their own memory — never bank a guess. Any
understanding debt the quiz left standing banks too — "no human currently understands
X", with the trigger that repays it (the first bug touching X earns a guided
walkthrough). If there were no surprises, deviations, or findings, say "nothing to
bank" and stop — an empty banking step after clean work is the correct outcome, not a
failure.

Then close the second loop: for each Surprise, Deviation, and audit finding, ask
**"which barrier should have caught this, and why didn't it?"** — a kickoff technique
that didn't fire, a question the interview never asked, a premise nobody challenged, a
contract line never written, a notes discipline that lapsed. Propose one concrete
update to that barrier, and prefer landing it somewhere **executable and owned by the
project** — a line in the project's contract-template section of CLAUDE.md, an actual
regression test in the repo — over prose memory. Never edit this skill's own files:
they are shared across projects and overwritten on update. If kickoff never ran, the
adjustment is simply "run kickoff next time" — name one surprise it would have caught;
don't invent finer tuning. The first loop improves the map; this one improves the
map-making.
