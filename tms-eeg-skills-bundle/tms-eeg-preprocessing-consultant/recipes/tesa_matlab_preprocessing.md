---
type: code-recipe
id: tesa-matlab-preprocessing
title: MATLAB EEGLAB/TESA Preprocessing Skeleton
tags:
  - code:matlab
  - language:matlab
  - ecosystem:eeglab
  - ecosystem:tesa
  - pipeline:tesa-inspired
---

## Purpose

MATLAB/EEGLAB/TESA skeleton for epoched single-pulse TMS-EEG preprocessing. Grounded in the local Science Factory lesson script and verified TESA function families.

## Verify First

Use Context7 `/nigelrogasch/tesa` or the GitHub fallback before writing unfamiliar TESA calls. The helper functions `setup_project_paths`, `prepare_epoched_events_for_tesa`, `apply_eeg_filter`, and `downsample_epoched_eeg` are project-specific and must not be assumed in other projects.

## Dependencies

```matlab
% Required:
% - MATLAB
% - EEGLAB
% - TESA EEGLAB plugin
% - FastICA package if using pop_tesa_fastica
```

## Template

```matlab
clear; close all; clc;

% TODO: set paths for EEGLAB, TESA plugin, FastICA, and data.
data_dir = 'PATH_TO_EEGLAB_SET_FILES';
out_dir = 'PATH_TO_OUTPUT';
data_name = 'SUBJECT_OR_EXAMPLE';

% Launch EEGLAB.
eeglab;

% Load epoched data. If data are continuous, epoch around the TMS trigger first.
EEG = pop_loadset('filename', [data_name, '.set'], 'filepath', data_dir);

% TODO: project-specific only; remove if unavailable.
% EEG = prepare_epoched_events_for_tesa(EEG);

% Baseline correction; verify the pre-TMS window is clean.
baseline_time_interval = [-50 -10]; % ms relative to TMS
EEG = pop_rmbase(EEG, baseline_time_interval, []);

% Initial visualization: common reference and average reference.
figure; pop_timtopo(EEG, [-150 190], [15 30 45 60 100], ...
    'Raw epoched data, common reference');
EEG_plot = pop_reref(EEG, []);
figure; pop_timtopo(EEG_plot, [-150 190], [15 30 45 60 100], ...
    'Raw epoched data, average reference');
clear EEG_plot;

% Inspect and remove/interpolate the TMS pulse artifact.
figure; pop_timtopo(EEG, [-5 10], [0.75 2 5 10], 'Pulse artifact check');

artifact_time_interval = [-2 12]; % TODO: verify from pulse/recharge QC
EEG = pop_tesa_removedata(EEG, artifact_time_interval);
EEG = pop_tesa_interpdata(EEG, 'cubic', [1 1]);

figure; pop_timtopo(EEG, [-5 20], NaN, 'After pulse interpolation');

% Save a full-channel reference dataset before removing bad channels.
EEG_tmp = EEG;
EEG_one_trial = pop_select(EEG_tmp, 'trial', 1);
pop_saveset(EEG_one_trial, 'filename', 'data_with_bad_channels.set', 'filepath', out_dir);
clear EEG_tmp EEG_one_trial;

% Manual bad-channel and bad-trial inspection.
EEG_plot = pop_reref(EEG, []);
figure; pop_plottopo(EEG_plot, [], 'Bad channel inspection', 0, ...
    'ydir', 1, 'ylim', [-20 20]);
pop_eegplot(EEG_plot, 1, 1, 1);
% TODO: after GUI selection, apply channel rejection to EEG as appropriate.
clear EEG_plot;

pop_eegplot(pop_reref(EEG, []), 1, 1, 1);
% TODO: reject selected bad trials via EEGLAB GUI or scripted criteria.

% ICA preparation and FastICA.
% In this SOUND/SSP-SIR order, use ICA for ocular, blink, eye-movement, and
% non-stimulus-locked/background muscle artifacts. Do not reject components
% with clear TMS-stimulus-locked activity or TMS-evoked muscle; handle those
% with artifact-window interpolation, projection/SSP-SIR, trial rejection, or
% target/protocol adjustment. Mark/exclude bad channels before ICA; repair
% them later with SOUND or interpolation rather than using them in ICA.
% Auditory/sensory-related activity is not removed by default; handle it with
% masking, sham/control contrasts, or justified ERP subtraction if needed.
EEG = pop_rmbase(EEG, baseline_time_interval, []);
EEG = pop_tesa_pcacompress(EEG, 'compVal', 20, 'plot', 'on');
EEG = pop_tesa_fastica(EEG, 'approach', 'symm', 'g', 'tanh', ...
    'stabilization', 'off');
EEG = pop_tesa_compplot(EEG, 'figSize', 'large', ...
    'plotTimeX', [-190 190], 'plotFreqX', [1 100], ...
    'freqScale', 'log', 'saveWeights', 'off');
% TODO: reject artifact components after review.

EEG = pop_rmbase(EEG, baseline_time_interval, []);
pop_saveset(EEG, 'filename', [data_name, '_after_ICA.set'], 'filepath', out_dir);

% SOUND: can replace removed channels if supplied the full-channel dataset.
data_with_all_channels = fullfile(out_dir, 'data_with_bad_channels.set');
lambda = 0.02; % TODO: tune with diagnostics; higher means more cleaning.
EEG = pop_tesa_sound(EEG, ...
    'lambdaValue', lambda, ...
    'iter', 10, ...
    'leadfieldInFile', [], ...
    'leadfieldChansFile', [], ...
    'replaceChans', data_with_all_channels, ...
    'multipleConds', []);
figure; pop_timtopo(EEG, [-100 190], [15 30 45 60 100], 'After SOUND');
pop_saveset(EEG, 'filename', [data_name, '_after_SOUND.set'], 'filepath', out_dir);

% SSP-SIR for remaining early TMS-evoked muscle artifact.
EEG = pop_tesa_sspsir(EEG, ...
    'artScale', 'manual', ...
    'timeRange', [-2 35], ... % TODO: verify artifact window
    'PC', []);
EEG = pop_rmbase(EEG, baseline_time_interval, []);
figure; pop_timtopo(EEG, [-50 190], [15 30 45 60 100], 'After SSP-SIR');
pop_saveset(EEG, 'filename', [data_name, '_after_SSPSIR.set'], 'filepath', out_dir);

% Optional second artifact removal/interpolation.
artifact_time_interval_2 = [-3 10]; % TODO: use only if QC justifies.
EEG = pop_tesa_removedata(EEG, artifact_time_interval_2);
EEG = pop_tesa_interpdata(EEG, 'cubic', [5 5]);

% Late analysis filtering. Avoid 1 Hz high-pass on short epochs; high-pass
% continuous data when needed, or use a separate ICA-training copy if justified.
% Apply analysis filters only after pulse/artifact-window handling and major
% artifact cleaning so filters do not spread sharp TMS artifacts into the TEP.
% TODO: replace apply_eeg_filter with verified EEGLAB/TESA filter calls if helper unavailable.
% EEG = apply_eeg_filter(EEG, 0, 80);
% EEG = apply_eeg_filter(EEG, 48, 52, 'revfilt', 1, 'plotfreqz', 1);
EEG = pop_rmbase(EEG, baseline_time_interval, []);

% Optional downsample/trim. Use verified helper or EEGLAB pop_resample.
% Do this only after pulse/artifact windows and timing have been checked.
% Reinspect early post-pulse traces for anti-alias/filter ringing afterward.
% EEG = downsample_epoched_eeg(EEG, 1000);
% EEG = pop_resample(EEG, 1000);
EEG = pop_select(EEG, 'time', [-1 1]);

% Final bad-trial inspection and visualization.
pop_eegplot(EEG, 1, 1, 1);
figure; pop_timtopo(EEG, [-100 190], [20 40 60 80], ...
    'Final cleaned TEPs');

% Before GMFA/LMFP or ROI feature calculation, apply the final reference to
% all EEG channels first. Do not average-reference only the ROI channels.
% EEG_features = pop_reref(EEG, []);  % CAR example for full-channel features.

pop_saveset(EEG, 'filename', [data_name, '_cleaned.set'], 'filepath', out_dir);
```

## QC Add-On

Compare final cleaned data against minimally preprocessed data in artifact-free windows. Large differences outside artifact windows may indicate preprocessing distortion.
