# CurseForge Upload Script — Datapack (EnchantVenture_fixes)
# Adapted from codex-docs/scripts/curseforge-upload.ps1 (mods): reads version.txt instead of
# gradle.properties, uploads the ZIP from build/ as application/zip with Datapack game versions.
#
# Usage (desde la raíz del repo):
#   powershell -File scripts/curseforge-upload.ps1
#
# Requires:
#   - docs/curseforge/project_vars.md with: project_id, api_token, game_versions
#   - version.txt with the current version
#   - build/EnchantVenture_fixes-<version>.zip (run python build_fix_pack.py first)
#   - docs/curseforge/versions/<version>.md with release notes in HTML

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoPath = Resolve-Path "$scriptPath/.."

function Get-VarFromMd($file, $key) {
    $line = Select-String -Path $file -Pattern "^\s*$key\s*=\s*(.+)" | Select-Object -First 1
    if ($line) { return $line.Matches.Groups[1].Value.Trim() }
    return $null
}

# Load vars
$varsFile = "$repoPath/docs/curseforge/project_vars.md"
$projectId = Get-VarFromMd $varsFile "project_id"
$apiToken = Get-VarFromMd $varsFile "api_token"
$gameVersionsStr = Get-VarFromMd $varsFile "game_versions"
$releaseType = Get-VarFromMd $varsFile "release_type"
if (-not $releaseType) { $releaseType = "beta" }
if (-not $gameVersionsStr) { $gameVersionsStr = "107,26.2" }

$modVersion = (Get-Content "$repoPath/version.txt").Trim()
$modName = "EnchantVenture Fixes"

# @(...) forces an array; otherwise PowerShell unwraps single values and ConvertTo-Json
# emits an integer instead of a JSON array, which CurseForge rejects.
$gameVersions = @($gameVersionsStr -split "," | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" } | ForEach-Object { [int]$_ })

# Build paths
$zipName = "EnchantVenture_fixes-${modVersion}.zip"
$zipPath = "$repoPath/build/$zipName"
$changelogPath = "$repoPath/docs/curseforge/versions/${modVersion}.md"

# Validate
if (-not (Test-Path $zipPath)) {
    Write-Host "ERROR: ZIP not found at $zipPath" -ForegroundColor Red
    Write-Host "Run 'python build_fix_pack.py' first"
    exit 1
}

if (-not (Test-Path $changelogPath)) {
    Write-Host "ERROR: Changelog not found at $changelogPath" -ForegroundColor Red
    exit 1
}

if ($projectId -eq "PENDIENTE" -or -not $projectId) {
    Write-Host "ERROR: curseforge_project_id not set in docs/curseforge/project_vars.md" -ForegroundColor Red
    exit 1
}

$changelog = [System.IO.File]::ReadAllText((Resolve-Path $changelogPath))

$metadata = @{
    displayName = "${modName} (${modVersion})"
    gameVersions = $gameVersions
    releaseType = $releaseType
    changelogType = "html"
    changelog = $changelog
}

$metadataJson = $metadata | ConvertTo-Json -Compress

Add-Type -AssemblyName System.Net.Http

$fileItem = Get-Item -Path (Resolve-Path $zipPath)
$fileBytes = [System.IO.File]::ReadAllBytes($fileItem.FullName)

$httpClient = New-Object System.Net.Http.HttpClient
$httpClient.DefaultRequestHeaders.Add('X-Api-Token', $apiToken)

$multipart = New-Object System.Net.Http.MultipartFormDataContent
$multipart.Add((New-Object System.Net.Http.StringContent($metadataJson, [System.Text.Encoding]::UTF8, "application/json")), "metadata")

$fileContent = New-Object System.Net.Http.ByteArrayContent(,$fileBytes)
$fileContent.Headers.ContentType = [System.Net.Http.Headers.MediaTypeHeaderValue]::Parse("application/zip")
$multipart.Add($fileContent, "file", $fileItem.Name)

Write-Host "Uploading $zipName to CurseForge project $projectId..." -ForegroundColor Cyan

try {
    $response = $httpClient.PostAsync("https://minecraft.curseforge.com/api/projects/$projectId/upload-file", $multipart).GetAwaiter().GetResult()
    $responseBody = $response.Content.ReadAsStringAsync().GetAwaiter().GetResult()
    if ($response.IsSuccessStatusCode) {
        Write-Host "Status: $([int]$response.StatusCode)" -ForegroundColor Green
        Write-Host "Response: $responseBody"
    } else {
        Write-Host "Status: $([int]$response.StatusCode)" -ForegroundColor Red
        Write-Host "Body: $responseBody"
        exit 1
    }
} catch {
    Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
} finally {
    $httpClient.Dispose()
    $multipart.Dispose()
}
