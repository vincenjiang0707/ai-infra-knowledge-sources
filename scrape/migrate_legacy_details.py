#!/usr/bin/env python3
"""One-time migration: github_details/{issue|pr}_N.md → github_details/{ch_key}/.

Pre-channel-aware detail_fetcher.py dumped everything flat under one
github_details/. After github.py gained per-channel subdir support, legacy
files sit at the top of github_details/ instead of under their repo's ch_key.

This walks every SRC's _meta.json, finds the channel each flat .md file
belongs to (by parsing the `source:` URL header), and moves it.

Usage:
  python3 scrape/migrate_legacy_details.py                 # all SRCs
  python3 scrape/migrate_legacy_details.py SRC-006         # single
  python3 scrape/migrate_legacy_details.py --dry-run       # report only
  python3 scrape/migrate_legacy_details.py --cleanup       # delete flat
                                                        # duplicate when
                                                        # target exists
  python3 scrape/migrate_legacy_details.py --cleanup-index # delete flat
                                                        # _index.jsonl after
                                                        # migration is complete
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_RE = re.compile(r'^source:\s*https://github\.com/([^/]+)/([^/]+)/')
CHANNEL_URL_RE = re.compile(r'^https://github\.com/([^/]+)/([^/]+)')


def build_url_to_chkey(src_dir):
    """Return {owner_repo: ch_key} for all github_repo channels in _meta.json."""
    meta_path = os.path.join(src_dir, '_meta.json')
    if not os.path.exists(meta_path):
        return {}
    meta = json.load(open(meta_path))
    out = {}
    for ch_key, ch in (meta.get('channels') or {}).items():
        if ch.get('type') != 'github_repo':
            continue
        m = CHANNEL_URL_RE.match(ch.get('url', ''))
        if not m:
            continue
        out[f'{m.group(1)}/{m.group(2)}'] = ch_key
    return out


def detect_owner_repo(filepath):
    """Read first 5 lines, return owner/repo or None."""
    try:
        with open(filepath) as f:
            for _, line in zip(range(5), f):
                m = SOURCE_RE.match(line)
                if m:
                    return f'{m.group(1)}/{m.group(2)}'
    except (OSError, UnicodeDecodeError):
        pass
    return None


def migrate_src(src_dir, dry=False, cleanup=False):
    src_id = os.path.basename(src_dir.rstrip('/'))
    base = os.path.join(src_dir, 'github_details')
    if not os.path.isdir(base):
        return 0, 0, 0, []

    url_to_ch = build_url_to_chkey(src_dir)
    if not url_to_ch:
        return 0, 0, 0, []

    # flat .md files only (not in subdirs)
    flat_files = [
        f for f in os.listdir(base)
        if f.endswith('.md')
        and os.path.isfile(os.path.join(base, f))
    ]

    moved = skipped = warned = 0
    log = []
    for fn in flat_files:
        src_path = os.path.join(base, fn)
        owner_repo = detect_owner_repo(src_path)
        if not owner_repo:
            log.append(f'  WARN no source URL: {src_id}/{fn}')
            warned += 1
            continue
        ch_key = url_to_ch.get(owner_repo)
        if not ch_key:
            log.append(f'  WARN no channel match for {owner_repo}: {src_id}/{fn}')
            warned += 1
            continue
        dst_dir = os.path.join(base, ch_key)
        dst_path = os.path.join(dst_dir, fn)
        if os.path.exists(dst_path):
            if cleanup:
                log.append(f'  DELETE flat duplicate: {src_id}/{fn} (target exists at {ch_key}/)')
                if not dry:
                    os.remove(src_path)
                skipped += 1
            else:
                skipped += 1
            continue
        log.append(f'  MOVE {src_id}/{fn} → {ch_key}/{fn}')
        if not dry:
            os.makedirs(dst_dir, exist_ok=True)
            os.rename(src_path, dst_path)
            moved += 1
        else:
            moved += 1  # count as would-move for dry-run summary
    return moved, skipped, warned, log


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('srcs', nargs='*', help='SRC-IDs to process (default: all)')
    ap.add_argument('--dry-run', action='store_true',
                    help='print intended moves, do not rename')
    ap.add_argument('--cleanup', action='store_true',
                    help='delete flat file when target already exists')
    ap.add_argument('--cleanup-index', action='store_true',
                    help='backup+delete flat _index.jsonl after migration')
    args = ap.parse_args()

    src_root = os.path.join(ROOT, 'sources')
    if args.srcs:
        roots = [os.path.join(src_root, s) for s in args.srcs]
    else:
        roots = sorted(
            d for d in glob.glob(os.path.join(src_root, 'SRC-*'))
            if os.path.isdir(d)
        )

    total_moved = total_skipped = total_warned = 0
    total_index_removed = 0
    for src_dir in roots:
        if not os.path.isdir(src_dir):
            print(f'NOT FOUND: {src_dir}', file=sys.stderr)
            continue
        moved, skipped, warned, log = migrate_src(src_dir, dry=args.dry_run, cleanup=args.cleanup)
        if moved or skipped or warned:
            sid = os.path.basename(src_dir)
            tag = ' [DRY-RUN]' if args.dry_run else ''
            print(f'>>> {sid}{tag}')
            for line in log:
                print(line)
            print(f'  summary: moved={moved} skipped={skipped} warned={warned}\n')
            total_moved += moved
            total_skipped += skipped
            total_warned += warned

        # --cleanup-index: delete flat _index.jsonl
        # (only safe when no flat .md remains — migration is complete)
        if args.cleanup_index:
            base = os.path.join(src_dir, 'github_details')
            legacy_idx = os.path.join(base, '_index.jsonl')
            if os.path.exists(legacy_idx):
                flat_md_left = [
                    f for f in os.listdir(base)
                    if f.endswith('.md')
                    and os.path.isfile(os.path.join(base, f))
                ]
                if flat_md_left:
                    print(f'>>> {os.path.basename(src_dir)} [SKIP index cleanup] '
                          f'{len(flat_md_left)} flat .md remain — run migration first')
                else:
                    tag = ' [DRY-RUN]' if args.dry_run else ''
                    print(f'>>> {os.path.basename(src_dir)}{tag} '
                          f'REMOVE _index.jsonl')
                    if not args.dry_run:
                        os.remove(legacy_idx)
                    total_index_removed += 1

    verb = ('would move' if args.dry_run
             else 'moved' if not args.cleanup
             else 'moved+deleted')
    print(f'=== {verb}={total_moved}, skipped={total_skipped}, warned={total_warned}',
          file=sys.stderr)
    if args.cleanup_index:
        verb2 = 'would remove' if args.dry_run else 'removed'
        print(f'=== legacy _index.jsonl {verb2}={total_index_removed}',
              file=sys.stderr)


if __name__ == '__main__':
    main()