---
type: target-card
id: somatosensory-s1
title: Somatosensory / S1 TMS-EEG Planning
tags:
  - target:s1
  - target:somatosensory
  - tactile
  - sensory-confounds
  - sham
---

## Planning Focus

Use this card when the user wants to study tactile feeling, somatosensory cortex, S1/S2-adjacent targets, or subjective sensory perception with TMS-EEG.

## Main Risks

- Confusing TMS-evoked scalp sensation with cortical tactile processing.
- Interpreting late sensory PEP components as target-specific TEPs.
- Cranial/scalp muscle contamination if the coil activates face, jaw, temporal, or neck muscles.
- Target ambiguity between S1, S2, parietal operculum, PPC, or sensory-network effects.
- Expectancy and report bias when subjective tactile feeling is the endpoint.

## Required Design Decisions

- Anatomical or functional target definition.
- Whether the endpoint is EEG response, subjective tactile report, behavioral detection, or a combination.
- Sham/sensory-control strategy.
- Sensory rating scale and timing.
- Auditory masking and scalp-contact control.
- Whether an active control site is needed.
- Trial count sufficient for both EEG and perceptual report reliability.

## Practical Advice

- Define tactile feeling operationally before acquisition: location, quality, intensity, threshold, or detection report.
- Separate reports of coil click, scalp sensation, muscle twitch, and tactile percept.
- Use sham or sensory-only controls when interpreting subjective reports.
- If late N100/P180/P200-like components are central, require strong sensory controls because these windows are vulnerable to auditory/somatosensory PEPs.
- If early local components are central, require artifact-appearance checks, muscle inspection, lead/cable QC, and pulse/decay window reporting.
- Use neuronavigation and record coil orientation/current direction because S1/S2-adjacent effects can be spatially sensitive.

## Online QC

- Inspect single trials for muscle and decay artifacts.
- Track whether subjective tactile reports change with small coil shifts, intensity changes, or sham/sensory controls.
- Use short online averages to ensure the response is not dominated by sensory/muscle artifacts before full collection.

## Claims To Avoid

- Do not claim a participant's tactile feeling is cortical unless controls separate scalp stimulation, click, expectation, and muscle.
- Do not assume M1-derived TEP peak labels transfer directly to somatosensory targets.
- Do not infer neurotransmitter mechanisms from tactile TEP peaks without a specific pharmacological or validated paradigm.

## Sources

Local tactile-feeling notes; Hernandez-Pavon et al. 2023; Gordon et al. 2026 somatosensory inputs; Biabani et al. 2019 sensory inputs; relevant sham/control cards.
