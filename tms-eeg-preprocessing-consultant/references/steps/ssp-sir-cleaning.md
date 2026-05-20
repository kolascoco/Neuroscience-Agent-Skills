---
type: step-card
id: ssp-sir-cleaning
title: SSP-SIR Cleaning
tags:
  - step:ssp-sir
applies_to:
  - sound-ssp-sir-enhanced
load_with:
  - repos/pytep-sound-ssp-sir.md
---

## Purpose

Apply projection/subspace methods to attenuate structured TMS-related artifacts when justified.

## When To Apply

After pulse handling and with verified method assumptions.

## Inputs Needed

Artifact definition windows, projection parameters, rank information, and validation plots.

## Decision Rules

Track rank and compare evoked responses before/after. Do not project away early responses without explicit justification.

## Method Options

Use verified SSP-SIR implementation, MNE projection primitives if applicable, or pseudocode with source-check notes.

## Learning Mode Explanation

Projection methods remove dimensions of the data; that can clean artifacts but can also remove meaningful signal.

## Code-Engineer Notes

Always print/report projection count and rank effects.

## QC Checks

Rank, projection vectors/topographies, pre/post TEPs, and residual artifacts.

## Failure Modes

Rank loss, overprojection, condition imbalance, and undocumented artifact windows.

## Sources

PyTEP-SOUND-SSP-SIR repo card; SOUND/SSP-SIR pipeline card.
