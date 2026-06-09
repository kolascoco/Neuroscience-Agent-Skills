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
  - steps/muscle-artifact-handling.md
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
  - papers/maki-2011-projecting-muscle-artifacts.md
  - papers/mutanen-2016-recovering-muscle-masked-teps.md
  - papers/mutanen-2022-source-based-artifact-rejection.md
---

## Use When

Use when the user asks about SOUND, SSP-SIR, alternatives to ICA, or source/forward-model-informed artifact handling.

## Required Inputs

Raw or epoched data, montage/electrode locations, event timing, target, artifact window, and method-specific assumptions verified from source docs.

## Workflow Order

1. Load data, verify montage/channel coordinates, and reject missing/zero coordinate setups before SOUND/SSP-SIR.
2. Handle pulse artifact before filtering or model-based denoising.
3. Apply baseline/diagnostic preprocessing as needed without broad analysis filtering.
4. If stereotyped ocular, blink, eye-movement, or non-stimulus-locked/background muscle artifacts are present, run ICA/component review here, before SOUND and SSP-SIR. This is the order used in the TESA SOUND/SSP-SIR example and the local MATLAB lesson. Do not use this ICA pass to remove TMS-evoked muscle artifacts or components with clear TMS-stimulus-locked activity; SSP-SIR/projection or explicit artifact-window handling is the safer route for those.
5. Apply SOUND where appropriate for channel-level noise suppression.
6. Inspect SSP-SIR components before choosing the number of PCs.
7. Apply SSP-SIR to early TMS-evoked muscle artifact when justified.
8. Optionally run a later ICA/component review only for residual stereotyped non-sensory artifacts that remain after SOUND/SSP-SIR, with explicit rank and before/after TEP QC. Auditory/sensory-related components are normally handled by masking, controls, contrasts, or justified subtraction rather than default ICA removal.
9. Apply low-pass/notch or other analysis filters late, after major TMS-specific cleaning, and inspect ringing.
10. Apply the final feature reference across all EEG channels, then compute TEP/GMFA/LMFP and QC before/after each major cleaning stage. Select LMFP ROI channels only after full-channel referencing.

Do not describe SOUND/SSP-SIR as a high-pass-first pipeline. The PyTEP/TESA SSP-SIR implementation estimates muscle-artifact topographies from an internal high-pass-filtered copy, and some published SOUND/SSP-SIR methods apply a 1 Hz high-pass before SOUND after earlier pulse handling, ICA/QC, and trial cleanup. For general advisor/code output, prefer pulse-window handling and major artifact cleaning before analysis filters. If reproducing a source-specific early high-pass, require explicit ringing QC and report exactly where the high-pass was applied.

## Step Cards To Load

Load SOUND and SSP-SIR step cards plus pulse, muscle artifact, TEP, metrics, and QC cards. For DLPFC or other lateral/frontal muscle-artifact cases, also load Maki 2011 and Mutanen 2016 paper cards.

## Parameter Defaults To Consider

Use the starting values in `steps/ssp-sir-cleaning.md`, including pulse interpolation windows, cautious late filter/baseline settings, SOUND `iter_num`/`lambda_val`, and SSP-SIR `art_scale`, `time_range`, `pc`, and `M`. Treat them as starting values requiring dataset QC, not universal defaults.

## QC Checkpoints

Show before/after butterfly plots around `0-100 ms`, GMFA/GFP, channel RMS/peak-to-peak diagnostics, topographies at TEP peaks, early TEP amplitude/latency, retained rank if projections are used, and condition-specific effects.

## Common Failure Modes

Applying model-based cleaning with missing geometry, using too aggressive `lambda_val` or `pc`, flattening early TEPs, rank loss, removing real evoked structure, and poor documentation of assumptions.

## Learning Mode Response

Explain how model/projection approaches differ from ICA, why they still require pulse-artifact precautions, and why ICA placement depends on the artifact target: ocular/movement ICA can precede SOUND/SSP-SIR, whereas TMS-evoked muscle and TMS-stimulus-locked components should not be removed by ordinary ICA rejection.

## Code-Engineer Mode Response

Use verified PyTEP-SOUND-SSP-SIR and MNE APIs. If unavailable, provide pseudocode with explicit source-check notes.

## Claims And Caveats

Model-based cleaning can reduce artifacts but does not remove the need for sham/control and early-latency caution. SSP-SIR over-projection of the early window can suppress genuine early cortical activity; because early local responses (<100 ms) feed later recurrent network dynamics, distorting them can cascade into the late TEP (Momi et al. 2023), so compare before/after topographies in the 0–60 ms window, not only GMFA. SOUND still requires valid electrode positions and forward-model assumptions — missing or inaccurate coordinates invalidate its noise estimates.
