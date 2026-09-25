#!/usr/bin/env bash
# 🏥 DevHealth CLI Diagnostics Launcher Script
# Author: Sujal Bendkar | RabTech Academy Python Software Engineering Task 02

echo "=================================================="
echo "  🏥 DEVHEALTH CLI DIAGNOSTICS LAUNCHER"
echo "=================================================="

# Ensure package is installed locally
python3 -m pip install -e . --quiet 2>/dev/null || python -m pip install -e . --quiet

# Execute CLI tool with all passed arguments
python3 -m devhealth.cli "$@" 2>/dev/null || python -m devhealth.cli "$@"
