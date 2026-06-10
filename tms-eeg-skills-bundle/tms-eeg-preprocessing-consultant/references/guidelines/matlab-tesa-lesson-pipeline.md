---
type: guideline-card
id: matlab-tesa-lesson-pipeline
title: MATLAB EEGLAB/TESA Lesson Pipeline
source_script: lesson1_data_preprocessing.m (TMS_EEG_SF_data_analysis)
tags:
  - language:matlab
  - ecosystem:eeglab
  - ecosystem:tesa
  - pipeline:tesa-inspired
---

## Why This Matters For The Agent

This local teaching script provides a concrete MATLAB/EEGLAB/TESA preprocessing workflow for epoched TMS-EEG data. Use it to strengthen MATLAB code-generation answers while preserving dataset-specific placeholders.

## Dependencies

- MATLAB, tested in the source script with R2024b.
- EEGLAB, tested in the source script with 2024.1.
- TESA EEGLAB plugin, source script notes version 1.1.1.
- FastICA package.
- Project helper functions such as `setup_project_paths`, `prepare_epoched_events_for_tesa`, `apply_eeg_filter`, and `downsample_epoched_eeg` if using the lesson project structure.

## Workflow Summary

1. Initialize MATLAB, project paths, and EEGLAB.
2. Load an epoched EEGLAB `.set` dataset and prepare events for TESA.
3. Baseline correct with a clean pre-TMS window chosen for the protocol and current preprocessing stage.
4. Visualize raw TEPs and average-reference TEPs.
5. Inspect pulse artifact, remove the shortest justified pulse/muscle-contaminated window, and interpolate with `pop_tesa_interpdata(..., 'cubic', [1 1])`.
6. Save one-trial dataset with full channel locations for later SOUND channel replacement.
7. Manually inspect bad channels/trials. Exclude bad channels before ICA so they are not used in decomposition, while preserving a full-channel reference dataset for later SOUND/channel repair.
8. Baseline correct and run PCA compression plus FastICA using `pop_tesa_pcacompress`, `pop_tesa_fastica`, and `pop_tesa_compplot`; use this ICA stage for ocular, blink, eye-movement, and non-stimulus-locked/background muscle artifacts.
9. Run SOUND with `pop_tesa_sound`; the lesson notes SOUND transforms to average reference.
10. Run SSP-SIR with `pop_tesa_sspsir` for remaining TMS-evoked muscle artifact.
11. Optionally remove/interpolate a second artifact window.
12. Low-pass and notch filter; avoid unreliable high-pass filtering on short epochs.
13. Downsample and trim edges to reduce filtering edge effects.
14. Reinspect bad trials, visualize final TEPs, and save cleaned `.set`.
15. Compare cleaned data against minimally preprocessed raw data to detect preprocessing distortion.

## Methodological Nuances

- The source data are already epoched; normally epoching happens early in preprocessing.
- The lesson uses baseline correction rather than a 1 Hz high-pass on short epochs.
- The lesson places analysis filtering late, after pulse interpolation, bad channel/trial inspection, ICA for ocular/movement/background muscle artifacts, SOUND, SSP-SIR for early TMS-evoked muscle artifact, and optional second artifact-window interpolation.
- Do not use the pre-SOUND ICA stage to remove the early TMS-evoked muscle response or other clear TMS-stimulus-locked components; that artifact target is reserved for interpolation/projection/SSP-SIR or trial/target decisions in this workflow.
- The script comments that detrending or high-pass filtering can help ICA, but it also warns that filtering can create edge artifacts, remove slow components, and distort signals if applied before high-amplitude artifact removal.
- SOUND can extrapolate previously removed channels if supplied a full-channel reference dataset.
- SSP-SIR can use manual or automatic artifact windows; manual windows are preferable when known.
- Visual comparison with minimally processed data is a key QC step.

## Parameter Guidance

- Baseline `[-50 -10] ms` is usually a safe short baseline and can be useful after ICA and SOUND to adjust slow baseline shifts after interventions.
- Baseline correction is used to set the pre-TMS signal level to zero, so TEP amplitudes start from the same pre-pulse reference level rather than from an arbitrary voltage offset.
- Baseline `[-300 -5] ms` can be more robust because it uses more samples, but only if the interval is physiologically quiet for the experiment. Inspect the data and design carefully: do not include evoked activity, task-related preparation, residual artifact, or intervention-related drift that should not be subtracted. The `300 ms` length is not a magic value or universal truth; it is a practical choice that must fit the design and data.
- Pulse-only removal `[-2 3] ms` or `[-2 4] ms` is a good starting point for motor, parietal, or other targets where TMS-evoked muscle artifact does not strongly affect the signal. Even these short windows remove possible immediate TEP samples, so do not use them without caveat if the acquisition setup could record interpretable i-TEPs.
- Pulse/muscle removal `[-2 12] ms` is a reasonable recommendation for DLPFC TEPs or other cases with strong early muscle artifact that cannot be repaired. Some articles use `[-2 10] ms`. Inspect the actual pulse and muscle artifact and adjust per dataset; remove as little data as possible while still preventing the artifact from contaminating later cleaning and filtering.
- SOUND `lambdaValue=0.1` is a good starting point. Higher values produce stronger cleaning and greater risk of overcorrection, so adjust or increase only when diagnostics show residual channel-level noise and before/after TEP checks remain acceptable.

## Agent Rules Extracted

- For MATLAB/TESA answers, include visualization checkpoints after pulse removal, ICA, SOUND, SSP-SIR, filtering, and final cleaning.
- Use "filters late" as the default for epoched TMS-EEG analysis output. If an ICA-preparation filter is used, describe it as a separate training-data choice, not as the final analysis filter.
- Keep lesson helper functions separate from general TESA functions; mark them as project-specific.
- Do not treat the lesson's numeric parameters as universal defaults.
