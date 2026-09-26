#!/usr/bin/env python3
"""Backfill body field into existing github_{issues,pulls}.jsonl.

Re-calls list API with same params, rewrites files. Run AFTER batch finishes
(running batch writes old-format rows). ~2-3 gh calls per repo.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import common

LISTS = {
    'github_issues.jsonl': ('issues',
                            'per_page=100&state=all&sort=updated&direction=desc'),
    'github_pulls.jsonl': ('pulls',
                           'per_page=100&state=all&sort=updated&direction=desc'),
}
CAP = 100


def row_for(it, kind):
    if kind == 'issues' and 'pull_request' in it:
        return None
    base = {'number': it.get('number'), 'title': it.get('title'),
            'state': it.get('state'), 'created_at': it.get('created_at'),
            'updated_at': it.get('updated_at'), 'closed_at': it.get('closed_at'),
            'labels': [l['name'] for l in it.get('labels', [])],
            'comments_count': it.get('comments'),
            'body': it.get('body') or '',
            'url': it.get('html_url')}
    if kind == 'pulls':
        base['is_pr'] = True
        base['merged_at'] = it.get('merged_at')
    else:
        base['is_pr'] = False
    return base


def main():
    root = common.ROOT
    only = [a.upper() for a in sys.argv[1:]]
    for sid in sorted(os.listdir(root)):
        if not sid.startswith('SRC-') or (only and sid not in only):
            continue
        d = os.path.join(root, sid)
        meta_p = os.path.join(d, '_meta.json')
        if not os.path.exists(meta_p):
            continue
        meta = json.load(open(meta_p))
        for ch in (meta.get('channels') or {}).values():
            if ch.get('type') != 'github_repo':
                continue
            m = re.match(r'https://github\.com/([^/]+)/([^/]+)', ch['url'])
            if not m:
                continue
            owner_repo = f'{m.group(1)}/{m.group(2)}'
            for fname, (kind, params) in LISTS.items():
                fp = os.path.join(d, fname)
                if not os.path.exists(fp):
                    continue
                rows, page = [], 1
                while True:
                    data, st = common.gh_api(
                        f'repos/{owner_repo}/{kind}?{params}&page={page}')
                    if st != 'ok' or not data:
                        break
                    rows += [r for it in data if (r := row_for(it, kind))]
                    if len(rows) >= CAP or len(data) < 100:
                        break
                    page += 1
                if rows:
                    with open(fp, 'w') as f:
                        for r in rows[:CAP]:
                            f.write(json.dumps(r, ensure_ascii=False) + '\n')
                    print(f'{sid} {kind}: {len(rows)} rows (body backfilled)', flush=True)
                else:
                    print(f'{sid} {kind}: API fail, kept old file', flush=True)


if __name__ == '__main__':
    main()
