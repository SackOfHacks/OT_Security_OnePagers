#!/usr/bin/env python3
"""Run every repo check. Stdlib only — no pytest, no install step.

    python3 tools/run_tests.py     (Linux)
    py -3 tools\\run_tests.py       (Windows)

Checks:
  1. README links, deliverable coverage, protocol-directory completeness
  2. .gitignore holds the strict-allowlist policy
  3. control: the same .gitignore audit, run against a throwaway repo
     carrying the OLD denylist, must FAIL

Check 3 is the one that matters most. Both other checks exit 0 on success,
and an exit 0 reads as an assurance — so if a rule ever silently stops
matching, the suite goes green while checking nothing. The control asserts
the audit still reports a violation when the policy is genuinely violated.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TOOLS = REPO / "tools"

# The .gitignore this repo used before the allowlist: a denylist that only
# blocks what it already enumerated. Kept inline as a fixture so the control
# cannot drift away from the thing it is meant to represent.
DENYLIST_FIXTURE = """\
# Office lock/owner files
~$*.pptx
~$*.docx
~$*.xlsx
*.tmp

# PowerPoint/LibreOffice recovery + backup artefacts
*.~ppt*
.~lock.*#

# OS cruft
.DS_Store
._*
Thumbs.db
desktop.ini

# Editor
.vscode/
.idea/
*.swp

# Machine-local Claude Code settings
.claude/settings.local.json
"""


def run(script, *args):
    return subprocess.run([sys.executable, str(script), *args],
                          capture_output=True, text=True)


def report(name, proc, expect):
    ok = proc.returncode == expect
    print(f"\n{'=' * 68}\n{name}\n{'=' * 68}")
    print(proc.stdout.rstrip() or "(no output)")
    if proc.stderr.strip():
        print(f"stderr:\n{proc.stderr.rstrip()}")
    verb = "PASS" if ok else "FAIL"
    print(f"--> {verb} (exit {proc.returncode}, expected {expect})")
    return ok


def control_denylist_must_fail():
    """Run the audit against a temp repo holding the old denylist."""
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        tmp = Path(tmp)
        init = subprocess.run(["git", "init", "-q", str(tmp)],
                              capture_output=True, text=True)
        if init.returncode != 0:
            raise RuntimeError(f"git init failed: {init.stderr}")
        (tmp / ".gitignore").write_text(DENYLIST_FIXTURE, encoding="utf-8")
        return run(TOOLS / "gitignore_audit.py", str(tmp))


def main():
    results = []

    results.append(report(
        "1. README links, coverage and protocol-directory completeness",
        run(TOOLS / "readme_links.py"), expect=0))

    results.append(report(
        "2. .gitignore strict-allowlist policy",
        run(TOOLS / "gitignore_audit.py"), expect=0))

    results.append(report(
        "3. CONTROL — same audit vs the old denylist, must report failures",
        control_denylist_must_fail(), expect=1))

    passed = sum(results)
    print(f"\n{'=' * 68}")
    print(f"{passed}/{len(results)} checks passed")
    print("=" * 68)
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
