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
from mne.preprocessing import compute_current_source_density

reference_mode = "average"  # TODO: choose "average", "csd", or "already_referenced"

# Prefer starting from cleaned epochs so referencing is applied to all EEG channels
# before averaging and before selecting ROI channels.
if "epochs" in globals():
    if reference_mode == "average":
        epochs_features = epochs.copy().set_eeg_reference("average", projection=False)
    elif reference_mode == "csd":
        epochs_features = compute_current_source_density(epochs.copy())
    elif reference_mode == "already_referenced":
        epochs_features = epochs.copy()
    else:
        raise ValueError(f"Unknown reference_mode: {reference_mode}")
    evoked = epochs_features["active"].average()  # TODO: choose condition
else:
    # If only evokeds are available, verify they were referenced on all EEG
    # channels before ROI selection. Do not CAR only the ROI channels.
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
print("Reference mode:", reference_mode)
print("ROI mean amplitude:", itep_roi_global)

evoked.plot_joint(times=[np.mean(itep_window)])
```

## QC

Plot raw/interpolated traces with pulse and i-TEP windows marked; compare active vs sham/control; test nearby windows; report sampling rate, synchronization, reference mode, and whether reference/CSD was applied before ROI selection.
