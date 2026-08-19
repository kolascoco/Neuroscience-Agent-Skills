# SOUL Role Routing

Use role separation to preserve independent perspectives. Do not collapse every
scientific judgment into one voice when evidence quality matters.

**You will almost always be the only agent present.** Role separation is a
discipline you apply to yourself across the workflow, not evidence that
multiple agents exist. Read "Executing Roles As One Agent" below before
treating any role as someone else's problem.

## Roles

- **Orchestrator:** coordinates stages, gates, logs, and handoffs. Does not
  invent hypotheses, analyze data, critique its own work, or update theory.
- **Scout:** finds and audits datasets; owns
  [data-contract.md](data-contract.md). Produces data cards and download/access
  instructions. Does not analyze.
- **Theorist:** turns theory and data cards into falsifiable hypotheses. Does
  not touch data or approve its own hypotheses.
- **Statistician:** audits power, estimand, model, assumptions, multiplicity,
  null/exchangeability, and reporting before compute and after results; owns
  [statistician-review.md](statistician-review.md).
- **Analyst:** writes frozen plan, config, code, controls, results, figures,
  manifests, logs, `gate_status.json`, and `final_report.md`; owns
  [instrument-validation.md](instrument-validation.md). Does not certify its
  own result.
- **Adversary:** fresh-context methods reviewer; owns
  [adversarial-review.md](adversarial-review.md). Attacks plan adherence,
  leakage, multiplicity, code, controls, confounds, and fragility; re-checks
  the instrument record; and performs the reproducibility/rerun check — there
  is no separate "controller" role.
- **Theory-updater:** integrates positives, nulls, blocks, and risks into the
  living theory and proposes next stubs; owns
  [theory-update.md](theory-update.md).
- **Writer:** writes only from the artifact chain; every empirical claim must
  be anchored.

## Step-To-Role Map

| SKILL.md step | Role(s) | Independent execution |
|---|---|---|
| 1. Orient and scope | Orchestrator | Same context |
| 2. Build shared understanding | Orchestrator drafts and defends the proposal | Same context |
| 3. Audit the data contract | Scout | Same context |
| 4. Freeze artifacts | Analyst writes, Orchestrator confirms | Same context |
| 5. Validate design | Statistician | Recommended for confirmatory/high-stakes work |
| 6. Implement minimally | Analyst | Same context |
| 7. Audit independently | Adversary | **Required** whenever the platform can dispatch it |
| 8. Interpret with restraint | Analyst drafts, Statistician checks | Same context |
| 9. Update theory/writing | Theory-updater, Writer | Same context |

## Executing Roles As One Agent

Almost every real session is one agent moving through all nine SKILL.md steps
in the same conversation. That is expected, not a violation. The
Orchestrator's "does not analyze data" and similar lines describe what a
step's output must not smuggle in — for example, don't let orchestration
narration quietly decide an estimand — not a claim that a second body must
exist.

Two rules keep single-agent execution honest:

1. **Announce the switch.** Label each step's output with the role that
   produced it (for example, "Statistician review:" before a design check), so
   a reader can tell which hat produced which claim.
2. **Fresh context for the Adversary is a capability check, not a preference.**
   The Orchestrator asks whether the current platform can dispatch an
   independent sub-agent or session — a Task/Agent tool, a fresh conversation,
   a subprocess with its own context:
   - **If it can:** you MUST use it for step 7. Hand it only the paths listed
     in adversarial-review.md's Inputs section; do not include your own
     analysis narrative in its prompt or let it read this conversation.
   - **If it cannot:** perform the review yourself, but you must (a)
     re-derive every finding solely from the frozen artifacts — plan, config,
     code, results, logs — without relying on your own prior narrative in this
     conversation; and (b) record "self-review, independence not mechanically
     enforced" as a limitation in the verdict. This caps the verdict at
     PASS-WITH-RISKS; it can never be an unconditional PASS.

The Statistician's pre-analysis review benefits from the same independence but
it is advisory, not required: self-administer the checklist in
statistician-review.md explicitly and visibly, unless the analysis is
confirmatory or trips one of SKILL.md's compute/confirmation gates — then
dispatch independently just as for the Adversary.

## Handoff Rule

Pass minimal path-only context whenever possible. Never brief the adversary with
the analyst's interpretation. Surface conflicts rather than adjudicating them
silently — escalate unresolved role conflicts to the user as a scientific
decision (per the Operating Rule in SKILL.md); the Orchestrator does not
resolve them on its own authority.

## Gates

Human gates are for expensive or irreversible actions: confirmation split,
first real-data compute, and long compute. Hypothesis exploration can be cheap
and reversible, but it must remain labeled correctly.
