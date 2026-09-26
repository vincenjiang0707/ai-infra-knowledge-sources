#!/usr/bin/env python3
"""Backfill channel.post_urls from existing posts/*.md files.

Each post file has a `source: URL` line in body — extract and build
{url: filename} map, save into _meta.json channel.

Run once after old-style posts/ exist without post_urls tracking.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import common

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_RE = re.compile(r'source:\s*(\S+)', re.IGNORECASE)


def backfill(sid):
    meta_path = os.path.join(ROOT, 'sources', sid, '_meta.json')
    if not os.path.exists(meta_path):
        return False
    m = json.load(open(meta_path))
    changed = False
    for ck, cv in m.get('channels', {}).items():
        if cv.get('type') != 'blog':
            continue
        post_urls = cv.get('post_urls') or {}
        if len(post_urls) >= len(os.listdir(os.path.join(ROOT, 'sources', sid, 'posts'))):
            continue  # already backfilled
        posts_dir = os.path.join(ROOT, 'sources', sid, 'posts')
        if not os.path.isdir(posts_dir):
            continue
        for fn in sorted(os.listdir(posts_dir)):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(posts_dir, fn)
            try:
                with open(fp) as f:
                    head = f.read(2000)
            except Exception:
                continue
            m_src = SRC_RE.search(head)
            if not m_src:
                continue
            url = m_src.group(1).strip()
            if url not in post_urls:
                post_urls[url] = fn
                changed = True
        cv['post_urls'] = post_urls
        print(f'[{sid}] {ck}: backfilled {len(post_urls)} urls')
    if changed:
        common.save_meta(sid, m)
    return changed


def main():
    ap_targets = sys.argv[1:]
    if ap_targets:
        targets = ap_targets
    else:
        targets = sorted(d for d in os.listdir(os.path.join(ROOT, 'sources'))
                         if d.startswith('SRC-'))
    n = 0
    for sid in targets:
        if backfill(sid):
            n += 1
    print(f'\nbackfilled {n} SRCs')


if __name__ == '__main__':
    main()