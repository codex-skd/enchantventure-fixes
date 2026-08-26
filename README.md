# EnchantVenture Fixes

Server-side datapack for Minecraft 26.2 that patches broken recipes, advancements, loot tables and predicates in the EnchantVenture modpack — without touching the mods themselves.

## Fixes included

- **formationsoverworld** — `stone_tower` / `witch_tower` smithing loot tables drop `minecraft:iron_ingot` instead of the broken `minecraft:chain`.
- **fokus** — added `is_night` predicate (overworld night hours) and fixed `nxf/kp4o6wh`, `nxf/11z33h0q4`, `nxf/_ignored_bffhan5h` functions (obsolete `play_one_minute` criterion → `play_time`, and malformed `schedule` / `replaceitem` commands).
- **berezka_api** — fixed `chests/treasure` loot table failing to parse (`minecraft:item` entry with `minecraft:air` is invalid; replaced with `minecraft:empty`).
- **Orphaned Lootr container** — added a `minecraft:chests/houseloot` stub loot table for a leftover chest (BlockPos -4854, 70, 669 in the overworld) whose original loot table no longer exists in any installed mod.
- **marsward** — `data/marsward/field_manual/field_manual.json` is present but currently has **no effect**: the mod's Field Manual GUI reads its text from hardcoded Java `String` literals compiled into `marsward-1.0.6.jar` (confirmed via bytecode inspection), not from this datapack file. Translating the in-game manual would require patching the mod itself (e.g. a Mixin), which is out of scope for a datapack. Left in place for a possible future mod version that reads this file for real.

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
