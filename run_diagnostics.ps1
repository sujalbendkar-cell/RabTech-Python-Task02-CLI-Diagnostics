# 🏥 DevHealth CLI Diagnostics Launcher Script for PowerShell
# Author: Sujal Bendkar | RabTech Academy Python Software Engineering Task 02

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  🏥 DEVHEALTH CLI DIAGNOSTICS LAUNCHER" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

python -m pip install -e . --quiet
python -m devhealth.cli $args
