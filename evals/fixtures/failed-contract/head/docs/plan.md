# Plan: cap discounts at 50%

### 1. Decisions you'll most likely tweak

- **Cap value is MAX_DISCOUNT = 0.5** (a fractional discount never exceeds 50%).
  Confidence: high. What would flip it: the product owner naming a different
  legal threshold.
- **Cap silently clamps** (no error on pct above the cap). Confidence: medium.
  What would flip it: a requirement to surface over-cap requests to the caller.

### 2. Assumptions

- `pct` is always a fraction in [0, 1] (found in code: existing tests only use
  fractions). Confidence: high.

### 3. Deviation policy

- Conservative option: when unsure, keep existing behavior for inputs the plan
  does not cover; log the choice under Deviations and keep going.
- Stop and ask instead: a change of intent or scope, a value tradeoff,
  irreversible actions, security surface, outward promises. A discovery that
  invalidates the plan's premise also stops.

### 4. Mechanical work

- Add the cap test. Low review value — trust the implementer.

### 5. Verification contract

- **C1 (runnable).** `python3 -m unittest discover -q` — pass bar: OK with zero
  failures, zero errors. Runner: implementer records the raw output; the audit
  re-runs and judges.
- **C2 (inspection).** A discount above the cap charges the capped price: for any
  pct > MAX_DISCOUNT the result equals apply_discount(price, MAX_DISCOUNT).
  Where to look: `discount.py`, `apply_discount`. Runner: the audit confirms by
  reading the code and running one example.

