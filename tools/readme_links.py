#!/usr/bin/env python3
"""Check README.md against the files actually in the repo.

Three assertions, all mechanical:

  1. every relative link and image target in README.md resolves to a real path
  2. every deliverable in the repo is referenced by README.md, so a sheet
     cannot be added and then left off the page
  3. every protocol directory carries the full pdf/png/pptx set plus a
     thumbnail in assets/
  4. the sheet-count badge matches the number of protocol directories, so
     the headline number cannot quietly go stale when a sheet is added

Run directly, or via tools/run_tests.py.
Exit 0 = all pass, 1 = at least one failure.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".claude", ".github", "assets", "tools"}
REQUIRED_FORMATS = {".pdf", ".png", ".pptx"}


def protocol_dirs():
    return sorted(
        d for d in REPO.iterdir()
        if d.is_dir() and d.name not in SKIP_DIRS and not d.name.startswith(".")
    )


def main():
    readme = (REPO / "README.md").read_text(encoding="utf-8")

    targets = [m.group(1) for m in re.finditer(r"\]\(([^)\s]+)\)", readme)]
    targets += [m.group(1) for m in re.finditer(r'(?:src|href)="([^"]+)"', readme)]

    broken, referenced = [], set()
    for t in targets:
        if t.startswith(("http://", "https://", "#", "mailto:")):
            continue
        rel = t.split("#")[0].lstrip("./")
        referenced.add(rel)
        if not (REPO / rel).exists():
            broken.append(t)

    print(f"[1] README link/image targets resolve ({len(targets)} checked)")
    for t in broken:
        print(f"    FAIL  broken target: {t}")
    if not broken:
        print("    all pass")

    deliverables = [
        f"{d.name}/{f.name}" for d in protocol_dirs() for f in sorted(d.iterdir())
    ]
    deliverables += [
        f"assets/{f.name}" for f in sorted((REPO / "assets").iterdir())
    ]
    unreferenced = [d for d in deliverables if d not in referenced]

    print(f"\n[2] deliverables referenced by README ({len(deliverables)} checked)")
    for d in unreferenced:
        print(f"    FAIL  not referenced: {d}")
    if not unreferenced:
        print("    all pass")

    print(f"\n[3] protocol directories complete ({len(protocol_dirs())} checked)")
    incomplete = []
    for d in protocol_dirs():
        exts = {f.suffix.lower() for f in d.iterdir()}
        missing = REQUIRED_FORMATS - exts
        pdf = next((f for f in d.iterdir() if f.suffix.lower() == ".pdf"), None)
        thumb = (REPO / "assets" / f"{pdf.stem}_thumb.jpg") if pdf else None
        no_thumb = thumb is None or not thumb.exists()
        if missing or no_thumb:
            incomplete.append(d.name)
            detail = []
            if missing:
                detail.append(f"missing formats {sorted(missing)}")
            if no_thumb:
                detail.append(
                    f"missing thumbnail assets/{pdf.stem}_thumb.jpg" if pdf
                    else "no .pdf to derive a thumbnail name from"
                )
            print(f"    FAIL  {d.name}: {'; '.join(detail)}")
        else:
            print(f"    ok    {d.name}")

    print("\n[4] sheet-count badge matches the repo")
    badge_wrong = []
    actual = len(protocol_dirs())
    m = re.search(r"img\.shields\.io/badge/sheets-(\d+)-", readme)
    if m is None:
        badge_wrong.append("no sheets badge found in README.md")
    elif int(m.group(1)) != actual:
        badge_wrong.append(
            f"badge says {m.group(1)} sheet(s), repo has {actual} "
            f"({', '.join(d.name for d in protocol_dirs())})"
        )
    for msg in badge_wrong:
        print(f"    FAIL  {msg}")
    if not badge_wrong:
        print(f"    ok    badge and repo both say {actual}")

    total = len(broken) + len(unreferenced) + len(incomplete) + len(badge_wrong)
    print(f"\n{'PASS' if total == 0 else f'FAIL: {total} violation(s)'}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
