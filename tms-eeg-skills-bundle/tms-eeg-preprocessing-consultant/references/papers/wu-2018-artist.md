---
type: paper-card
id: wu-2018-artist
title: "ARTIST: A fully automated artifact rejection algorithm for single-pulse TMS-EEG data"
year: 2018
authors: Wu, Keller, Rogasch, Longwell, Shpigel, Rolle, Etkin
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/Human Brain Mapping - 2018 - Wu - ARTIST  A fully automated artifact rejection algorithm for single%E2%80%90pulse TMS%E2%80%90EEG data.pdf
doi: 10.1002/hbm.23938
tags:
  - pipeline:artist-aaratep
  - step:automated-rejection
  - caution:overcleaning
use_for:
  - automated artifact rejection
  - single-pulse TMS-EEG preprocessing
confidence: seed-card
---

## Why This Matters For The Agent

Defines ARTIST (Automated aRTIfact rejection for Single-pulse TMS-EEG Data), the fully automated ICA-based rejection algorithm that AARATEP builds on. Core source for automated, reproducible single-pulse TMS-EEG cleaning and its validation logic.

## Key Methods

ICA decomposition into independent components, then a supervised pattern classifier trained on the spatio-temporal-spectral profile of neural vs. artefactual ICs (artifact classes include decay/residual-decay, TMS-evoked blink, vertical/horizontal eye movement, EKG, persistent EMG; neural ICs show dipolar maps and 1/f spectra). Three-stage workflow targeting different artifacts. Validated on n = 90 datasets across stimulation sites/subjects/populations/montages: ~95% IC-classification accuracy referenced to expert manual rejection; autocleaned and hand-cleaned data yield qualitatively similar group evoked waveforms; reported to outperform existing automated algorithms and relatively novice human cleaners.

## Practical Recommendations

Use when the user asks for automated rejection, reproducible large-scale preprocessing, or ARTIST/AARATEP-style logic. ARTIST classifies components but the algorithm and its accuracy are tied to the training distribution — verify it generalizes to a new montage/population, and still QC group and single-subject TEPs before/after.

## Agent Rules Extracted

Automated rejection must remain auditable: report what was rejected, why, and how retained data differ by condition. A classifier matching expert performance is not the same as ground-truth artifact removal — treat ~95% IC accuracy as agreement with manual labels, not proof of clean neural signal.

## Claims To Avoid

Do not present automated rejection as artifact-free preprocessing. Do not reimplement ARTIST from memory; verify function names/parameters against the repository.

## Questions This Source Helps Answer

What is ARTIST and what does it add over manual/semi-automated rejection? When is automated rejection appropriate for single-pulse TMS-EEG? How was it validated?

## Related Cards

`pipelines/automated-artist-aaratep.md`; `steps/automated-artifact-rejection.md`; `repos/aaratep-pipeline.md`; `papers/cline-2021-aaratep.md`; `artifacts/overcleaning-and-ica-risk.md`.
