---
type: targeting-card
id: neuronavigation-and-efield
title: Neuronavigation And E-Field Planning
tags:
  - neuronavigation
  - efield
  - simnibs
  - slicertms
---

## Purpose

Use neuronavigation and E-field modeling to improve target precision, reproducibility, and reporting.

## Planning Rules

- Use neuronavigation when comparing sessions, targets, subjects, or source-level TEPs.
- Save target coordinates, coil pose, coil orientation/current direction, head registration quality, and deviations.
- Use E-field simulation when individual anatomy, target depth/orientation, or dose estimates matter.
- E-field/neuronavigation improves target reporting but does not guarantee clean TEPs.
- Combine anatomical/E-field targeting with online TEP and artifact QC.

## Tool Roles

| Tool | Role |
|---|---|
| SimNIBS | individualized E-field simulation and dose/target planning |
| SlicerTMS | visualization / Slicer-based TMS targeting and E-field/fiber display workflows |
| NaviNIBS | open-source neuronavigation, tracking, registration, and electrode digitization context |

## Output Rule

For target planning, return both an anatomical/E-field plan and a physiological/online-QC plan.

## Sources

Lioumis and Rosanova 2022; local SlicerTMS troubleshooting note; SimNIBS and SlicerTMS repo cards.
