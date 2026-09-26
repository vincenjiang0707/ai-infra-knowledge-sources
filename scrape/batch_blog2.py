#!/usr/bin/env python3
"""Batch blog channel scrape: flip any channel whose URL is a blog index
and scrape up to 100 posts.

Used after blog.py POST_HINTS extension (Discourse /t/, Jekyll YYYY/MM/,
HN /item?id=, etc.).
"""
import json
import os
import sys

sys.path.insert(0, '/mnt/d/vincenjiang/AI学习/chaoyuan/scrape')
from scrapers import blog, common

ROOT = '/mnt/d/vincenjiang/AI学习/chaoyuan/knowledge-sources'
MAX_RSS_SKIP = 100

# Targeted SRCs (already verified to be blog indexes from registry)
CANDIDATES = [
    'SRC-063',  # HF blog (huggingface.co/blog) — likely captcha
    'SRC-125',  # NVIDIA dev blog
    'SRC-126',  # Baseten blog
    'SRC-129',  # Fireworks blog
    'SRC-131',  # Anyscale blog
    'SRC-132',  # AWS ML blog (retry)
    'SRC-133',  # Google Cloud blog
    'SRC-140',  # Lei Mao blog (was RSS, retry as blog)
]


def process(sid):
    p = f'{ROOT}/sources/{sid}/_meta.json'
    meta = json.load(open(p))
    posts_dir = f'{ROOT}/sources/{sid}/posts'
    if os.path.isdir(posts_dir):
        n = len(os.listdir(posts_dir))
        if n >= MAX_RSS_SKIP:
            print(f'== {sid} SKIP (already {n} posts) ==', flush=True)
            return
    src = {'src_id': sid, 'name': meta.get('name', '')}
    out = {}
    for k, c in list(meta.get('channels', {}).items()):
        if c.get('type') in ('site', 'reference', 'academic', 'hf', 'js') \
                and c.get('status') != 'error':
            c['type'] = 'blog'
            try:
                blog.run(src, k, c, out, {})
            except Exception as e:
                out[k] = {'type': 'blog', 'url': c.get('url', ''),
                          'status': 'error', 'error': repr(e)[:200]}
            break
    if not out:
        print(f'== {sid} SKIP (no flippable channel) ==', flush=True)
        return
    v = out.get(list(out.keys())[0])
    print(f'== {sid} posts={len(v.get("posts", []))} '
          f'chars={v.get("total_chars", 0)} status={v.get("status")} ==',
          flush=True)
    meta['channels'].update(out)
    meta['attempts'] = meta.get('attempts', 0) + 1
    meta['status'] = 'success' if v.get('status') == 'ok' and v.get('posts') \
        else ('partial' if v.get('status') == 'ok' else 'error')
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