# Adversarial Review

Use after an analysis produces results. Independent execution is required
whenever your platform can provide it — see
[soul-roles.md](soul-roles.md#executing-roles-as-one-agent) for the mechanics
and the self-review fallback when it can't. Write the review to
`results/adversarial_review.md` per the canonical filename table in
[analysis-artifact-contract.md](analysis-artifact-contract.md).

## Inputs

Read only artifacts: hypothesis or question, plan, config, code, tests,
results, logs, registry/lab journal, manifests. Avoid the analyst's narrative
unless it is part of the formal summary under review.

## Reviewer Composition

The review is not independent unless both properties hold:

- At least one reviewer generates new measurements rather than only reading
  documents.
- At least one reviewer forms its verdict from raw artifacts alone, without
  the analyst's conclusions — this is the Inputs rule above (avoid the
  analyst's narrative), restated as a required property of the review rather
  than a habit of the reviewer.

A review missing either property does not count as adversarial review.

## Checklist

1. Plan adherence: code and outputs match frozen plan/config.
2. Leakage: no outcome-to-feature, test-to-train, confirmation peeking, or
   preprocessing fit on full data.
3. Multiplicity: count actual loops/tests/maps/endpoints versus stated family.
4. Code audit: joins, NA handling, boundary windows, signs, contrasts,
   package defaults, seeds, cache reuse.
5. Reproduction tier: hash check, targeted rerun, or full rerun when cheap and
   justified. State which tier was used.
6. Controls: positive, negative/null, boundary, and rendering controls passed.
7. Confounds and alternatives: list plausible non-target explanations.
8. Fragility: name the single defensible change most likely to weaken result.
9. Instrument record: every stage holds a PASS, no stage is STALE, and the
   chain's `validated_at` ordering is consistent. Coverage: every tool the
   analysis actually depends on for a result has a record; a tool used in
   `code/` with no record is a finding — see
   [instrument-validation.md](instrument-validation.md).

## Verdicts

- **BLOCK:** flaw invalidates the result.
- **REVISE:** fixable problem; provide executable checklist.
- **PASS-WITH-RISKS:** sound within limits; residual risks become limitations.

Every finding ships with the exact command or query that produced each number
it cites.

Do not issue unconditional PASS. A clean null can pass with risks.
