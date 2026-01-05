---
id: F007
title: Base (Footprint) Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, CodeCharta, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, SoftViz3D, m3triCity]
related_features: [F001, F005, F018]
taxonomy:
  granularity: [file, class]
  visual_element: [building]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC009, CC015, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC043, CC059, CC091, CC093, CC102, CC104]
---

# Base (Footprint) Mapping

## Definition

A property mapping where a building’s footprint (length/width/area) encodes a metric, allowing a second quantitative dimension alongside height.

## Mechanism

**Input**: Numeric metric value.

**Process**: Scale a footprint dimension (or area) based on the metric, then render the building with that footprint.

**Output**: Buildings whose “base size” communicates a metric.

## Evidence (from CC023)

CC023 maps width and length to number of attributes (NOA), making “many attributes / few methods” classes appear like platforms (“parking lots”).

CC009 describes the same mapping in Code2City/Code2CityVR: building base size reflects NOA.

CC020 describes the same mapping in CodeCity: number of attributes is mapped to both width and length (the building’s footprint).

CC024 repeats the same mapping in a “nutshell” description of CodeCity (NOA mapped to base size).

CC036 maps the number of variables (NOV) to the building footprint/width for function-level buildings in JSCity.

CC093 maps the number of variables (NOV) to the building base size in GoCity. CC104 describes the same mapping using “number of attributes/fields” for structs (and for methods/attributes declared outside structs in files), which is consistent with Go’s field/variable terminology.

CC102 maps method cyclomatic complexity (McCC) to floor width and length in CodeMetropolis (method-as-floor representation).

CC091 documents CodeCharta mapping a user-selected “area” metric to the building footprint/area for file nodes.

CC038 describes SoftVis3D mapping a selected SonarQube metric (default: complexity) to building footprint for file buildings.

CC040 further shows SoftVis3D applying selectable scaling strategies (logarithmic/exponential/linear) to the footprint (mapped to both width and length).

CC043 maps an input metric to the building footprint side length in its 2D layout phase; in its dependency view, node footprint is derived from dependency counters and edge thickness is scaled by dependency counts.

CC059 describes choosing a metric for the **depth** of cuboids (in addition to height), making footprint/depth a configurable mapping parameter in m3triCity.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — NOA mapped to footprint
- [CC035] Wettel PhD thesis — magnitude mapping (NOA → width and length)
- [CC015] Jeffery survey — later description of the same mapping
- [CC091] CodeCharta docs — interactive selection of area metric for building footprint
- [CC009] Romano et al. (2019) — NOA mapped to building base size in Code2City/Code2CityVR
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — number of attributes mapped to building width+length (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — NOA mapped to base size in CodeCity overview description
- [CC036] Viana et al. (arXiv 2017) — NOV mapped to footprint/width for function-level buildings in JSCity
- [CC038] SoftVis3D website — configurable footprint metric for file buildings (default: complexity)
- [CC040] SoftVis3D repository — footprint scaling strategies and width+length mapping rule
- [CC043] SoftViz3D repository — footprint side length derived from input metrics/counters (structure and dependency views)
- [CC059] Pfahler et al. (2020) — configurable depth metric for cuboids in m3triCity (paired with height)
- [CC093] GoCity repository — NOV mapped to footprint/base size
- [CC104] GoCity SANER 2019 — struct/file attributes mapped to base size
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis maps McCC to floor width/length

## See Also

- [[height-mapping]] — typically paired with base mapping for two metrics
- [[class-as-building]] — common granularity where base mapping is practical
