---
type: pipeline-card
id: tesa-inspired-two-pass-ica
title: TESA-Inspired Two-Pass ICA Pipeline
tags:
  - pipeline:tesa-inspired
  - ecosystem:matlab
  - step:ica
default_for:
  - TESA-style preprocessing explanations
  - MATLAB/EEGLAB code generation
  - EEGLAB .set teaching workflows
  - two-stage component cleaning
  - comparison with Python workflows
avoid_when:
  - user requires pure MNE implementation
  - insufficient trials for stable ICA
step_cards:
  - steps/pulse-artifact-removal-or-interpolation.md
  - steps/amplifier-decay-and-recharge-artifacts.md
  - steps/muscle-artifact-handling.md
  - steps/filtering.md
  - steps/ica-component-rejection.md
  - steps/sound-cleaning.md
  - steps/ssp-sir-cleaning.md
  - steps/ocular-cardiac-auditory-components.md
  - steps/tep-averaging.md
  - steps/qc-plots-and-reporting.md
artifact_cards:
  - artifacts/pulse-artifact.md
  - artifacts/muscle-artifact.md
  - artifacts/auditory-somatosensory-confounds.md
  - artifacts/overcleaning-and-ica-risk.md
repo_cards:
  - repos/tesa.md
paper_cards:
  - papers/rogasch-2016-tesa.md
  - papers/rogasch-designing-comparing-cleaning.md
---

## Use When

Use when the user asks for TESA logic, MATLAB/EEGLAB style preprocessing, two ICA passes, or canonical TMS-EEG cleaning rationale.

## Required Inputs

Sampling rate, event timing, artifact removal windows, target, number of trials, channel count, reference, EEGLAB `.set` path, channel locations, whether data are continuous or already epoched, and whether the user wants MATLAB/TESA or a Python approximation.

## Workflow Order

1. Initialize MATLAB paths, EEGLAB, TESA, and FastICA.
2. Load EEGLAB `.set` data and prepare events; epoch early if data are continuous.
3. Baseline correct and visualize raw/common-reference plus average-reference TEPs.
4. Inspect the pulse artifact, remove a window such as `[-2 12] ms`, and cubic-interpolate with TESA.
5. Save a full-channel-location reference dataset before bad-channel removal if SOUND will replace channels later.
6. Inspect/remove bad channels and bad trials.
7. Run PCA compression and FastICA; inspect components with TESA component plots.
8. Run SOUND when channel locations/lead field assumptions are acceptable.
9. Run SSP-SIR for remaining early TMS-evoked muscle artifact when justified.
10. Optionally remove/interpolate a second artifact window.
11. Filter after pulse/gross artifact handling; avoid unreliable high-pass filtering on short epochs.
12. Downsample/trim edges, reject remaining bad trials, visualize final TEPs, and save.
13. Compare cleaned data with minimally preprocessed data to detect preprocessing distortion.

## Step Cards To Load

Load pulse, decay/recharge, muscle, filtering, ICA, SOUND, SSP-SIR, ocular/auditory, TEP, and QC step cards. For MATLAB code, load `recipes/tesa_matlab_preprocessing.md` and `guidelines/matlab-tesa-lesson-pipeline.md`.

## Parameter Defaults To Consider

Artifact windows and ICA settings must follow the dataset and verified TESA documentation. Lesson-script starting examples include baseline `[-50 -10] ms`, first pulse removal `[-2 12] ms` with cubic `[1 1]`, PCA compression `compVal=20`, SOUND `lambda=0.02`, SSP-SIR manual `timeRange=[-2 35]`, second removal `[-3 10]` with cubic `[5 5]`, low-pass `80 Hz`, notch `48-52 Hz`, downsample `1000 Hz`, and final time range `[-1 1] s`. Use as teaching-script examples, not universal defaults. If downsampling is used, apply it only after verifying pulse handling and inspect anti-alias/filter ringing around the pulse and interpolation boundaries.

## QC Checkpoints

Compare pre-cleaning and post-cleaning averages, average-reference topographies, pulse-window traces, component topographies/time courses/frequencies, SOUND/SSP-SIR outputs, retained components, retained trials, and whether cleaned data match minimally preprocessed data in artifact-free windows.

## Common Failure Modes

ICA instability, component misclassification, SOUND overcorrection, SSP-SIR overprojection, filtering short epochs too aggressively, overcorrection of early TEPs, insufficient trials, and treating lesson-script order as universally optimal.

## Learning Mode Response

Explain why two passes may be used: one for large TMS-related artifacts and one for physiological/sensory artifacts after signal conditioning.

## Code-Engineer Mode Response

For MATLAB, use verified TESA/EEGLAB calls and state dependencies. For Python, describe a TESA-inspired approximation and label it as such.

## Claims And Caveats

Two-pass ICA can be useful but is not automatically superior. It requires transparent component decisions and QC.
