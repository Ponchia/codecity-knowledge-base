---
id: I026
name: BabiaXR-CodeCity
origin: Universidad Rey Juan Carlos (URJC) + USI (REVEAL)
year_introduced: 2019
status: research
source_refs: [CC034, CC096, CC134, CC143]
repo_url: https://gitlab.com/babiaxr/aframe-babia-components
demo_url: https://babiaxr.gitlab.io
primary_language: JavaScript (A-Frame/BabiaXR) + Python (data pipeline)
features_implemented: [F001, F011, F017, F038, F005, F006, F007, F008, F022, F035, F037, F042, F059, F015, F032]
last_updated: 2026-01-04
updated_from: [CC096, CC134, CC034, CC143]
---

# BabiaXR-CodeCity

## Overview

BabiaXR-CodeCity is a browser-based implementation of the CodeCity metaphor that can be used either on-screen or in immersive VR (via WebXR). It represents directories as districts and files as buildings, mapping software metrics to building base area, height, and color. The BabiaXR components support multiple city layouts (treemap and spiral) and include optional time-evolution playback and multi-user demos.

CC034 motivates the project as a “modern”, open-source, web-based successor to the original Smalltalk-based CodeCity, with a particular focus on adding time-evolution support and broader device accessibility via the browser and VR.

CC143 is the BabiaXR documentation site (GPL-3.0) and links to tutorials, examples, and publications around the BabiaXR toolset.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | CodeCity metaphor rendered as a web 3D scene. |
| [[F038]] file-as-building | One building per file; directories form districts. |
| [[F017]] package-as-district | Directory hierarchy rendered as nested districts. |
| [[F005]] height-mapping | Metric chosen/configured for height (e.g., LOC per function in study tasks). |
| [[F007]] base-mapping | Metric chosen/configured for footprint/base area (e.g., number of functions). |
| [[F006]] color-mapping | Metric chosen/configured for color (configurable). |
| [[F059]] spiral-layout | Buildings (and hierarchical “quarters”) are placed in a spiral-like order intended to reduce disruptive motion under evolution. |
| [[F008]] treemap-layout | Alternative city visualizer (`babia-city`) supports treemap-like splitting (naive/pivot) of nested quarters. |
| [[F032]] time-travel | Time-evolution dataset format can step through snapshots/commits, animating building geometry and fading removed entities. |
| [[F015]] evolution-visualization | Commit/date metadata is surfaced in the scene during evolution playback (date/commit overlay). |
| [[F022]] selection | Clickable buildings/quarters toggle legends/highlights (raycaster-targeted entities). |
| [[F037]] hover-inspection | Tooltips show file name and mapped metric values (mouse hover; VR controller raycasting). |
| [[F011]] vr-immersion | Same scene can be explored in immersive VR using VR device controls. |
| [[F035]] view-configuration | A-Frame component attributes define metric-to-visual mappings; UI components can switch mapped fields dynamically. |
| [[F042]] collaborative-multi-user-vr | Networked-AFrame demos show shared exploration of the same boats/city scene by multiple users. |

## Technical Details (from CC096)

**Granularity**: file (buildings) + directory (districts)

**Platform**: web (A-Frame/BabiaXR) + VR via WebXR

**Scene composition**: HTML defines an A-Frame scene that loads JSON data and builds the city via BabiaXR components (`babia-queryjson`, `babia-treebuilder`, `babia-boats`).

**Data pipeline**: Python tooling clones a Git repository at a specific commit, computes per-file metrics (via Graal/Perceval and related tooling), stores them in ElasticSearch, and exports a JSON file consumed by the scene.

## Technical Details (from CC134)

**Visualizers**: The repository includes multiple A-Frame components used to render software cities:
- `babia-boats` implements a spiral-style placement algorithm (right/down/left/up growth around current bounds) for buildings and nested “quarters”.
- `babia-city` / `babiaxr-codecity` implement a treemap-like quarter/building layout with `split: naive|pivot`.

**Time evolution**: `babiaxr-codecity` supports a dataset format with a `time_evolution` flag and a `data_files` list (date + optional commit SHA). During playback it updates building height/footprint per snapshot (optionally animated), and fades buildings that are not present in the current snapshot.

**Stable identifiers** (from CC034): an early prototype version emphasizes assigning a unique identifier per building so time-evolution updates change geometry (area/height) while keeping positions fixed (avoiding re-layout across snapshots).

**Multi-user**: Example scenes use Networked-AFrame (socket.io/easyrtc) to synchronize a shared boats-based software city across users, with VR controller raycasting targeting `.babiaxraycasterclass`.

## Evaluation (from CC096)

Two controlled experiments compared VR vs on-screen usage of the same implementation (n=24 and n=26). VR participants completed tasks significantly faster (Mann–Whitney U; large Cliff’s delta), while achieving comparable correctness to on-screen participants.

## Sources

- [CC034] Moreno-Lumbreras et al. (Benelux 2019) — web-based CodeCity prototype focused on time evolution and stable per-building identifiers
- [CC096] Moreno-Lumbreras et al. (2022) — on-screen vs VR comparison, BabiaXR-CodeCity implementation, spiral layout, and experiments
- [CC134] BabiaXR repository — A-Frame components for code cities (treemap/spiral), time evolution playback, and multi-user demos
- [CC143] BabiaXR documentation site — toolset overview, licensing, and links to tutorials/examples/publications
