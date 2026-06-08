---
type: code-recipe
id: qc-report
title: QC Report Template
tags:
  - code:mne
  - step:qc
---

## Purpose

Template for a minimal auditable QC report.

## Template

```python
import mne

report = mne.Report(title="TMS-EEG preprocessing QC")

report.add_raw(raw, title="Raw data overview", psd=True)
report.add_raw(raw_interp, title="After pulse artifact interpolation", psd=True)

for name, evoked in evokeds.items():
    report.add_evokeds(evoked, titles=f"Evoked TEP: {name}")

# TODO: add ICA figures if saved.
# report.add_figure(fig, title="ICA components")

report.save("tms_eeg_qc_report.html", overwrite=True, open_browser=False)
```

## Include In Text Report

- data file and format
- sampling rate
- event detection method and event counts
- pulse artifact window
- filter settings
- bad channels and interpolated channels
- ICA/projection decisions
- rejected/retained trials per condition
- TEP/GMFA/LMFP/i-TEP windows
- reference mode for feature calculation; confirm CAR/Laplacian/CSD was applied before ROI selection for LMFP
- unresolved caveats
