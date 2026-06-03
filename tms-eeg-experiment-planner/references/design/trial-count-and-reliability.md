---
type: design-card
id: trial-count-and-reliability
title: Trial Count And Reliability Planning
tags:
  - trial-count
  - reliability
  - metric:tep
---

## Purpose

Plan enough pulses/trials for the target, endpoint, and expected artifact rejection rate.

## Decision Rules

- Trial count depends on target, TEP component, endpoint, trial rejection, and whether the goal is single-subject reliability or group-level inference.
- DLPFC and lateral/frontal targets may need more trials or stricter target selection because muscle and sensory confounds reduce reliability.
- For online rt-TEP adjustment, use short averages such as 10-30 trials as QC, not as the final reliability basis.
- For i-TEP or early local TEP endpoints, require enough trials to assess both amplitude and artifact stability.

## Planning Questions

- Is the endpoint peak amplitude, peak-to-peak, GMFA/LMFP, source TEP, i-TEP, behavior, or state-dependent modulation?
- What trial loss is expected from artifacts?
- Are active/sham/control conditions balanced?
- Is the target known to produce reliable early local TEPs?

## Output Rule

Give a trial-count plan as a range plus justification, and explicitly separate online QC averages from final-analysis trial requirements.

## Sources

Lioumis 2009 reproducibility; Gogulski 2024 DLPFC reliability; good-practice note.
