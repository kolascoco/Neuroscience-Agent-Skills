---
type: paper-card
id: wu-2018-artist
title: "ARTIST: A fully automated artifact rejection algorithm for single-pulse TMS-EEG data"
year: 2018
authors: Wu, Keller, Rogasch, Longwell, Shpigel, Rolle, Etkin
source_pdf: ../../../TMS-EEG-artifacts/articles/TMS-EEG/Human Brain Mapping - 2018 - Wu - ARTIST  A fully automated artifact rejection algorithm for single%E2%80%90pulse TMS%E2%80%90EEG data.pdf
doi: 10.1002/hbm.23938
tags:
  - pipeline:artist-aaratep
  - step:automated-rejection
  - caution:overcleaning
use_for:
  - automated artifact rejection
  - single-pulse TMS-EEG preprocessing
confidence: seed-card
---

## Why This Matters For The Agent

Core source for ARTIST-style automated artifact rejection in single-pulse TMS-EEG.

## Key Methods

Digest the full paper before extracting exact algorithm thresholds, validation metrics, or implementation details.

## Practical Recommendations

Use this card when the user asks for automated rejection, reproducible large-scale preprocessing, or ARTIST/AARATEP-style logic.

## Agent Rules Extracted

Automated rejection must remain auditable: report what was rejected, why, and how retained data differ by condition.

## Claims To Avoid

Do not present automated rejection as artifact-free preprocessing. Do not reimplement ARTIST from memory.

## Questions This Source Helps Answer

What is ARTIST? When is automated artifact rejection appropriate for single-pulse TMS-EEG?

## Related Cards

`pipelines/automated-artist-aaratep.md`; `steps/automated-artifact-rejection.md`; `repos/aaratep-pipeline.md`.
