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

## Template

```python
import numpy as np
import mne

event_id = {"active": 1, "sham": 2}  # TODO: replace with actual IDs
tmin, tmax = -0.5, 0.5
baseline = (-0.2, -0.01)  # TODO: avoid contaminated baseline

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

evokeds = {name: epochs[name].average() for name in event_id}

def compute_gmfa(evoked, picks="eeg"):
    data = evoked.copy().pick(picks).data
    return data.std(axis=0, ddof=0)

def compute_lmfp(evoked, roi_channels):
    data = evoked.copy().pick_channels(roi_channels).data
    return data.std(axis=0, ddof=0)

gmfa = {name: compute_gmfa(evoked) for name, evoked in evokeds.items()}

roi_channels = ["C3", "Cz", "C4"]  # TODO: preregister or justify ROI
lmfp = {name: compute_lmfp(evoked, roi_channels) for name, evoked in evokeds.items()}
times = next(iter(evokeds.values())).times
```

## QC

Report retained epochs per condition, channel picks, ROI channels, baseline, and time windows. Do not interpret GMFA/LMFP as direct excitability measures.
