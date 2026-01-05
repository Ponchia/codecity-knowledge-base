---
id: F046
title: Remodularization Analysis Mode
category: analysis
status: variant
introduced_by: CC106
implementations: [VR City]
related_features: [F010, F006]
taxonomy:
  granularity: [class]
  visual_element: [building]
  metric_category: [coupling]
last_updated: 2026-01-03
updated_from: [CC106]
---

# Remodularization Analysis Mode

## Definition

An analysis mode that supports remodularization tasks by comparing a coupling-driven layout against module/grouping assignments (e.g., packages or semantic clusters) using color encodings, helping reveal mismatches between coupling structure and current modular boundaries.

## Mechanism (from CC106)

**Input**: A coupling-aware city layout of classes plus a grouping assignment per class (package membership or semantic-cluster membership).

**Process**:
1. Choose a color scheme representing either package hierarchy or semantic clusters.
2. Color buildings accordingly (CC106 describes using similar colors for subpackages to reflect hierarchy).
3. Inspect how colored groups distribute across the coupling-driven geometry to identify cohesion/coupling issues and candidate remodularizations.

**Output**: A city view where module/group cohesion or fragmentation is visible as color segmentation over the coupling layout.

## Sources

- [CC106] Vincúr et al. (QRS-C 2017) — remodularization mode (package vs semantic-cluster coloring in VR City)

## See Also

- [[coupling-layout]] — spatial basis for modularity inspection
- [[color-mapping]] — mechanism used to encode group membership
