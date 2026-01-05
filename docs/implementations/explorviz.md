---
id: I009
name: SynchroVis / ExplorViz
origin: Waller et al. (VISSOFT 2013) + Fittkau et al. (2015 VR extension)
year_introduced: 2013
status: research
source_refs: [CC015, CC053, CC071, CC077, CC080, CC108, CC084]
repo_url: https://github.com/SoftwareImpacts/SIMPAC-2020-36
demo_url: https://www.explorviz.net/download.php
primary_language: Java + JavaScript/TypeScript (web)
features_implemented: [F001, F002, F005, F006, F011, F013, F014, F040, F041, F042, F058]
last_updated: 2026-01-04
updated_from: [CC015, CC053, CC071, CC077, CC080, CC108, CC084]
---

# SynchroVis / ExplorViz

## Overview

Dynamic city-metaphor visualization for monitoring traces. CC015 describes SynchroVis as representing classes as buildings and visualizing runtime behavior (instances, calls, concurrency), and reports a VR adaptation of ExplorViz for Oculus Rift with gesture-based manipulation.

CC053 positions ExplorViz as a web-based, open-source research tool (started in 2012) for live monitoring and visualization of large software landscapes. ExplorViz provides two levels: a **landscape-level** overview (servers/applications and their communication) and an **application-level** view using the 3D city metaphor. It also supports collaboration in software development teams, including multi-user VR.

CC108 (VISSOFT 2013) introduces the ExplorViz approach for live trace visualization in large software landscapes. It outlines a monitoring/preprocessing/aggregation pipeline for traces and presents a two-perspective UI: a 2D landscape-level view (UML-deployment/activity inspired) and a 3D system-level city view per application, with on-demand expansion of grouped entities/relations for scalability.

CC084 (Fittkau’s dissertation, 2015/2016) provides the most detailed end-to-end description of the ExplorViz approach: it covers monitoring and trace processing for large landscapes, a time-shift mode and trace replayer for analyzing specific situations, and interaction concepts beyond mouse/keyboard (including a gesture-controlled VR setup with Oculus Rift DK1 + Kinect v2). It also reports multiple controlled experiments: ExplorViz vs Extravis on application-level program comprehension tasks (PMD; replication on Babsi) and a landscape-level perspective compared against state-of-the-art APM visualizations.

CC080 is an archived repository snapshot of the ExplorViz web client. It confirms the WebGL/HTML5 stack, adds code-viewer support, time-shift navigation over live traces, OpenSCAD export for 3D printing, and a WebVR/Leap Motion integration path.

CC071 adds live heat-map overlays for runtime metrics (dynamic coupling) on package tiles, with user-selectable metrics and heat-map time modes (snapshot, continuously aggregated, windowed). Heat maps also run in the AR client and are planned for VR integration; city opacity is reduced during heat-map view to keep both layers visible.

CC077 (ExplorViz “About” page) reiterates ExplorViz as an open-source, web-based live trace visualization for software landscapes using the 3D city metaphor, and highlights a modern stack (OpenTelemetry, WebGL, WebXR). It also notes that static-analysis support is under development and references controlled experiments (without reporting details on the page).

## CC015 Table 1

- **Language**: Java
- **VR**: Rift
- **Building**: class
- **Source code**: n/a
- **Static**: implementation, association, LOC
- **Dynamic**: instances, calls, thread operations
- **Instrumentation**: Kieker traces

## Notable Details (from CC015)

- Each instance of a class is visualized as a storey on the building.
- Threads are depicted with colored arrows; CC015 notes concurrency issues such as deadlock.
- VR interaction supports translation/rotation/scale (Kinect gestures).

## Notable Details (from CC053)

- **Multi-level visualization**: landscape-level overview + application-level city visualization.
- **Dynamic analysis**: live trace visualization for monitoring communication in landscapes.
- **Collaboration**: multi-user VR evolved from single-user (2017) to multi-user (2019) to fully collaborative multi-user VR (2020), enabling remote teams.
- **Architecture/tooling**: modernization toward a modular microservice architecture and replacement of a custom monitoring component with the Kieker monitoring framework.
- **Licensing**: open source under Apache License 2.0 (commercial use allowed).

## Notable Details (from CC080)

- **Archived snapshot**: README flags this repo as archived after migration to a new architecture.
- **Web-based stack**: WebGL/HTML5 client with a GWT module and a browser UI shell.
- **Time shift**: a timeline of method-call activity lets users pause live updates and fetch historical landscapes.
- **Source-code viewer**: context-menu action opens a CodeMirror-based code viewer via a server-side code service.
- **3D printing**: OpenSCAD exporter generates printable application models (optional puzzle cuts + labels).
- **Monitoring pipeline**: Kieker-backed record writer and monitoring configuration for runtime trace ingestion.
- **VR integration**: WebVR mode combines Oculus canvas output with Leap Motion hand tracking.

## Sources

- [CC015] Jeffery survey - SynchroVis/ExplorViz description and Table 1
- [CC053] Hasselbring et al. (Software Impacts 2020) - ExplorViz history, multi-level landscape+city visualization, and collaborative VR support
- [CC080] ExplorViz archived repo - WebGL/HTML5 client, time shift chart, code viewer, OpenSCAD export, and WebVR/Leap Motion integration
- [CC071] Krause et al. (2021) - ExplorViz live heat-map overlays for runtime metrics (web/AR) and planned VR support
- [CC077] ExplorViz About page - web-based tool positioning and stack notes (OpenTelemetry, WebXR)
- [CC108] Fittkau et al. (VISSOFT 2013) — ExplorViz approach (trace pipeline + 2D landscape + 3D city) with on-demand relation exploration
- [CC084] Fittkau dissertation (2015/2016) — ExplorViz end-to-end approach (monitoring/analysis + interaction concepts + multiple controlled experiments)
