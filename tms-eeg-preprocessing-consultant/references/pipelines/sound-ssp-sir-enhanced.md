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
---

## Use When

Use when the user asks about SOUND, SSP-SIR, alternatives to ICA, or source/forward-model-informed artifact handling.

## Required Inputs

Raw or epoched data, montage/electrode locations, event timing, target, artifact window, and method-specific assumptions verified from source docs.

## Workflow Order

1. Load data and verify metadata.
2. Handle pulse artifact before model-based denoising.
3. Apply SOUND where appropriate for sensor noise suppression.
4. Apply SSP-SIR or related projection strategy for TMS-related artifact structure when justified.
5. Compute TEP/GMFA/LMFP and QC before/after each major cleaning stage.

## Step Cards To Load

Load SOUND and SSP-SIR step cards plus pulse, TEP, metrics, and QC cards.

## Parameter Defaults To Consider

Require verified repo/API details. Do not guess model parameters or geometry assumptions.

## QC Checkpoints

Show before/after signal variance, spatial maps, evoked responses, retained rank if projections are used, and condition-specific effects.

## Common Failure Modes

Applying model-based cleaning with missing geometry, rank loss, removing real evoked structure, and poor documentation of assumptions.

## Learning Mode Response

Explain how model/projection approaches differ from ICA and why they still require pulse-artifact precautions.

## Code-Engineer Mode Response

Use verified PyTEP-SOUND-SSP-SIR and MNE APIs. If unavailable, provide pseudocode with explicit source-check notes.

## Claims And Caveats

Model-based cleaning can reduce artifacts but does not remove the need for sham/control and early-latency caution.
