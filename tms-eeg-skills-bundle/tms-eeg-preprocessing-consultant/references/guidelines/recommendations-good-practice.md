---
type: guideline-card
id: recommendations-good-practice
title: TMS-EEG Recommendations, Instructions, And Good Practice
source_note: ../../../../TMS-EEG-artifacts/Recommendations, instructions, and good practice.md
tags:
  - recommendations
  - good-practice
  - acquisition
  - qc
  - metric:itep
---

## Why This Matters For The Agent

This card distills local good-practice notes into operational behavior for TMS-EEG preprocessing and TEP analysis. Use it when advice touches acquisition quality, online TEP monitoring, source analysis, i-TEPs, or experimental design.

## TEP Nature And Interpretation

- Treat early local TEP amplitude as a quality-control variable, not only as an outcome.
- If early local responses are weak, late N100-P200 activity may be dominated by auditory/sensory contamination.
- TEP morphology varies by target; do not expect one component shape to generalize.
- Natural-frequency interpretations should consider whether peaks are oscillatory cycles, not isolated components.

## Methodological Tips

- Use real-time TEP monitoring before formal acquisition when available.
- Use 10-30 trial online averages to check whether responses are large and clean enough.
- Optimize coil orientation and intensity empirically; fixed 45-degree orientation or fixed percent-RMT may be poor for non-motor targets.
- Rotate/reposition the coil when muscle artifacts appear, and verify the improvement online.
- Retune masking noise when stimulation intensity changes.
- For DLPFC, consider recording blinks beforehand so ICA has better ocular templates.

## i-TEP Nuances

- Very high sampling rates can reveal immediate TEPs hidden by conventional acquisition.
- The local notes cite 50 kHz EEG as reducing the pulse artifact to about 2 ms in an i-TEP context.
- For i-TEPs, active online QC is essential because relevant responses occur within a few milliseconds.
- Current-direction manipulations can help test whether early peaks simply invert with pulse-artifact polarity.

## Source Analysis And Topography

- Fit/scale head models to electrode positions and inspect electrode-to-head-model distances.
- Keep electrode-to-head-model distances below about 1 cm where possible.
- Do not trust goodness-of-fit alone; inspect dipole location, induced topography, and explained data.
- High pre-stimulus source activity can indicate filtering leakage or unstable source estimates.

## Agent Rules Extracted

- If advising acquisition, mention online single-trial and short-average QC.
- If advising preprocessing, mention that offline cleaning cannot recover every recharge/discharge/decay artifact.
- If advising source analysis, require electrode locations, reference, triggers, physiological channels, and head-model checks.
- If advising i-TEPs, require artifact window, sampling rate, online QC, and control-condition evidence.

## Claims To Avoid

- Do not present late TEPs as direct cortical activation when early local responses are weak and sensory controls are poor.
- Do not imply coil orientation/intensity choices are settled by RMT alone.
- Do not claim source-level results are reliable from goodness-of-fit alone.
