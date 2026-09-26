#!/usr/bin/env python3
"""Generate _summary/*.md from _registry.json + per-SRC _meta.json."""
import glob
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import common

SUM = os.path.join(common.ROOT, '_summary')


def main():
    os.makedirs(SUM, exist_ok=True)
    registry = {s['src_id']: s for s in
                json.load(open(os.path.join(common.ROOT, '_registry.json')))}
    metas = {}
    for p in glob.glob(os.path.join(common.ROOT, 'sources', 'SRC-*', '_meta.json')):
        m = json.load(open(p))
        metas[m['src_id']] = m

    rows = []
    for sid in sorted(registry):
        reg, m = registry[sid], metas.get(sid)
        if reg.get('blocked_reason') and not m:
            status, reason = 'blocked', reg['blocked_reason']
        elif not m:
            status, reason = 'not_fetched', '未跑'
        else:
            status, reason = m['status'], (m.get('blocked_reason') or '')
        rows.append({'src_id': sid, 'name': reg['name'], 'category': reg['category'],
                     'status': status, 'reason': reason, 'meta': m})

    n = Counter(r['status'] for r in rows)
    total_files = sum(len(glob.glob(os.path.join(common.ROOT, 'sources', r['src_id'], '**'), recursive=True))
                      for r in rows)
    total_bytes = sum(
        os.path.getsize(f) for f in glob.glob(os.path.join(common.ROOT, 'sources', 'SRC-*', '**'), recursive=True)
        if os.path.isfile(f))

    # index.md
    with open(os.path.join(SUM, 'index.md'), 'w') as f:
        f.write('# 知识来源抓取总表\n\n')
        f.write(f'- 日期: {common.now()}\n- 来源总数: {len(rows)}\n')
        f.write(f'- 状态: {json.dumps(dict(n), ensure_ascii=False)}\n')
        f.write(f'- 产物: {total_files} 项 / {total_bytes / 1e6:.1f} MB\n\n')
        f.write('| SRC | 名称 | 类别 | 状态 | 说明 |\n|---|---|---|---|---|\n')
        for r in rows:
            note = r['reason'] or ''
            if r['meta']:
                chs = r['meta'].get('channels', {})
                bits = []
                for k, c in chs.items():
                    st = c.get('status', '?')
                    extra = c.get('posts_fetched', c.get('pages_fetched', c.get('models', '')))
                    bits.append(f"{c.get('type','?')}:{st}" + (f"({extra})" if extra != '' else ''))
                note = '; '.join(bits) or note
            f.write(f"| {r['src_id']} | {r['name'][:24]} | {r['category'][:16]} | "
                    f"{r['status']} | {note[:120]} |\n")

    def dump(fname, title, want, group_by_reason=False):
        with open(os.path.join(SUM, fname), 'w') as f:
            f.write(f'# {title}\n\n共 {sum(1 for r in rows if r["status"] in want)} 项\n\n')
            if group_by_reason:
                by = defaultdict(list)
                for r in rows:
                    if r['status'] in want:
                        by[r['reason'] or '未分类'].append(r)
                for reason, rs in sorted(by.items()):
                    f.write(f'\n## {reason} ({len(rs)})\n\n')
                    for r in rs:
                        f.write(f"- {r['src_id']} {r['name']}\n")
            else:
                for r in rows:
                    if r['status'] in want:
                        f.write(f"- {r['src_id']} {r['name']} — {r['category']}\n")

    dump('fetched.md', '抓取成功', ('success',))
    dump('partial.md', '部分成功', ('partial',))
    dump('not_fetched.md', '未抓取（按原因）', ('not_fetched', 'error'), group_by_reason=True)
    dump('blocked.md', '待人工（blocked）', ('blocked',), group_by_reason=True)
    print(f'summary written: {dict(n)}')


if __name__ == '__main__':
    main()
