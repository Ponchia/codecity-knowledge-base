---
id: I016
name: Code2City
origin: Romano et al. (Roma2019b)
year_introduced: 2019
status: research
source_refs: [CC009, CC055, CC064]
repo_url: null
demo_url: http://graphics.unibas.it/Code2City/index.md.html
primary_language: C++ / Blueprints (Unreal Engine 4)
features_implemented: [F001, F002, F005, F006, F007, F008, F017, F022, F023, F025, F026, F034]
last_updated: 2026-01-04
updated_from: [CC009, CC055, CC064]
---

# Code2City

## Overview

Desktop 3D implementation of the CodeCity-style city metaphor used for program comprehension tasks. CC009 describes Code2City as providing first-person navigation (mouse/keyboard), viewfinder-based selection, and search (by name and by callers). CC055 adds implementation detail: Java metrics are exported via an Eclipse plugin (CodePro AnalytiX) to XML, reconstructed as a package/type tree, and laid out using a recursive bin-packing algorithm in Unreal Engine 4.

## City Metaphor Instance (from CC009)

- **Buildings**: types (classes and interfaces), rendered as square-based cuboids.
- **Districts**: packages.
- **Footprint**: Number Of Attributes (NOA).
- **Height**: Number Of Methods (NOM).
- **Building color**: Lines Of Code (LOC), dark-blue → light-blue scale.
- **District shading**: indicates package nesting level.

## Interaction (from CC009)

- **Select** building/district via a viewfinder; selection is highlighted (yellow).
- **Inspect selected type**: name, NOM, NOA, LOC, and package.
- **Inspect selected package**: full name and contained classes.
- **Search** types by name or by callers; matches are highlighted (red).

## Additional Capabilities (from CC055)

- **Bin-packing layout**: packages/types are positioned via a recursive rectangle-packing (“bin-packing”) algorithm over the reconstructed hierarchy.
- **Code-smell highlighting**: supports color-based highlighting for selected smells (brain class, data class, god class) while preserving the city structure.

## Empirical Evidence (from CC064)

CC064 reports a controlled experiment comparing Eclipse (with a “Metrics & Smells” plugin) vs Code2City vs Code2CityVR on program-comprehension tasks (FindBugs; 42 participants in experimental sessions). Key outcomes:

- **Correctness**: both Code2City and Code2CityVR achieve significantly higher scores than Eclipse (ANOVA p=0.005; post-hoc p=0.006 and p=0.035).
- **Time**: Code2CityVR is significantly faster than Code2City and Eclipse; Code2City and Eclipse are not significantly different in completion time (ANOVA p<0.001; post-hoc Code2CityVR–Code2City p=0.001; Code2CityVR–Eclipse p<0.001; Code2City–Eclipse p=0.171).

## Sources

- [CC009] Romano et al. — tool description + study context
- [CC055] Code2City project report — pipeline, bin-packing layout, and additional interaction/quality-highlighting details
- [CC064] Romano et al. (IST 2019) — controlled experiment (Eclipse vs screen city vs VR city) and detailed task/tool mapping
