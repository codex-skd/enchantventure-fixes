# EnchantVenture Fixes

Server-side datapack for Minecraft 26.2 that patches broken recipes, advancements, loot tables and predicates in the EnchantVenture modpack — without touching the mods themselves.

## Fixes included

- **formationsoverworld** — `stone_tower` / `witch_tower` smithing loot tables drop `minecraft:iron_ingot` instead of the broken `minecraft:chain`.
- **fokus** — added `is_night` predicate (overworld night hours) and fixed `nxf/kp4o6wh`, `nxf/11z33h0q4`, `nxf/_ignored_bffhan5h` functions (obsolete `play_one_minute` criterion → `play_time`, and malformed `schedule` / `replaceitem` commands).
- **berezka_api** — fixed `chests/treasure` loot table failing to parse (`minecraft:item` entry with `minecraft:air` is invalid; replaced with `minecraft:empty`).
- **Orphaned Lootr container** — added a `minecraft:chests/houseloot` stub loot table for a leftover chest (BlockPos -4854, 70, 669 in the overworld) whose original loot table no longer exists in any installed mod.
- **marsward** — full `es_ES` translation of the in-game Field Manual (`data/marsward/field_manual/field_manual.json`, 18 chapters). The manual's text is hardcoded into the mod's own datapack JSON rather than a `lang/` file, so a resource pack cannot translate it — this override replaces the file entirely.

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
