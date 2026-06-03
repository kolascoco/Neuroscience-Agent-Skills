---
type: code-recipe
id: interpolate-pulse-artifact
title: Interpolate TMS Pulse Artifact Window
tags:
  - code:mne
  - step:pulse-interpolation
---

## Purpose

Template for replacing a short pulse artifact window with interpolation before filtering.

## Warning

This is a generic placeholder. Verify artifact window and method against dataset and selected library. For i-TEPs, the interpolation window is part of the scientific claim.

## Template

```python
import numpy as np

sfreq = raw.info["sfreq"]
pulse_samples = tms_events[:, 0]

tmin_art = -0.002  # TODO: seconds relative to pulse
tmax_art = 0.010   # TODO: seconds relative to pulse; justify for i-TEP

data = raw.get_data()
times = np.arange(data.shape[1])

for sample in pulse_samples:
    start = max(0, sample + int(round(tmin_art * sfreq)))
    stop = min(data.shape[1], sample + int(round(tmax_art * sfreq)))
    left = max(0, start - 1)
    right = min(data.shape[1] - 1, stop)

    if right <= left or stop <= start:
        continue

    for ch in range(data.shape[0]):
        data[ch, start:stop] = np.interp(
            times[start:stop],
            [left, right],
            [data[ch, left], data[ch, right]],
        )

raw_interp = raw.copy()
raw_interp._data = data
```

## QC

Plot raw and interpolated traces around pulse onset. Check for edge discontinuities, ringing after filtering, and condition-specific residuals.
