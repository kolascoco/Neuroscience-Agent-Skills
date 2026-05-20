---
type: code-recipe
id: itep-early-window-analysis
title: i-TEP Early Window Analysis
tags:
  - code:mne
  - metric:itep
  - caution:early-latency
---

## Purpose

Template for early-window amplitude/topography analysis with artifact boundaries visible.

## Warning

Do not run i-TEP analysis unless pulse artifact, sampling/synchronization, lead configuration, and control conditions have been reviewed.

## Template

```python
import numpy as np

evoked = evokeds["active"]  # TODO: choose condition

pulse_artifact_window = (-0.002, 0.010)  # TODO: from protocol/QC
itep_window = (0.010, 0.030)             # TODO: justify from source/protocol
roi_channels = ["C3", "Cz", "C4"]        # TODO: define before analysis

times = evoked.times
win_mask = (times >= itep_window[0]) & (times <= itep_window[1])

roi_evoked = evoked.copy().pick_channels(roi_channels)
itep_roi_mean = roi_evoked.data[:, win_mask].mean(axis=1)
itep_roi_global = itep_roi_mean.mean()

print("Pulse artifact window:", pulse_artifact_window)
print("i-TEP window:", itep_window)
print("ROI channels:", roi_channels)
print("ROI mean amplitude:", itep_roi_global)

evoked.plot_joint(times=[np.mean(itep_window)])
```

## QC

Plot raw/interpolated traces with pulse and i-TEP windows marked; compare active vs sham/control; test nearby windows; report sampling rate and synchronization.
