---
type: code-recipe
id: aaratep-matlab-skeleton
title: AARATEP MATLAB Skeleton
tags:
  - code:matlab
  - pipeline:artist-aaratep
---

## Purpose

Minimal MATLAB skeleton for AARATEP-style usage after verifying current repository APIs.

## Verify First

Use Context7 or GitHub fallback for `chriscline/AARATEPPipeline`. Confirm dependency paths, preparation helper names, required EEGLAB extensions, and current parameters.

## Template

```matlab
% TODO: verify paths for local machine and current AARATEP release.
addpath('AARATEPPipeline');
addpath('AARATEPPipeline/Common');
addpath('AARATEPPipeline/Common/EEGAnalysisCode');

% TODO: verify this helper and parameters against the repo README/source.
[EEG, misc] = c_TMSEEG_prepareForPreprocessing( ...
    'inputFilePath', 'PATH_TO_RECORDING.vhdr', ...
    'epochTimespan', [-1 2]);

% TODO: verify current main function signature and optional parameters.
EEG = c_TMSEEG_Preprocess_AARATEPPipeline(EEG, ...
    'pulseEvent', misc.pulseEvent, ...
    'epochTimespan', misc.epochTimespan, ...
    'outputDir', 'PATH_TO_DERIVATIVES', ...
    'outputFilePrefix', 'SUBJECT_OR_RECORDING_ID');
```

## QC

Archive logs and outputs for bad channels, interpolated artifacts, SOUND/decay cleaning, rejected ICs, retained trials, and before/after TEPs.
