# Theory Update

Use after confirmed, exploratory, null, blocked, or fragile results when the
project maintains a living theory or lab journal.

## Rules

1. Every theory edit cites the artifact that caused it.
2. Nulls become constraints, not silence.
3. Exploration-only results remain provisional.
4. PASS-WITH-RISKS limitations carry into the theory text.
5. Contradictions become open tensions rather than quiet resolutions.
6. Do not create rescue chains. A follow-up that keeps a failed idea alive must
   state the specific flaw or new estimand and become a new analysis.
7. Propose at most three next stubs per update. Stubs are recorded in the
   project `ideas.md` (see
   [analysis-artifact-contract.md](analysis-artifact-contract.md)) so the two
   artifacts stay consistent. Stubs are inputs to a future Theorist pass
   (SKILL.md step 2), not self-authorizing — they still need shared
   understanding before compute.

## Changelog Entry

Write the entry to `lab_journal_entry.md` per the canonical filename table in
[analysis-artifact-contract.md](analysis-artifact-contract.md). Record:

- analysis id/result status;
- what changed in belief;
- what is now constrained or unsupported;
- residual risks;
- proposed next steps;
- `ideas.md`: which ideas this update added or closed.

## Journal And Theory Are Different Artifacts

- The **lab journal** is an append-only record. It grows without bound. It
  is written on every update and is not a decision aid.
- The **theory document** is current-state and bounded. It is
  **re-derived**, not appended to: superseded claims are removed or marked,
  never accumulated. Its canonical filename is `theory.md`, at the project
  root above `analyses/` (see the canonical filename table in
  [analysis-artifact-contract.md](analysis-artifact-contract.md)).
- The **theory document** states the direction the project is committed to.
  The **project ideas list** (`ideas.md`) holds the directions it is not
  committed to. A candidate stays in `ideas.md` until an artifact moves it
  into the theory; a claim the theory no longer supports leaves the theory
  and re-enters `ideas.md` as an open idea, or is dropped with its reason.
- Appending a journal entry does not satisfy step 9. A theory update that
  leaves the theory document unchanged states why in the journal entry,
  naming the artifact that failed to move it.
