---
type: pipeline-card
id: sound-ssp-sir-enhanced
title: SOUND/SSP-SIR Enhanced TMS-EEG Pipeline
tags:
  - pipeline:sound-ssp-sir
  - step:sound
  - step:ssp-sir
default_for:
  - source-informed denoising
  - PyTEP-SOUND-SSP-SIR discussions
  - comparing alternatives to ICA-heavy workflows
avoid_when:
  - no electrode positions or geometry needed by selected method
  - user needs a minimal first-pass workflow
step_cards:
  - steps/data-intake-and-metadata.md
  - steps/pulse-artifact-removal-or-interpolation.md
  - steps/sound-cleaning.md
  - steps/ssp-sir-cleaning.md
  - steps/tep-averaging.md
  - steps/gmfa-lmfp-computation.md
  - steps/qc-plots-and-reporting.md
artifact_cards:
  - artifacts/pulse-artifact.md
  - artifacts/overcleaning-and-ica-risk.md
repo_cards:
  - repos/pytep-sound-ssp-sir.md
  - repos/mne-python.md
paper_cards:
  - papers/methodological-choices-matter.md
  - papers/mutanen-2022-source-based-artifact-rejection.md
---

## Use When

Use when the user asks about SOUND, SSP-SIR, alternatives to ICA, or source/forward-model-informed artifact handling.

## Required Inputs

Raw or epoched data, montage/electrode locations, event timing, target, artifact window, and method-specific assumptions verified from source docs.

## Workflow Order

1. Load data, verify montage/channel coordinates, and reject missing/zero coordinate setups before SOUND/SSP-SIR.
2. Handle pulse artifact before filtering or model-based denoising.
3. Apply basic preprocessing with cautious filters and a clean pre-TMS baseline.
4. Apply SOUND where appropriate for channel-level noise suppression.
5. Inspect SSP-SIR components before choosing the number of PCs.
6. Apply SSP-SIR to early TMS-evoked muscle artifact when justified.
7. Run ICA after SSP-SIR for residual ocular, blink, decay, and non-early artifacts.
8. Compute TEP/GMFA/LMFP and QC before/after each major cleaning stage.

## Step Cards To Load

Load SOUND and SSP-SIR step cards plus pulse, TEP, metrics, and QC cards.

## Parameter Defaults To Consider

Use the starting values in `steps/ssp-sir-cleaning.md`, including pulse interpolation windows, cautious filter/baseline settings, SOUND `iter_num`/`lambda_val`, and SSP-SIR `art_scale`, `time_range`, `pc`, and `M`. Treat them as starting values requiring dataset QC, not universal defaults.

## QC Checkpoints

Show before/after butterfly plots around `0-100 ms`, GMFA/GFP, channel RMS/peak-to-peak diagnostics, topographies at TEP peaks, early TEP amplitude/latency, retained rank if projections are used, and condition-specific effects.

## Common Failure Modes

Applying model-based cleaning with missing geometry, using too aggressive `lambda_val` or `pc`, flattening early TEPs, rank loss, removing real evoked structure, and poor documentation of assumptions.

## Learning Mode Response

Explain how model/projection approaches differ from ICA and why they still require pulse-artifact precautions.

## Code-Engineer Mode Response

Use verified PyTEP-SOUND-SSP-SIR and MNE APIs. If unavailable, provide pseudocode with explicit source-check notes.

## Claims And Caveats

Model-based cleaning can reduce artifacts but does not remove the need for sham/control and early-latency caution.
