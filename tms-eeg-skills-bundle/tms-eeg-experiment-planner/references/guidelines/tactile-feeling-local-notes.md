---
type: guideline-card
id: tactile-feeling-local-notes
title: EEG-TMS For Tactile Feeling Local Notes
source_file: EEG-TMS for tactile feeling .docx
tags:
  - tactile
  - somatosensory
  - tep-nature
  - experiment-planning
  - sensory-confounds
use_for:
  - planning tactile/somatosensory TMS-EEG questions
  - explaining TEPs and TMS-triggered oscillations to a learner
  - linking tactile-feeling designs to sensory-control caveats
confidence: local-notes
---

## Why This Matters For The Agent

This local DOCX is a study note rather than a peer-reviewed article. Use it as a routing and teaching aid for tactile/somatosensory TMS-EEG planning, then ground methodological claims in paper cards such as Hernandez-Pavon et al. 2023, Biabani et al. 2019, Gordon et al. 2018/2026, and i-TEP cards.

## Useful Points To Reuse

- TMS-EEG can provide an EEG endpoint for non-motor targets where MEPs are unavailable.
- TEPs are time-locked responses obtained by averaging trials.
- TEPs reflect a spatiotemporal mixture of excitatory and inhibitory postsynaptic potentials rather than a single physiological process.
- Early local peaks can be more target-related, but very early peaks may be contaminated by cranial muscle or residual pulse artifacts.
- Later components, especially around N100/P180/P200-like windows, may be strongly influenced by auditory and somatosensory inputs.
- TMS-triggered oscillations require distinguishing phase-locked evoked responses from non-phase-locked induced responses.
- Time-frequency analyses should be computed at the single-trial level when induced, non-phase-locked activity is the endpoint.

## Tactile/Somatosensory Planning Implications

For a tactile-feeling study, separate at least three concepts:

- cortical response to TMS at the target
- peripheral tactile/scalp sensation caused by the pulse
- subjective tactile feeling or perceptual report

The design should not interpret a scalp sensation or late sensory PEP as evidence of cortical tactile processing unless the sham/control and behavioral report structure support that claim.

## Recommended Design Additions

- Include explicit sensory ratings: click loudness, scalp sensation intensity, location, unpleasantness, and tactile/perceptual quality.
- Include a sham or sensory-control condition if the hypothesis depends on subjective tactile feeling.
- Consider active control sites when the question is target-specific rather than generic stimulation sensation.
- Record target, coil orientation, intensity, and current direction because TEP morphology depends on target, orientation, and stimulation strength.
- Plan auditory masking and retune it if intensity changes.
- Use online TEP/artifact QC to avoid collecting a tactile-perception dataset dominated by muscle, auditory, or somatosensory artifacts.

## Teaching Mode Notes

When explaining this topic to a beginner:

- Say that TMS causes a chain from E-field to neuronal activation, postsynaptic currents, volume conduction, and scalp EEG.
- Explain that TEPs are not just "the brain response"; they are the measured scalp-level result of brain activity plus sensory inputs, artifacts, and preprocessing choices.
- Explain that TMS-evoked and TMS-induced oscillations differ: evoked responses are phase-locked and survive averaging, induced responses may not be phase-locked and require single-trial time-frequency analysis.

## Claims To Avoid

- Do not state that TEPs are direct proof of tactile feeling.
- Do not present N100/P180/P200-like components as cortical tactile responses without sensory controls.
- Do not overstate neurotransmitter mappings for individual TEP peaks; use cautious language and cite source cards.
- Do not treat the local notes as a primary citation.

## Related Cards

- `references/papers/hernandez-pavon-2023-recommendations-open-issues.md`
- `references/design/sham-and-sensory-controls.md`
- `references/papers/gordon-2026-somatosensory-inputs.md`
- `references/targets/somatosensory-s1.md`
- `references/online-qc/rt-tep-monitoring.md`
