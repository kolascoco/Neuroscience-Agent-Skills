---
type: paper-card
id: gogulski-2024-dlpfc-tep-reliability
title: Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex
year: 2024
authors: Gogulski, Cline, Ross, and colleagues
source_pdf: ../../../../TMS-EEG-artifacts/new articles/bhae130.pdf
doi: 10.1093/cercor/bhae130
tags:
  - target:dlpfc
  - reliability
  - metric:tep
use_for:
  - DLPFC TEP reliability
  - trial-count and target-selection caveats
  - non-motor TEP methodology
confidence: seed-card
---

## Why This Matters For The Agent

Supports concrete discussion of DLPFC TEP reliability, a major bottleneck for prefrontal TMS-EEG.

## Main TEP Nature Points

Reliable DLPFC TEP measurement depends on target, artifact burden, quantification choices, and number of trials.

The paper explicitly links anterolateral dlPFC stimulation to larger early muscle artifacts around `0-20 ms`, citing Maki and Ilmoniemi, and notes that offline removal can mask or suppress the underlying early-local TEP. Medial/posterior dlPFC targets may yield larger and more reliable EL-TEPs partly because they produce weaker muscle activation.

## Methodological Tips And Nuances

Ask about DLPFC subregion, early local TEP window, ROI, quantification method, and trial count. The preprocessing example uses AARATEP, replacing `-2` to `12 ms` around each pulse with interpolated values, then includes early eye-ICA, SOUND, decay removal, a second ICA stage, and a second `-2` to `12 ms` interpolation before low-pass filtering and average rereferencing.

For reliability, the paper found later/wider early windows such as `20-60 ms` and `30-60 ms`, plus peak-to-peak quantification, often improved reliability compared with earlier/narrower windows.

## Agent Rules Extracted

- Load for DLPFC reliability or "how many trials?" questions.
- Mention that reliability is not uniform across DLPFC targets.
- When discussing preprocessing, state that the `-2` to `12 ms` interval was interpolated and should not be interpreted as physiological data.

## Claims To Avoid

Do not generalize reliability from one DLPFC target or metric to all prefrontal TMS-EEG. Do not treat the measured EL-TEP as free from muscle/preprocessing effects without checking target, analysis window, and preprocessing choices.

## Questions This Source Helps Answer

How reliable are DLPFC TMS-evoked potentials?

## Related Cards

`papers/gogulski-2024-dlpfc-excitability-mapping.md`; `papers/gogulski-2025-dlpfc-methodological-considerations.md`; `papers/maki-2011-projecting-muscle-artifacts.md`; `artifacts/muscle-artifact.md`.
