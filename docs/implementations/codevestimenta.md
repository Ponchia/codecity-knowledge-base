---
id: I037
name: CodeVestimenta
origin: Babes-Bolyai University (Romania)
year_introduced: 2025
status: research
source_refs: [CC041]
repo_url: null
demo_url: null
primary_language: IntelliJ Platform (PSI)
features_implemented: [F072, F073, F074]
last_updated: 2026-01-05
updated_from: [CC041]
---

# CodeVestimenta

## Overview

CodeVestimenta is an IDE plugin that applies a clothing metaphor to software visualization, mapping object-oriented classes to garment shapes and encoding software quality metrics as garment attributes. The tool targets Java systems and generates static “wardrobe” images in batches (about 50 classes per image) accompanied by a legend so users can identify classes without overcrowding the view.

## Features Implemented

| Feature | Notes |
|---------|-------|
| [[F072]] clothing-metaphor | Wardrobe-style view with garments standing in for classes. |
| [[F073]] class-as-clothing-item | One garment per class; legend maps garments back to class names. |
| [[F074]] clothing-attribute-mapping | Sleeves, color, collar/belt, stripes, and garment type encode metrics. |

## Technical Details

**Granularity**: class

**Visual Element**: clothing items (t-shirt, shirt, pants)

**Metrics Supported**:
- LOC → overall garment size
- Number of class members → left sleeve length
- Number of class methods → right sleeve length
- NOC → garment color (pale → dark)
- RFC → garment type (t-shirt < 50, shirt 50–100, pants > 100)
- DIT → collar/belt when DIT > 6
- CBO → stripe patterns (none, one, or two stripes)

**Platform**: IDE plugin using IntelliJ PSI for metric extraction; outputs static image sets with a legend.

## Evaluation (from CC041)

CC041 reports a controlled study with 68 enrolled participants (41 completed) split into Text vs Visual groups. Participants answered 10 comprehension tasks across four scopes (internal structure, dependencies, component usage, and design quality). The visual group improved on harder tasks, especially dependency analysis and design-quality assessment, with reductions in completion time and increases in correctness.

## Sources

- [CC041] CodeVestimenta paper (KES 2025) — clothing metaphor, metric mappings, and controlled study results.
