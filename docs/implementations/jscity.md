---
id: I018
name: JSCity
origin: Viana et al. (arXiv 2017)
year_introduced: 2017
status: research
source_refs: [CC036, CC094]
repo_url: https://github.com/ASERG-UFMG/JSCity
demo_url: https://github.com/ASERG-UFMG/JSCity/wiki/JSCITY
primary_language: JavaScript
features_implemented: [F001, F003, F005, F006, F007, F017, F026, F037, F043, F044]
last_updated: 2026-01-02
updated_from: [CC036, CC094]
---

# JSCity

## Overview

Browser-based implementation of the CodeCity “software city” metaphor for JavaScript. CC036 positions JSCity as an open-source tool that runs in standard web browsers (Three.js), aiming to reduce installation friction for producing 3D city visualizations of JavaScript systems.

## Mappings (from CC036)

- **Districts**: directories/folders (yellow).
- **Sub-districts**: files (red).
- **Buildings**: functions.
- **Nested functions**: buildings stacked on top of the enclosing function’s building.

Metric mappings:
- **Height**: LOC (number of lines of code).
- **Footprint / width**: NOV (number of variables).
- **Building color**: named functions (blue) vs anonymous functions (green).

## Pipeline (from CC036)

- **Offline phase**: parse source code with Esprima to produce an AST and persist the data needed for visualization.
- **Online phase**: retrieve persisted data and draw the city in the browser via Three.js.

## Notes (from CC036)

CC036 reports producing visualizations for 40 popular JavaScript systems and observing common patterns such as “tall and wide buildings” corresponding to core functions and large districts with many small buildings corresponding to internationalization-related code.

## Setup (from CC094)

CC094 (the JSCity repository) documents a local setup that uses:
- **Node.js** for both the web server and the offline generator.
- **MySQL** as a persistence layer for the extracted city model.

Typical flow:
1. Run `sql/schema.sql` to create the `jscity` database (includes a sample city).
2. Configure DB credentials and server port in `js/config.json` (defaults include port `8888` and DB `jscity`).
3. Start the server from `js/` via `node server.js`, then open `http://localhost:8888/`.

The repo also provides a Vagrant-based setup that serves the UI on `http://localhost:8080/`.

## City generation pipeline (from CC094)

CC094 implements an offline generator (`js/backend/generator.js`) that:
- Recursively scans a project directory for JavaScript files (by MIME type).
- Parses files with Esprima using `loc: true` and `tolerant: true`.
- Builds a nested model and inserts it into MySQL tables (`tb_city`, `tb_district`, `tb_building`).

Notable CLI options (from the generator code):
- `-c` / `--city`: city name (defaults to the project folder name).
- `-v` / `--verbose`: print progress messages.
- `-x` / `--exclude`: comma-separated glob patterns to exclude.

## Mappings (repository-specific details from CC094)

In addition to the CC036-described function/city mapping, CC094’s generator and UI legend include an extra building type:
- **Module-as-building**: certain module declarations are rendered as buildings (e.g., AMD `define(...)` and `angular.module(...)` patterns), shown as “AMD Module [Building]” in the UI help.

## Interaction (from CC094)

CC094 provides two navigation controls:
- **Orbital**: orbit/pan/zoom around the city (via Three.js orbit controls).
- **First-person**: keyboard/mouse navigation with adjustable movement speed (`+` / `-` / `*` for default).

It also implements **hover inspection** by raycasting against rendered blocks and showing a tooltip/details-on-demand label for the hovered element.

## Sources

- [CC036] Viana et al. — JSCity design, mappings, and usage examples
- [CC094] JSCity repository — setup instructions, generator/server implementation, UI controls, and module building type
