---
type: paper-card
id: kabir-2024-large-scale-brain-state-dynamics
title: Influence of Large-Scale Brain State Dynamics on the Evoked Response to Brain Stimulation
year: 2024
authors: Kabir, Dhami, and colleagues
source_pdf: ../../../../TMS-EEG-artifacts/articles/nature of effects/Kabir_2024_JofNeuroscience_Influence_of_Large_Scale_Brain_Dynamics.pdf
doi: 10.1523/JNEUROSCI.0782-24.2024
tags:
  - target:dlpfc
  - state-dependency
  - metric:gmfa
  - metric:lmfa
  - preprocessing-example
use_for:
  - DLPFC state-dependent TEP interpretation
  - DLPFC preprocessing example
  - early GMFA/LMFA caveats
confidence: local-pdf-extracted
---

## Why This Matters For The Agent

This DLPFC TMS-EEG paper is useful both for state-dependency interpretation and as a concrete recent preprocessing example for prefrontal TMS-EEG.

## Main TEP Nature Points

The paper reports that stimulation during a Microstate C-like brain state was associated with stronger early evoked response measures up to about `80 ms`, replicated across sessions/datasets and absent during sham. Treat this as state-dependent DLPFC TEP evidence, not as proof that every early DLPFC response is artifact-free.

## Methodological Tips And Nuances

The methods remove data from `-2` to `10 ms` around the TMS pulse before downsampling and ICA. The pipeline then uses an ICA step for TMS decay artifact, filters, and a second ICA step for physiological artifacts. It also notes replacing the interpolated pulse segment with constant-amplitude data before each ICA step to avoid ICA distortion.

For DLPFC muscle-artifact advice, this paper supports the common pragmatic choice of removing/interpolating the earliest pulse/muscle-contaminated interval rather than interpreting it.

## Agent Rules Extracted

- Load for DLPFC state-dependency and early GMFA/LMFA questions.
- Mention the `-2` to `10 ms` artifact-removal example when discussing DLPFC early-window preprocessing.
- Keep state-dependency interpretation separate from artifact-removal validity.

## Claims To Avoid

Do not claim Microstate C effects prove direct local cortical excitability without sensory, muscle, and preprocessing caveats.

## Questions This Source Helps Answer

How did a recent DLPFC brain-state TMS-EEG study preprocess early TMS artifacts? How should state-dependent DLPFC TEP changes be interpreted?

## Related Cards

`papers/gogulski-2024-dlpfc-tep-reliability.md`; `steps/muscle-artifact-handling.md`; `artifacts/muscle-artifact.md`; `steps/ica-component-rejection.md`.
