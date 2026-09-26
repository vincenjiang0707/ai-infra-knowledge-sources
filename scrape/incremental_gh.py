#!/usr/bin/env python3
"""Incremental GH append: pull items newer than cursor, merge into jsonl.

For each SRC with github jsonl + cursor:
  fetch list page1 (sort=updated desc), walk pages until all numbers seen
  or updated_at <= cursor; rewrite file with refreshed+new rows.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import common
from scrapers.github import _row

PARAMS = 'per_page=100&state=all&sort=updated&direction=desc'


def merge_file(jf, api_base, kind):
    rows = {json.loads(l)['number']: json.loads(l) for l in open(jf)}
    cursor_key = f'{kind}_last_updated_at'
    new_ct = upd_ct = 0
    page = 1
    while page <= 5:  # 500 items per run cap
        data, st = common.gh_api(f'{api_base}?{PARAMS}&page={page}')
        if st != 'ok' or not data:
            break
        stop = False
        for it in data:
            row = _row(it, 'release' if kind == 'releases' else
                       ('issue' if kind == 'issues' else 'pr'))
            if row is None:
                continue
            n = row['number']
            if n in rows:
                if rows[n] != row:
                    rows[n] = row  # refreshed
                    upd_ct += 1
                stop = True  # reached known territory on this page
            else:
                rows[n] = row
                new_ct += 1
        if stop or len(data) < 100:
            break
        page += 1
    with open(jf, 'w') as f:
        for r in rows.values():
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return new_ct, upd_ct


def main():
    only = [a.upper() for a in sys.argv[1:]]
    for fp in sorted(glob.glob(os.path.join(common.ROOT, 'sources', 'SRC-*', '_meta.json'))):
        sid = os.path.basename(os.path.dirname(fp))
        if only and sid not in only:
            continue
        meta = json.load(open(fp))
        repos = []
        for ch in (meta.get('channels') or {}).values():
            m = re.match(r'https://github\.com/([^/]+)/([^/]+)', ch.get('url', ''))
            if m:
                repos.append(f'{m.group(1)}/{m.group(2)}')
        if not repos:
            continue
        # multi-repo SRC: jsonl shared — skip (rare; only single-repo SRCs here
        # have per-file mapping; multi-repo SRCs get full list refresh instead)
        if len(repos) > 1:
            for jf_kind in ('issues', 'pulls'):
                jf = os.path.join(common.ROOT, 'sources', sid, f'github_{jf_kind}.jsonl')
                if os.path.exists(jf):
                    # union list: refresh from each repo and merge
                    merged = {}
                    for rp in repos:
                        page = 1
                        while page <= 3:
                            data, st = common.gh_api(
                                f'repos/{rp}/{jf_kind}?{PARAMS}&page={page}')
                            if st != 'ok' or not data:
                                break
                            for it in data:
                                row = _row(it, 'issue' if jf_kind == 'issues' else 'pr')
                                if row:
                                    merged.setdefault(row['number'], row)
                            if len(data) < 100:
                                break
                            page += 1
                    if merged:
                        with open(jf, 'w') as f:
                            for r in merged.values():
                                f.write(json.dumps(r, ensure_ascii=False) + '\n')
                        print(f'{sid} {jf_kind}: refreshed {len(merged)} (multi-repo)')
            continue
        rp = repos[0]
        for jf_kind in ('issues', 'pulls'):
            jf = os.path.join(common.ROOT, 'sources', sid, f'github_{jf_kind}.jsonl')
            if os.path.exists(jf):
                new_ct, upd_ct = merge_file(jf, f'repos/{rp}/{jf_kind}', jf_kind)
                print(f'{sid} {jf_kind}: +{new_ct} new, {upd_ct} refreshed', flush=True)
        # bump cursor
        cur = meta.get('cursor') or {}
        for jf_kind in ('issues', 'pulls'):
            jf = os.path.join(common.ROOT, 'sources', sid, f'github_{jf_kind}.jsonl')
            if os.path.exists(jf):
                rows = [json.loads(l) for l in open(jf)]
                if rows:
                    mx = max(r['updated_at'] for r in rows if r.get('updated_at'))
                    for k in cur:
                        if k.endswith(f'{jf_kind}') or k.endswith(f':{jf_kind[:-1]}') \
                           or k.endswith(f':{jf_kind}'):
                            cur[k]['last_updated_at'] = mx
        meta['cursor'] = cur
        common.save_meta(sid, meta)


if __name__ == '__main__':
    main()
