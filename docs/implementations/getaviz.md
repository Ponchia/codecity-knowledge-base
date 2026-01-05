---
id: I027
name: Getaviz
origin: Visual Software Analytics (Leipzig University)
year_introduced: 2017
status: maintained
source_refs: [CC131]
repo_url: https://github.com/softvis-research/Getaviz
demo_url: https://home.uni-leipzig.de/svis/getaviz/Index.html
primary_language: Java (generator) + JavaScript (UI)
features_implemented: [F001, F002, F017, F027, F045, F011, F014, F015]
last_updated: 2026-01-04
updated_from: [CC131]
---

# Getaviz

## Overview

Getaviz is an open-source research platform for generating and exploring software visualizations in 2D, 3D, and VR. It includes multiple city-metaphor variants (City, City Floors, City Bricks) and can enrich structural views with behavioral (dynamic) and evolutionary information (git/svn), targeting tasks like antipattern refactoring, bottleneck analysis, and change tracking.

## Architecture / Pipeline (from CC131)

- **Generator**: consumes structural models (FAMIX) and optionally dynamic and/or Hismo models, and generates visualization models for the UI (the legacy `generator` component is marked deprecated in favor of `generator2`).
- **UI**: browser-based exploration of generated models; sample outputs include A-Frame HTML scenes with per-entity metadata (`metaData.json`) keyed by FAMIX element IDs.
- **Extractors**: language-specific extractors exist in-repo (e.g., Ruby and C#).

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | City-based structural visualization variants are provided (“City”, “City Floors”, “City Bricks”). |
| [[F017]] package-as-district | Namespace/package regions are rendered as base plates/blocks in the city examples. |
| [[F002]] class-as-building | Classes are represented as vertical buildings in the city examples. |
| [[F045]] method-as-floors | “City Floors” includes method-level floors rendered within class buildings. |
| [[F027]] method-as-bricks | “City Bricks” includes method-level bricks rendered within class buildings. |
| [[F014]] dynamic-visualization | Generator supports dynamic (behavior) model inputs for behavioral views. |
| [[F015]] evolution-visualization | Supports enriching views with git/svn history and evolutionary models (Hismo). |
| [[F011]] vr-immersion | Explorable via VR headsets (HTC Vive, Oculus Rift) per repository README. |

## Sources

- [CC131] Getaviz repository — overview, supported city variants (floors/bricks), supported model inputs (FAMIX/dynamic/Hismo), and platform claims (browser + VR)

