# Verification Audit

At kickoff, the user's request was the map and the codebase the territory. Now the
implementation's story — the plan's promises, the notes, this session's own memory —
is the map, and **the diff plus the running system are the territory**. Same rule as
the premise challenge, pointed the other way: verify against the territory, never by
re-asking the author. Including when the author is you.

**Language:** templates and section names in this file are the spec, not literal output —
render everything user-facing in the user's language. Code identifiers, file paths, and
anchor tokens (VERIFIED / FAILED / NOT RUN, DEFERRED, AMENDMENT PENDING, CONFIRMED /
FALSE / UNVERIFIABLE, PASS / NOT YET, "(self-audited)") stay in English.

## 0. Read in this order

Both contract copies (plan §5 and the top of `implementation-notes.md`), then the diff,
then the recorded evidence — the narrative (notes prose, session memory) **last**. In a
fresh session this is simply the order the inputs load, and it is why the audit prefers
one: an implementing session cannot unread its own rationalizations. Divergence between
the two contract copies without a matching Amendments entry is itself a finding.

## 1. Re-run the contract

One row per §5 line: verdict + evidence.

- **Runnable checks: re-execute, don't trust logs.** Re-running a listed command is
  cheaper than deciding whether to believe a transcript. Judge the output against the
  line's pre-committed bar → **VERIFIED / FAILED / NOT RUN**.
- **Inspection checks:** verify the criterion where the line says to look; cite what
  you saw.
- **Structurally can't run before merge** (ops executes it at cutover): mark
  `DEFERRED — runner: <name>, due: <moment>`. The human gate then signs the
  *checklist's completeness*, not results that don't exist yet.
- **Amended lines:** judge against the stricter reading and mark AMENDMENT PENDING for
  the human's countersign — never FAILED for the crime of being amended.
- **Host can't execute anything:** hand the user each line's exact command and bar;
  pasted output is territory evidence (the premise challenge's protocol). Lines nobody
  ran are `DEFERRED — runner: you`.

## 2. Reconstruct the deviations

Walk the diff against the plan and rebuild the true deviation set — *then* reconcile it
with the notes. An undocumented deviation is detected, not confessed: it is the
implementer's own not-knowing-what-it-doesn't-know, and this pass is the only place it
surfaces.

- **Materiality filter:** a divergence counts as a finding only if it touches §1
  decisions, §2 assumptions, §3's stop-and-ask base, or §5 contract lines.
  Mechanical-section divergence gets one summary line, unitemized — a reconciliation
  table that is 90% plumbing noise trains the reader to skip the row that matters.
- **Consequences:** material and unreported → the merge tally cannot read all-green;
  the item gets its own verdict-table row with a one-line risk read; and it feeds
  wrapup's barrier retro (which guard should have caught it — the notes discipline?
  a contract line never written?). Immaterial → one line, no drama.

## 3. Grade the story's claims

Every assertion in the notes' summary and prose of the form "works", "handled",
"nothing else calls this" is a premise about the territory. Verdict each one whose
falsity would change the merge decision: **CONFIRMED** (evidence cited) / **FALSE** /
**UNVERIFIABLE** — the standard kickoff applies to the user's beliefs (evidence, not
vibes), finally applied to the implementer's. The default that makes tags unnecessary:
**all narrative is uncorroborated until this step corroborates it** — a default cannot
be gamed by silence. Narrative is welcome; it gets reconciled, not punished.

## No contract? (the common path)

When no plan §5 exists — kickoff never ran, or the plan predates contracts — say so
plainly and **never fabricate acceptance criteria after seeing the results, then
"verify" them**: that is the single-author problem wearing the audit's vocabulary.
Downgrade honestly: run passes 2–3, build the spot-check menu, and stamp the merge line
`NO CONTRACT — verified by inspection`, closing with one line: "pre-committed contracts
next time → run kickoff first."

## Self-audit (the most common invocation)

Same session that implemented? The audit still runs, asymmetrically by evidence type:

- Contract re-runs stay **strong evidence even self-run** — a command's raw output is
  territory, reproducible by the reader from the verdict table. A self-audited merge
  axis may read all-green **only when every contract row carries output the reader
  could reproduce**; a row resting on the session's memory stays NOT RUN.
- Passes 2–3 are narrative-vs-narrative and are **weak under self-audit** — the auditor
  shares the author's blind spots. Say so in the verdict table.
- Tag the verdict **"(self-audited)"** and name when a fresh-session audit is worth
  demanding: any FAILED line, a material unreported deviation, or work touching the
  stop-and-ask base.

Where the host offers subagents or a second model, hand the audit to an independent
instance — independence beats a disclosure tag.

## Write it down

The audit's product is a one-screen verdict table: contract rows with verdicts, the
deviation reconciliation, graded claims, and the rollback path. Write findings to disk
as you go (wrapup's write-to-files rule). The tally line **is** the merge axis:
"contract: 4/6 VERIFIED, 1 DEFERRED, 1 FAILED — not mergeable yet."

## Guardrails

- Depth scales with the contract, which scales with the plan's §1. A one-line contract
  is a one-command audit.
- A FAILED line or FALSE claim is the audit **succeeding** — it fired before the
  reviewer or production did. Surface it, recommend fix-and-re-audit; don't proceed to
  quiz a human on a change that doesn't work.
- Honest exit: for a diff whose only claims are visible in the diff itself, "nothing to
  audit beyond the contract re-run" is a valid outcome, not a failure.
