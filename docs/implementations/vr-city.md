---
id: I011
name: VR City
origin: Vincur et al. (QRS-C 2017)
year_introduced: 2017
status: research
source_refs: [CC015, CC106]
repo_url: null
demo_url: null
primary_language: Java
features_implemented: [F001, F002, F006, F010, F011, F013, F014, F015, F022, F045, F046]
last_updated: 2026-01-03
updated_from: [CC015, CC106]
---

# VR City

## Overview

VR City (Vincúr et al., QRS-C 2017) is a VR software analysis environment for HTC Vive that adapts the software-city metaphor to support **static**, **dynamic**, and **evolution** analysis in an immersive setting. CC106 describes a coupling-driven layout algorithm, fine-grained method representation inside class buildings, trace playback overlays, author/evolution animation, and in-VR source-code browsing.

## Layout and representation (from CC106)

- **City artifacts**: classes are buildings; methods are represented as **floors** within buildings.
- **Coupling-driven layout**: building positions are derived from a weighted coupling graph (classes as nodes; weighted dependencies as edges). The paper uses spectral ordering (Fiedler vector) and Hilbert-curve placement to arrange building-floor blocks and merge them into buildings.
- **Fine-grained metric distribution**: floors are sized using a per-method metric (the case study demonstrates LOC), making the distribution of metric values across methods visible within a class.

## Dynamic trace visualization (from CC106)

VR City provides a trace mode where:
- Buildings start as uniformly translucent/white.
- Playing a trace highlights the invoked methods by coloring their corresponding floors and reducing building translucency.
- Multiple traces can be compared by color; methods shared by multiple traces are shown with a reserved color.

Traces are recorded using the Eclipse inTrace plugin (no source-code modification) with user-defined filters.

## Evolution / authorship (from CC106)

VR City includes an evolution animation over a selected commit range (chosen by date or SHA):
- Authors are rendered as colored spheres moving through waypoints derived from the centroid of modified classes.
- Users can pause the animation to inspect changes (including source code), and filter by author or by selected buildings.
- The paper notes that positions are kept stable (no re-layout during animation) and that classes created/removed outside the current revision are not shown.

## Interaction and navigation (from CC106)

- Room-scale navigation by walking (limited play area), augmented with **teleportation** for large cities.
- Point-and-trigger selection using controller pointers; grab/move interactions via grip buttons; UI scrolling via the trackpad.
- A controller-attached menu provides actions such as scaling/rotating/translating the city, playing author animations, selecting traces, and changing color schemes.

## CC015 Table 1

- **Language**: Java
- **VR**: Vive
- **Building**: class
- **Source code**: yes
- **Static**: LOC, #methods, coupling, author
- **Dynamic**: trace locations
- **Instrumentation**: inTrace traces

## Sources

- [CC015] Jeffery survey — VR City description and Table 1
- [CC106] Vincúr et al. (QRS-C 2017) — VR City layout algorithm, interaction, trace mode, evolution animation, and case studies
