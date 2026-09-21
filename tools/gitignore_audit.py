#!/usr/bin/env python3
"""Audit .gitignore against the repo's strict-allowlist policy.

The policy is that .gitignore ignores everything and re-includes the known
good file types by exception, so a file type nobody has thought about is not
committable until a rule admits it. This script asserts that in both
directions: the files the repo must carry stay addable, and a set of paths a
poster repo should never carry stay refused.

The verdict comes from `git check-ignore` — git's own matcher — rather than
from reading .gitignore and reasoning about it. No probe files are created
on disk; check-ignore evaluates hypothetical paths.

Run directly, or via tools/run_tests.py.
Exit 0 = policy holds, 1 = at least one assertion failed.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def git(*args, **kw):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, **kw)


def set_repo(path):
    """Point the audit at another working tree.

    Used by tools/run_tests.py to re-run these same assertions against a
    throwaway repo holding the old denylist, proving the check reports a
    failure when the policy is actually violated rather than passing
    vacuously.
    """
    global REPO
    REPO = Path(path).resolve()


def tracked():
    out = git("ls-files", text=True, check=True).stdout
    return [p for p in out.splitlines() if p]


def check_ignored(paths):
    """Return {path: (ignored_bool, rule_str)} using git's own matcher."""
    # Explanatory rule strings, in one batch call.
    #
    # Input is passed as BYTES deliberately. With text=True, Python on
    # Windows rewrites the "\n" separators to "\r\n", git then receives each
    # path with a trailing CR, and every path but the last silently reports
    # "no match" — which reads exactly like a real finding.
    proc = git("check-ignore", "--no-index", "-v", "--non-matching", "--stdin",
               input="\n".join(paths).encode("utf-8"))
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"git check-ignore failed: {proc.stderr.decode()}")

    rules = {}
    for line in proc.stdout.decode("utf-8").splitlines():
        if not line:
            continue
        src, _, path = line.rpartition("\t")
        src = src.strip()
        rules[path] = src if src not in ("::", "") else "no rule matched"

    # The VERDICT comes from check-ignore's exit code, one path at a time:
    # 0 = ignored, 1 = not ignored. That is git's own answer with nothing to
    # misparse. Deriving it from the -v pattern text instead is a trap: -v
    # reports the LAST matching pattern, and for an allowlisted file that is
    # the "!" negation rule, which means the opposite of ignored.
    result = {}
    for p in paths:
        rc = git("check-ignore", "--no-index", "-q", "--", p).returncode
        if rc not in (0, 1):
            raise RuntimeError(f"git check-ignore failed on {p!r}")
        result[p] = (rc == 0, rules.get(p, "?"))

    # Invariant: a verdict for every path submitted. A short result set means
    # the harness is broken, not that the policy passed.
    missing = [p for p in paths if p not in result]
    if missing:
        raise RuntimeError(
            f"no verdict for {len(missing)}/{len(paths)} paths "
            f"(first: {missing[0]!r}) — harness bug, not a policy result"
        )
    return result


# MUST NOT be ignored: everything the repo legitimately carries today...
MUST_KEEP_EXTRA = [
    # ...the next protocol sheet, so the policy cannot silently block growth...
    "IEC61850/IEC61850_Attack_Defend_Poster.pdf",
    "IEC61850/IEC61850_Attack_Defend_Poster.png",
    "IEC61850/IEC61850_Attack_Defend_Poster.pptx",
    "assets/IEC61850_Attack_Defend_Poster_thumb.jpg",
    # ...and this tooling, asserted explicitly so the rule survives a run
    # made before these files are tracked.
    "tools/gitignore_audit.py",
    "tools/readme_links.py",
    "tools/run_tests.py",
]

# MUST be ignored: what a strict allowlist is actually for.
MUST_IGNORE = [
    # credentials / local environment
    ".env",
    "secrets.env",
    "id_rsa",
    "credentials.json",
    "DNP3/api_key.txt",
    "tools/.env",
    # machine-local agent + editor state
    ".claude/settings.local.json",
    ".claude/hooks.json",
    ".vscode/settings.json",
    ".idea/workspace.xml",
    # scratch / working files
    "notes.txt",
    "scratch.py",
    "movies.db",
    "DNP3/draft.docx",
    "assets/working.xcf",
    "tools/scratch.txt",
    "tools/__pycache__/gitignore_audit.cpython-311.pyc",
    # Office lock + recovery artefacts, written beside a real .pptx
    "DNP3/~$DNP3_Attack_Defend_Poster.pptx",
    "DNP3/.~lock.DNP3_Attack_Defend_Poster.pptx#",
    "DNP3/DNP3_Attack_Defend_Poster.~pptx",
    # OS cruft
    "Thumbs.db",
    ".DS_Store",
    "desktop.ini",
    # depth checks: a deliverable extension where it does not belong
    "node_modules/pkg/logo.png",
    "build/out/poster.pdf",
]


def main():
    must_keep = tracked() + MUST_KEEP_EXTRA
    verdict = check_ignored(must_keep + MUST_IGNORE)

    fail_keep = [p for p in must_keep if verdict[p][0]]
    fail_ignore = [p for p in MUST_IGNORE if not verdict[p][0]]

    print("policy: strict allowlist\n")
    print(f"[A] must NOT be ignored ({len(must_keep)} paths)")
    if fail_keep:
        for p in fail_keep:
            print(f"    FAIL  {p}\n          blocked by {verdict[p][1]}")
    else:
        print("    all pass")

    print(f"\n[B] must BE ignored ({len(MUST_IGNORE)} paths)")
    if fail_ignore:
        for p in fail_ignore:
            print(f"    FAIL  {p}   <-- would be committable")
    else:
        print("    all pass")

    total = len(fail_keep) + len(fail_ignore)
    print(f"\n{'PASS' if total == 0 else f'FAIL: {total} violation(s)'}")
    return 1 if total else 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        set_repo(sys.argv[1])
    sys.exit(main())
