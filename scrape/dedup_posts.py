#!/usr/bin/env python3
"""Deduplicate posts/*.md by source URL.

Strategy: for each SRC, group files by their `source:` URL.
Keep the FIRST (alphabetically smallest) file per URL — preserves history.
Delete the rest. Reports what it would delete, asks for confirmation unless
--yes is passed.
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_source(path):
    """Read first `source:` line from a post .md file."""
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                if line.startswith('source:'):
                    return line[len('source:'):].strip()
                if line.startswith('# '):
                    continue
    except Exception:
        pass
    return None


def dedup_src(sid, yes=False, dry=False):
    d = os.path.join(ROOT, 'sources', sid, 'posts')
    if not os.path.isdir(d):
        return 0
    # recursive: covers posts/ top level and posts/<tab>/ subdirs
    files = sorted(
        os.path.relpath(os.path.join(root, fn), d)
        for root, _dirs, fns in os.walk(d)
        for fn in fns if fn.endswith('.md'))
    if not files:
        return 0
    by_url = {}  # url -> [filename, ...]
    for fn in files:
        url = extract_source(os.path.join(d, fn))
        if not url:
            continue
        by_url.setdefault(url, []).append(fn)
    to_delete = []
    for url, group in by_url.items():
        if len(group) > 1:
            keep = sorted(group)[0]  # alphabetical first (01_xxx before 13_xxx)
            for fn in group:
                if fn != keep:
                    to_delete.append((fn, url))
    if not to_delete:
        return 0
    print(f'[{sid}] {len(files)} files → {len(to_delete)} dup to delete:')
    for fn, url in to_delete:
        print(f'  rm {fn}  ({url})')
    if dry:
        return len(to_delete)
    if not yes:
        ans = input(f'  proceed? [y/N] ').strip().lower()
        if ans != 'y':
            print('  skipped')
            return 0
    for fn, _ in to_delete:
        os.remove(os.path.join(d, fn))
    print(f'  deleted {len(to_delete)}')
    return len(to_delete)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src_ids', nargs='*')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--yes', action='store_true', help='skip confirmation')
    ap.add_argument('--dry', action='store_true', help='show only')
    args = ap.parse_args()
    if args.all or not args.src_ids:
        targets = sorted(d for d in os.listdir(os.path.join(ROOT, 'sources'))
                         if d.startswith('SRC-'))
    else:
        targets = args.src_ids
    total = 0
    for sid in targets:
        n = dedup_src(sid, yes=args.yes, dry=args.dry)
        total += n
    print(f'\nTOTAL dups: {total}')


if __name__ == '__main__':
    main()