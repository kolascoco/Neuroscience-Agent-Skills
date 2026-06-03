---
type: repo-card
id: slicertms
title: SlicerTMS
source_url: https://github.com/lorifranke/SlicerTMS
tags:
  - slicertms
  - visualization
  - efield
  - 3d-slicer
---

## Role In The Skill

Use SlicerTMS for visualization-oriented planning around TMS targeting, E-field display, and 3D Slicer workflows. Keep it as experiment-planning/neuronavigation context, not preprocessing.

## Local Troubleshooting Notes

`TMS-EEG-artifacts/SlicerTMS_TROUBLESHOOTING.md` notes that SlicerDMRI modules may be required for fiber visualization and that UKFTractography can crash Slicer after SlicerDMRI installation. SlicerTMS should ideally continue loading non-fiber visualization when fiber modules are unavailable.

## Planning Use

Use for target visualization, communication of coil/field setup, and integration with Slicer-based anatomy workflows.

## Failure Modes

Missing SlicerDMRI modules, extension startup crashes, server environment missing `pyigtl`, `vtk`, `nibabel`, `torch`, or `numpy`, and confusing visualization with validated target engagement.

## Related Cards

`targeting/neuronavigation-and-efield.md`; `repos/simnibs.md`.
