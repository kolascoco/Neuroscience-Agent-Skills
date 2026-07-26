# Adversarial Review

Use after an analysis produces results. Independent execution is required
whenever your platform can provide it — see
[soul-roles.md](soul-roles.md#executing-roles-as-one-agent) for the mechanics
and the self-review fallback when it can't.

## Inputs

Read only artifacts: hypothesis or question, plan, config, code, tests,
results, logs, registry/lab journal, manifests. Avoid the analyst's narrative
unless it is part of the formal summary under review.

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

## Verdicts

- **BLOCK:** flaw invalidates the result.
- **REVISE:** fixable problem; provide executable checklist.
- **PASS-WITH-RISKS:** sound within limits; residual risks become limitations.

Do not issue unconditional PASS. A clean null can pass with risks.
