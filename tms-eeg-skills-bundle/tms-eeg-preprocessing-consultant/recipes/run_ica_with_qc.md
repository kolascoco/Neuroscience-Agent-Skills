---
type: code-recipe
id: run-ica-with-qc
title: Run ICA With QC
tags:
  - code:mne
  - step:ica
---

## Purpose

Template for fitting ICA after pulse artifact handling and appropriate filtering.

## Warning

ICA decisions are methodological decisions. Mark bad channels before fitting ICA so they are not used in the decomposition; repair them afterward with interpolation, SOUND, or another documented channel-repair method. Do not reject components without topography, time course, spectrum, and before/after TEP checks. Do not reject components with clear TMS-stimulus-locked activity or TMS-evoked muscle morphology; use explicit artifact-window handling, projection/SSP-SIR, trial rejection, or target/protocol adjustment instead. Do not remove auditory/sensory-related components by default; use masking, control-condition contrasts, or justified ERP subtraction when needed.

## Template

```python
from mne.preprocessing import ICA

raw_for_ica = raw_interp.copy()

# Optional ICA-training filter after pulse artifact handling.
# Mark bad channels before this point so ICA does not fit noisy/dead channels.
# Keep this separate from the final analysis data; do not let an early
# high-pass silently become the TEP/GMFA/LMFP analysis waveform.
raw_for_ica.filter(l_freq=1.0, h_freq=None)

ica = ICA(
    n_components=0.99,  # TODO: confirm rank/data sufficiency
    method="fastica",
    random_state=97,
    max_iter="auto",
)
ica.fit(raw_for_ica)

ica.plot_components()
ica.plot_sources(raw_for_ica)

# TODO: choose components after review.
ica.exclude = []

raw_clean = raw_interp.copy()
ica.apply(raw_clean)
```

## QC

Save component maps, sources, excluded component IDs, before/after evoked responses, and retained trial counts.
