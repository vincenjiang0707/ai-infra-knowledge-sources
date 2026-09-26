#!/usr/bin/env python3
"""CLI shim for per-channel github detail (comments + PR reviews).

Standalone usage: python3 scrape/detail_fetcher.py [SRC-IDs...]
Without args: walks all github_repo channels across every SRC.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import common, github_detail

GITHUB_CHANNEL_TYPES = {'github_repo'}


def _owner_repo(url):
    m = re.match(r'https://github\.com/([^/]+)/([^/]+)', url or '')
    return (m.group(1), m.group(2)) if m else (None, None)


def main():
    only = set(a.upper() for a in sys.argv[1:])
    total = 0
    for fp in sorted(glob.glob(os.path.join(common.ROOT, 'sources', 'SRC-*', '_meta.json'))):
        sid = os.path.basename(os.path.dirname(fp))
        if only and sid not in only:
            continue
        meta = json.load(open(fp))
        for ch_key, ch in (meta.get('channels') or {}).items():
            if ch.get('type') not in GITHUB_CHANNEL_TYPES:
                continue
            owner, repo = _owner_repo(ch.get('url', ''))
            if not owner:
                continue
            owner_repo = f'{owner}/{repo}'
            d = common.src_dir(sid)
            base = os.path.join(d, 'github_details')
            ddir = os.path.join(base, ch_key)
            for kind_file, kind in (('github_issues.jsonl', 'issue'),
                                    ('github_pulls.jsonl', 'pr')):
                jf = os.path.join(d, kind_file)
                if not os.path.exists(jf):
                    continue
                rows = [json.loads(l) for l in open(jf)]
                repo_rows = [r for r in rows
                             if (r.get('url') or '').startswith(f'https://github.com/{owner_repo}')]
                if not repo_rows:
                    continue
                github_detail.migrate_legacy_flat(base, ch_key, owner_repo, kind, repo_rows)
                stats = github_detail.process_repo(
                    owner_repo, ch_key, repo_rows, kind, ddir)
                if any(stats.values()):
                    print(f'{sid} {ch_key} {kind}: {stats}', flush=True)
                    total += sum(stats.values())
    print(f'total: {total}')


if __name__ == '__main__':
    main()