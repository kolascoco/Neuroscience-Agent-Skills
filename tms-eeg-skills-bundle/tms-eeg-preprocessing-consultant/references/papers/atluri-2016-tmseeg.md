---
type: paper-card
id: atluri-2016-tmseeg
title: "TMSEEG: A MATLAB-Based Graphical User Interface for Processing Electrophysiological Signals during Transcranial Magnetic Stimulation"
year: 2016
authors:
  - Sravya Atluri
  - Matthew Frehlich
  - Ye Mei
  - Luis Garcia Dominguez
  - Nigel C. Rogasch
  - Willy Wong
  - Zafiris J. Daskalakis
  - Faranak Farzan
source_pdf:
doi: https://doi.org/10.3389/fncir.2016.00078
tags:
  - paper:tmseeg
  - ecosystem:matlab
  - ecosystem:eeglab
  - preprocessing
  - qc
use_for:
  - MATLAB GUI preprocessing workflows
  - step-by-step artifact QC
  - TMS artifact ordering rationale
confidence: medium
---

## Why This Matters For The Agent

This paper describes TMSEEG, a MATLAB/EEGLAB graphical workflow for TMS-EEG preprocessing. It is useful as a methodological source for staged artifact handling, visual QC after each step, and the distinction between large variable artifacts and consistent artifacts suitable for component-based removal.

## Key Methods

- MATLAB GUI built on EEGLAB data structures and common EEGLAB functions.
- Step-by-step workflow with saved intermediate datasets.
- Early handling of the large TMS pulse artifact before ICA-heavy processing.
- Repeated visual inspection of trials, channels, and average TEPs.
- ICA used after gross artifacts are handled, especially for decay and repeated physiological artifacts.

## Practical Recommendations

- Remove or interpolate the largest pulse-contaminated segment before filters/ICA when following the TMSEEG rationale.
- Inspect bad epochs/channels before ICA to reduce instability from sporadic artifacts.
- Use a second cleaning/QC pass after ICA and filtering, because residual bad epochs/channels may become clearer.
- Use before/after TEP views to monitor whether cleaning improves artifacts without erasing plausible evoked structure.

## Agent Rules Extracted

- Load this card when the user asks about TMSEEG, MATLAB GUI preprocessing, or interactive TMS-EEG QC.
- Explain that artifacts larger in amplitude/variance are commonly addressed early so they do not dominate decomposition.
- Treat TMSEEG's step order as one documented workflow, not as a universal standard.
- For runnable code, use current EEGLAB/TESA/source documentation rather than inventing MATLAB function signatures from memory.

## Claims To Avoid

- Do not claim TMSEEG or any GUI workflow guarantees artifact-free TEPs.
- Do not treat interactive visual approval as a replacement for reporting artifact windows, channel/trial rejection, IC decisions, reference, baseline, filters, and retained trials.

## Questions This Source Helps Answer

- Why remove the pulse artifact before ICA?
- Why inspect bad channels/trials before and after component cleaning?
- How can a MATLAB GUI structure preprocessing for novice and experienced users?

## Related Cards

- `pipeline-tables/preprocessing-step-order.md`
- `pipelines/tesa-inspired-two-pass-ica.md`
- `steps/pulse-artifact-removal-or-interpolation.md`
- `steps/ica-component-rejection.md`
- `steps/qc-plots-and-reporting.md`
