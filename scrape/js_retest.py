#!/usr/bin/env python3
"""Retest SPA-shell candidates via js.py without going through scrape.py.

Bypasses the success-skip logic. For each (src_id, ch_key):
  - flip channel type to 'js'
  - call js.run()
  - merge result into _meta.json channels
"""
import json
import sys
import time

sys.path.insert(0, '/home/jj/.claude/skills/chaoyuan/scrape') if False else \
    sys.path.insert(0, '/mnt/d/vincenjiang/AI学习/chaoyuan/scrape')
from scrapers import common
from scrapers import js as js_mod

ROOT = '/mnt/d/vincenjiang/AI学习/chaoyuan/knowledge-sources'

# Candidate list: (src_id, ch_key). Only site/acad channels with page.md < 5KB
# and no pages/ dir. Filtered out login-walled & known-noresult.
CANDIDATES = [
    'SRC-030',  # 昇腾文档中心 (Nuxt SPA, same as SRC-031)
    'SRC-123',  # LMSYS blog
    'SRC-126',  # Baseten blog
    'SRC-127',  # Baseten inference-engineering
    'SRC-129',  # Fireworks blog
    'SRC-131',  # Anyscale blog
    'SRC-138',  # Horace He
    'SRC-004',  # SGLang docs
    'SRC-007',  # vLLM Ascend
    'SRC-016',  # CUDA docs
    'SRC-019',  # ROCm docs
    'SRC-026',  # Google TPU
    'SRC-049',  # Qwen readthedocs
    'SRC-074',  # PyTorch docs
    'SRC-101',  # Nsight Systems
    'SRC-122',  # NVIDIA On-demand
    'SRC-133',  # Google Cloud blog
    'SRC-137',  # 火山引擎
    'SRC-166',  # Ascend gitcode
    'SRC-169',  # NVIDIA NGC
    'SRC-170',  # ROCm Docker
]


def retest(sid):
    p = f'{ROOT}/sources/{sid}/_meta.json'
    meta = json.load(open(p))
    src = {'src_id': sid, 'name': meta.get('name', '')}
    out = {}
    for k, c in list(meta.get('channels', {}).items()):
        if c.get('type') not in ('site', 'academic'):
            continue
        if c.get('status') != 'ok':
            continue
        url = c.get('url', '')
        ch = {**c, 'type': 'js'}
        t0 = time.time()
        try:
            js_mod.run(src, k, ch, out, {})
        except Exception as e:
            out[k] = {'type': 'js', 'url': url, 'status': 'error',
                      'error': repr(e)[:200], 'mode': 'js'}
        dt = time.time() - t0
        print(f'  {sid}.{k}: {out[k].get("status")} '
              f'{out[k].get("chars", "?")}c {dt:.1f}s '
              f'{out[k].get("reason") or out[k].get("error") or ""}',
              flush=True)
    # merge: only update channels we retested
    new_meta = {**meta, 'channels': {**meta.get('channels', {}), **out}}
    # bump attempts
    new_meta['attempts'] = meta.get('attempts', 0) + 1
    # overall status: only js channels now; if any error stays partial
    statuses = [v.get('status') for v in new_meta['channels'].values()]
    if all(s == 'ok' for s in statuses):
        new_meta['status'] = 'success'
    elif any(s == 'ok' for s in statuses):
        new_meta['status'] = 'partial'
    else:
        new_meta['status'] = 'error'
    common.save_meta(sid, new_meta)


def main():
    args = [a.upper() for a in sys.argv[1:]]
    want = set(args) if args else set(CANDIDATES)
    for sid in CANDIDATES:
        if sid not in want:
            continue
        print(f'== {sid} ==', flush=True)
        retest(sid)


if __name__ == '__main__':
    main()