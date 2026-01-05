---
id: F014
title: Dynamic Visualization
category: analysis
status: canonical
maturity: established
bounded_context: [universal]
introduced_by: CC015
implementations: [Vizz3D, SynchroVis / ExplorViz, VR City, High-Rise, Getaviz, DynaCity]
related_features: [F015, F001, F058, F069]
supersedes: []
taxonomy:
  granularity: [class, function]
  visual_element: [building]
  metric_category: [behavior]
last_updated: 2026-01-05
updated_from: [CC015, CC053, CC106, CC080, CC071, CC108, CC131, CC133, CC137, CC084]
---

# Dynamic Visualization

## Problem & Motivation

Static city overviews explain structure, but many comprehension and performance questions depend on runtime behavior. CC015 highlights dynamic city visualizations as an underexplored direction; tools like ExplorViz and VR City overlay traces and timing/instance information to support runtime reasoning (CC053, CC106, CC108).

## Definition

Visualization of runtime program execution behavior within the city metaphor, including function calls, thread operations, timing data, and object instances — complementing static structural information.

## Context & Applicability

**Use when:**
- Investigating performance hotspots, runtime call paths, or inter-service communication using trace/monitoring data (CC053, CC106, CC108).
- You need to correlate runtime behavior with structural context (which components/classes are active) (CC053).

**Avoid when:**
- Instrumentation overhead or data sensitivity makes trace collection infeasible (production constraints).
- The system produces too much event volume without aggregation; the visualization would become unstable/noisy (CC084, CC108).

**Prerequisites:** A monitoring/tracing pipeline (e.g., Kieker/inspectIT/inTrace) plus mapping from runtime events to static entities and an aggregation/time-bucketing strategy (CC015, CC108, CC071, CC133).
**Alternatives:** [[evolution-visualization]] for version history signals, or selection-scoped dependency overlays when tracing is unavailable.

## Forces

| Force | Pull |
|-------|------|
| Fidelity vs. noise/stability | Show detailed runtime behavior, but avoid unstable visuals from high-volume, bursty traces. |
| Observability vs. overhead/privacy | Collect enough runtime data to be useful, but limit instrumentation overhead and sensitive-data exposure. |
| Real-time insight vs. reproducibility | Live views support diagnosis, but time-shift/replay is needed for repeatable analysis and communication. |

## Mechanism (Solution)

**Input**: Execution traces, profiler output, or monitoring data

**Process**:
1. Instrument program or collect traces
2. Map runtime events to visual elements
3. Animate or overlay on static city

**Output**: City with dynamic behavior visualization

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Connects runtime behavior to structural context (where are the active/hot components?). | Requires aggregation/filtering; otherwise becomes noisy and can undermine locality/orientation. |
| Enables runtime reasoning (calls, instances, timing) without leaving the city overview. | Depends on instrumentation/tracing pipelines and adds operational/privacy constraints. |

**Complexity**: Medium
**Performance**: Depends on analysis pipeline and refresh cadence.
**Cognitive Load**: Medium–High (interpretation requires metric literacy).

## Variations

| Tool/approach | Dynamic signal | Visualization pattern |
|---------------|----------------|-----------------------|
| ExplorViz | live monitoring + traces | time-shifted live snapshots; runtime communication/traces linked to landscape + application city (CC108, CC084, CC071). |
| VR City | recorded traces | “trace mode” highlights invoked methods as floors with per-trace colors (CC106). |
| DynaCity / Holoware | spans/transactions over time | time-bucket aggregation with recoloring + dynamic dependency arcs; step through buckets (CC133, CC137). |
| Getaviz | (dynamic model input) | positions the platform to accept dynamic behavior models for runtime-oriented analysis (CC131). |

## Implementation Notes

### Instrumentation Sources

From CC015 Table 1:

| Tool | Instrumentation | Data Captured |
|------|-----------------|---------------|
| Vizz3D | gprof (-pg) | timing, call graphs |
| SynchroVis / ExplorViz | Kieker traces | instances, calls, thread operations |
| VR City | inTrace traces | trace locations |
| High-Rise | ASM injection | real-time timing |

CC071 describes a later ExplorViz monitoring setup using the **inspectIT Ocelot** Java agent to continuously capture executed operations and update the city in 10-second snapshots.

CC108 describes an earlier ExplorViz monitoring pipeline using **Kieker** to collect live monitoring logs, consolidate them into traces (including trace-reduction techniques), and provide a time-shift mode for analyzing specific traces within a live stream.

CC084 (Fittkau’s dissertation) gives a full account of ExplorViz as a live-trace visualization approach for large software landscapes, including details of monitoring/analysis scalability and a time shift mode to analyze specific situations and traces.

CC131 notes that Getaviz can visualize software **behavior** and supports generator inputs that include a “dynamic” model, positioning the platform for runtime-oriented analyses such as bottleneck identification (the repository README does not specify the concrete instrumentation/tracing tooling).

CC133 (DynaCity) ingests ElasticSearch-exported span and transaction JSON files, aggregates durations into time buckets, and visualizes per-component activity and dynamic call dependencies over time by recoloring buildings and drawing per-call arcs. Users can step through time buckets (left/right arrows) to update the visualization.

CC137 (Holoware) contains additional dynamic-trace views in the same Unity city codebase, including:
- a “use case” view that draws arcs from ElasticSearch span JSON files and can step through points of interest, and
- an error-codes view that recolors buildings and arcs based on HTTP status categories while stepping through time frames.

### Dynamic Elements Visualized

From CC015:
- **Instances**: SynchroVis — "Each instance of a class is visualized as a storey on the building"
- **Threads**: SynchroVis — "colored arrows, allowing the visualization of concurrent behavior, communication and synchronization issues such as deadlock"
- **Timing**: High-Rise — building height proportional to time consumed
- **Call traces**: VR City — execution traces visualized as method-level highlights (see CC106)

### Research Gap

CC015 argues that, relative to static structure visualizations, city metaphors have been used less for making dynamic execution behavior understandable.

Opportunities identified:
- Data structures and access patterns
- Stack and heap allocation
- Input/output behavior

## Evidence

### Evidence (from CC106)

CC106 describes VR City’s “trace mode”:
- All buildings are first rendered in a uniform translucent/white style.
- Playing a recorded trace highlights invoked methods by coloring the corresponding **floors** within class buildings and reducing building transparency.
- Multiple traces can be compared via distinct colors; a reserved color indicates methods that appear in multiple traces.

CC106 uses the Eclipse **inTrace** plugin for recording traces without source-code modification, and supports custom trace filters.

### Evidence (from CC053)

CC053 positions ExplorViz as a dynamic-analysis tool providing **live trace visualization** of communication in large software landscapes and using the city metaphor at the application level to support program comprehension and collaboration.

### Evidence (from CC080)

CC080’s ExplorViz repository shows a live “landscape exchange” loop that periodically fetches the current landscape, plus a **time-shift** chart of method-call activity that can pause live updates and fetch historical snapshots. The repo also ships a Kieker monitoring configuration and a Kieker-backed record writer for incoming runtime events.

## Known Limitations

- Dynamic data is high-volume and noisy; aggregation and filtering are required for readability and performance (CC084, CC108).
- Instrumentation/tracing introduces overhead and may miss events depending on sampling/reduction (CC108, CC084).
- Frequently changing overlays can undermine locality/orientation unless updates are smoothed or time-shifted (CC108, CC071).

## Open Questions

- What aggregation levels (class/method/service) and time scales best support common runtime tasks (performance diagnosis, incident review, communication)?
- How should tools represent uncertainty and incompleteness in dynamic data (sampling, missing traces) to avoid false confidence?
- Can dynamic and static dependency views be meaningfully integrated without overwhelming the city (hybrid, toggles, progressive disclosure)?

## Sources

- [CC015] Jeffery survey — identifies dynamic visualization as underexplored area
- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz live trace visualization for landscapes + city metaphor at application level
- [CC106] Vincúr et al. (QRS-C 2017) — VR City trace mode (method-level highlights, trace comparison)
- [CC080] ExplorViz archived repo — landscape exchange loop, time-shift timeline, and Kieker-based monitoring
- [CC071] Krause et al. (2021) — ExplorViz live trace snapshots (inspectIT Ocelot) and heat-map overlays for runtime metrics
- [CC108] Fittkau et al. (VISSOFT 2013) — ExplorViz live trace visualization pipeline (Kieker monitoring, trace preprocessing/aggregation) and time-shift analysis
- [CC084] Fittkau dissertation (2015/2016) — ExplorViz live trace visualization for large software landscapes (monitoring/analysis + evaluation)
- [CC131] Getaviz repository — generator supports “dynamic” model inputs and positions Getaviz for behavioral/runtime analyses
- [CC133] DynaCity repository — ElasticSearch span aggregation into time buckets and dynamic dependency overlays in a Unity software city
- [CC137] Holoware software-city repository — use-case trace arcs and HTTP error-code-based dynamic dependency overlays

## See Also

- [[evolution-visualization]] — temporal changes across versions (different from runtime)
- [[city-metaphor]] — provides context for dynamic data
- [[heat-map-overlay]] — ground-plane heat map overlay for live runtime metrics
- [[time-shift-mode]] — pause/rewind live views to inspect earlier trace windows
