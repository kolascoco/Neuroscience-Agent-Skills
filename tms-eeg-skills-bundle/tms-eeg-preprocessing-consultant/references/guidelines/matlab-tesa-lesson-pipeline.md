---
type: guideline-card
id: matlab-tesa-lesson-pipeline
title: MATLAB EEGLAB/TESA Lesson Pipeline
source_script: /Users/nikolaj_syrov/Documents/GitHub/TMS_EEG_SF_data_analysis/lesson1_data_preprocessing.m
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
3. Baseline correct with a clean pre-TMS window, e.g. `[-50 -10] ms` in the lesson.
4. Visualize raw TEPs and average-reference TEPs.
5. Inspect pulse artifact, remove a window such as `[-2 12] ms`, and interpolate with `pop_tesa_interpdata(..., 'cubic', [1 1])`.
6. Save one-trial dataset with full channel locations for later SOUND channel replacement.
7. Manually inspect and remove bad channels/trials.
8. Baseline correct and run PCA compression plus FastICA using `pop_tesa_pcacompress`, `pop_tesa_fastica`, and `pop_tesa_compplot`.
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
- The lesson places analysis filtering late, after pulse interpolation, bad channel/trial inspection, ICA, SOUND, SSP-SIR, and optional second artifact-window interpolation.
- The script comments that detrending or high-pass filtering can help ICA, but it also warns that filtering can create edge artifacts, remove slow components, and distort signals if applied before high-amplitude artifact removal.
- SOUND can extrapolate previously removed channels if supplied a full-channel reference dataset.
- SSP-SIR can use manual or automatic artifact windows; manual windows are preferable when known.
- Visual comparison with minimally processed data is a key QC step.

## Agent Rules Extracted

- For MATLAB/TESA answers, include visualization checkpoints after pulse removal, ICA, SOUND, SSP-SIR, filtering, and final cleaning.
- Use "filters late" as the default for epoched TMS-EEG analysis output. If an ICA-preparation filter is used, describe it as a separate training-data choice, not as the final analysis filter.
- Keep lesson helper functions separate from general TESA functions; mark them as project-specific.
- Do not treat the lesson's numeric parameters as universal defaults.
