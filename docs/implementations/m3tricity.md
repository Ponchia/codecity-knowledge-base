---
id: I021
name: m3triCity
origin: REVEAL @ Software Institute (USI Lugano)
year_introduced: 2020
status: research
source_refs: [CC059, CC079]
repo_url: null
demo_url: https://metricity.si.usi.ch/v2
primary_language: Unknown (web application)
features_implemented: [F001, F002, F017, F005, F007, F008, F015, F022, F023, F025, F029, F032, F033, F035, F037, F049, F050, F051]
last_updated: 2026-01-03
updated_from: [CC059, CC079]
---

# m3triCity

## Overview

m3triCity is a web-based platform for visualizing Git repositories as evolving software cities. It focuses on evolution as a first-class concept and addresses layout instability (“layout jumps”) by using a history-resistant layout that keeps artifacts at fixed positions across time. CC079 introduces **m3triCity 2 (Metricity v2)**, which extends the city to include data files and database entities.

## Key Capabilities (from CC059, CC079)

- **GitHub ingestion**: users can open a pre-existing project or start analyzing a new GitHub repository.
- **Evolution model**: an evolution model inspired by Hismo and adapted to Git, tracking repository/package/class histories across versions.
- **History-resistant layout**: stable placement over time by pre-allocating the final space needed for entities and keeping positions stationary across versions.
- **Evolution controls**: timeline view + play/pause/rewind/forward, with optional time bucketing (day/week/month/year).
- **Refactoring visualization**: structural refactorings (moves/renames) are shown as explicit movements, using 3D edge bundling to draw arcs from old to new positions.
- **Exploration UX**: hover tooltips, regex-based hiding, manual colorization/tagging, and an elision mode to remove obstructing objects.
- **Data-file integration**: data files (e.g., XML/JSON) are represented with dedicated meshes and mapped with data-structure metrics (entity counts, nesting, properties).
- **Database integration**: database schemas are inferred via SQLInspect; tables are rendered as separate entities connected to accessing classes, with the database placed above (City with Clouds) or below (City with Underground) the code city.

## Sources

- [CC059] Pfahler et al. (2020) — “Visualizing Evolving Software Cities” (m3triCity platform and history-resistant layout)
- [CC079] Ardigò et al. (2021) — “Visualizing Data in Software Cities” (m3triCity 2 data + database integration)
