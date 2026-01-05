---
id: F017
title: Package-as-District Mapping
category: mapping
status: canonical
introduced_by: CC023
implementations: [CodeCity, CodeMetropolis, CodeCharta, GoCity, Code2City, Code2CityVR, JSCity, SoftVis3D, m3triCity, SecCityVR]
related_features: [F001, F002, F008, F021]
taxonomy:
  granularity: [package]
  visual_element: [district]
  metric_category: [size]
last_updated: 2026-01-03
updated_from: [CC009, CC017, CC020, CC023, CC024, CC035, CC036, CC038, CC040, CC059, CC091, CC093, CC102, CC104, CC069]
---

# Package-as-District Mapping

## Definition

A concept mapping where each package is rendered as a city district (a grouped ground area) that contains buildings for the package’s classes.

## Mechanism (from CC023)

**Input**: Package hierarchy + contained classes.

**Process**:
1. Create a district region per package.
2. Place buildings (classes) inside the district via a layout algorithm.
3. For nested packages, apply layout recursively and use topology cues to reflect nesting.

**Output**: A city where package structure provides the primary spatial organization.

## Sources

- [CC023] Wettel & Lanza (VISSOFT 2007) — packages as districts; classes as buildings
- [CC035] Wettel PhD thesis — concept mapping rationale + package-hierarchy organization
- [CC091] CodeCharta docs — folders as districts for file-level buildings
- [CC017] Wettel CodeCity homepage — packages depicted as districts
- [CC009] Romano et al. (2019) — Code2City/Code2CityVR (packages as districts)
- [CC020] Wettel & Lanza (ICSE 2008 tool demo) — packages depicted as districts (CodeCity)
- [CC024] Wettel & Lanza (WASDeTT 2008) — CodeCity nutshell mapping (packages as districts)
- [CC036] Viana et al. (arXiv 2017) — directories as districts and files as sub-districts in JSCity
- [CC038] SoftVis3D website — folders/packages as districts for file buildings
- [CC040] SoftVis3D repository — district layout implementation (file leaf nodes, parent package/directory nodes)
- [CC059] Pfahler et al. (2020) — packages depicted as districts in an evolving web-based city (m3triCity)
- [CC093] GoCity repository — folders rendered as districts
- [CC104] GoCity SANER 2019 — directories as districts in GoCity
- [CC102] Balogh & Beszedes (2013) — namespace plates organized as treemap-like districts
- [CC069] Wueppelmann & Yigitbas (2025) — package platforms for SecCityVR with treemap/bin-packing placement
