# Changelog

Todos los cambios notables de EnchantVenture Fixes se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.0-beta.3] - 2026-08-01

### Añadido

- fokus: corregidas las funciones `nxf/kp4o6wh`, `nxf/11z33h0q4` y `nxf/_ignored_bffhan5h` — criterio `minecraft.play_one_minute` renombrado a `minecraft.play_time`, y comandos mal formados (`schedule function $this.file`, `replaceitem entity @s weapon`) reescritos a sintaxis válida de 26.2.

### Eliminado

- nerologistics: la sobreescritura de la receta del `configurator` se elimina del datapack — el mod ya aporta una receta válida y la versión del datapack usaba el formato de ingrediente antiguo (`"I": {"item": ...}`) que fallaba al parsear.

## [0.0.0-beta.2] - 2026-07-31

### Añadido

- Icono del proyecto (`pack.png`) incluido en el zip del datapack (visible en la lista de datapacks in-game).
- `build_fix_pack.py` copia `pack.png` a `datapack/` y al zip.

## [0.0.0-beta.1] - 2026-07-31

### Añadido

- Primer versionado del datapack contra GitLab (`26.2-0.0.0-beta.1`).
- `build_fix_pack.py` regenera `datapack/` desde los JARs de la instancia y empaqueta `build/EnchantVenture_fixes-<version>.zip` con `pack.mcmeta` en la raíz.
- tntfoundry: 6 advancements con entradas de ítem inválidas corregidas (`hollow`, `paperwork`, `precision`, `remote_work`, `the_big_one`, `full_catalogue`).
- formationsoverworld: loot tables de smithing de `stone_tower` y `witch_tower` ahora otorgan `minecraft:iron_ingot`.
- fokus: predicate `is_night` añadido.
- nerospace: advancement `guide/new_life` de cría añadido.
- nerologistics: receta del `configurator` restaurada.
- Docs CurseForge (`docs/curseforge/`) y workflow propio (`docs/WORKFLOW_ENCHANTVENTURE_FIXES_26-2.md`).

### Cambiado

- `ageforged_armor` eliminado del datapack: las correcciones viven en el mod (`ageforged_armor/26.2`).
- El ZIP ya no embebe la carpeta interna: carga directa en `world/datapacks/`.
