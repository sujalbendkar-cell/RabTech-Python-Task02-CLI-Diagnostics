"""
Report Formatter Module.
"""
import json

class HealthReporter:
    @staticmethod
    def to_json(d):
        return json.dumps(d, indent=2)

    @staticmethod
    def to_console(d):
        s = d["sys"]
        c = d["checks"]
        o = d["overall"]
        
        lines = [
            "==================================================",
            "  🏥 DEVHEALTH CLI DIAGNOSTICS REPORT",
            "==================================================",
            f" OS: {s['os']} | Host: {s['host']} | Overall: [{o}]",
            "--------------------------------------------------",
            f" 🐍 Python: [{c['python']['status']}] Version {c['python']['val']}",
            f" 💾 Disk:   [{c['disk']['status']}] {c['disk']['msg']}",
            f" 🌐 Env:    [{c['env']['status']}] VirtualEnv: {'Active' if c['env']['vars']['VIRTUAL_ENV'] else 'Not Active'}",
            f" 🛠️  Tools:  [{c['tools']['status']}] Missing Req: {c['tools']['missing_req'] or 'None'}",
            "=================================================="
        ]
        return "\n".join(lines)