---
id: I023
name: GoCity
origin: Federal University of Minas Gerais (UFMG)
year_introduced: 2019
status: research
source_refs: [CC092, CC093, CC104]
repo_url: https://github.com/rodrigo-brito/gocity
demo_url: https://go-city.github.io/
primary_language: Go + JavaScript (React/Babylon.js)
features_implemented: [F001, F005, F006, F007, F013, F017, F037, F038, F043]
last_updated: 2026-01-03
updated_from: [CC092, CC093, CC104]
---

# GoCity

## Overview

GoCity is an implementation of the Code City metaphor for visualizing Go source code in 3D. The SANER 2019 paper details how Go-specific structures are mapped (files as buildings, structs stacked on file buildings, folders as districts) and how metrics are encoded (attributes/fields → base size, methods → height, LOC → color intensity). The tool provides hover inspection of metrics and links to the corresponding GitHub source code. As of November 2018, the authors reported ~23K unique users and ~1.3K GitHub stars.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F017]] package-as-district | Folders are rendered as districts. |
| [[F038]] file-as-building | Files are rendered as buildings. |
| [[F043]] nested entities as stacked buildings | Structs are stacked on top of their file buildings. |
| [[F006]] color-mapping | LOC mapped to building color (darker = higher). |
| [[F007]] base-mapping | Attributes/fields (NOV) mapped to footprint/base size. |
| [[F005]] height-mapping | NOM mapped to building height. |
| [[F037]] hover-inspection | Hover shows LOC, NOM, and NOA for the element. |
| [[F013]] source-code-display | Button opens the element’s GitHub source file. |

## Technical Details

**Granularity**: file + struct (stacked)

**Visual Element**: buildings + districts

**Metrics Supported**:
- LOC (color)
- NOV (footprint)
- NOM (height)

**Platform**: web (React + Babylon.js frontend)

## Architecture (from CC104)

**Processing module**: Git service fetches the repository, parser extracts metrics (methods/fields/LOC), position service assigns hierarchy/placement, and an LRU cache stores processed projects.

**Front-end module**: validation service handles input errors, 3D processor renders the city, and navigation supports rotate/zoom interactions.

## Evaluation Notes (from CC104)

The authors emailed 60 Go project owners (top-100 GitHub projects, filtered), receiving 12 responses (20% response rate). Reported benefits include insights on design/modularization (73% said GoCity provided useful insights) and maintenance support (60% agreed), with themes of code comprehension (67%) and refactoring candidate identification (33%).

## Sources

- [CC092] GoCity website metadata — "Code City metaphor for visualizing Go source code in 3D"
- [CC093] GoCity repository — folder/file/struct mappings and metric encodings; React + Babylon.js UI
- [CC104] GoCity SANER 2019 paper — architecture, metric mappings, hover metrics, GitHub linking, and developer survey
