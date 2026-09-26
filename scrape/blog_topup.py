#!/usr/bin/env python3
"""Top up blog-channel SRCs to first 100 posts (incremental, no file delete).

Per SRC:
  - if channel_type=site but URL is blog-like: flip to blog in registry + _meta
  - run scrapers.blog.run with MAX_POSTS=100, WAIT configurable
  - existing files in posts/ preserved; new files start numbering at len(existing)+1

Usage:
  python3 blog_topup.py                    # all 18 blog-flavor SRCs
  python3 blog_topup.py SRC-132 SRC-140    # specific (with WAIT=domcontentloaded)
  python3 blog_topup.py --flip-only SRC-021 SRC-124 SRC-128 SRC-130
"""
import argparse
import json
import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import blog, common

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# URL contains /blog keyword or blog-pattern endpoints
BLOG_URL_PATTERNS = ['/blog/', '/blog', '/blogs/', 'discuss.huggingface.co',
                     'lmsys.org/blog', 'fireworks.ai/blog', 'anyscale.com/blog',
                     'aws.amazon.com/blogs', 'cloud.google.com/blog',
                     'siboehm.com', 'colfax-intl.com', 'salykova.github.io',
                     'news.ycombinator.com', 'leimao.github.io/blog',
                     'rocm.blogs.amd.com', 'pytorch.org/blog',
                     'baseten.co/blog', 'vllm.ai/blog', 'developer.nvidia.com/blog',
                     'together.ai/blog', 'modal.com/blog']

# SRCs that need wait_until=domcontentloaded (timeout-prone)
WAIT_DOMCONTENT = {'SRC-125', 'SRC-132', 'SRC-140'}


def is_blog_url(url):
    return any(p in url for p in BLOG_URL_PATTERNS)


def flip_to_blog(sid):
    """Flip channel type in _meta.json and _registry.json from site to blog."""
    meta_path = os.path.join(ROOT, 'sources', sid, '_meta.json')
    if not os.path.exists(meta_path):
        return False
    m = json.load(open(meta_path))
    flipped = False
    for ck, cv in m.get('channels', {}).items():
        if cv.get('type') == 'site' and is_blog_url(cv.get('url', '')):
            cv['type'] = 'blog'
            cv['mode'] = 'blog'
            flipped = True
    if flipped:
        common.save_meta(sid, m)
    # registry
    reg_path = os.path.join(ROOT, '_registry.json')
    reg = json.load(open(reg_path))
    for r in reg:
        if r['src_id'] == sid:
            cts = set(r.get('channel_types', []))
            if 'blog' not in cts:
                cts.add('blog')
                cts.discard('site')
                r['channel_types'] = sorted(cts)
            break
    with open(reg_path, 'w') as f:
        json.dump(reg, f, ensure_ascii=False, indent=1)
    return flipped


def run_one(sid, force_wait=None):
    """Run blog.run for one SRC."""
    meta = common.load_meta(sid)
    if not meta:
        print(f'[{sid}] NO META — skip')
        return False
    src_entry = {'src_id': sid, 'name': meta.get('name', sid)}
    channel = None
    for ck, cv in meta.get('channels', {}).items():
        if cv.get('type') == 'blog':
            channel = cv
            break
    if not channel:
        print(f'[{sid}] NO BLOG CHANNEL — skip')
        return False
    wait = force_wait or ('domcontentloaded' if sid in WAIT_DOMCONTENT else None)
    old_max = os.environ.get('SCRAPE_BLOG_MAX')
    old_wait = os.environ.get('SCRAPE_BLOG_WAIT')
    os.environ['SCRAPE_BLOG_MAX'] = '100'
    if wait:
        os.environ['SCRAPE_BLOG_WAIT'] = wait
    try:
        print(f'[{sid}] starting blog.run (wait={wait or "networkidle"})')
        blog.run(src_entry, 'channel', channel, meta.get('channels', {}), {})  # last args unused
    except Exception as e:
        print(f'[{sid}] ERROR: {e}')
        traceback.print_exc()
        return False
    finally:
        if old_max is None:
            os.environ.pop('SCRAPE_BLOG_MAX', None)
        else:
            os.environ['SCRAPE_BLOG_MAX'] = old_max
        if old_wait is None:
            os.environ.pop('SCRAPE_BLOG_WAIT', None)
        else:
            os.environ['SCRAPE_BLOG_WAIT'] = old_wait
    # sync posts list + total_chars into channel (recursive: posts/<tab>/*.md)
    posts_dir = os.path.join(ROOT, 'sources', sid, 'posts')
    files = sorted(
        os.path.relpath(os.path.join(root, fn), posts_dir)
        for root, _dirs, fns in os.walk(posts_dir) if os.path.isdir(posts_dir)
        for fn in fns if fn.endswith('.md')) if os.path.isdir(posts_dir) else []
    channel['posts'] = files
    channel['total_chars'] = sum(os.path.getsize(os.path.join(posts_dir, f)) for f in files)
    # status: ok if any new posts OR already >= 100; partial if some fetched < MAX
    channel['status'] = 'ok' if len(files) >= 100 else 'partial'
    common.save_meta(sid, meta)
    print(f'[{sid}] done — {len(files)} files, {channel["total_chars"]} chars, status={channel["status"]}')
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('src_ids', nargs='*')
    ap.add_argument('--flip-only', action='store_true', help='only flip site→blog, no scrape')
    args = ap.parse_args()

    if args.src_ids:
        targets = args.src_ids
    else:
        targets = ['SRC-021', 'SRC-064', 'SRC-123', 'SRC-124', 'SRC-125',
                   'SRC-126', 'SRC-128', 'SRC-129', 'SRC-130', 'SRC-131',
                   'SRC-132', 'SRC-133', 'SRC-139', 'SRC-140', 'SRC-141',
                   'SRC-142', 'SRC-154', 'SRC-165']

    # skip SRCs already at >=100 posts on disk (no need to top up)
    skip = set()
    for sid in targets:
        pdir = os.path.join(ROOT, 'sources', sid, 'posts')
        if os.path.isdir(pdir):
            n = sum(len([f for f in fns if f.endswith('.md')])
                    for _r, _d, fns in os.walk(pdir))
            if n >= 100:
                skip.add(sid)
    targets = [t for t in targets if t not in skip]

    print(f'Top-up batch: {len(targets)} SRCs (skipped already-OK: {sorted(skip & set(targets))})\n')

    for sid in targets:
        flipped = flip_to_blog(sid)
        if flipped:
            print(f'[{sid}] flipped site→blog')
        if args.flip_only:
            continue
        run_one(sid)
        print()


if __name__ == '__main__':
    main()