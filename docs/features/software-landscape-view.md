---
id: F041
title: Software Landscape View
category: analysis
status: variant
introduced_by: CC053
implementations: [ExplorViz, CrocoCosmos]
related_features: [F014, F001, F058]
taxonomy:
  granularity: [system]
  visual_element: [building, district]
  metric_category: [behavior]
last_updated: 2026-01-05
updated_from: [CC053, CC080, CC071, CC108, CC084, CC101]
---

# Software Landscape View

## Definition

A high-level view that visualizes a monitored **software landscape**—multiple servers and applications and their communication—to support system-level comprehension beyond a single application.

## Mechanism (from CC053)

**Input**: Monitoring/trace data describing applications and their interactions in a landscape.

**Process**:
1. Construct an overview model of the landscape (servers, applications, and communication between them).
2. Present this as a dedicated landscape-level visualization.
3. Allow switching/drilling down to an application-level view for deeper inspection.

**Output**: A multi-level visualization that connects system-level overview to application-level details.

## Additional Details (from CC108)

CC108 describes ExplorViz’s landscape level as a 2D visualization inspired by a mix of UML deployment and activity diagram elements:
- **Macro view**: shows application nodes and their communication; edges encode request volume (thickness) within a time window.
- **Aggregation for scalability**: similar node configurations may be combined into a single entity in the macro view.
- **Relationship view**: users can expand a combined entity to reveal its contained applications and their communication.
- **Micro view**: links from the landscape view into the corresponding system-level perspective for deeper inspection.

## Evidence (from CC080)

CC080’s README emphasizes live trace visualization of communication in **large software landscapes**, and confirms that ExplorViz uses a landscape-level perspective before drilling down into an application-level 3D city.

## Evidence (from CC084)

CC084 (Fittkau’s dissertation) positions ExplorViz as a live trace visualization approach for large software landscapes with a landscape-level perspective based on UML elements, linked to an application-level city metaphor view.

## Structural Software City Landscapes (from CC101)

CC101 introduces **software city landscapes** that combine multiple software cities to represent component-level architecture. Cities correspond to fine-grained components, and placement strategies are used to convey architectural structure and dependencies while preserving the internal city layouts.

## Sources

- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz landscape-level vs application-level perspectives
- [CC080] ExplorViz archived repo — README confirmation of landscape-level communication view
- [CC108] Fittkau et al. (VISSOFT 2013) — landscape-level view (UML-inspired), aggregation/expansion for scalability, and linking to system level
- [CC084] Fittkau dissertation (2015/2016) — ExplorViz landscape-level perspective + application-level software city metaphor view
- [CC101] Steinbrückner dissertation — software city landscapes and component-level placement strategies

## See Also

- [[heat-map-overlay]] — an application-level overlay available in ExplorViz’s city view
