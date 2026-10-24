# Starts the local WordPress copy and installs the same theme and plugins the live site uses.
# Safe to run again: it skips anything already done.
# Usage (from this folder):  .\setup.ps1

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

function Wp { docker compose run --rm wpcli wp @args }

Write-Host 'Starting containers...'
docker compose up -d
if ($LASTEXITCODE -ne 0) { throw 'docker compose up failed. Is Docker Desktop running?' }

Write-Host 'Waiting for WordPress to come up...'
$ready = $false
foreach ($i in 1..60) {
	$code = curl.exe -s -o NUL -w '%{http_code}' --max-time 5 http://localhost:8080/wp-login.php
	if ($code -in '200', '302') { $ready = $true; break }
	Start-Sleep -Seconds 2
}
if (-not $ready) { throw 'WordPress did not respond on http://localhost:8080 within 2 minutes.' }

docker compose run --rm wpcli wp core is-installed 2>$null
if ($LASTEXITCODE -ne 0) {
	Write-Host 'Installing WordPress...'
	Wp core install --url=http://localhost:8080 --title='Paws Fur Thought (LOCAL COPY)' `
		--admin_user=admin --admin_password=admin --admin_email=admin@example.com --skip-email
}

Write-Host 'Installing theme and plugins used on the live site...'
Wp theme install zakra --activate
Wp plugin install elementor ninja-forms modula-best-grid-gallery all-in-one-wp-migration --activate
Wp rewrite structure '/%postname%/' --hard

Write-Host ''
Write-Host 'Ready.'
Write-Host '  Site:      http://localhost:8080'
Write-Host '  Admin:     http://localhost:8080/wp-admin   (admin / admin until you import the live copy)'
Write-Host '  Mail trap: http://localhost:8025'
Write-Host ''
Write-Host 'Next: import a copy of the live site. See README.md, step 2.'
