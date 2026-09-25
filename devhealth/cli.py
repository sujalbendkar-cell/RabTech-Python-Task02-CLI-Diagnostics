"""
CLI Entry Point.
"""
import sys, argparse, os
from devhealth.inspector import DevInspector
from devhealth.reporter import HealthReporter
from devhealth.utils import ExitCode

def main():
    p = argparse.ArgumentParser(prog="devhealth", description="CLI Health Tool")
    p.add_argument("-j", "--json", action="store_true", help="JSON output")
    p.add_argument("-o", "--output", type=str, help="Output file")
    p.add_argument("-p", "--path", type=str, default=".", help="Target path")

    args = p.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Invalid path '{args.path}'", file=sys.stderr)
        sys.exit(ExitCode.CONFIG_ERROR)

    insp = DevInspector()
    data = insp.run_all(args.path)

    out = HealthReporter.to_json(data) if args.json else HealthReporter.to_console(data)
    print(out)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"Report saved to {args.output}")

    code = ExitCode.SUCCESS if data["overall"] == "OK" else (
        ExitCode.WARNING if data["overall"] == "WARN" else (
        ExitCode.CONFIG_ERROR if data["overall"] == "CONFIG_ERROR" else ExitCode.FAILURE
    ))
    sys.exit(code)

if __name__ == "__main__":
    main()