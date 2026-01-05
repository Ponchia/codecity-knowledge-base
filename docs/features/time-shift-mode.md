---
id: F069
title: Time Shift Mode (Live Trace History Navigation)
category: analysis
status: variant
introduced_by: CC108
implementations: [SynchroVis / ExplorViz]
related_features: [F014, F041, F032, F033]
taxonomy:
  granularity: [system, class]
  visual_element: [district, building]
  metric_category: [behavior]
last_updated: 2026-01-04
updated_from: [CC108, CC080, CC084]
---

# Time Shift Mode (Live Trace History Navigation)

## Definition

A runtime-analysis control that lets users **shift away from “now”** to inspect earlier snapshots/time windows in a live monitoring visualization, supporting investigation of specific situations and traces without losing the system-level context.

## Mechanism

**Input**: Monitoring/trace stream plus a persisted history of snapshots/traces.

**Process**:
1. Provide a time control (e.g., a timeline) that selects a past point or window.
2. Fetch the corresponding historical snapshot/trace data from the backend.
3. Render the landscape/city based on the selected time range and allow returning to live mode.

**Output**: A live visualization that can be paused/rewound to analyze past runtime behavior.

## Evidence

CC108 and CC084 describe ExplorViz supporting time-shifted analysis of traces within a live stream, enabling retrospective inspection of specific situations.

CC080 shows a time-shift UI element (timeline) that can pause live updates and fetch historical landscapes/snapshots.

## Sources

- [CC108] Fittkau et al. (VISSOFT 2013) — ExplorViz time-shift mode for analyzing specific traces within a live stream
- [CC084] Fittkau dissertation (2015/2016) — time shift mode described as part of ExplorViz’s live trace visualization approach
- [CC080] ExplorViz archived repo — time-shift chart/timeline to pause live updates and fetch historical snapshots

## See Also

- [[dynamic-visualization]] — time shift is a navigation/control variant for dynamic trace views
- [[software-landscape-view]] — time shift applies at the landscape level as well as application-level views
- [[time-travel]] and [[timeline-visualization]] — related controls for evolution (version history), not runtime traces
