# Graph Report - EnchantVenture_fixes  (2026-08-03)

## Corpus Check
- 34 files · ~110,370 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 68 nodes · 58 edges · 16 communities (14 shown, 2 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c65d8f90`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Fix Item Field
- Jar Operations
- Datapack Icons
- Project Variables
- Flujo de trabajo — EnchantVenture_fixes (Datapack)
- EnchantVenture Fixes
- [0.0.0-beta.4] - 2026-08-01
- CurseForge Upload Script

## God Nodes (most connected - your core abstractions)
1. `CurseForge — Variables del proyecto` - 13 edges
2. `Flujo de trabajo — EnchantVenture_fixes (Datapack)` - 10 edges
3. `Changelog` - 7 edges
4. `EnchantVenture Fixes` - 6 edges
5. `main()` - 5 edges
6. `read_from_jar()` - 3 edges
7. `[0.0.0-beta.4] - 2026-08-01` - 3 edges
8. `[0.0.0-beta.3] - 2026-08-01` - 3 edges
9. `[0.0.0-beta.1] - 2026-07-31` - 3 edges
10. `jar()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Project Icon` ----> `Datapack Project Icon`  [EXTRACTED]
  pack.png → datapack/pack.png

## Import Cycles
- None detected.

## Communities (16 total, 2 thin omitted)

### Community 0 - "Fix Item Field"
Cohesion: 0.52
Nodes (6): clean(), fix_item_field(), jar(), main(), read_from_jar(), write()

### Community 1 - "Jar Operations"
Cohesion: 0.14
Nodes (13): [0.0.0-beta.1] - 2026-07-31, [0.0.0-beta.2] - 2026-07-31, [0.0.0-beta.3] - 2026-08-01, [0.0.0-beta.5] - 2026-08-01, [0.0.0-beta.6] - 2026-08-03, Añadido, Añadido, Añadido (+5 more)

### Community 3 - "Project Variables"
Cohesion: 0.14
Nodes (13): CurseForge — Variables del proyecto, Descripcion del proyecto, Estructura del changelog (HTML), Flujo completo, Parámetros del upload, Proyecto, Rama, Subir archivo (ZIP) con Python (+5 more)

### Community 5 - "Flujo de trabajo — EnchantVenture_fixes (Datapack)"
Cohesion: 0.18
Nodes (10): Buenas prácticas, Commits (Conventional Commits), Diferencias con un mod NeoForge, Específico del datapack, Estructura del proyecto, Flujo de trabajo — EnchantVenture_fixes (Datapack), Flujo por tarea, Idioma (+2 more)

### Community 6 - "EnchantVenture Fixes"
Cohesion: 0.29
Nodes (6): Build, EnchantVenture Fixes, Fixes included, Installation, License, Requirements

### Community 7 - "[0.0.0-beta.4] - 2026-08-01"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.4] - 2026-08-01, Añadido, Cambiado

## Knowledge Gaps
- **38 isolated node(s):** `Añadido`, `Añadido`, `Añadido`, `Cambiado`, `Añadido` (+33 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Changelog` connect `Jar Operations` to `[0.0.0-beta.4] - 2026-08-01`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **What connects `Añadido`, `Añadido`, `Añadido` to the rest of the system?**
  _38 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Jar Operations` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `Project Variables` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._