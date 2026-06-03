---
type: code-recipe
id: load-mne-data
title: Load TMS-EEG Data With MNE
tags:
  - code:mne
  - step:data-intake
---

## Purpose

Template for loading data and printing metadata before preprocessing.

## Verify First

Use Context7 or GitHub fallback for current MNE reader APIs.

## Template

```python
from pathlib import Path
import mne

data_path = Path("PATH_TO_DATA")
data_format = "brainvision"  # TODO: fif, brainvision, eeglab, edf, bids, etc.

if data_format == "fif":
    raw = mne.io.read_raw_fif(data_path, preload=True)
elif data_format == "brainvision":
    raw = mne.io.read_raw_brainvision(data_path, preload=True)
elif data_format == "eeglab":
    raw = mne.io.read_raw_eeglab(data_path, preload=True)
else:
    raise ValueError(f"Add a verified reader for {data_format}")

print(raw)
print("Sampling rate:", raw.info["sfreq"])
print("Channels:", len(raw.ch_names))
print("Bad channels:", raw.info["bads"])
print("Annotations:", raw.annotations)

# TODO: set montage if needed and available.
# raw.set_montage("standard_1020")
```

## QC

Confirm sampling rate, channel types, montage, annotations, event channel, and condition labels before continuing.
