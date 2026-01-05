---
id: I034
name: CoderCity
origin: INSO-World (open-source)
year_introduced: 2021
status: research
source_refs: [CC136]
repo_url: https://github.com/INSO-World/CoderCity
demo_url: null
primary_language: TypeScript (Angular frontend) + TypeScript/Node.js (NestJS backend)
features_implemented: [F001, F005, F006, F017, F021, F038, F071]
last_updated: 2026-01-04
updated_from: [CC136]
---

# CoderCity

## Overview

CoderCity is a three-dimensional proof-of-concept code-city visualization focused on **code ownership**. It renders a city where folders become stacked districts and files become buildings, then subdivides each file-building into segments derived from `git blame` hunks and colors those segments by author.

## Key Mappings (from CC136)

- **Buildings**: files
- **Districts**: folders (stacked to represent nested folder structure)
- **Height**: total line count of the file
- **Ownership**: building is segmented by blame hunks; each segment is colored by author

## Running / Configuration (from CC136)

- Backend scans a configured folder for Git projects via the `GIT_PROJECTS_FOLDER` environment variable.
- Supports running via `docker-compose` (frontend on port 80; backend on port 3000) or locally (NodeJS + Angular CLI).

## Sources

- [CC136] CoderCity repository — README and implementation structure for code-ownership visualization using a code city metaphor
