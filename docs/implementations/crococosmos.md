---
id: I038
name: CrocoCosmos
origin: Brandenburg University of Technology (BTU) Cottbus
year_introduced: 2012
status: research
source_refs: [CC101]
repo_url: null
demo_url: null
primary_language: Java
features_implemented: [F001, F005, F006, F007, F009, F015, F041]
last_updated: 2026-01-05
updated_from: [CC101]
---

# CrocoCosmos

## Overview

CrocoCosmos is a long-running academic software visualization tool that evolved into a software-city platform. The dissertation describes CrocoCosmos as a Java-based research system used to evaluate **consistent software cities** built with the EvoStreets layout, and to generate thematic maps for software evolution and quality analysis.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F009]] street-layout | EvoStreets layout with streets representing hierarchical structure and buildings attached to streets. |
| [[F015]] evolution-visualization | Stable layouts over time plus thematic evolution maps (authorship, modification history). |
| [[F006]] color-mapping | Last-modified recency and authorship mapped to color in thematic views. |
| [[F005]] height-mapping | Modification counts or dependency counts mapped to tower height. |
| [[F007]] base-mapping | Coupling/dependency magnitude mapped to tower base area. |
| [[F041]] software-landscape-view | Software city landscapes combine multiple cities to represent component architecture. |
| [[F001]] city-metaphor | City metaphor baseline for comprehension and quality analysis. |

## Technical Details

**Granularity**: package + class

**Visual Elements**: streets + building plots + towers

**Metrics & Overlays**:
- Coupling magnitude (base area; incoming/outgoing segments in height)
- Modification history (height = number of modifications, color = last-modified recency)
- Authorship (color by author; height/size to emphasize modification or dependency intensity)

**Platform**: Research tool integrated into the CrocoCosmos software model and visualization pipeline.

## Evaluation (from CC101)

CC101 reports multiple case studies using CrocoCosmos and EvoStreets-based cities, including detailed analyses of CrocoCosmos itself and two industrial systems. The studies emphasize layout consistency over evolution, and show how thematic maps (authorship, modification history, coupling) support comprehension and quality assessment.

## Sources

- [CC101] Steinbrückner dissertation — CrocoCosmos tool description, EvoStreets layout, thematic maps, and software city landscapes.
