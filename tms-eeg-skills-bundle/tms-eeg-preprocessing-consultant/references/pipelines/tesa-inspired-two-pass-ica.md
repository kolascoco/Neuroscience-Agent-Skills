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
  - artifacts/filter-ringing.md
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
6. Inspect and mark/remove bad channels before ICA so they are not used in decomposition; keep a full-channel-location reference if SOUND or later interpolation will repair them. Inspect/remove bad trials.
7. Run PCA compression and FastICA; inspect components with TESA component plots. In SOUND/SSP-SIR-style TESA workflows, use this slot for ocular, blink, eye-movement, and non-stimulus-locked/background muscle artifacts, not for the early TMS-evoked muscle response that SSP-SIR will model. Do not reject components with clear TMS-stimulus-locked activity by ordinary ICA review.
8. Run SOUND when channel locations/lead field assumptions are acceptable.
9. Run SSP-SIR for remaining early TMS-evoked muscle artifact when justified.
10. Optionally remove/interpolate a second artifact window.
11. Filter after pulse/gross artifact handling; avoid unreliable high-pass filtering on short epochs.
12. Downsample/trim edges, reject remaining bad trials, visualize final TEPs, and save.
13. Compare cleaned data with minimally preprocessed data to detect preprocessing distortion.

Canonical TESA-style summaries may start with channel rejection before epoching, use a long pre-TMS baseline such as `-650` to `-250 ms`, downsample to `1 kHz` soon after pulse interpolation, then perform bad-epoch rejection, two ICA rounds, late bad-channel interpolation, average reference, and final baseline. The local lesson-script order in this card is a teaching variant, so verify the target source before writing methods text.

## Step Cards To Load

Load pulse, decay/recharge, muscle, filtering, ICA, SOUND, SSP-SIR, ocular/auditory, TEP, and QC step cards. For MATLAB code, load `recipes/tesa_matlab_preprocessing.md` and `guidelines/matlab-tesa-lesson-pipeline.md`.

## Parameter Defaults To Consider

Artifact windows and ICA settings must follow the dataset and verified TESA documentation. Lesson-script starting examples include baseline `[-50 -10] ms`, first pulse removal `[-2 12] ms` with cubic `[1 1]`, PCA compression `compVal=20`, SOUND `lambda=0.02`, SSP-SIR manual `timeRange=[-2 35]`, second removal `[-3 10]` with cubic `[5 5]`, low-pass `80 Hz`, notch `48-52 Hz`, downsample `1000 Hz`, and final time range `[-1 1] s`. Use as teaching-script examples, not universal defaults. If downsampling is used, apply it only after verifying pulse handling and inspect anti-alias/filter ringing around the pulse and interpolation boundaries.

## QC Checkpoints

Compare pre-cleaning and post-cleaning averages, average-reference topographies, pulse-window traces, component topographies/time courses/frequencies, SOUND/SSP-SIR outputs, retained components, retained trials, and whether cleaned data match minimally preprocessed data in artifact-free windows.

## Common Failure Modes

ICA instability, component misclassification, SOUND overcorrection, SSP-SIR overprojection, filtering short epochs too aggressively, overcorrection of early TEPs, insufficient trials, and treating lesson-script order as universally optimal.

## Learning Mode Response

Explain why two passes may be used, but keep the target of each pass explicit. For SOUND/SSP-SIR workflows, the practical physiological-artifact ICA slot is often before SOUND for ocular/movement artifacts; any later ICA pass should be framed as residual non-sensory cleanup after signal conditioning, not as a mandatory step. Auditory/sensory activity should usually be controlled or contrasted, not removed by default ICA rejection.

## Code-Engineer Mode Response

For MATLAB, use verified TESA/EEGLAB calls and state dependencies. For Python, describe a TESA-inspired approximation and label it as such.

## Claims And Caveats

Two-pass ICA can be useful but is not automatically superior. It requires transparent component decisions and QC. The independence assumption is partly violated by time-locked TMS-evoked activity, so components carrying real cortical responses can be misclassified; vary the rejected-component count by ±2 and check TEP stability (Rogasch et al. 2022). PCA compression before ICA is commonly set to retain ~25–30 components from a ~60-channel montage (Rogasch et al. 2017); for low-channel-count recordings this rank choice affects the decomposition. Varying a single step such as the decay-suppression method changes both early TEP amplitude and topography, so transparent parameter reporting is required for interpretation.
