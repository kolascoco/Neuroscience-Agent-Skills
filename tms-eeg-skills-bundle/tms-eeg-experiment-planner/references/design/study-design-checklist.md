---
type: design-card
id: study-design-checklist
title: TMS-EEG Study Design Checklist
tags:
  - study-design
  - checklist
---

## Purpose

Turn a research question into a pre-collection TMS-EEG protocol with explicit target, stimulation, control, acquisition, and QC decisions.

## Required Decisions

| Domain | Decisions |
|---|---|
| Scientific aim | target construct, hypothesis, primary endpoint, planned interpretation limits |
| Targeting | target coordinates/anatomy, backup target, neuronavigation/E-field plan |
| Coil setup | coil type, handle/current direction, initial orientation, orientation search plan |
| Intensity | RMT starting point, TEP/i-TEP online adjustment, safety maximum, artifact ceiling |
| EEG acquisition | cap/channel count, sampling rate, reference, electrode/lead layout, physiological channels |
| Hardware integration | recharge delay, pulse waveform/current direction, trigger synchronization, coil cooling if long blocks |
| Controls | sham, auditory masking, somatosensory control, active control target if needed |
| Trials | minimum usable trials, expected rejection, blocks/rest breaks, condition balance |
| Online QC | rt-TEP monitoring, single-trial artifact checks, early TEP go/no-go rule |
| Reporting | all settings needed to reproduce stimulation, EEG, controls, and preprocessing |

## Planning Rule

Optimize the experiment for interpretable TEPs, not just anatomical placement. A perfect target with weak early local response, strong muscle artifact, or poor sensory controls can still yield unusable data.

## Output Shape

When asked for a study plan, return:

- protocol summary
- participant/session flow
- stimulation settings and adjustment logic
- control/sham/masking plan
- online QC plan with go/no-go criteria
- trial count and reliability plan
- target-specific artifact risks
- reporting checklist

## Sources

Good-practice note; Hernandez-Pavon et al. 2023 recommendations card; rt-TEP and neuronavigation cards.
