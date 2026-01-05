---
id: F032
title: Time Travel
category: analysis
status: canonical
introduced_by: CC116
implementations: [CodeCity, m3triCity, BabiaXR-CodeCity]
related_features: [F015, F031, F001]
taxonomy:
  granularity: [file, class, package, method]
  visual_element: [district, building, brick]
  metric_category: [evolution]
last_updated: 2026-01-04
updated_from: [CC035, CC059, CC116, CC128, CC134, CC034]
---

# Time Travel

## Definition

An evolution navigation technique that steps backward/forward through a system’s version history while keeping the city’s spatial layout stable so changes are perceived as transformations rather than re-layouts.

## Mechanism (from CC035)

**Input**: Version history with per-entity histories (lifetimes and metric values).

**Process**:
1. Assign each entity history a stable “lifetime real estate” position in the city.
2. As the viewed version changes, update geometry/attributes for entities that exist in that version.
3. Represent not-yet-created or removed entities as empty space that other entities cannot occupy.

**Output**: A temporally stable city that reveals births, changes, and removals.

## Evidence (from CC116)

CC116 demonstrates time travel on ArgoUML to explain a major design change: a large “ModelFacade” class disappears and is replaced by an interface plus multiple implementors, visible as births/deaths and geometry changes across versions when stepping through time.

## Implementation Notes (from CC128)

CC128 documents an implementation-oriented “model for evolving software systems” as a 5-tuple `(G, T, R, fe, A)`:
- `G`: directed dependency graph between entities
- `T`: containment hierarchy tree (packages → classes)
- `R`: ordered list of versions (with timestamps/ordering)
- `fe`: existence function (whether an entity exists in a given version)
- `A`: attribute function (metric/property values for an entity in a given version)

## Variations (m3triCity, from CC059)

CC059 describes a **history-resistant layout** for evolution visualization: every element is assigned a fixed position that remains stationary over the whole evolution. The approach leverages an evolution model (repository/package/class histories with per-version metric values) to infer the maximum “real estate” needed for each entity and pre-allocate it from the start, preventing layout “jumps”.

CC059 also describes **time bucketing** (day/week/month/year) to reduce overly fine-grained commit stepping when desired.

## Variations (BabiaXR, from CC134)

CC134’s `babiaxr-codecity` component implements a snapshot/commit stepping mode driven by a JSON format that includes a `time_evolution` flag and a `data_files` list (each entry includes a Unix timestamp and optional `commit_sha`). During playback it updates per-building footprint and height (by `id`) and can animate these geometry changes; buildings not present in the current snapshot are visually faded/hidden.

CC034 describes an early web-based CodeCity prototype where each building is assigned a unique HTML identifier so the city can evolve over time without re-layout: the building’s **area and height** are updated per snapshot while keeping its position fixed; missing buildings leave empty terrain.

## Sources

- [CC035] Wettel PhD thesis — coarse- and fine-grained time travel technique
- [CC059] Pfahler et al. (2020) — history-resistant layout and time bucketing in m3triCity
- [CC116] Wettel & Lanza (WCRE 2008) — time travel technique for exploring structural evolution across versions
- [CC128] codecity-visualizer repository — practical evolution-model representation `(G, T, R, fe, A)` used for consistent cities
- [CC134] BabiaXR repository — `babiaxr-codecity` time-evolution stepping with commit/date overlay and animated geometry updates
- [CC034] Moreno-Lumbreras et al. (Benelux 2019) — stable per-building IDs and geometry updates (area/height) for city evolution in BabiaXR
