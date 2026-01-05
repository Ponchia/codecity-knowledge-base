---
id: F065
title: Variability Hotspot Overlay (OO Variability)
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC045
implementations: [VariCity / VariMetrics]
related_features: [F001, F002, F035, F006, F016]
supersedes: []
taxonomy:
  granularity: [class]
  visual_element: [building, street, district]
  metric_category: [variability, quality]
last_updated: 2026-01-05
updated_from: [CC045]
---

# Variability Hotspot Overlay (OO Variability)

## Problem & Motivation

This capability helps connect analysis findings to structural and spatial context so they are explainable and actionable. An analysis overlay that adapts the software-city metaphor to reveal **zones of high density of implemented object-oriented (OO) variability**, by encoding variability-related implementation metrics on class buildings and emphasizing neighborhoods of interacting classes. Without it, findings stay detached from structure, making prioritization and communication harder.

## Definition

An analysis overlay that adapts the software-city metaphor to reveal **zones of high density of implemented object-oriented (OO) variability**, by encoding variability-related implementation metrics on class buildings and emphasizing neighborhoods of interacting classes.

## Mechanism (Solution)

**Input**: Class-level variability metrics computed from an OO codebase (symfinder/symfinder-2), usage relationships between classes, inheritance relationships, and optional software-quality metrics (from SonarCloud/SonarQube).

**Process**:
1. Render classes as buildings; by default, map **method-level variants** to building height and **constructor variants** to building width.
2. Color buildings to emphasize variability hotspots and variation points (e.g., yellow/blue/gray categories) and add distinct crowns for entry points and detected design patterns (e.g., Strategy/Factory/Template/Decorator).
3. Render relationships as streets: a root street aggregating entry points, green plan/underground streets for usage relationships, and aerial streets for inheritance; additional links can appear on hover to reduce clutter.
4. Provide configuration options (entry points, usage orientation IN/OUT/IN-OUT, usage level, blocklists, and metric bindings for height/width) to focus on subparts of the system or specific variability mechanisms.
5. Optionally overlay quality/technical-debt signals (VariMetrics) on building walls using configurable color strategies (red↔green or saturation) and a crackled texture to combine multiple quality metrics.

**Output**: A city view that highlights variability-implementation hotspots and (optionally) which hotspots are also quality/technical-debt-critical.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Evidence

CC045 reports applying VariCity/VariMetrics to multiple variability-rich Java systems (RQ1/RQ3) and a controlled experiment comparing VariCity to an IDE + CSV baseline (24 vs 25 subjects). The experiment reports statistically higher correctness on 6/11 tasks and faster completion time on tasks focused on complex variability structures (including hotspots/design patterns), with perceived difficulty also favoring VariCity on several of those tasks.

## Sources

- [CC045] Mortara et al. (JSS 2024 preprint) — VariCity variability hotspot visualization, VariMetrics technical-debt overlay strategies, and controlled-experiment results

## See Also

- [[city-metaphor]] — base visualization paradigm
- [[class-as-building]] — entity mapping used by VariCity
- [[view-configuration]] — configuration options for focusing the view
- [[color-mapping]] and [[texture-mapping]] — channels used by VariMetrics for quality overlays
- [[disharmony-maps]] — related “quality overlay” concept in CodeCity
