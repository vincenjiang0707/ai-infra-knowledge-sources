#!/usr/bin/env python3
"""Batch-flip SRC channels to 'blog' and re-scrape up to 100 posts each.

For each (src_id, ch_key) where channel has a blog-like URL pattern or
already had posts/ from RSS, flip type to 'blog' and invoke blog.run.
Skips SRCs already at 100+ RSS posts to avoid regression.
"""
import json
import os
import sys

sys.path.insert(0, '/mnt/d/vincenjiang/AI学习/chaoyuan/scrape')
from scrapers import blog, common

ROOT = '/mnt/d/vincenjiang/AI学习/chaoyuan/knowledge-sources'
MAX_RSS_SKIP = 100  # skip if existing posts >= this (don't regress)

CANDIDATES = [
    'SRC-064',  # HF 论坛 discuss.huggingface.co
    'SRC-125',  # NVIDIA developer blog
    'SRC-132',  # AWS ML blog
    'SRC-139',  # Simon Boehm
    'SRC-141',  # Colfax Research
    'SRC-142',  # Salykova
    'SRC-154',  # Hacker News
    'SRC-165',  # vLLM Blog
]


def process(sid):
    p = f'{ROOT}/sources/{sid}/_meta.json'
    meta = json.load(open(p))
    # skip if existing posts >= cap
    posts_dir = f'{ROOT}/sources/{sid}/posts'
    if os.path.isdir(posts_dir):
        n = len(os.listdir(posts_dir))
        if n >= MAX_RSS_SKIP:
            print(f'== {sid} SKIP (already {n} posts) ==', flush=True)
            return
    # flip first site/reference channel to blog
    src = {'src_id': sid, 'name': meta.get('name', '')}
    out = {}
    flipped = False
    for k, c in list(meta.get('channels', {}).items()):
        if c.get('type') in ('site', 'reference', 'academic') and \
           c.get('status') == 'ok':
            c['type'] = 'blog'
            flipped = True
            try:
                blog.run(src, k, c, out, {})
            except Exception as e:
                out[k] = {'type': 'blog', 'url': c.get('url', ''),
                          'status': 'error', 'error': repr(e)[:200]}
            break  # only first matching channel
    if not flipped:
        print(f'== {sid} SKIP (no flippable channel) ==', flush=True)
        return
    v = out.get(list(out.keys())[0]) if out else {}
    print(f'== {sid} posts={len(v.get("posts", []))} '
          f'chars={v.get("total_chars", 0)} ==', flush=True)
    # merge
    meta['channels'].update(out)
    meta['attempts'] = meta.get('attempts', 0) + 1
    meta['status'] = 'success' if v.get('status') == 'ok' else 'error'
    common.save_meta(sid, meta)


def main():
    only = set(a.upper() for a in sys.argv[1:])
    for sid in CANDIDATES:
        if only and sid not in only:
            continue
        try:
            process(sid)
        except Exception as e:
            print(f'== {sid} EXCEPTION {e} ==', flush=True)


if __name__ == '__main__':
    main()