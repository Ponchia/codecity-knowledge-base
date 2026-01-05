---
id: I036
name: Viseagull
origin: Charles Géry (open-source)
year_introduced: 2021
status: research
source_refs: [CC148]
repo_url: https://github.com/charlesgery/viseagull
demo_url: null
primary_language: unknown
features_implemented: [F001, F005, F006, F010, F015, F022, F023, F026, F037, F038, F048]
last_updated: 2026-01-04
updated_from: [CC148]
---

# Viseagull

## Overview

Viseagull is an open-source, “ludic design” visualization tool that lets developers explore a repository like a city by
grouping files into clusters based on coupling and linking clusters with roads. It supports both **logical coupling**
(co-change) and **semantic coupling** (shared lexicon) analyses and renders the results as an interactive city map.

## Analysis Model (from CC148)

- **Logical coupling**: computes a file×commit matrix, derives pairwise file distances using **Jaccard distance**, and
  clusters files frequently modified together.
- **Semantic coupling**: computes **tf-idf** vectors per file and uses **cosine similarity** (as a distance matrix) for
  clustering; described as supported for Python files.

## Visualization (from CC148)

- **Buildings**: files
- **Cities / clusters**: groups of strongly-coupled files
- **Height**: number of commits modifying the file
- **Roads**: connect clusters when files from both clusters were modified in common commits

## Layout (from CC148)

To place clusters, Viseagull:
1. Runs **t-SNE** on the coupling distance matrix to get 2D coordinates for files.
2. Computes a centroid per cluster.
3. Applies a spring-layout-like overlap-removal step to keep clusters from overlapping while preserving distances.

## Interaction (from CC148)

- Scroll/zoom navigation, hover for details-on-demand, and click a cluster to highlight its connected roads.
- Filters and controls include: road-width thresholding, recoloring buildings by creation/last-modified date, and
  highlighting files modified in a given commit hash.

## Sources

- [CC148] Medium post — Viseagull coupling model (logical/semantic), clustering and layout approach (t-SNE + spring), and
  interaction/encoding overview; links to the GitHub repository
