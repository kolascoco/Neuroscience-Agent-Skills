---
type: code-recipe
id: compute-teps-gmfa-lmfp
title: Compute TEPs, GMFA, And LMFP
tags:
  - code:mne
  - metric:tep
  - metric:gmfa
  - metric:lmfp
---

## Purpose

Template for creating epochs, evoked TEPs, GMFA, and LMFP.

Important: apply the chosen EEG reference to the full EEG channel set before computing GMFA/LMFP or selecting an LMFP ROI. Do not compute CAR after picking only ROI channels, because nearby ROI channels will reference against each other and can artificially suppress local activity.

## Template

```python
import numpy as np
import mne
from mne.preprocessing import compute_current_source_density

event_id = {"active": 1, "sham": 2}  # TODO: replace with actual IDs
tmin, tmax = -0.5, 0.5
baseline = (-0.2, -0.01)  # TODO: avoid contaminated baseline
reference_mode = "average"  # TODO: choose "average", "csd", or "already_referenced"

epochs = mne.Epochs(
    raw_clean,
    events,
    event_id=event_id,
    tmin=tmin,
    tmax=tmax,
    baseline=baseline,
    preload=True,
    reject_by_annotation=True,
)

if reference_mode == "average":
    # Common average reference across all EEG channels before ROI selection.
    epochs_features = epochs.copy().set_eeg_reference("average", projection=False)
elif reference_mode == "csd":
    # Surface Laplacian / current source density. Requires valid EEG montage.
    # Use for local topography/LMFP only when appropriate for the study.
    epochs_features = compute_current_source_density(epochs.copy())
elif reference_mode == "already_referenced":
    epochs_features = epochs.copy()
else:
    raise ValueError(f"Unknown reference_mode: {reference_mode}")

evokeds = {name: epochs_features[name].average() for name in event_id}

def compute_gmfa(evoked, picks="eeg"):
    data = evoked.copy().pick(picks).data
    return data.std(axis=0, ddof=0)

def compute_lmfp(evoked, roi_channels):
    # ROI is selected after full-channel re-referencing above.
    data = evoked.copy().pick_channels(roi_channels).data
    return data.std(axis=0, ddof=0)

gmfa = {name: compute_gmfa(evoked) for name, evoked in evokeds.items()}

roi_channels = ["C3", "Cz", "C4"]  # TODO: preregister or justify ROI
lmfp = {name: compute_lmfp(evoked, roi_channels) for name, evoked in evokeds.items()}
times = next(iter(evokeds.values())).times
```

## QC

Report retained epochs per condition, reference mode, channel picks, ROI channels, baseline, and time windows. Confirm that CAR/CSD/Laplacian was applied to the full EEG channel set before LMFP ROI selection. Do not interpret GMFA/LMFP as direct excitability measures.
