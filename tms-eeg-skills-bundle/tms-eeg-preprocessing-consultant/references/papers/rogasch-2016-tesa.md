---
type: paper-card
id: rogasch-2016-tesa
title: TESA / TMS-EEG preprocessing reference
year: 2016
authors: Rogasch et al.
source_pdf: ../../../../TMS-EEG-artifacts/articles/TMS-EEG/rogasch2016.pdf
doi:
tags:
  - pipeline:tesa-inspired
  - step:ica
  - metric:tep
use_for:
  - TESA-style preprocessing
  - artifact cleaning rationale
confidence: seed-card
---

## Why This Matters For The Agent

Review and introduction of TESA (NeuroImage 147, 2017), the open-source EEGLAB extension for TMS-EEG. Core source for TESA-style preprocessing logic and for the taxonomy of TMS-EEG artifacts and the analysis-introduced artifacts that generic EEG pipelines create.

## Key Methods

Reviews artifacts and methods rather than reporting a single study; example data: 150 monophasic pulses over left superior parietal cortex at 68% of maximum stimulator output, 62-channel c-ring electrodes, digitized at 5 kHz (DC–1000 Hz), impedance <5 kΩ, epoched −1000 to 1000 ms. Distinguishes (1) the TMS pulse artifact — a very large (up to ~3 T field), brief (~200 µs) transient, 4–5 orders of magnitude larger than neural signal, that saturated older amplifiers; (2) capacitor recharge artifact (stimulator-dependent timing/shape); (3) TMS-evoked muscle artifact — biphasic, peaks ~4–5 and 7–10 ms, can exceed 1 mV, exponential decay >50 ms; (4) electrical/electrode artifacts (decay offsets, largest near the coil, ~50 ms to seconds); (5) movement, ocular, persistent-muscle, line-noise, and sensory (auditory/somatosensory) artifacts. Removal/minimization methods: sample-and-hold vs. DC-coupled high-rate amplifiers; cubic/linear interpolation of the pulse window; PCA suppression/compression (retain ~25–30 of 60 components); SSP/SSP-SIR; ICA (FastICA, EDM, infomax); detrending of decay-shaped artifacts; cautious filtering.

## Practical Recommendations

Remove or interpolate the pulse (and TMS-evoked muscle peaks) before filtering or ICA; filtering across them introduces ringing/ripple and drift. Prefer cubic interpolation when large transients (e.g., muscle) lie in the window; linear interpolation can leave high-frequency edges. For PCA before ICA, compress to ~25–30 components to avoid over-fitting and component splitting. Minimize muscle artifact at acquisition (coil toward midline, focal coils, lower intensity) rather than relying on cleaning. Handle auditory/somatosensory contributions by masking and matched controls, not default component removal.

## Agent Rules Extracted

TMS-EEG preprocessing requires domain-specific artifact handling, not generic EEG cleaning alone; the order of TMS-EEG steps necessarily departs from standard ERP pipelines. ICA assumes artifacts are temporally independent of and topographically separable from neural signal — both assumptions are imperfect for large TMS-evoked components, so verify before/after. No offline method is yet validated to fully recover neural signal under >1 mV muscle artifact.

## Claims To Avoid

Do not imply TESA choices are universally mandatory or that any single removal method is validated as ground-truth-accurate. Do not treat signal recovery after the pulse as recovery of clean neural signal.

## Questions This Source Helps Answer

What is the classical TESA-style preprocessing logic? Why must the pulse be handled before filtering/ICA? What are the main TMS-EEG artifact classes and their appearance? Why use PCA compression before ICA?

## Related Cards

`repos/tesa.md`; `pipelines/tesa-inspired-two-pass-ica.md`; `artifacts/pulse-artifact.md`; `artifacts/muscle-artifact.md`; `artifacts/filter-ringing.md`; `artifacts/overcleaning-and-ica-risk.md`.
