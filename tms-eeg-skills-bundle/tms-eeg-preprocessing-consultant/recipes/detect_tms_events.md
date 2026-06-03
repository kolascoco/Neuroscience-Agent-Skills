---
type: code-recipe
id: detect-tms-events
title: Detect Or Verify TMS Events
tags:
  - code:mne
  - step:pulse-detection
---

## Purpose

Template for extracting TMS pulse events from triggers or annotations.

## Verify First

Confirm the real trigger channel and event IDs from acquisition notes.

## Template

```python
import mne

stim_channel = "STI 014"  # TODO: replace with actual trigger channel
tms_event_id = 1          # TODO: replace with actual TMS trigger code

events = mne.find_events(raw, stim_channel=stim_channel, shortest_event=1)
print("Events shape:", events.shape)
print("Unique event IDs:", sorted(set(events[:, 2])))

tms_events = events[events[:, 2] == tms_event_id]
print("TMS pulses:", len(tms_events))

raw.plot(events=tms_events, event_id={"TMS": tms_event_id}, duration=10)
```

## Fallback Pattern

If no trigger channel exists, detect pulse artifacts from a dedicated channel or EEG transient only as a fallback and visually validate all detected pulses.

## QC

Check event count, duplicates, missing pulses, inter-pulse interval, and alignment with visible pulse artifacts.
