#!/usr/bin/env python3
"""Check relative Markdown links against files and directories in this repository."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]*)\)")

def main() -> int:
    markdown_files = sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )
    failures: list[str] = []

    for markdown_file in markdown_files:
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">") ]
            else:
                target = target.split()[0] if target else ""
            if not target:
                continue

            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue

            relative_path = unquote(parsed.path)
            candidate = (markdown_file.parent / relative_path).resolve()
            if not candidate.is_relative_to(ROOT):
                failures.append(f"{markdown_file.relative_to(ROOT)}: link escapes repository: {target}")
            elif not candidate.exists():
                failures.append(f"{markdown_file.relative_to(ROOT)}: missing link target: {target}")

    if failures:
        print("Broken internal Markdown links:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Checked internal links in {len(markdown_files)} Markdown files; all targets exist.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
