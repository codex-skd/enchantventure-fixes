# EnchantVenture Fixes

Server-side datapack for Minecraft 26.2 that patches broken recipes, advancements, loot tables and predicates in the EnchantVenture modpack — without touching the mods themselves.

## Fixes included

- **tntfoundry** — 6 advancements with invalid single item entries fixed (`hollow`, `paperwork`, `precision`, `remote_work`, `the_big_one`, `full_catalogue`).
- **formationsoverworld** — `stone_tower` / `witch_tower` smithing loot tables drop `minecraft:iron_ingot` instead of the broken `minecraft:chain`.
- **fokus** — added `is_night` predicate (overworld night hours).
- **nerospace** — added `guide/new_life` breeding advancement.
- **nerologistics** — restored a working `configurator` recipe.

## Requirements

- Minecraft **26.2** (pack format 107)
- World or server with the EnchantVenture modpack

## Installation

1. Download `EnchantVenture_fixes-<version>.zip` from `build/`.
2. Place it in `world/datapacks/` (or `saves/<world>/datapacks/`).
3. Load the world — fixes apply automatically.

## Build

The datapack is regenerated from the mod JARs in the local CurseForge instance, then zipped with `pack.mcmeta` at the root (loads directly):

```bash
python build_fix_pack.py
# → build/EnchantVenture_fixes-<version>.zip
```

Version is read from `version.txt` (`0.0.0-beta.1`).

## License

All Rights Reserved.
