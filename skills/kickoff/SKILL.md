---
name: kickoff
description: Kickoff (开工) — run before starting any non-trivial task. Diagnoses the gap between what the user asked for (the map) and what the codebase or domain actually requires (the territory), then applies only the techniques needed — blindspot briefing for unfamiliar territory, premise challenges that falsify what's treated as fact, throwaway prototypes and feasibility spikes for "I'll know it when I see it", one-question-at-a-time interviews for ambiguities, reference extraction, and an unknowns-first plan. Use when the user says "kickoff", "开工", "帮我开始", "找找我的盲区", "help me start", "find my unknowns", "what am I missing", "I don't know where to start", or when a previous attempt — theirs or an AI's — came back wrong and they don't know why.
---

# Kickoff

The user's request is the map. The codebase and the real world are the territory. The
difference between them is the user's **unknowns** — and when you hit one mid-task, you
guess. This skill spends a little time up front so you guess less later.

**The deliverable is clarity, not code.** Kickoff never implements.

**Language:** write everything user-facing — briefings, questions, prototypes' copy,
plans — in the language the user is speaking. File names and code identifiers stay in
English.

## Step 1 — Diagnose (quietly)

Read the request, glance at the relevant territory (code, docs, history, and
working-tree state — uncommitted changes are territory too), and score the signals
below. Assess silently — don't lecture the framework; the diagnosis surfaces as one
line at the top of Step 2:

| Signal | Evidence |
|---|---|
| **Unfamiliar territory** | New domain or untouched part of the codebase; user says "I've never…" / "I don't know X" |
| **Confident assertions** | Statements about the territory phrased as certainty — "it's stored in X", "nothing else calls this" — especially about code nobody has touched recently |
| **Failed prior attempts** | Reverted commits, abandoned branches, "we tried it and it broke", "the last attempt came back wrong and I don't know why" |
| **Taste-driven criteria** | Vague quality words — "clean", "modern", "feels right" — user will know it when they see it |
| **Feasibility in doubt** | Nobody knows if the approach is physically possible, accurate enough, or fast enough |
| **Open decisions** | Ambiguities where different answers produce different architectures |
| **A reference exists** | User points at (or you find) code, a library, or a site that already does it |

Also collect the user's starting point if not stated — their experience with this
problem and codebase, and where they are in their thinking — but ask only if the answer
could change what fires; otherwise infer it from context. One short question at most;
uncommitted local changes always earn it (are they intended state?).

## Step 2 — Run only what fires

**Open with the diagnosis in one line** — name the signals that fired, the techniques
you'll run, and the rough cost: "Two signals fired: unfamiliar territory, open
decisions — blind spot pass on src/auth first, then a ~5-question interview." The user
can veto or reorder before anything runs; they should never wonder why they're being
asked things. When three or more techniques fire, quote the cost as total expected user
turns and offer a lite path (premise challenge + interview + plan); fold questions into
other techniques' reaction rounds rather than stacking full loops.

For each technique you run, **read its reference file first** and follow it:

| Fires when | Technique | Read |
|---|---|---|
| Unfamiliar territory | Blind spot pass — brief them on the questions they didn't know to ask | `references/blindspot.md` |
| Confident assertions | Premise challenge — verify what's treated as fact against the territory, before building on it | `references/challenge.md` |
| Failed prior attempts | The wreckage is territory — blind spot pass over the failed diffs, premise challenge on the failure's framing ("it's flaky", "it broke X") | `references/blindspot.md`, `references/challenge.md` |
| Taste-driven criteria; feasibility or cause in doubt; an open decision whose option space is unexplored | Brainstorm, throwaway prototypes, or a feasibility/diagnostic spike — turn reactions and measurements into explicit criteria | `references/brainstorm.md` |
| A reference exists | Extract its semantics into a keep/adapt/drop checklist | `references/use-reference.md` |
| Open decisions remain | Interview — one question at a time, biggest blast radius first | `references/interview.md` |

The listed order is a default — reorder when one technique's output is another's input:
a reference's checklist feeds the brainstorm, and a premise that could invalidate the
framing gets challenged before anything else. Run **only the ones that fired** — kickoff
is a diagnosis, not a ceremony. Between techniques, keep the user in the loop with one-line status
("territory is clear, but three decisions could flip the architecture — interviewing you
next").

If nothing fires: say plainly "no meaningful unknowns here — just implement", and offer
to start right away — once nothing fires, kickoff is over and normal work continues in
this same session. That answer is kickoff succeeding, not failing.

## Step 3 — Always land on a handoff

Every kickoff that ran at least one technique lands on an artifact — the nothing-fired
exit needs none; "just implement" *is* its handoff:

- **An unknowns-first plan** (read `references/plan.md`) if the user is heading into
  implementation. The plan embeds a deviation policy, ends in a verification contract
  whose pass bars the user approves in the same single review pass — locked before any
  implementation exists, executed by wrapup's audit after — and instructs the
  implementer to keep implementation notes (read `references/impl-notes.md` and fold
  its setup into the plan's handoff section).
- **A rewritten prompt** if the user just wanted clarity — their original request with
  resolved assumptions inlined and remaining open questions flagged, ready to paste into
  a fresh session.
- **The requested document itself**, when the deliverable is a plan or doc (a migration
  runbook, a design doc) — the unknowns-first plan is its skeleton, and writing it is
  not "implementing". Adapt the section vocabulary to the domain and hand off to
  whoever actually executes (see plan.md's handoff).

## Guardrails

- One technique at a time; each technique's output feeds the next.
- If diagnosis reveals the problem should be solved a different way altogether, say so
  before anything else — that's the most valuable outcome a kickoff can have.
- Simple task, familiar territory, clear spec → don't invent process. Say so and stop.
