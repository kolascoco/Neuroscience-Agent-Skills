---
type: repo-card
id: simnibs
title: SimNIBS
source_url: https://simnibs.github.io/simnibs/build/html/index.html
context7: preferred
github_fallback: https://github.com/simnibs/simnibs
tags:
  - repo:simnibs
  - ecosystem:python
  - topic:efield
---

## Role In The Skill

Secondary reference for stimulation targeting, E-field modeling, and experiment-planning context that may affect preprocessing interpretation.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

Targeting/E-field concepts, coil position/orientation context, and stimulation-dose reporting expectations.

## Workflow Concepts

Preprocessing interpretation can depend on target, coil geometry, and expected stimulated tissue.

## Important Assumptions

SimNIBS is not a TMS-EEG preprocessing toolbox; use it for targeting and E-field context only.

## Useful Source Areas To Inspect

Official docs, examples, tutorials, and Python API docs.

## Failure Modes

Mixing E-field modeling code into preprocessing answers unless the user asks for targeting/modeling.

## Related Cards

`tms-eeg-skills-bundle/tms-eeg-experiment-planner`; i-TEP target/topography discussions.
