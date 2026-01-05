---
id: F038
title: File-as-Building Mapping
category: mapping
status: variant
introduced_by: CC091
implementations: [CodeCharta, GoCity, SoftVis3D, BabiaXR-CodeCity]
related_features: [F001, F017, F005, F007, F006]
taxonomy:
  granularity: [file]
  visual_element: [building, district]
  metric_category: [size, complexity, quality]
last_updated: 2026-01-04
updated_from: [CC014, CC038, CC040, CC091, CC093, CC104, CC096]
---

# File-as-Building Mapping

## Definition

A concept mapping where each **file** is rendered as a building and folders form spatial districts, enabling city-like visualization at file granularity (useful for language-agnostic analysis and large codebases).

## Mechanism (from CC091)

**Input**: File/folder hierarchy + per-file metrics (e.g., LOC, complexity, churn, issues).

**Process**:
1. Build a tree model of folders and files.
2. Render each file node as a building.
3. Group buildings by folder as districts; apply a layout algorithm within each district.
4. Map chosen metrics to building footprint/height/color.

**Output**: A city where files are the primary “buildings” and folders provide districts.

## Variations

| Primary Entity | Typical Use Case | Example |
|----------------|------------------|---------|
| file | Language-independent overview; mixed-language repos | CodeCharta |
| class | OO-structure understanding at design level | CodeCity |

## Sources

- [CC091] CodeCharta docs — “each file becomes a building and each folder becomes a district”
- [CC014] CodeCharta website — reiterates file-as-building and folder-as-district mapping for code maps
- [CC038] SoftVis3D website — folders/packages as districts and files as buildings (SonarQube-integrated)
- [CC040] SoftVis3D repository — repo modules and UI confirm file-level buildings in the city metaphor
- [CC093] GoCity repository — files rendered as buildings in the GoCity mapping
- [CC104] GoCity SANER 2019 — files represented as buildings (structs stacked on top)
- [CC096] Moreno-Lumbreras et al. (2022) — BabiaXR-CodeCity maps files to buildings and directories to districts (web + VR)
