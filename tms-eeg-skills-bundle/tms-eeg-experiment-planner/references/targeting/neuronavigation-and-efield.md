---
type: targeting-card
id: neuronavigation-and-efield
title: Neuronavigation And E-Field Planning
tags:
  - neuronavigation
  - efield
  - simnibs
  - slicertms
  - nexstim
---

## Purpose

Use neuronavigation and E-field modeling to improve target precision, reproducibility, and reporting.

## Planning Rules

- Use neuronavigation when comparing sessions, targets, subjects, or source-level TEPs.
- Save target coordinates, coil pose, coil orientation/current direction, head registration quality, and deviations.
- Use E-field simulation when individual anatomy, target depth/orientation, or dose estimates matter.
- If the lab has a Nexstim system, distinguish on-board real-time E-field navigation from offline simulation. Nexstim NBS / SmartFocus nTMS publicly describes MRI-based 3D rendering, multi-sphere E-field modeling, and dynamic recalculation of E-field location/orientation/magnitude as the coil is moved, turned, or tilted.
- E-field/neuronavigation improves target reporting but does not guarantee clean TEPs.
- Combine anatomical/E-field targeting with online TEP and artifact QC.

## Tool Roles

| Tool | Role |
|---|---|
| SimNIBS | individualized E-field simulation and dose/target planning |
| Nexstim NBS / SmartFocus / Eximia-style systems | commercial on-board E-field navigated TMS with real-time coil/E-field visualization during stimulation |
| SlicerTMS | visualization / Slicer-based TMS targeting and E-field/fiber display workflows |
| NaviNIBS | open-source neuronavigation, tracking, registration, and electrode digitization context |

## Nexstim / eXimia Notes

Older papers may refer to Nexstim Eximia/eXimia, while current public Nexstim pages emphasize NBS and SmartFocus nTMS. When the user says "eXima", interpret this as likely Nexstim Eximia/eXimia-style E-field navigated TMS, but verify the local system name/version before writing methods text.

For TMS-EEG planning, treat Nexstim on-board E-field navigation as an acquisition-time guidance and documentation tool. It can help maintain the estimated maximum E-field location, orientation, and magnitude over individual MRI anatomy while the operator adjusts coil position. It should be paired with online TEP/artifact QC because accurate E-field targeting does not by itself exclude muscle, auditory/somatosensory, pulse, decay, or lead-configuration artifacts.

## Output Rule

For target planning, return both an anatomical/E-field plan and a physiological/online-QC plan.

## Sources

Lioumis and Rosanova 2022; Nexstim technology and TMS-EEG pages; local SlicerTMS troubleshooting note; SimNIBS, Nexstim, NaviNIBS, and SlicerTMS repo cards.
