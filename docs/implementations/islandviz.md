---
id: I033
name: IslandViz
origin: Schreiber et al. (IEEE 2019)
year_introduced: 2018
status: research
source_refs: [CC070, CC074, CC076, CC078, CC083]
repo_url: https://github.com/DLR-SC/island-viz
demo_url: https://doi.org/10.5281/zenodo.1464633
primary_language: C# (Unity3D)
features_implemented: [F011, F012, F022, F055, F068]
last_updated: 2026-01-04
updated_from: [CC070, CC074, CC076, CC078, CC083]
---

# IslandViz

## Overview

IslandViz visualizes component-based software architectures (OSGi) using an **island metaphor** and supports both VR and AR exploration. CC070 describes a pipeline that mines repository data into a Neo4j graph database (via JQA SSISTANT) and renders bundles as islands, packages as regions, and classes as buildings; dependencies are shown between islands and through service layers.

## Key Capabilities (from CC070)

- **Metaphor + hierarchy**: bundle → island; package → region; class → building (multi-storey buildings; LOC mapped to storeys).
- **Data mining**: extracts OSGi artifacts from source (Java/MANIFEST/XML) and stores them in Neo4j for querying and visualization.
- **Dependency visualization**: shows package import/export relations via ports and arced arrows; can also visualize OSGi service relationships using distinct node types and layered height slices (CC078 routes service connections via intermediate nodes distributed over height).
- **VR interaction**: uses a virtual-table (“world-in-miniature”) setup with translate/rotate/scale interactions; scaling acts as a level-of-detail control across abstraction layers. A “virtual tablet” attached to the user provides textual details-on-demand.
- **AR interaction + collaboration**: HoloLens-based AR view using gesture/gaze/voice; supports shared state via the Mixed Reality Toolkit sharing API.
- **2D web client**: CC074 notes an additional web-based 2D application variant (besides VR/AR).
- **Scale/performance (VR)**: CC078 reports testing on HTC Vive with an RCE subset (1700 classes / 500 packages / 160 bundles, plus 550 service and 1200 package dependencies) and sustaining >90 Hz.

## Sources

- [CC070] Schreiber et al. — IslandViz in VR/AR for OSGi-based architectures (data mining + metaphor + interaction)
- [CC074] DLR project page — high-level description of IslandViz and listed modalities (VR/AR + 2D web)
- [CC076] Heidrich & Schreiber (MuC 2019 demo) — short IslandViz overview (OSGi modules as islands on a virtual table)
- [CC078] Misiak et al. (IEEE VR 2018) — IslandViz in VR with virtual-table interaction, module/service dependencies, and performance notes
- [CC083] Mišiak et al. (VISSOFT 2018) — IslandViz tool paper metadata (DOI and bibliographic record)
