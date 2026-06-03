---
type: online-qc-card
id: itep-acquisition-practice
title: i-TEP Acquisition Practice
tags:
  - itep
  - early-latency
  - online-qc
---

## Purpose

Plan acquisition when immediate TEPs or very early post-pulse responses are endpoints or QC variables.

## Planning Rules

- Use very high temporal precision when i-TEPs are central.
- Separate the initial TMS-pulse artifact from later decay/back-to-baseline recovery.
- High sampling rate helps characterize and shorten the visible TMS-pulse artifact, but it does not fully solve decay artifacts.
- Treat stimulation intensity as an important determinant of decay/back-to-baseline duration.
- Manage scalp muscle activity actively with online inspection and small coil shifts.
- Require pulse artifact duration/recovery documentation.
- Track lead configuration and sampling/synchronization.
- Use current-direction/polarity controls when testing whether early peaks are neural rather than pulse-polarity artifacts.
- Do not interpret i-TEPs without control-condition and artifact evidence.

## Required Metadata

Sampling rate, amplifier/filter settings when available, trigger timing, pulse artifact window, decay/back-to-baseline timing, stimulation intensity, lead/cable configuration, coil orientation/current direction, target, artifact-control steps, and control conditions.

## Output Rule

For i-TEP studies, return a stricter acquisition protocol than for late TEPs, including early artifact go/no-go criteria.

## Sources

Beck et al. 2024; Nuyts et al. 2025; Lankinen et al. 2026; Stango et al. 2025; local good-practice note.
