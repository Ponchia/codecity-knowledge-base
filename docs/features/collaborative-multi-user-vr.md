---
id: F042
title: Collaborative Multi-User VR
category: interaction
status: variant
introduced_by: CC053
implementations: [ExplorViz, SecCityVR, BabiaXR-CodeCity]
related_features: [F011, F014, F067]
taxonomy:
  granularity: [system]
  visual_element: [building, district]
  metric_category: [behavior]
last_updated: 2026-01-04
updated_from: [CC053, CC069, CC134, CC057]
---

# Collaborative Multi-User VR

## Definition

A collaboration capability where multiple users simultaneously explore and discuss a shared software visualization in virtual reality, supporting team-based program/system comprehension.

## Mechanism (from CC053)

**Input**: A shared visualization session (same monitored system and view state) and multiple VR clients.

**Process**:
1. Connect multiple users (potentially from different sites) to the same session.
2. Provide VR interactions via controllers/gestures for navigation and exploration.
3. Synchronize view and interaction state so users can collaborate during analysis.

**Output**: Multi-user immersive exploration of a monitored system, enabling collaborative comprehension tasks.

## Variations (SecCityVR, from CC069)

SecCityVR supports paired users exploring the same vulnerability-focused city; positions/controllers are synchronized, and users can teleport to join each other's findings while discussing issues and mitigations.

## Variations (BabiaXR, from CC134)

CC134 includes multi-user demos built on Networked-AFrame (socket.io/easyrtc) that synchronize shared visualization entities across clients. The `multi_boats` example uses a software-city dataset (JetUML metrics), builds a hierarchy via `babia-treebuilder`, and renders it via `babia-boats`, enabling multiple users to explore the same city concurrently in VR.

## Notes (from CC057)

CC057 motivates collaboration in immersive software visualization and proposes “Multiple Collaborative Representations” (MCR) as an alternative to a single shared representation: collaborators can create and tailor their own views during a session.

## Sources

- [CC053] Hasselbring et al. (Software Impacts 2020) — ExplorViz single-user → multi-user (2019) → fully collaborative multi-user VR (2020)
- [CC069] Wueppelmann & Yigitbas (2025) — SecCityVR collaborative exploration of vulnerabilities in VR
- [CC134] BabiaXR repository — Networked-AFrame multi-user demos (incl. shared software-city boats visualization)
- [CC057] Maletic et al. (ICSE 2001) — collaboration motivation and MCR concept for immersive software visualization
