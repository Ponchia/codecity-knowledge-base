---
id: F005
title: Height Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [Software World, CodeCity, SkyscrapAR, VizzAspectJ-3D, SynchroVis / ExplorViz, High-Rise, CodeCharta, CodeMetropolis, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, SoftViz3D, m3triCity, Langelier Quality Visualization Framework, SecCityVR]
related_features: [F002, F006, F018, F007]
taxonomy:
  granularity: [file, class, function, method]
  visual_element: [building, floor]
  metric_category: [size, evolution, behavior]
last_updated: 2026-01-03
updated_from: [CC009, CC015, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC043, CC059, CC075, CC091, CC093, CC102, CC103, CC104, CC069]
---

# Height Mapping

## Definition

A property mapping where the vertical dimension (height) of a building encodes a numeric metric of the represented software entity, creating a skyline where taller buildings indicate higher metric values.

## Mechanism

**Input**: Numeric metric value (e.g., NOM, LOC, churn, time)

**Process**:
- Linear scaling (simple baseline), or
- Discretized mapping into a small number of height categories (used in CodeCity as an optional strategy to keep overviews readable)

**Output**: Building height proportional to metric value

## Variations

| Implementation | Height Metric | Notes |
|----------------|---------------|-------|
| Software World | LOC / 10 | "one storey per 10 LOC" |
| CodeCity | # methods (NOM) | CC035 documents both identity mapping and optional binned strategies (boxplot/threshold) |
| Code2City / Code2CityVR | # methods (NOM) | CC009 describes NOM mapped to height in both desktop and VR variants. |
| CodeCity (tool demo) | # methods (NOM) | CC020 reiterates the same mapping: number of methods mapped to building height. |
| CodeCity (WASDeTT) | # methods (NOM) | CC024 reiterates the same mapping: number of methods mapped to building height. |
| SkyscrapAR | churn | change frequency |
| VizzAspectJ-3D | # pointcuts + advice | for aspects |
| SynchroVis / ExplorViz | # instances | each instance visualized as a storey |
| High-Rise | time | near real-time profiling (time window) |
| CodeMetropolis | LLOC or McCC | method floor height is configurable via mapping files (LLOC or complexity examples) |
| SecCityVR | LOC | class building height extruded to lines of code; method floor size/position derived from LOC within class |
| GoCity | # methods (NOM) | CC104 maps struct methods to height (and file-level methods for non-struct elements). |
| JSCity | LOC | CC036 maps function LOC to building height; for nested functions, parent height sums LOC across nested children. |
| CodeCharta | (user-selectable) | height metric is chosen interactively in the visualization |
| SoftVis3D | `ncloc` / `new_lines` / `duplicated_lines` | CC038 describes profile presets (default risk, leak period, duplicated lines). CC040 defines these as SonarQube metric IDs and shows that height (and footprint) can be scaled using selectable strategies (logarithmic/exponential/linear). |
| SoftViz3D | metric2 (or width) | CC043 maps an input metric to building height: if a second metric is provided, it drives height; otherwise height is set equal to the footprint side length (volume-based encoding). |
| m3triCity | (user-selectable) | CC059 describes choosing metrics for geometry (e.g., height and depth); the settings screenshot shows “Number of methods” as a height metric option. |
| Langelier Quality Visualization Framework | WMC (Weighted Methods per Class) | CC075 maps WMC to box height for size/complexity. |

## Dynamic Height

CC015 notes that some dynamic-oriented cities animate building heights to depict runtime properties such as instance counts or time spent, but also cautions that rapidly changing building geometry can weaken the “city” analogy.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — NOM mapped to height; category-based mapping strategies
- [CC035] Wettel PhD thesis — magnitude mapping + identity/boxplot/threshold mapper designs
- [CC015] Jeffery survey — later survey of height mapping across implementations
- [CC091] CodeCharta docs — interactive selection of height metric for file/building nodes
- [CC009] Romano et al. (2019) — NOM mapped to height in Code2City/Code2CityVR
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — number of methods mapped to building height (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — NOM mapped to height in CodeCity overview description
- [CC036] Viana et al. (arXiv 2017) — LOC mapped to height for function-level buildings in JSCity
- [CC038] SoftVis3D website — file buildings with configurable height metric (profiles + `ncloc`)
- [CC040] SoftVis3D repository — height metric IDs and scaling options (log/exponential/linear)
- [CC043] SoftViz3D repository — height derived from a second metric or from footprint (volume encoding)
- [CC059] Pfahler et al. (2020) — configurable height metric for evolving web-based city buildings (m3triCity)
- [CC075] Langelier et al. (ASE 2005) — WMC mapped to class box height
- [CC104] GoCity SANER 2019 — methods mapped to building height for structs/files
- [CC102] Balogh & Beszedes (2013) — CodeMetropolis maps method LLOC to floor height
- [CC103] Balogh et al. (2015) - CodeMetropolis height mapping via mapping file (LLOC or McCC examples)

## See Also

- [[color-mapping]] — complementary visual encoding
- [[base-mapping]] — footprint for second metric
