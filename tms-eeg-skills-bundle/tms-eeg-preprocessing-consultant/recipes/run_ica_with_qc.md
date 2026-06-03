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

ICA decisions are methodological decisions. Do not reject components without topography, time course, spectrum, and before/after TEP checks.

## Template

```python
from mne.preprocessing import ICA

raw_for_ica = raw_interp.copy()

# TODO: choose filters for ICA fitting after pulse artifact handling.
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
