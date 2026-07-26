# Understanding Quiz

Reading diffs gives only a light understanding, because much of the new behavior depends
on **existing code paths the diff never shows**. Explain, then verify the explanation
landed. The user merges only after passing.

**Language:** templates and section names in this file are the spec, not literal output —
render everything user-facing in the user's language. Code identifiers, file paths, and
the verdict keywords PASS / NOT YET stay in English.

## 1. Scope what "the change" really is

The diff itself; the existing code paths the new code calls into or is called from;
behavior that changed *without its code changing* (a config default now taking effect, a
caller now hitting a different branch); and what the change relies on staying true
(invariants, ordering, formats).

## 2. Write the report

1. **Why** — the problem this change solves, one paragraph
2. **Mental model** — the intuition in one diagram or metaphor; if the user keeps one
   idea, it's this one
3. **What changed** — a guided walk through the diff, grouped by intent, not by file
4. **What it stands on** — the pre-existing code paths and invariants the change
   depends on; the part diffs never show
5. **Where it could break** — the inputs, states, or future edits most likely to hurt it

For small changes, sections may be a sentence or two and Why / What changed may merge —
but never thin out "What it stands on" or "Where it could break"; they are the point.

Default Markdown; a single self-contained HTML file if the change is big enough that
navigation helps.

**The report is the answer key, and the key is a map.** Every claim in it must be
territory-backed — a file/line you actually opened, or output you actually executed
(tracing and failure-mode answers especially: walk the real code path or run the input
before asserting what happens). When the wrapup audit ran, cite its verdict rows. A
claim you can only assert goes into "Where it could break", and no quiz question may
hang on it — a strictly graded quiz keyed to a wrong map teaches the error harder.

Write the report to a file, not only into chat — grading spans multiple turns, and the
report is the answer key; it must survive context compaction. Put it in the project's
working-docs home or a gitignored directory in the repo — not a session temp dir
(grading may resume in a fresh session), and never loose in the source tree.

## 3. Quiz — 3–8 questions, scaled to the change

The no-trivia rule below outranks the count: write fewer questions rather than pad. For
substantial changes include at least one of each; drop a category the change genuinely
doesn't have rather than invent trivia:

- Behavior that depends on **pre-existing code** (not visible in the diff)
- A **failure mode**: "what happens if <input/state X>?"
- A **tracing** question: "a request comes in with Y — walk me through what runs"
- A **design** question: "why was alternative Z not used?"

Format for low friction — a quiz nobody takes verifies nothing:

- **Default to multiple choice** (at least two-thirds), distractors built from
  plausible misconceptions, not filler.
- **At most one short-answer question per three questions**, answerable in keywords or
  arrows — say so explicitly.
- **At most one or two prediction items**, where a check is cheap to run: the user
  states what the system will do for a concrete input, then it is actually run and
  checked (on a host that can't execute, hand the user the command). Prediction beats
  recall — but only in small doses; the low-friction format is what makes the quiz get
  taken at all.
- Number questions and letter options so the whole quiz can be answered in one line
  ("1B 2A 3C"). If the host provides a structured choice UI, use it.
- No trivia — every answer should matter for operating or reviewing this code.

## 4. Grade strictly

Partial credit is a fail for that question. Attribution runs in two rounds: a **first
miss is presumed a clarity defect in the explanation** — re-explain with a file/line
reference, no penalty — then ask a **variant** (not the same question — echoing isn't
understanding). A miss on the variant is an understanding gap and counts toward NOT
YET. The burden of legibility starts on the explainer; it transfers to the reader only
after a better explanation failed. Repeat until everything passes — or the user stops.
Stopping early is always allowed and always a NOT YET, never a reluctant PASS.
