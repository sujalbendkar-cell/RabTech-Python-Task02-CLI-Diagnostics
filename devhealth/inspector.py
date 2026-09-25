"""
Developer Environment Inspector Module.
"""
import sys, shutil, os, platform, subprocess

class DevInspector:
    def __init__(self):
        self.req_tools = ["git", "python", "pip"]
        self.opt_tools = ["docker", "code", "node"]

    def check_python(self):
        v = sys.version_info[:3]
        ver_str = f"{v[0]}.{v[1]}.{v[2]}"
        ok = v >= (3, 8)
        return {"name": "Python", "val": ver_str, "status": "OK" if ok else "FAIL"}

    def check_disk(self, p="."):
        if not os.path.exists(p):
            return {"name": "Disk", "status": "CONFIG_ERROR", "msg": f"Path '{p}' invalid"}
        total, used, free = shutil.disk_usage(p)
        free_gb = round(free / (1024 ** 3), 2)
        status = "FAIL" if free_gb < 2.0 else ("WARN" if free_gb < 10.0 else "OK")
        return {"name": "Disk", "free_gb": free_gb, "status": status, "msg": f"{free_gb} GB free"}

    def check_env(self):
        env_vars = ["PATH", "VIRTUAL_ENV", "PYTHONPATH"]
        found = {k: os.environ.get(k) for k in env_vars}
        status = "WARN" if not os.environ.get("VIRTUAL_ENV") else "OK"
        return {"name": "Env", "vars": found, "status": status}

    def check_tools(self):
        res = {}
        missing_req = []
        for t in self.req_tools + self.opt_tools:
            path = shutil.which(t)
            is_req = t in self.req_tools
            res[t] = {"installed": bool(path), "path": path, "req": is_req}
            if not path and is_req:
                missing_req.append(t)
        status = "FAIL" if missing_req else "OK"
        return {"name": "Tools", "tools": res, "missing_req": missing_req, "status": status}

    def run_all(self, p="."):
        c1 = self.check_python()
        c2 = self.check_disk(p)
        c3 = self.check_env()
        c4 = self.check_tools()
        
        statuses = [c1["status"], c2["status"], c3["status"], c4["status"]]
        if "CONFIG_ERROR" in statuses: overall = "CONFIG_ERROR"
        elif "FAIL" in statuses: overall = "FAIL"
        elif "WARN" in statuses: overall = "WARN"
        else: overall = "OK"

        return {
            "sys": {"os": platform.system(), "host": platform.node()},
            "checks": {"python": c1, "disk": c2, "env": c3, "tools": c4},
            "overall": overall
        }