# Common Understanding Gate

Use this gate before result-producing scientific work. The Orchestrator
conducts this interview; attribute estimand/hypothesis reasoning to Theorist
judgment and null/multiplicity/design reasoning to Statistician judgment (see
[soul-roles.md](soul-roles.md)), even though you answer as the same agent.

## Rule

Common understanding remains mandatory: the planning stage always ends in
confirmed shared understanding. Reaching it is by proposal, not by interview —
the mechanism changed, the requirement did not. Confirmation is explicit.
Silence is not confirmation, and absence of objection is not confirmation. An
agent that cannot draft a proposal it can defend has not established
understanding; it returns to fact-finding rather than presenting a proposal
full of open questions.

Treat the open scientific choices as a design tree.
[decision-tree.md](decision-tree.md)'s section order (Scientific Target, Data
And Sample, Preprocessing And Features, Statistics, Outputs) is that tree's
approximate dependency order already — use it as the default traversal
unless a specific choice obviously reorders it.

**The necessity test.** A question reaches the user only when none of the
following resolves it:

1. **A fact the agent can establish itself.** Facts are never asked of the
   user. Before every question, distinguish facts from decisions:
   - **Facts** (paths, hashes, schema, existing metadata, prior
     documentation): look them up yourself. A single read, grep, or
     directory listing is trivial — do it inline. Anything requiring a
     directory-tree exploration, a script run, or cross-referencing multiple
     files is nontrivial — dispatch it to a sub-agent instead of resolving it
     inline and blocking on it; only the part of the proposal that depends on
     that fact waits, draft the rest of the proposal now.
   - **Decisions** (anything requiring scientific judgment): these are not
     facts, and branch 1 does not resolve them — test branches 2 and 3
     instead, recommending an answer rather than assuming a default,
     especially when high risk.
2. **A decision already confirmed in this session.** The agent derives the
   consequence and states the derivation rather than asking again.
3. **A defensible default.** The agent states it as a named assumption the
   user can reject, rather than asking or silently assuming it.

When none of the three resolves a question, ask it in the proposal.
Otherwise decide and record the choice with its basis (fact, prior
confirmation, or named default).

**Derived decisions inherit confirmation.** A decision determined by an
already-confirmed choice is presented as a consequence — "because you chose
X, Y follows" — not re-asked. Confirming one decision shrinks the remaining
question set; it never unlocks a new round of questions.

**Mechanical check.** More than three questions surviving the necessity test
is evidence that facts were not established. The agent returns to
fact-finding and re-derives rather than presenting the list.

The frontier concept survives with a changed job: it no longer sequences
questions to the user; it orders what the agent resolves for itself before a
coherent proposal exists.

Before explicit confirmation:

1. Perform only read-only inspection needed to establish facts.
2. Record accepted choices — facts, prior confirmations, and named
   defaults — in a decision ledger as they are settled.
3. Do not create result-producing code, inspect scientific outcomes, tune
   thresholds, or launch real-data compute.
4. Present the full proposal once: the ledger, every named default and its
   rationale, unresolved risks, expected artifacts, compute estimate, and any
   questions that survived the necessity test. Ask whether shared
   understanding is confirmed.

This necessity test governs any grilling or interview procedure invoked on
an analysis in this skill's scope, including `anthropic-skills:grilling`.

## Compact Ledger Mode

For read-only planning or simple low-risk tasks, skip the round structure: a
single compact ledger may group related decisions. Label anything unresolved
and do not proceed to outcomes.

## Reopening Choices

If a frozen scientific choice changes, reopen the relevant branch and obtain
confirmation before continuing. Implementation-only fixes may proceed when they
do not alter the estimand, sample, preprocessing, statistic, null model,
multiplicity family, or interpretation.
