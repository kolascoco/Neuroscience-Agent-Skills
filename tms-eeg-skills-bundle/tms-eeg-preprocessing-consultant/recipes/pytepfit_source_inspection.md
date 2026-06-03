---
type: code-recipe
id: pytepfit-source-inspection
title: PyTepFit Source Inspection
tags:
  - pipeline:tepfit
  - code:python
---

## Purpose

Guide the agent to inspect PyTepFit before writing code, because this is a research reproduction repository rather than a stable preprocessing API.

## Verify First

Context7 did not resolve PyTepFit on 2026-05-19. Use the GitHub fallback:

```text
https://github.com/GriffithsLab/PyTepFit
```

## Inspection Checklist

```bash
git clone https://github.com/GriffithsLab/PyTepFit
cd PyTepFit
sed -n '1,220p' README.md
find nb tepfit -maxdepth 2 -type f | sort
sed -n '1,200p' requirements.txt
```

## Code-Writing Rule

Only write runnable PyTepFit code after confirming:

- expected folder structure
- required data and fsaverage paths
- notebook/script entry point
- model parameter names
- empirical TEP input format
- output metrics and figures

## QC

Report empirical TEP preprocessing status, model/data alignment, fit diagnostics, and assumptions about connectome, atlas, lead field, and optimization.
