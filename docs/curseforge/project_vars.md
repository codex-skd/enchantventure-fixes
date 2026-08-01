# CurseForge — Variables del proyecto

## Proyecto

| Variable | Valor |
|----------|-------|
| `curseforge_project_id` | `1633366` (en espera de validación) |
| `mod_id` | `enchantventure_fixes` |
| `display_name` | `EnchantVenture Fixes` |

## Tokens

| API | Token | Uso |
|-----|-------|-----|
| Upload | `PENDIENTE` (token de cuenta, mismo que los mods) | Subir archivos ZIP |
| Core (GET) | `PENDIENTE` | Consultar datos del proyecto |

Autenticación Upload: cabecera `X-Api-Token`
Autenticación Core: cabecera `x-api-key`

> El API token de CurseForge es el mismo para todos los proyectos (token de cuenta, no de proyecto).

## Versión actual

| Variable | Valor |
|----------|-------|
| `minecraft_version` | `26.2` |
| `pack_format` | `107` |
| `environment` | `Server` |

## Rama

```
minecraft/26.2/datapack/production
```

## Tag

Formato: `<mc-version>-<version>`
Ejemplo: `26.2-0.0.0-beta.1`

## Parámetros del upload

| Campo | Valor | Notas |
|-------|-------|-------|
| `displayName` | `EnchantVenture Fixes (0.0.0-beta.3)` | Nombre visible: `display_name (version)` |
| `changelog` | HTML (no Markdown) | Ver estructura abajo |
| `changelogType` | `html` | Obligatorio para que se vea bien |
| `releaseType` | `beta` | Según el tipo de versión |
| `gameVersions` | `[107, 26.2]` | Pack format + MC version. CurseForge trata los datapacks como versión de juego "Datapack" |

## Estructura del changelog (HTML)

```html
<h2>v0.0.0-beta.1 - Initial release</h2>

<h3>Added</h3>
<ul>
<li><strong>EnchantVenture Fixes</strong>: first versioned release of the datapack.</li>
</ul>

<hr>

<p><strong>ZIP</strong>: <code>EnchantVenture_fixes-0.0.0-beta.1.zip</code></p>
```

## Subir archivo (ZIP) con Python

```python
import json, uuid, urllib.request

boundary = uuid.uuid4().hex
version = "0.0.0-beta.3"
project_id = 1633366
api_token = "<API_TOKEN>"

metadata = {
    "displayName": f"EnchantVenture Fixes ({version})",
    "changelog": "<h2>v0.0.0-beta.1 - Initial release</h2>",
    "changelogType": "html",
    "gameVersions": [107, 26.2],
    "releaseType": "beta"
}

with open(f"build/EnchantVenture_fixes-{version}.zip", "rb") as f:
    zip_data = f.read()

meta_bytes = json.dumps(metadata, ensure_ascii=False).encode("utf-8")

body = b""
body += f"--{boundary}\r\n".encode()
body += b'Content-Disposition: form-data; name="metadata"\r\n'
body += b"Content-Type: application/json\r\n\r\n"
body += meta_bytes + b"\r\n"
body += f"--{boundary}\r\n".encode()
body += b'Content-Disposition: form-data; name="file"; filename="EnchantVenture_fixes-{version}.zip"\r\n'
body += b"Content-Type: application/zip\r\n\r\n"
body += zip_data + b"\r\n"
body += f"--{boundary}--\r\n".encode()

req = urllib.request.Request(
    f"https://minecraft.curseforge.com/api/projects/{project_id}/upload-file",
    data=body,
    headers={
        "X-Api-Token": api_token,
        "Content-Type": f"multipart/form-data; boundary={boundary}"
    },
    method="POST"
)

resp = urllib.request.urlopen(req)
print(resp.read().decode())
```

> Nota: `gameVersions` usa el `gameVersionId` de Minecraft (de `GET /v1/minecraft/version`), no el pack format. Para `26.2` el id válido es `16498`.

## Verificar con GET

```bash
curl -s "https://api.curseforge.com/v1/mods/1633366/files/<FILE_ID>" \
  -H "x-api-key: <API_TOKEN>"
```

## Descripcion del proyecto

No hay endpoint API para actualizar la descripcion. Se edita manualmente desde la web de CurseForge pegando el HTML de `docs/curseforge/project_description.md`.

## Variables parseables (para scripts)

El script `scripts/curseforge-upload.ps1` lee estas líneas (`key = value`):

```
project_id = 1633366
api_token = PENDIENTE
game_versions = 16498
release_type = beta
```

## Flujo completo

1. `python build_fix_pack.py`
2. Actualizar `docs/curseforge/versions/<version>.md` con HTML
3. Actualizar `CHANGELOG.md`
4. `git commit -m "chore: bump version to <version>"` + `git push`
5. `git tag -a 26.2-<version> -m "v<version>: descripcion"` + `git push origin <tag>`
6. Subir ZIP a CurseForge con `scripts/curseforge-upload.ps1`
7. Verificar con GET que el changelog se vea bien
8. Liberar manualmente desde la web si es necesario
