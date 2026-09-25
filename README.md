# 🏥 DevHealth - Packaged CLI Diagnostics Tool

**Intern Name:** Sujal Bendkar  
**Intern ID:** `RAB-2026-9471669A59`  
**Track:** Python Software Engineering (RabTech Academy)  
**Task 02:** Packaged CLI Diagnostics Tool  

---

## 📌 Project Overview
`devhealth` is a distributable, production-ready command-line diagnostic tool built in Python. It inspects a developer's machine environment and produces a deterministic health report covering Python runtime versions, available disk space, environment variables, and essential developer tools (`git`, `docker`, `python`, `pip`, `vscode`, `node`).

---

## 🛠️ Features & Architecture

* **📦 Distributable Package:** Packaged using modern `pyproject.toml` standards with entry point (`devhealth`).
* **🔍 System Inspection:** Inspects Python runtime version, disk space, environment variables, and developer tools.
* **📊 Dual Reporting:** Human-readable console output & `--json` structured format.
* **🎯 Exit Codes:** `0` (Success), `1` (Warning), `2` (Failure), `3` (Config Error).
* **⚡ One-Click Shell Launchers:** Includes `run_diagnostics.sh` (Bash) and `run_diagnostics.ps1` (PowerShell).
* **🧪 Unit Testing:** Automated test suite using Python `unittest`.

---

## 🚀 Quick Start & Installation

### Option 1: One-Click Shell Script (Linux / macOS / Git Bash)
```bash
chmod +x run_diagnostics.sh
./run_diagnostics.sh
```

### Option 2: One-Click PowerShell Script (Windows)
```powershell
.\run_diagnostics.ps1
```

### Option 3: Manual Installation & CLI Commands
```bash
# 1. Install locally in editable mode
pip install -e .

# 2. Run standard console health check
devhealth

# 3. Output structured JSON
devhealth --json

# 4. Save report to file
devhealth --output report.json

# 5. Run automated unit tests
python -m unittest discover tests
```

---

## 📋 Repository Structure
```text
RabTech-Python-Task02-CLI-Diagnostics/
├── pyproject.toml                     # Package setup manifest
├── README.md                          # Comprehensive documentation
├── run_diagnostics.sh                 # One-click Bash launcher script
├── run_diagnostics.ps1                # One-click PowerShell launcher script
├── devhealth/                         # Main Python package
│   ├── __init__.py                    # Version metadata
│   ├── cli.py                         # CLI entry point
│   ├── inspector.py                   # Health inspection engine
│   ├── reporter.py                    # Console & JSON formatters
│   └── utils.py                       # Exit code definitions
└── tests/                             # Unit tests
    └── test_inspector.py              # Inspection unit tests
```

---

## 👤 Author & Credits
* **Developer:** Sujal Bendkar
* **Batch:** `BATCH-SEP-2026`
* **Academy:** RabTech Academy - Python Software Engineering Internship