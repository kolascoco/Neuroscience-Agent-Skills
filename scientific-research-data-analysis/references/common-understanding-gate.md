# Common Understanding Gate

Use this gate before result-producing scientific work. The Orchestrator
conducts this interview; attribute estimand/hypothesis reasoning to Theorist
judgment and null/multiplicity/design reasoning to Statistician judgment (see
[soul-roles.md](soul-roles.md)), even though you answer as the same agent.

## Rule

Treat the open scientific choices as a design tree. [decision-tree.md](decision-tree.md)'s
section order (Scientific Target, Data And Sample, Preprocessing And Features,
Statistics, Outputs) is that tree's approximate dependency order already —
use it as the default traversal unless a specific choice obviously reorders it.

Work the tree in rounds:

1. **Frontier:** the decisions whose prerequisites are already settled — the
   ones you can ask now without guessing at an answer you haven't heard yet.
   A decision that depends on another still-open decision belongs to a later
   round, not this one.
2. **Ask the whole frontier at once**, numbered, each with a recommended
   answer and a short reason — except pull any individually high-risk or
   deeply consequential decision (e.g., the primary estimand, the null model)
   into its own round even when it is frontier-ready. "Its own round" means
   asked alone and confirmed before the rest of that frontier is presented,
   not just visually separated within the same message. Frontier logic
   decides what CAN be batched; risk decides what gets split out anyway.
3. **Recompute the frontier** from the user's answers and ask the next round.
   Repeat until the frontier is empty: every relevant branch of the decision
   tree visited, nothing left silently assumed.

Facts are never a frontier question for the user. Before every round,
distinguish facts from decisions:

- **Facts** (paths, hashes, schema, existing metadata, prior documentation):
  look them up yourself. A single read, grep, or directory listing is trivial
  — do it inline. Anything requiring a directory-tree exploration, a script
  run, or cross-referencing multiple files is nontrivial — dispatch it to a
  sub-agent instead of blocking the round on it; only the decisions
  downstream of that fact wait, ask the rest of the frontier now.
- **Decisions** (anything requiring scientific judgment): ask the user,
  recommend an answer, and wait rather than assuming a default, especially
  when high risk.

Before explicit confirmation:

1. Perform only read-only inspection needed to establish facts.
2. Record accepted choices in a decision ledger as each round closes.
3. Do not create result-producing code, inspect scientific outcomes, tune
   thresholds, or launch real-data compute.
4. When the frontier is empty, present the full ledger, unresolved risks,
   expected artifacts, and compute estimate. Ask whether shared understanding
   is confirmed.

## Compact Ledger Mode

For read-only planning or simple low-risk tasks, skip the round structure: a
single compact ledger may group related decisions. Label anything unresolved
and do not proceed to outcomes.

## Reopening Choices

If a frozen scientific choice changes, reopen the relevant branch and obtain
confirmation before continuing. Implementation-only fixes may proceed when they
do not alter the estimand, sample, preprocessing, statistic, null model,
multiplicity family, or interpretation.
