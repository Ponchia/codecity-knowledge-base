---
id: F045
title: Method-as-Floors Mapping
category: mapping
status: variant
introduced_by: CC106
implementations: [VR City, CodeMetropolis, SecCityVR, Getaviz, Code Arcades]
related_features: [F002, F027, F005, F057]
taxonomy:
  granularity: [method]
  visual_element: [floor]
  metric_category: [size]
last_updated: 2026-01-04
updated_from: [CC106, CC102, CC069, CC131, CC026]
---

# Method-as-Floors Mapping

## Definition

A fine-grained representation where methods are rendered as **floors (storeys)** within the building representing their class, enabling method-level inspection while preserving class-as-building structure.

## Mechanism (from CC106)

**Input**: Classes with declared methods and a per-method metric (e.g., LOC).

**Process**:
1. Represent each class as a building.
2. For each class, collect per-method metric values and sort them (descending).
3. Treat each value as a floor; size each floor by the metric (CC106 describes floors composed of blocks where the block count equals the metric value).
4. Stack floors to form the full building; optionally use floor height as another metric or a constant.

**Output**: Buildings whose internal floor structure exposes per-method metric distribution.

## Notes

CC106 reports that varying floor shapes can help visually distinguish interfaces, abstract classes, and ordinary classes without requiring separate overlays.

## Variations

| Implementation | Container | Notes |
|----------------|-----------|-------|
| VR City | class building | methods are stacked as floors within class buildings |
| CodeMetropolis | class district | methods are glass floors stacked inside a building container placed within the class district |
| SecCityVR | class building | method floors normally hidden; vulnerable methods rendered wider and colored by severity |
| Getaviz | class building | “City Floors” renders method-level elements as stacked floors inside class buildings |
| Code Arcades | class building | each method is a floor; windows designate method arguments (CC026) |

## Sources

- [CC106] Vincúr et al. (QRS-C 2017) — methods as floors composed of metric-sized blocks (VR City)
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis represents methods as floors
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR renders vulnerable methods as widened, colored floors
- [CC131] Getaviz repository — “City Floors” example output with method-level floors
- [CC026] Savidis & Vasilopoulos (ICSEng 2025 preprint) — methods as floors; windows encode method arguments

## See Also

- [[class-as-building]] — coarse-grained structure that floors refine
- [[method-as-bricks]] — alternative fine-grained method representation
- [[vulnerability-overlay]] — method-floor overlays for security findings (SecCityVR)
