## Finding your unknowns

- When executing a non-trivial plan, keep an `implementation-notes.md`: log decisions as you go; when a surprise forces deviating from the plan, pick the conservative option, log it under "Deviations", and keep going. Five things always stop and ask instead, at any level of trust: changes of intent, value tradeoffs, irreversible actions, security surface, and outward promises.
- When the user says a previous attempt came back wrong and they don't know why, suggest the `kickoff` skill to find their unknowns before retrying.
- Before merging a large change the user hasn't reviewed, suggest the `wrapup` skill (verify + explain + spot-check).
