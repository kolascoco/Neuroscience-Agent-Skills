---
type: pipeline-card
id: automated-artist-aaratep
title: Automated ARTIST/AARATEP Pipeline
tags:
  - pipeline:artist-aaratep
  - ecosystem:matlab
  - ecosystem:eeglab
  - step:automated-rejection
default_for:
  - automated TMS-EEG artifact rejection
  - AARATEP pipeline discussions
  - reproducible MATLAB/EEGLAB preprocessing
avoid_when:
  - user requires pure Python/MNE code
  - automated decisions cannot be reviewed
  - dataset differs strongly from assumptions in source pipeline
step_cards:
  - steps/data-intake-and-metadata.md
  - steps/epoching-and-baseline.md
  - steps/pulse-artifact-removal-or-interpolation.md
  - steps/automated-artifact-rejection.md
  - steps/sound-cleaning.md
  - steps/amplifier-decay-and-recharge-artifacts.md
  - steps/filtering.md
  - steps/downsampling-and-resampling.md
  - steps/ica-component-rejection.md
  - steps/trial-rejection.md
  - steps/tep-averaging.md
  - steps/qc-plots-and-reporting.md
artifact_cards:
  - artifacts/pulse-artifact.md
  - artifacts/muscle-artifact.md
  - artifacts/auditory-somatosensory-confounds.md
  - artifacts/overcleaning-and-ica-risk.md
repo_cards:
  - repos/aaratep-pipeline.md
  - repos/tesa.md
paper_cards:
  - papers/wu-2018-artist.md
  - papers/cline-2021-aaratep.md
---

## Use When

Use when the user asks about ARTIST, AARATEP, automated TMS-EEG artifact rejection, or reproducible MATLAB/EEGLAB preprocessing pipelines.

## Required Inputs

EEGLAB-compatible data, event labels, pulse event, epoch timespan, sampling rate, output path, installed EEGLAB dependencies, ICLabel/TESA availability, and a plan for reviewing automated decisions.

## Workflow Order

Based on the AARATEP README, the pipeline stages include epoching, artifact interpolation with custom autoregressive blending, downsampling, baseline correction, high-pass filtering, bad-channel identification, early eye-related IC rejection, SOUND, decay component removal, a second artifact interpolation, line-noise filtering, ICA, IC rejection with ICLabel plus TMS-specific rules, low-pass filtering, and average rereferencing.

Treat the mid-pipeline high-pass step as part of that specific automated workflow, not as the advisor's default. When giving general TMS-EEG advice, prefer late analysis filtering after major TMS-specific artifact handling unless the user is reproducing AARATEP exactly.

Do not collapse all ARTIST-family workflows into this exact order. The original ARTIST summary is often described as pulse artifact removal, early downsampling, first ICA for decay, filters, epoching, bad epoch/channel handling, second ICA, average reference, and baseline. Treat AARATEP and ARTIST as related but not identical sources; load `pipeline-tables/preprocessing-step-order.md` when comparing them.

## Step Cards To Load

Load automated artifact rejection, pulse interpolation, SOUND, decay/recharge, filtering/downsampling, ICA, trial rejection, TEP averaging, and QC cards. Load the AARATEP repo card before writing MATLAB code.

## Parameter Defaults To Consider

Do not invent AARATEP parameters. Verify current names in Context7 or the GitHub fallback before producing runnable MATLAB.

## QC Checkpoints

Automated decisions must be auditable: bad channels, rejected ICs, interpolation windows, SOUND/decay outputs, retained trials, and before/after TEPs.

## Common Failure Modes

Treating automated rejection as ground truth, unreviewed ICLabel/TMS-specific IC decisions, dependency mismatch, hidden resampling/filtering assumptions, and applying AARATEP assumptions to incompatible recordings.

## Learning Mode Response

Explain automation as a reproducibility aid that still requires QC, not as a replacement for methodological judgment.

## Code-Engineer Mode Response

Use verified AARATEP entry points and README usage. If APIs are not verified, provide a MATLAB skeleton with explicit source-check placeholders.

## Claims And Caveats

Automated pipelines improve consistency but can systematically remove or preserve artifacts. Report decisions and run sensitivity/QC checks.
