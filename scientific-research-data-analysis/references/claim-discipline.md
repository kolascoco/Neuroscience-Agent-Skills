# Claim Discipline

Every number and identifier that leaves a session traces to an executed
lookup or measurement. This file is a standing rule, not a workflow step: it
applies at every step of the nine-step workflow, from framing through
reporting, wherever a claim, identifier, count, or number is written down.

## Standing Rule

A claim earns its place in an artifact by being checked at the moment it is
written, not by having seemed true earlier in the session. Re-verify a claim
carried forward from an earlier step before it appears in a later artifact —
carrying it forward unchecked does not count as re-verifying it.

## State Only What You Established

Every factual claim in a summary, figure caption, or manuscript traces to an
executed computation or a saved artifact that can be cited. A claim that does
not trace this way is not established, no matter how plausible it reads.
"Verified" means a check was run and its output exists — it does not mean the
check would obviously have passed.

## Identifiers Are Never Written From Memory

Every DOI, PMID, accession, dataset id, URL, atlas coordinate, and citation
is the literal output of a lookup executed in the same session that wrote
it. Recalling an identifier from training data or an earlier session does
not satisfy this rule, even when the recollection turns out correct — the
rule is about how the identifier was produced, not whether it is right.

This repository's own lookup skills are the means of compliance:
`paper-lookup` for papers, preprints, and citation metadata;
`zotero-research-skill` for the user's library; and
`neuroscience-database-lookup` for datasets, accessions, and atlas
coordinates. An identifier with no lookup behind it is not written at all —
label it UNRESOLVED (see Epistemic Tiers At Synthesis) rather than filling
the gap from memory.

## Counts Are Measured, Never Intended

N at every stage is read from the artifact at write time, never
reconstructed from what the config commanded or what the plan intended. Where
measured disagrees with planned, report measured and the gap, and name the
step at which the two diverged.

## One Source Per Number

Every reported figure comes from a single saved query re-run at write time.
Numbers are not hand-carried between `final_report.md`, a figure caption, and a
manuscript: copying a value from one artifact into another breaks the
single-source rule even when the copied value is currently correct.

## Open, Do Not Path-Resolve

Before declaring outputs complete, open every file the summary references.
Confirming a path resolves — the file exists — is not the same check as
reading what the file says, and reading what it says is the requirement
here.

## Epistemic Tiers At Synthesis

Label each statement in a synthesis with one of four tiers:

- **OBSERVATION** — a measured fact, traceable to an executed computation or
  a saved artifact.
- **INFERENCE** — a conclusion drawn from observations, not itself
  independently measured.
- **HYPOTHESIS** — a claim proposed for future testing, not yet supported by
  this project's data.
- **UNRESOLVED** — a claim that cannot currently be traced to a lookup,
  computation, or artifact, left open rather than resolved by assertion.

The agent's own proposals and any sub-agent's recommendation carry one of
these four labels. Writing a proposal in declarative language does not
promote it to OBSERVATION.

## Lead With The Unfavorable Reading

The headline states the worst defensible reading of the data, not the most
flattering reading the evidence still supports. Deviations from the frozen
plan are disclosed in the same report, not left for a reader to find by
diffing `config.json` against the narrative. An analysis tuned after seeing
its results is reported as such, with the number of configurations tried —
omitting the count does not shrink the tuning, only its visibility. Where
the analysis belongs to a family declared in `config.json`, the count is the
family size at write time, not a recollection.

Report messy or inconclusive results as messy or inconclusive. A genuinely
ambiguous result is not rounded up to a clean finding for readability.

## Standards Bind Tighter Under Autonomy

Propose-then-verify reduces human review, which leaves the agent's own
verification as the only gate between a claim and the record. Between
shipping a confident result and flagging an uncertainty, flag the
uncertainty.
