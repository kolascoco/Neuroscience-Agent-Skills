---
type: pipeline-card
id: conservative-mne-python
title: Conservative MNE-Python TMS-EEG Pipeline
tags:
  - pipeline:mne
  - language:python
  - metric:tep
  - metric:gmfa
  - metric:lmfp
default_for:
  - first-pass preprocessing
  - Python code generation
  - TEP/GMFA/LMFP analysis
avoid_when:
  - no reliable TMS event timing
  - severe uncharacterized amplifier artifact
  - user needs a faithful TESA/EEGLAB workflow
step_cards:
  - steps/data-intake-and-metadata.md
  - steps/tms-pulse-detection.md
  - steps/pulse-artifact-removal-or-interpolation.md
  - steps/bad-channel-detection-and-interpolation.md
  - steps/filtering.md
  - steps/downsampling-and-resampling.md
  - steps/epoching-and-baseline.md
  - steps/ica-component-rejection.md
  - steps/trial-rejection.md
  - steps/tep-averaging.md
  - steps/gmfa-lmfp-computation.md
  - steps/qc-plots-and-reporting.md
artifact_cards:
  - artifacts/pulse-artifact.md
  - artifacts/muscle-artifact.md
  - artifacts/auditory-somatosensory-confounds.md
  - artifacts/overcleaning-and-ica-risk.md
  - artifacts/filter-ringing.md
repo_cards:
  - repos/mne-python.md
  - repos/tmseegpy.md
paper_cards:
  - papers/rogasch-2016-tesa.md
  - papers/methodological-choices-matter.md
---

## Use When

Use as the default Python-oriented workflow for TEP, GMFA, and LMFP analysis when the user needs practical code and has event timing plus sufficient metadata.

## Required Inputs

Data format, sampling rate, event channel or pulse timestamps, target, active/sham/control labels, EEG channel montage/reference, bad-channel policy, analysis window, and desired outputs.

## Workflow Order

1. Load data and metadata.
2. Detect/verify TMS pulse events.
3. Mark or interpolate the pulse artifact window before filtering.
4. Inspect amplifier decay/recharge and large muscle artifacts.
5. Mark bad channels and gross bad epochs.
6. Epoch and baseline with a defensible pre-pulse window if needed.
7. Mark bad channels before ICA and exclude them from decomposition; repair them after ICA using interpolation/SOUND or another documented channel-repair method. Run ICA or equivalent component cleaning for ocular, movement, and non-stimulus-locked/background artifacts. Do not remove TMS-evoked muscle or clear TMS-stimulus-locked components with ordinary ICA rejection. Do not remove auditory/sensory-related components by default; use masking, control-condition contrasts, or justified ERP subtraction if the analysis specifically requires it. If ICA needs a filtered copy, keep that copy separate from the final analysis data.
8. Filter the analysis data late and cautiously, usually after TMS-specific cleaning. Prefer low-pass/notch choices over early high-pass on short epochs.
9. Downsample only after pulse/timing QC and filtering-edge checks.
10. Reject remaining bad trials.
11. Apply the final feature reference across all EEG channels, usually CAR or justified Laplacian/CSD.
12. Average TEPs and compute GMFA/LMFP, selecting LMFP ROI channels only after the full-channel reference.
13. Generate QC plots and a processing log.

## Step Cards To Load

Load only the listed step cards needed for the user's request. For code-only requests, also load matching recipes.

## Parameter Defaults To Consider

Use placeholders for artifact windows, filter bands, baseline windows, and rejection thresholds unless the user's dataset or cited protocol defines them. Never present defaults as universal.

## QC Checkpoints

Raw pulse alignment, pre/post interpolation traces, bad-channel map, ICA component reports, retained trial counts by condition, reference mode, TEP butterfly/topography, GMFA/LMFP, and condition-specific artifact balance.

## Common Failure Modes

Filtering across unhandled pulse artifacts, using analysis filters too early, downsampling before pulse/timing QC, anti-alias/filter ringing, ICA fitted on dominated artifact periods, condition-specific trial loss, overcleaning cortical signal, event timing shifts, and interpreting sensory responses as cortical excitability.

## Learning Mode Response

Explain each step by artifact type and scientific risk: pulse first, then signal conditioning, then component cleaning, then metrics and QC.

## Code-Engineer Mode Response

Use recipes for loading, event detection, artifact interpolation, ICA, full-channel re-referencing, TEP averaging, GMFA/LMFP, and QC. Verify APIs through Context7 or GitHub fallback.

## Claims And Caveats

TEPs and GMFA/LMFP are scalp-level responses shaped by cortical, network, sensory, muscle, and preprocessing factors. Avoid pure excitability claims. If this pipeline's ICA step is used, note that ICA-based cleaning is associated with systematically smaller TEP amplitudes across all peaks (see `papers/methodological-choices-matter.md`); amplitude comparisons against ICA-free pipelines or normative values may partly reflect this rather than physiology.
