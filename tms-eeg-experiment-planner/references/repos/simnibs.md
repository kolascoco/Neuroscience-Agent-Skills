---
type: repo-card
id: simnibs
title: SimNIBS
source_url: https://simnibs.github.io/simnibs/build/html/index.html
github_fallback: https://github.com/simnibs/simnibs
tags:
  - simnibs
  - efield
  - neuronavigation
---

## Role In The Skill

Use SimNIBS for individualized TMS E-field simulation, target/dose planning, coil-position optimization, and documentation of stimulation geometry.

## Software Lookup Policy

Context7 did not resolve SimNIBS reliably in this session. Prefer the official SimNIBS documentation and GitHub fallback for current APIs.

## Workflow Concepts

Official docs describe a workflow of generating head models from MRI, setting up/running simulations via GUI or MATLAB/Python scripts, and visualizing E-field results. SimNIBS also supports advanced TMS coil-position optimization.

## Planning Use

Use SimNIBS before data collection when target depth, anatomy, coil orientation, individualized dose, or cross-subject comparability matters.

## Failure Modes

Treating E-field maximum as proof of physiological engagement; ignoring online TEP/artifact QC; using poor MRI/segmentation; not reporting coil pose.

## Related Cards

`targeting/neuronavigation-and-efield.md`; `repos/slicertms.md`; `repos/navinibs.md`.
