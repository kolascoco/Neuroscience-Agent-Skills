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

Sampling rate, event timing, artifact removal windows, target, number of trials, channel count, reference, and whether the user wants MATLAB/TESA or a Python approximation.

## Workflow Order

1. Remove/interpolate pulse artifact.
2. Inspect decay/recharge artifacts.
3. First ICA or artifact-focused decomposition to reduce muscle/noise components.
4. Filter after gross pulse handling.
5. Second ICA to remove ocular, auditory/sensory, and residual components.
6. Trial rejection, averaging, TEP metrics, and QC.

## Step Cards To Load

Load pulse, decay/recharge, muscle, filtering, ICA, ocular/auditory, TEP, and QC step cards.

## Parameter Defaults To Consider

Artifact windows and ICA settings must follow the dataset and verified TESA/tmseegpy documentation. Use placeholders if not confirmed.

## QC Checkpoints

Compare pre-cleaning and post-cleaning averages, component topographies/time courses, retained components, retained trials, and whether active/sham artifacts were affected differently.

## Common Failure Modes

ICA instability, component misclassification, overcorrection of early TEPs, insufficient trials, and treating TESA workflow order as universally optimal.

## Learning Mode Response

Explain why two passes may be used: one for large TMS-related artifacts and one for physiological/sensory artifacts after signal conditioning.

## Code-Engineer Mode Response

For MATLAB, verify TESA APIs. For Python, describe a TESA-inspired approximation and label it as such.

## Claims And Caveats

Two-pass ICA can be useful but is not automatically superior. It requires transparent component decisions and QC.
