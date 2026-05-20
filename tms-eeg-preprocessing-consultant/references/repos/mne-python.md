---
type: repo-card
id: mne-python
title: MNE-Python
source_url: https://mne.tools/
context7: preferred
github_fallback: https://github.com/mne-tools/mne-python
tags:
  - repo:mne-python
  - ecosystem:python
  - pipeline:mne
---

## Role In The Skill

Primary Python ecosystem for loading EEG data, event handling, filtering, epoching, ICA, evoked responses, topographies, and reports.

## Software Lookup Policy

1. If Context7 is available, resolve/query this library there for current API names, parameters, examples, and installation notes.
2. If Context7 is unavailable or incomplete, use the GitHub fallback URL below.
3. Do not invent function signatures. If uncertain, say which repo/source should be checked.

## What The Agent Should Reuse

MNE object model: `Raw`, `Epochs`, `Evoked`, event arrays, channel picks, annotations, ICA/reporting concepts.

## Workflow Concepts

Use explicit readers, preserve metadata, annotate bad segments, epoch from verified events, and report preprocessing decisions.

## Important Assumptions

MNE is general EEG/MEG infrastructure, not a TMS-EEG-specific guarantee. TMS artifact handling still needs domain-specific windows and QC.

## Useful Source Areas To Inspect

Documentation/examples for raw readers, events, filtering, ICA, epoching, evoked plotting, and reports.

## Failure Modes

Applying generic EEG defaults to pulse-contaminated data, filtering before pulse handling, and omitting TMS-specific QC.

## Related Cards

`pipelines/conservative-mne-python.md`; `recipes/*.md`.
