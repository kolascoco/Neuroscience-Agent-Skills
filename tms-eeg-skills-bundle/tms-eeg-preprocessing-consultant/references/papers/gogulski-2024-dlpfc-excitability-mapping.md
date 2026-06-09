---
type: paper-card
id: gogulski-2024-dlpfc-excitability-mapping
title: Mapping cortical excitability in the human dorsolateral prefrontal cortex
year: 2024
authors: Gogulski, Cline, Ross, Truong, Sarkar, Parmigiani, Keller
source_pdf: ../../../../TMS-EEG-artifacts/new articles/1-s2.0-S1388245724001573-main.pdf
doi: 10.1016/j.clinph.2024.05.008
tags:
  - target:dlpfc
  - metric:tep
  - reliability
  - caution:causal-interpretation
use_for:
  - DLPFC TEP mapping
  - non-motor excitability caveats
  - target selection
confidence: seed-card
---

## Why This Matters For The Agent

Important for DLPFC-specific TEP analysis and the challenge of mapping "excitability" in a non-motor target.

## Main TEP Nature Points

DLPFC TEPs are target- and artifact-sensitive. Early-local TEPs (EL-TEPs, ~20–50 ms) vary strongly across dlPFC subregions: posterior-medial targets give the largest EL-TEPs (~100% larger than standard targets) and smallest muscle artifacts, while anterior-lateral targets show the largest artifacts. EL-TEP and artifact amplitudes are strongly negatively correlated (R ≈ −0.71). Personalized target/angle selection adds ~36% EL-TEP over the group-best target. Processing used an automated SOUND + decay-removal + two-round ICA + final-filter pipeline, with a high mean fraction of ICA components rejected (~61%). Cortical excitability language must be cautious and tied to operational measures.

## Methodological Tips And Nuances

Ask about target subregion, muscle artifact, sensory controls, early local responses, and reliability metrics. Standard "5 cm" / EEG-F3 DLPFC targeting is not optimal for EL-TEP quality; document the specific subregion and whether neuronavigation E-field equalization was used.

## Agent Rules Extracted

- Load for DLPFC target questions.
- Avoid generic DLPFC recommendations; target subregion matters.

## Claims To Avoid

Do not claim DLPFC TEP amplitude is a direct excitability measure without caveats.

## Questions This Source Helps Answer

How can cortical excitability be mapped in human DLPFC using TMS-EEG?

## Related Cards

`papers/gogulski-2024-dlpfc-tep-reliability.md`; `artifacts/muscle-artifact.md`.
