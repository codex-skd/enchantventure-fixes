# Flujo de trabajo — EnchantVenture_fixes (Datapack)

> **Versión del workflow**: 1.16.0 (codex-docs)
> Este archivo pertenece al proyecto **EnchantVenture_fixes**. Cambios aquí solo afectan a este proyecto.
> **Trabaja directamente con este archivo**: es el workflow operativo del datapack, autocontenido. No leas `codex-docs/WORKFLOW_AGENT.md` ni `WORKFLOW_GENERIC.md` de forma rutinaria.
> On-demand (solo si la tarea lo necesita): `codex-docs/reference/CURSEFORGE.md` (formato HTML al publicar), `codex-docs/reference/REPO_SETUP.md` (setup único de repo).

## Específico del datapack

| Dato | Valor |
|---|---|
| Nombre del proyecto (`version.txt`) | `EnchantVenture_fixes` |
| Display name (Title Case) | `EnchantVenture Fixes` |
| Versión de Minecraft | `26.2` |
| Pack format | `107` (`pack.mcmeta`, `min_format` 107) |
| Rama de trabajo | `minecraft/26.2/datapack/production` |
| Rama pública hermana | `minecraft/26.2/datapack/main` (protegida, la escribe CI/CD) |

## Diferencias con un mod NeoForge

| Aspecto | Mod | Datapack |
|---|---|---|
| Build | `./gradlew.bat clean build` → JAR | `python build_fix_pack.py` → ZIP |
| Artefacto | `build/libs/<mod_id>-...-<version>.jar` | `build/EnchantVenture_fixes-<version>.zip` |
| Versión | `mod_version` en `gradle.properties` | `version.txt` (única fuente de verdad) |
| Upload CurseForge | `curseforge-upload.ps1` genérico (lee `gradle.properties`) | `scripts/curseforge-upload.ps1` propio (lee `version.txt`) |
| gameVersions | `["Client", "Server", "26.2", "NeoForge"]` | `["Datapack", "26.2"]` |
| Tag | `<mc>-neoforge-<version>` | `26.2-<version>` (sin modloader) |
| docs/curseforge | project_description / project_vars / versions | **idéntica** |

## Estructura del proyecto

`build_fix_pack.py` (genera `datapack/` desde los JARs de la instancia) · `version.txt` · `datapack/` (datapack real, versionado) · `build/` (no versionado, solo el ZIP) · `docs/WORKFLOW...` + `docs/curseforge/` · `CHANGELOG.md` · `README.md`.

`build_fix_pack.py` lee los JARs desde la instancia local de CurseForge:

```
MODS = C:\Users\llagu\curseforge\minecraft\Instances\EnchantVenture\mods
```

`ageforged_armor` NO forma parte del datapack: sus correcciones viven en el mod (`ageforged_armor/26.2`). No reintroducir workarounds del mod en `build_fix_pack.py`.

## Versionado

- Beta `0.0.0-beta.X` · Release `X.Y.Z` (SemVer)
- Versión en `version.txt`. ZIP: `EnchantVenture_fixes-<version>.zip`
- Primer versionado: `0.0.0-beta.1`

## Commits (Conventional Commits)

`<tipo>[<ámbito>]: <descripción>` · tipos `feat fix refactor docs chore style perf test` · el mensaje incluye la versión (`v<version>`).

## Tags

Cada subida a CurseForge crea tag: beta `26.2-beta.X` · release `26.2-X.Y.Z`.

## Flujo por tarea

**0. Alcance** — si se plantea soporte multi-versión, preguntar con la herramienta `question`: **"Todas"** o una versión. No asumir.

**1. Desarrollo**

```bash
git checkout minecraft/26.2/datapack/production
python build_fix_pack.py
git add -A
git commit -m "feat: <descripción>

v<version>"
git push
```

El script regenera `datapack/` desde los JARs; revisar el diff (`git diff -- datapack/`) antes de commitear.

**2. CurseForge** — solo si el usuario confirma:
- Bump `version.txt` → `python build_fix_pack.py`
- Release notes `docs/curseforge/versions/<version>.md` (HTML) + actualizar `CHANGELOG.md`
- Commit `chore: bump version to <version>` → tag `26.2-<version>` → push
- Subir ZIP: `powershell -File scripts/curseforge-upload.ps1` (desde este repo)
- Formato HTML de descripciones/changelog: `codex-docs/reference/CURSEFORGE.md`

**3. Release estable** — bump `X.Y.Z` + tag.

**4. Graphify** — tras cada push a remoto. Versión 0.9.12: **`build` no existe**, usar `extract` (1ª vez) o `update . --force` (tras cambios):

```bash
GRAPHIFY="C:\Users\llagu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\graphify.exe"
"$GRAPHIFY" update . --force
git add graphify-out/ && git commit -m "chore: update knowledge graph" && git push
```

Leer siempre `GRAPH_REPORT.md`, nunca `graph.json`/`graph.html` (pesan >1MB). Sin copias fechadas de `graphify-out/`. Backend LLM: `codex-docs/reference/GRAPHIFY.md`.

## Buenas prácticas

- Un commit por cambio lógico · commit+push tras cada cambio funcional y de docs
- `python build_fix_pack.py` antes de subir · versionar antes de CurseForge · CHANGELOG al día
- El ZIP resultante debe tener `pack.mcmeta` en la raíz (carga directa en `datapacks/`)
- Sin basura en repo (`nul`, `*.zip` sueltos en raíz, `temp/`) · `.gitignore` excluye `build/`
- README en inglés siempre actualizado

## Idioma

| Ámbito | Idioma |
|---|---|
| código, logs, commits | en-US |
| README.md | en-US |
| docs internas (docs/, CHANGELOG, este archivo) | es-ES |
| CurseForge | en-US |
