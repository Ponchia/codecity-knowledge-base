---
id: I029
name: Code Arcades
origin: University of Crete + Alpha Omega Zed SA
year_introduced: 2025
status: research
source_refs: [CC026]
repo_url: null
demo_url: null
primary_language: C++
features_implemented: [F001, F002, F017, F045, F005, F006, F035, F063]
last_updated: 2026-01-04
updated_from: [CC026]
---

# Code Arcades

## Overview

Code Arcades is a 3D software city visualization system (ICSEng 2025 preprint) aimed at supporting program comprehension and quality supervision at scale. It renders packages as blocks (districts) and classes as buildings, shows methods as floors, visualizes multiple dependency types between classes, and provides an interactive GUI to change metric-to-visual mappings and rendering attributes.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | City/blocks/buildings metaphor for code structure. |
| [[F017]] package-as-district | Packages (namespaces or recovered components) as grouped blocks/areas. |
| [[F002]] class-as-building | Classes as buildings inside their package block. |
| [[F045]] method-as-floors | Methods stacked as floors; windows encode method arguments. |
| [[F005]] height-mapping | Building height emerges from the number of method floors (and/or method-size choices). |
| [[F006]] color-mapping | Encodes semantic qualifiers (e.g., access) and dependency direction/type using color. |
| [[F063]] configurable-grouping | Supports grouping by namespaces or architecture-recovery-derived components. |
| [[F035]] view-configuration | Interactive GUI to adjust rendering attributes (colors/dimensions/materials/textures) and metric encodings. |

## Technical Details (from CC026)

**Granularity**: package, class, method

**Visual Element**: districts/blocks, buildings, floors, edges

**Inputs**:
- Parsed C++ code (Clang Tooling + compilation database) with a global symbol table
- Architecture-recovery dependency analysis and clustering outputs (modules/components)
- Metrics and heuristics (e.g., size, commits/contributors/age used for ordering)

**Platform**: desktop 3D (Ogre3D renderer + Dear ImGui UI on OpenGL)

## Sources

- [CC026] Savidis & Vasilopoulos (ICSEng 2025 preprint) — Code Arcades features, architecture, and implementation stack

