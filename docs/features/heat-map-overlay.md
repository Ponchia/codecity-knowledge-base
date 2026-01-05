---
id: F058
title: Heat-Map Overlay (Dynamic Metrics)
category: analysis
status: variant
introduced_by: CC071
implementations: [SynchroVis / ExplorViz]
related_features: [F014, F041, F062]
taxonomy:
  granularity: [class]
  visual_element: [district, building]
  metric_category: [behavior]
last_updated: 2026-01-04
updated_from: [CC071, CC006]
---

# Heat-Map Overlay (Dynamic Metrics)

## Definition

An analysis overlay that renders a 2D heat map on the city ground/platforms to display live or recent runtime metrics (e.g., dynamic coupling) without recoloring buildings themselves.

## Mechanism (from CC071)

**Input**: Live execution traces (inspectIT Ocelot) aggregated into class-level metrics; user-selected metric at runtime.

**Process**:
1. ExplorViz updates the city on a fixed loop (default 10 seconds) using backend-provided monitoring/trace data.
2. On each update, compute per-class scores for the selected metric (heat-map mode is implemented in the frontend) and map scores to a heat-map color scale.
3. Draw heat-map patches on the application foundation plate beneath each class; link each class to its heat-map area with a thin line; reduce city opacity to improve visibility.
4. Allow users to switch metrics and select a heat-map time mode (via the heat-map legend controls).

**Output**: A city with an overlaid heat layer showing hotspots for the chosen runtime metric, refreshable live.

## Variations

| Mode | Description |
|------|-------------|
| Snapshot | Heat uses only current snapshot data. |
| Continuously aggregated | Each new score adds 50% of the previous score, so the heat map incorporates past runtime information. |
| Windowed | Heat shows the difference between the latest snapshot and one N time units ago (default 10); values can be negative or positive. |

## Sources

- [CC071] Krause et al. (2021) - Live heat-map overlays in ExplorViz web/AR with user-selectable metrics and snapshot modes

## See Also

- [[dynamic-visualization]] - live runtime depiction that the heat map augments
- [[software-landscape-view]] - ExplorViz landscape-level context for applications
- [[production-cost-overlay]] - broader class of overlays that annotate cities with operational signals
