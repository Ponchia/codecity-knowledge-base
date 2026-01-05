---
id: F046
title: Remodularization Analysis Mode
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC106
implementations: [VR City]
related_features: [F010, F006]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [coupling]
last_updated: 2026-01-05
updated_from: [CC106]
---

# Remodularization Analysis Mode

## Problem & Motivation

This capability helps connect analysis results to the system’s structural and spatial context. An analysis mode that supports remodularization tasks by comparing a coupling-driven layout against module/grouping assignments (e.g., packages or semantic clusters) using color encodings, helping reveal mismatches between coupling structure and current modular boundaries. Without it, findings stay detached from structural context, reducing explainability and prioritization.

## Definition

An analysis mode that supports remodularization tasks by comparing a coupling-driven layout against module/grouping assignments (e.g., packages or semantic clusters) using color encodings, helping reveal mismatches between coupling structure and current modular boundaries.

## Mechanism (Solution)

**Input**: A coupling-aware city layout of classes plus a grouping assignment per class (package membership or semantic-cluster membership).

**Process**:
1. Choose a color scheme representing either package hierarchy or semantic clusters.
2. Color buildings accordingly (CC106 describes using similar colors for subpackages to reflect hierarchy).
3. Inspect how colored groups distribute across the coupling-driven geometry to identify cohesion/coupling issues and candidate remodularizations.

**Output**: A city view where module/group cohesion or fragmentation is visible as color segmentation over the coupling layout.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Sources

- [CC106] Vincúr et al. (QRS-C 2017) — remodularization mode (package vs semantic-cluster coloring in VR City)

## See Also

- [[coupling-layout]] — spatial basis for modularity inspection
- [[color-mapping]] — mechanism used to encode group membership
