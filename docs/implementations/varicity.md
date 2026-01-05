---
id: I030
name: VariCity / VariMetrics
origin: Université Côte d’Azur / I3S - CNRS (France)
year_introduced: 2021
status: research
source_refs: [CC045]
repo_url: https://doi.org/10.5281/zenodo.7687914
demo_url: https://deathstar3.github.io/varicity-demo/
primary_language: unknown
features_implemented: [F001, F002, F006, F016, F035, F037, F065]
last_updated: 2026-01-04
updated_from: [CC045]
---

# VariCity / VariMetrics

## Overview

VariCity is a configurable 3D software-city visualization designed to help developers comprehend **implemented OO variability** in single-codebase systems by highlighting zones of high variability-implementation density. VariMetrics extends VariCity with quality-metric overlays (including texture and color strategies) to surface variability hotspots that are also technical-debt-critical.

## Features Implemented (from CC045)

| Feature | Notes |
|---------|-------|
| [[F001]] city-metaphor | Uses the city metaphor as the base representation. |
| [[F002]] class-as-building | Classes are rendered as buildings. |
| [[F065]] variability-hotspot-overlay | Variability metrics mapped to building dimensions; neighborhoods emphasize interacting variability-heavy classes. |
| [[F035]] view-configuration | Configurable views to focus on subparts of the system and selected variability mechanisms/metrics. |
| [[F006]] color-mapping | VariMetrics supports quality-metric overlays using strategies such as red↔green sequences and saturation. |
| [[F016]] texture-mapping | VariMetrics supports texture strategies such as a crackled texture to encode quality/technical-debt signals. |
| [[F037]] hover-inspection | Hover reveals additional usage/inheritance links to reduce clutter during exploration. |

## Technical Details (from CC045)

**Input**: Variability metrics about OO mechanisms (e.g., overloads, detected design patterns) computed using the symfinder toolchain, plus usage relationships and inheritance; optional software-quality metrics for VariMetrics (from SonarCloud API or local SonarQube).

**Encodings**:
- **Variability (default)**: building **height** encodes number of method-level variants; building **width** encodes constructor variants.
- **Hotspots**: buildings are colored to distinguish variation points and hotspot membership (e.g., yellow for variation points in hotspots, blue for non-variation-point classes in hotspots, gray otherwise).
- **Patterns/entry points**: crowns mark entry points and detected patterns (Strategy/Factory/Template/Decorator).
- **Relationships**: usage and inheritance relationships are rendered as streets (plan/underground usage streets; aerial inheritance streets), with additional links appearing on hover to avoid overloading the default view.
- **Quality/technical debt (VariMetrics)**: walls can encode quality metrics using color strategies (red↔green or saturation) and a crackled texture to combine two quality metrics simultaneously.

**Reproducibility**: CC045 provides replication materials online and a Zenodo reproduction package containing source code and artifacts.

## Evaluation Notes (from CC045)

Controlled experiment comparing VariCity to an IDE + CSV baseline on JFreeChart (24 vs 25 subjects). The paper reports:
- higher correctness on 6/11 tasks for VariCity (tasks involving complex variability structures like design patterns/hotspots),
- faster completion on tasks 3, 6, 7, and 8 for VariCity (and faster completion on task 2 for the IDE baseline), and
- perceived difficulty favoring VariCity on tasks 6–9.

## Sources

- [CC045] Mortara et al. (JSS 2024 preprint) — VariCity/VariMetrics design, encodings, evaluations, and replication artifacts
