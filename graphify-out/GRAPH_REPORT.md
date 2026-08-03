# Graph Report - .  (2026-08-03)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 13 nodes · 15 edges · 5 communities (2 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 171 input · 52 output

## Graph Freshness
- Built from commit: `c18bee19`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Fix Item Field
- Jar Operations
- Datapack Icons
- Project Variables

## God Nodes (most connected - your core abstractions)
1. `main()` - 5 edges
2. `read_from_jar()` - 3 edges
3. `jar()` - 2 edges
4. `clean()` - 2 edges
5. `write()` - 2 edges
6. `fix_item_field()` - 2 edges
7. `Project Variables` - 2 edges
8. `CurseForge Upload Script` - 1 edges
9. `Project Icon` - 1 edges
10. `Datapack Project Icon` - 1 edges

## Surprising Connections (you probably didn't know these)
- `CurseForge Upload Script` ----> `Project Variables`  [EXTRACTED]
  scripts/curseforge-upload.ps1 → docs/curseforge/project_vars.md
- `Project Icon` ----> `Datapack Project Icon`  [EXTRACTED]
  pack.png → datapack/pack.png

## Import Cycles
- None detected.

## Communities (5 total, 3 thin omitted)

### Community 0 - "Fix Item Field"
Cohesion: 0.70
Nodes (4): clean(), fix_item_field(), main(), write()

## Knowledge Gaps
- **3 isolated node(s):** `CurseForge Upload Script`, `Project Icon`, `Datapack Project Icon`
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Project Variables` connect `Project Variables` to `Fix Item Field`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Why does `main()` connect `Fix Item Field` to `Jar Operations`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `read_from_jar()` connect `Jar Operations` to `Fix Item Field`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **What connects `CurseForge Upload Script`, `Project Icon`, `Datapack Project Icon` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._