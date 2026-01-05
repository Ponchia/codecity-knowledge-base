---
id: F060
title: Danger Hazard Mapping (Spawners & Loot)
category: analysis
status: variant
maturity: emerging
bounded_context: [universal]
introduced_by: CC130
implementations: [CodeMetropolis]
related_features: [F020, F016, F057]
supersedes: []
taxonomy:
  granularity: [method]
  visual_element: [floor]
  metric_category: [quality]
last_updated: 2026-01-05
updated_from: [CC130]
---

# Danger Hazard Mapping (Spawners & Loot)

## Problem & Motivation

This capability helps connect analysis findings to structural and spatial context so they are explainable and actionable. A mapping that encodes a “danger” signal for a code element as game-mechanics hazards in a game-engine software city (e.g., hostile mob spawners and loot chests), making hotspots discoverable through exploration. Without it, findings stay detached from structure, making prioritization and communication harder.

## Definition

A mapping that encodes a “danger” signal for a code element as game-mechanics hazards in a game-engine software city (e.g., hostile mob spawners and loot chests), making hotspots discoverable through exploration.

## Mechanism (Solution)

**Input**: A buildable (floor/cellar) with a `danger` attribute (value used as a danger level).

**Process**:
1. If `danger` is present, place a mob spawner at the floor’s center configured to spawn zombies, and place four surrounding chests (cardinal directions) with a weapon item.
2. If `danger` is absent, render the normal “safe” floor decorations (e.g., torches).

**Output**: A city where “dangerous” code elements are rendered as dungeon-like hotspots that visibly and behaviorally stand out.

## Consequences & Trade-offs

| ✅ Benefits | ❌ Liabilities |
|-------------|----------------|
| Surfaces quality/evolution signals in context. | Overlays can overwhelm the base metaphor. |
| Supports prioritization (hotspots, anomalies). | Signals may be noisy or metric-dependent. |

## Sources

- [CC130] CodeMetropolis repository — rendering logic adds mob spawners + chests when a `danger` attribute exists on a floor/cellar.

## See Also

- [[threshold-metric-mapping]] — common way to derive discrete “levels” from metrics
- [[texture-mapping]] — another discrete channel used heavily in Minecraft-based cities
- [[vulnerability-overlay]] — risk/issue overlays on city elements (security-focused variant)
