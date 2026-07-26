---
name: quiz-me
description: Quiz-me (考考我) — after a large change, or any change the user didn't author themselves (AI-written code), generates a report explaining the context, intuition, and mechanics of what changed — then quizzes the user on it and grades the answers strictly, ending in an explicit understanding verdict (PASS / NOT YET). Understanding is one axis only — merge-worthiness belongs to wrapup's verification audit. Use when the user says "quiz me", "考考我", "测测我", "我不放心这次改动", "do I actually understand this change", "explain what happened then test me", or after a long working session before merge.
---

# Quiz Me

After a long session, more happened than the user realizes. Reading diffs gives only a
light understanding, because much of the new behavior depends on **existing code paths
the diff never shows**. This skill closes that gap: explain, then verify the explanation
landed. It measures one axis only — whether the user understands the change. Whether
the change *works* is wrapup's verification audit's question; a user who shouldn't
merge what they can't stand behind also shouldn't merge what nobody verified.

**Language:** write the report, quiz questions, and verdicts in the language the user is
speaking. The verdict keywords PASS / NOT YET stay in English in every language — they
are the trust anchor. File names and code identifiers stay in English.

## Step 1 — Scope what "the change" really is

Don't stop at the diff:

- The diff itself
- The existing code paths the new code calls into or is called from
- Behavior that changed *without its code changing* (a config default now taking
  effect, a caller now hitting a different branch)
- What the change relies on continuing to be true (invariants, ordering, formats)

## Step 2 — Write the report

Sections, in order:

1. **Why** — the problem this change solves, one paragraph
2. **Mental model** — the intuition: how to think about the new behavior in one diagram
   or metaphor. If the user keeps one idea, it's this one.
3. **What changed** — a guided walk through the diff, grouped by intent rather than by
   file
4. **What it stands on** — the pre-existing code paths and invariants the change depends
   on; the part diffs never show
5. **Where it could break** — the inputs, states, or future edits most likely to hurt it

For small changes, sections may be a sentence or two and Why / What changed may merge —
but never thin out "What it stands on" or "Where it could break"; they are the point.

Default to Markdown. If the user asks for HTML (or the change is big enough that
navigation helps), produce a single self-contained HTML file with the quiz at the bottom.

**The report is the answer key, and the key is a map.** Every claim in it must be
territory-backed — a file/line you actually opened, or output you actually executed
(tracing and failure-mode answers especially: walk the real code path or run the input
before asserting what happens). A claim you can only assert goes into "Where it could
break", and no quiz question may hang on it — a strictly graded quiz keyed to a wrong
map teaches the error harder. Quiz-me runs without wrapup's audit, so this rule is the
whole correctness safeguard here: if backing a claim would require running something
you can't, say so in the report rather than asserting.

Write the report to a file, not only into chat — grading spans multiple turns, and the
report is the answer key; it must survive context compaction. Put it in the project's
working-docs home or a gitignored directory in the repo — not a session temp dir
(grading may resume in a fresh session), and never loose in the source tree.

## Step 3 — Quiz

3–8 questions at the bottom of the report, scaled to the change's conceptual surface.
The no-trivia rule below outranks the count: write fewer questions rather than pad. For
substantial changes include at least one of each; drop a category the change genuinely
doesn't have rather than invent trivia:

- A question about behavior that depends on **pre-existing code** (not visible in diff)
- A **failure mode**: "what happens if <input/state X>?"
- A **tracing** question: "a request comes in with Y — walk me through what runs"
- A **design** question: "why was alternative Z not used?"

Format for low friction — a quiz nobody takes verifies nothing:

- **Default to multiple choice** (at least two-thirds of the questions), with
  distractors built from plausible misconceptions, not filler. A user who actually
  holds the misconception must find its distractor attractive.
- **At most one short-answer question per three questions** (the tracing question is
  usually the one), answerable in a handful of keywords or arrows — say so explicitly.
- **At most one or two prediction items**, where a check is cheap to run: the user
  states what the system will do for a concrete input, then it is actually run and
  checked (on a host that can't execute, hand the user the command). Prediction beats
  recall — but only in small doses; the low-friction format is what makes the quiz get
  taken at all.
- Number questions and letter the options so the whole quiz can be answered in one
  line ("1B 2A 3C"). If the host provides a structured choice UI, use it.
- No trivia — every question's answer should matter for operating or reviewing this
  code.

## Step 4 — Grade strictly

- Grade each answer; partial credit is a fail for that question. For short answers,
  judge the concept, not the prose — terse keyword answers are fine.
- Attribution runs in two rounds: a **first miss is presumed a clarity defect in the
  explanation** — re-explain with a file/line reference, no penalty — then ask a
  **variant** of the question (not the same one — the user can echo, that's not
  understanding). A miss on the variant is an understanding gap and counts toward NOT
  YET. The burden of legibility starts on the explainer; it transfers to the reader
  only after a better explanation failed.
- Repeat until everything passes — or the user stops. Stopping early is always allowed
  and always a NOT YET, never a reluctant PASS.

End with an explicit verdict:

- **PASS — you understand this change.** Understanding is one axis; merge-worthiness
  is the other, and it belongs to wrapup's verification audit. If merging is the
  question, say so in the same breath: run wrapup.
- **NOT YET — misses on: <topics>. Re-quiz when ready.**

Never soften the verdict. The whole value of the skill is that the user can trust a
PASS — and a PASS that promised less than "safe to merge" is one the user can trust
further. Everything after the dash is written in the user's language; the PASS / NOT
YET keywords stay English.
