# Changelog

Todos los cambios notables de EnchantVenture Fixes se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.0-beta.9] - 2026-08-18

### Corregido

- ancient_artifacts: `utilities/knockback/loop` usaba el formato antiguo (pre-1.21.5) del componente `enchantments` (`components: {enchantments: {"ancient_artifacts:knockback": 1}}`). En 26.2 el valor del componente `minecraft:enchantments` es `{"levels": {...}}`, por lo que el `summon` del armor_stand lanzaba un error cada vez que las combo boots disparaban un dash (alcanzado desde `tick` → `artifacts/tick` → `combo_boots/tick` → `dash` → `knockback/deal` → `loop`). Corregido a `{"minecraft:enchantments": {"levels": {"ancient_artifacts:knockback": 1}}}`.
- ancient_artifacts: `recycling_crystal/tag_arrow` usaba el mismo formato antiguo como patrón de coincidencia NBT, por lo que la detección de infinity/multishot nunca coincidía (las flechas siempre se etiquetaban `no_infinity`/`no_multishot`). Actualizado al formato `{"levels": {...}}` de 26.2.

## [0.0.0-beta.8] - 2026-08-11

### Corregido

- berezka_api: `chests/treasure` no cargaba — una entrada `minecraft:item` con `minecraft:air` es inválida en 26.2 (`Item must not be minecraft:air`), rechazada al parsear el datapack. Sustituida por `minecraft:empty`.
- `minecraft:chests/houseloot` (namespace vanilla, sin el mod `MineCraftJ` involucrado — ver nota abajo): añadida tabla de loot para un cofre huérfano en `BlockPos{x=-4854, y=70, z=669}` del overworld, cuya tabla original ya no existe en ningún mod instalado. Confirmado por error de Lootr en el log del servidor.

### Nota sobre beta.7

La entrada de beta.7 (`houseloot1` / mod `MineCraftJ`) era incorrecta: ni ese nombre de tabla ni ese mod existen en el modpack ni en los logs revisados. El fix real para el error de Lootr (`minecraft:chests/houseloot`, sin el mod inventado) se implementa en esta versión.

## [0.0.0-beta.7] - 2026-08-06

### Corregido

- minecraft:chests: añadida la tabla de loot faltante `houseloot1`. El mod MineCraftJ la referenciaba pero no estaba definida en el datapack, causando errores; la tabla ahora está correctamente definida con items de loot típicos de casa.

## [0.0.0-beta.6] - 2026-08-03

### Añadido

- berezka_api: reintroducidas las 6 loot tables de cofres (`chests/car`, `farm`, `store`, `diningroom`, `treasure`, `berezkahousesmall_0`). El datapack incorporado del mod (`berezka_api_data`) nunca llega a registrarse — `openPrimary()` lanza una `NullPointerException` al construir los metadatos del pack (el array del icono es `null`) — por lo que ningún cofre `berezka_api:chests/*` cargaba loot, confirmado por errores de Lootr (`couldn't be resolved`) en múltiples posiciones del mundo. Los items se recuperaron de las constantes de texto embebidas en `BuiltInResourcePack.class`; las cantidades son una aproximación razonable salvo en `treasure.json`, recuperada literal con sus valores reales.

## [0.0.0-beta.5] - 2026-08-01

### Añadido

- the_lost_city: añadidos los 5 template pools de spawners que faltaban (`spawners_husk`, `spawners_pillager`, `spawners_vindicator`, `spawners_zombie`, `spawners_zombie_moss`). Los jigsaw blocks de las estructuras los referenciaban pero el mod no los definía, lo que generaba avisos de `lithostitched` y spawners sin colocar; cada pool apunta a su estructura `spawner_<tipo>.nbt`.

## [0.0.0-beta.4] - 2026-08-01

### Añadido

- Tokens de API de CurseForge (Upload y Core) configurados en `docs/curseforge/project_vars.md`.

### Cambiado

- Publicación en CurseForge operativa: `gameVersions` usa el `gameVersionId` de Minecraft (`26.2` → `16498`) en lugar del pack format, y `scripts/curseforge-upload.ps1` solo lee la sección "Variables parseables" de `project_vars.md`.

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
