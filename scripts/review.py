#!/usr/bin/env python3
"""review.py - list, filter, and sample study items tagged in your notes.

Examples
  review.py                      # all open #review items
  review.py -t python            # only the python/ folder
  review.py --since 2026-10-01   # items from notes dated on/after this day
  review.py -r 3                 # 3 random items for a quick daily review
  review.py --stats              # open vs done counts per track
  review.py --tag '#todo'        # use a different tag

Notes root: --root, or $LEARNING_NOTES, or the notes/ directory beside scripts/.
"""
import argparse
import os
import random
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)")


def tag_regex(tag):
    # match the tag as a whole token so #review doesn't match #reviewed
    return re.compile(r"(?<![\w#])" + re.escape(tag) + r"(?![\w-])")


def note_date(path):
    m = DATE_RE.search(path.stem)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def scan(root, tag):
    """Yield dicts for every line containing `tag`."""
    rx = tag_regex(tag)
    for f in sorted(root.rglob("*.md")):
        rel = f.relative_to(root)
        if f.name.lower() == "readme.md":
            continue
        # skip top-level files (README etc.) and non-note folders
        if len(rel.parts) < 2 or rel.parts[0] in ("templates", ".git", ".obsidian"):
            continue
        topic = rel.parts[0]
        heading = ""
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as e:
            print(f"skipping {rel}: {e}", file=sys.stderr)
            continue
        in_code = False
        for i, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            h = HEADING_RE.match(line)
            if h and not rx.search(line):
                heading = h.group(1).strip()
                continue
            if rx.search(line):
                yield {
                    "path": rel,
                    "line": i,
                    "topic": topic,
                    "date": note_date(f),
                    "heading": heading,
                    "text": line.strip(),
                }


def show(items):
    if not items:
        print("Nothing to review. Nice.")
        return
    current = None
    for it in items:
        if it["path"] != current:
            current = it["path"]
            print(f"\n{current}")
        ctx = f"  [{it['heading']}]" if it["heading"] else ""
        print(f"  L{it['line']:<4} {it['text']}{ctx}")
    print(f"\n{len(items)} item(s)")


def stats(root, open_tag, done_tag):
    open_c, done_c = defaultdict(int), defaultdict(int)
    for it in scan(root, open_tag):
        open_c[it["topic"]] += 1
    for it in scan(root, done_tag):
        done_c[it["topic"]] += 1
    topics = sorted(set(open_c) | set(done_c))
    if not topics:
        print("No tagged items yet.")
        return
    print(f"{'track':<12}{'open':>6}{'done':>6}")
    for t in topics:
        print(f"{t:<12}{open_c[t]:>6}{done_c[t]:>6}")
    print(f"{'total':<12}{sum(open_c.values()):>6}{sum(done_c.values()):>6}")


def main():
    p = argparse.ArgumentParser(description="List tagged study items in your notes.")
    p.add_argument("--root", default=os.environ.get("LEARNING_NOTES", str(Path(__file__).resolve().parent.parent / "notes")))
    p.add_argument("-t", "--topic", help="only this top-level folder (python, linux, git, ai-dev, inbox)")
    p.add_argument("--tag", default="#review", help="tag to search for (default: #review)")
    p.add_argument("--done-tag", default="#done", help="tag counted as finished in --stats")
    p.add_argument("--since", help="only notes dated on/after YYYY-MM-DD (from the filename)")
    p.add_argument("-r", "--random", type=int, metavar="N", help="show N random items")
    p.add_argument("--stats", action="store_true", help="show open/done counts per track")
    args = p.parse_args()

    root = Path(args.root).expanduser()
    if not root.is_dir():
        sys.exit(f"Notes folder not found: {root}")

    if args.stats:
        stats(root, args.tag, args.done_tag)
        return

    items = list(scan(root, args.tag))
    if args.topic:
        items = [i for i in items if i["topic"] == args.topic]
    if args.since:
        try:
            cutoff = date.fromisoformat(args.since)
        except ValueError:
            sys.exit("--since must look like 2026-10-01")
        items = [i for i in items if i["date"] and i["date"] >= cutoff]
    if args.random:
        items = random.sample(items, min(args.random, len(items)))
        items.sort(key=lambda i: (str(i["path"]), i["line"]))
    show(items)


if __name__ == "__main__":
    main()
