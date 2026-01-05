---
id: I024
name: CodeMetropolis
origin: University of Szeged (Department of Software Engineering)
year_introduced: 2013
status: maintained
source_refs: [CC102, CC103, CC130, CC140]
repo_url: https://github.com/codemetropolis/CodeMetropolis
demo_url: https://codemetropolis.github.io/CodeMetropolis/
primary_language: Java (toolchain) + legacy C# (.NET)
features_implemented: [F001, F008, F017, F054, F045, F005, F007, F016, F026, F035, F055, F056, F060]
last_updated: 2026-01-04
updated_from: [CC102, CC103, CC130, CC140]
---

# CodeMetropolis

## Overview

CodeMetropolis is a prototype converter that visualizes source code as a Minecraft city. A C# command-line tool consumes analysis graphs and generates a Minecraft world, using plates for namespace hierarchy (treemap layout), class districts as fenced grass areas, and method floors stacked within a class container. A later version integrates with Eclipse via a plug-in and Minecraft mod, enabling IDE-driven builds and synchronized navigation while the analysis runs in the background.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | Uses a metropolis/city analogy with buildings, districts, and gardens. |
| [[F008]] treemap-layout | Namespace plates are arranged like a tree-map to fit contained elements. |
| [[F017]] package-as-district | Namespaces are represented as plates (grouping surfaces). |
| [[F054]] class-as-district | Each class is a fenced grass district containing the method structure. |
| [[F045]] method-as-floors | Methods are stacked as glass floors within a class container. |
| [[F005]] height-mapping | Floor height encodes method size (LLOC; later configurable via mapping files). |
| [[F007]] base-mapping | Floor width/length encode method complexity (McCC). |
| [[F016]] texture-mapping | Floor wall material encodes number of statements (NOS). |
| [[F026]] navigation-modes | Supports walking (street-level) and flying (bird's-eye view). |
| [[F035]] view-configuration | Mapping files define which metrics drive visual attributes. |
| [[F055]] multilevel-visualization | Level of detail depends on viewing distance (fly vs walk). |
| [[F056]] ide-synchronized-navigation | Eclipse plug-in provides jump/follow navigation to the active file. |
| [[F060]] danger-hazard-mapping | Floors/cellars with a `danger` attribute render as “dungeons” (spawner + loot chests). |

## Technical Details

**Granularity**: namespace, class, method

**Visual Element**: plate (namespace), district (class), floor (method)

**Metrics Supported**:
- McCC (floor width/length)
- LLOC (floor height)
- NOS (floor material)

**Platform**: game engine (Minecraft)

## Implementation Notes (from CC102/CC103)

- **Input**: CC102 uses Columbus tool output graphs (containment edges); CC103 integrates SourceMeter for metrics/structure when launched from Eclipse.
- **Rendering pipeline**: C# CLI converter generates a Minecraft world using the Substrate .NET library.
- **Scaling**: Metric values are normalized to a 4-25 block range for floor dimensions.
- **Labels**: Post/wall signs display entity names at close range.
- **Eclipse integration**: Plug-in adds build, jump, and follow actions plus settings for mapping file location.
- **Minecraft mod**: Disables UI during rebuilds and allows external processes to reposition the player.
- **Performance**: CC103 reports a new placing algorithm and a build system that is ~100x faster.
- **Status**: Prototype with hardcoded mappings; future work includes annotations, history replay, and testing overlays.

## Current Toolchain (from CC130)

CC130 documents a modernized CodeMetropolis toolchain implemented as multiple Java CLI tools (and a GUI wrapper):

- **Pipeline**: `converter` (SourceMeter or SonarQube -> CDF) → `mapping` (CDF + mapping XML -> CMXML/IXML) → `placing` (layout) → `rendering` (Minecraft world).
- **Mapping file**: XML-based mappings support conversions such as normalization and quantization, and can bind multiple metrics to multiple visual attributes.
- **GUI execution**: the GUI runs the full toolchain end-to-end and stores intermediate files under the user’s Minecraft folder (in a `.code-metropolis/<timestamp>` directory).
- **Gamified encoding**: the rendering module interprets a `danger` attribute on floors/cellars to place mob spawners and loot chests (see [[danger-hazard-mapping]]).

## Website Notes (from CC140)

CC140’s “In a nutshell” page describes CodeMetropolis as a Minecraft-based city-metaphor visualization and presents the toolchain stages (CDF converter, mapping, placing, rendering). It also directs users to GitHub releases for stable binaries.

## Early User Feedback (from CC102)

CC102 reports six interviews with lecturers, students, and industry developers. Key themes:

- **Navigation pain point**: large worlds create long travel distances; suggested solutions include a map/minimap and teleportation.
- **Limited simultaneous encodings**: users could easily perceive only width/length/height at once.
- **Motivation/expressiveness**: participants highlighted the “work while you play” aspect and the metaphor’s expressive power.

## Sources

- [CC102] Balogh & Beszedes (2013) - CodeMetropolis Minecraft-based city visualization and mappings
- [CC103] Balogh et al. (2015) - Eclipse integration, mapping files, and jump/follow navigation
- [CC130] CodeMetropolis repository — toolchain pipeline (converter/mapping/placing/rendering), SourceMeter/SonarQube inputs, and rendering extensions (e.g., danger hazards)
- [CC140] CodeMetropolis website — project overview and toolchain stage descriptions (“In a nutshell”)
