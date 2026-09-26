"""JS-rendered blog index + per-post fetcher.

Use when site.py captures only the index page (e.g. SPA blog like
lmsys.org/blog). Opens index via playwright, extracts post hrefs, then
visits each post in same browser session and writes posts/NN_slug.md.

Reuses js.py's CHROME_PATH override.
"""
import os
import random
import re
import time
from urllib.parse import parse_qs, urljoin, urlparse

from . import common
from . import cookies as cookies_mod
from . import js as js_mod

MAX_POSTS = int(os.environ.get('SCRAPE_BLOG_MAX', '100'))  # safety cap per run
WAIT = os.environ.get('SCRAPE_BLOG_WAIT', 'networkidle')  # networkidle | domcontentloaded
TIMEOUT_MS = int(os.environ.get('SCRAPE_BLOG_TIMEOUT_MS', '30000'))

# Cloudflare bypass: inject cf_clearance cookie from real Chrome.
# Map src_id -> (cookie_domain, clearance_value, [optional companion cookies])
CF_COOKIE_ENV = 'SCRAPE_CF_CLEARANCE'  # JSON with {src_id: {domain, value}}
CF_DOMAINS = {  # auto-apply by URL host
    'rocm.blogs.amd.com': '.amd.com',
    'developer.nvidia.com': '.nvidia.com',
}


def _load_cf_for(url, src_id=None):
    """Resolve CF cookie config for a URL/src_id. Returns None if not configured."""
    import json as _json
    raw = os.environ.get(CF_COOKIE_ENV)
    if not raw:
        return None
    cfg = _json.loads(raw)
    if src_id and src_id in cfg:
        return cfg[src_id]
    host = urlparse(url).netloc
    for sub, dom in CF_DOMAINS.items():
        if host.endswith(sub):
            return cfg.get(sub)
    return None

# href patterns that look like blog post permalinks.
# Broad tokens like '/security/' '/compute/' '/hpc/' match AWS nav-hub
# landing pages (e.g. aws.amazon.com/security/) which are NOT posts —
# excluded to avoid false positives. Real AWS blog posts live under
# '/blogs/<category>/<slug>' which is covered below.
POST_HINTS = (
    '/blog/', '/post/', '/article/', '/news/',
    '/20', '/202',  # year prefix (e.g. /2024/03/, /2025/)
    '/README.html',  # ablog / sphinx (e.g. rocm.blogs.amd.com)
    '/archives/', '/archive/',
    '/item?',  # Hacker News (item?id=NN)
    '/t/',  # Discourse topic permalinks (discuss.huggingface.co, lmsys)
    '/topic/', '/topics/',
    '/blogs/machine-learning/', '/blogs/ai/', '/blogs/database/',  # AWS blog
    '/ai/', '/ml/', '/hpc/',  # generic category paths (kept narrow on purpose)
)

# Host-aware hostnav exclusions: pure hub pages that look post-like but aren't.
_HUB_PATH_EXCLUDE = (
    ('aws.amazon.com', '/security/'),
    ('aws.amazon.com', '/compute/'),
    ('aws.amazon.com', '/containers/'),
    ('aws.amazon.com', '/gpu/'),
)


def _looks_like_post(path):
    """Heuristic: path has year/month or post-like prefix."""
    # Jekyll/Hugo: /YYYY/MM/slug or /YYYY/slug
    import re as _re
    if _re.search(r'/(20\d{2})/(0[1-9]|1[0-2])/', path):
        return True
    if _re.search(r'/(20\d{2})/(0[1-9]|1[0-2])-', path):
        return True
    return False


def _extract_post_links(html, base_url):
    """Pull candidate post URLs from rendered HTML."""
    seen = set()
    out = []
    base_netloc = urlparse(base_url).netloc
    for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\']', html, re.I):
        href = m.group(1)
        if href.startswith(('#', 'mailto:', 'javascript:')):
            continue
        full = urljoin(base_url, href)
        if urlparse(full).netloc != base_netloc:
            continue
        path = urlparse(full).path
        if not any(h in full for h in POST_HINTS) and not _looks_like_post(path):
            continue
        # skip pure index, anchors-only
        if full.rstrip('/') == base_url.rstrip('/'):
            continue
        # skip non-content files (feeds, sitemaps, hn item)
        if any(full.lower().endswith(s) for s in
               ('.xml', '.json', '.rss', '.atom')):
            continue
        if '/atom.xml' in full.lower() or '/sitemap.xml' in full.lower():
            continue
        # skip taxonomy/list pages: category, tag, author, archives indexes
        if any(seg in path.lower() for seg in ('/category/', '/tag/', '/tags/',
                                                '/author/', '/authors/',
                                                '/topics/', '/topic/',
                                                '/archives/', '/archive/')):
            continue
        # skip pagination (?page=N, /page/N)
        if '?page=' in full.lower() or '/page/' in path.lower():
            continue
        # skip Next.js internal pagination routes
        last_seg = path.strip('/').split('/')[-1] if path.strip('/') else ''
        if last_seg in ('page', 'page/2', 'page/3'):
            continue
        # skip HN front-page links (just /)
        if full.rstrip('/') == f'https://news.ycombinator.com' or \
           full.rstrip('/') == 'https://news.ycombinator.com/':
            continue
        # host-aware: drop known hub/landing pages that pass POST_HINTS
        host = urlparse(full).netloc
        parsed_full = urlparse(full)
        for hub_host, hub_path in _HUB_PATH_EXCLUDE:
            if host.endswith(hub_host) and path.startswith(hub_path):
                break
        else:
            # normalize trailing slash so the dedup set catches near-duplicate
            # `<a href="/foo/">` vs `<a href="/foo">` from same article
            norm = full if (parsed_full.query or parsed_full.fragment) else full.rstrip('/')
            if norm in seen:
                continue
            seen.add(norm)
            out.append(full)
    return out


def _jit(base):
    """Randomized delay ±50% — fixed intervals are a bot fingerprint."""
    return base * random.uniform(0.5, 1.5)


def _tab_name(idx_url):
    """Subdirectory name for a tab index URL: ai.html -> ai, index.html -> home."""
    base = os.path.basename(urlparse(idx_url).path)
    name = base.rsplit('.', 1)[0] if '.' in base else base
    name = re.sub(r'[^A-Za-z0-9_-]+', '-', name).strip('-')
    if name in ('', 'index'):
        name = 'home'
    return name


def _slug(url):
    """Stable slug: must be unique-per-URL so cross-run rewrites don't
    collide. HN-style query-param permalinks (item?id=NN) need the id."""
    parsed = urlparse(url)
    # HN: /item?id=NN — use id, otherwise every item collapses to 'item'
    if parsed.netloc == 'news.ycombinator.com':
        q = parse_qs(parsed.query)
        if 'id' in q:
            return f"item-{q['id'][0]}"
    path = parsed.path.strip('/')
    if not path:
        return 'index'
    parts = [p for p in path.split('/') if p]
    if not parts:
        return 'index'
    # if last is index.html/README.html, take parent dir as slug
    last = parts[-1].lower()
    if last in ('index.html', 'readme.html', 'index.htm', 'readme.htm', ''):
        return parts[-2] if len(parts) >= 2 else 'index'
    # strip .html / .htm suffix
    for suf in ('.html', '.htm', '/'):
        if last.endswith(suf):
            parts[-1] = parts[-1][:-(len(suf))]
            break
    return parts[-1] if parts[-1] else 'index'


def run(src, ch_key, ch, meta_channels, cursor):
    index_urls = ch.get('index_urls') or [ch['url']]
    index_url = ch['url']  # primary url, kept for backward compat
    d = common.src_dir(src['src_id'])
    posts_dir = os.path.join(d, 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    out = {'type': 'blog', 'url': index_url, 'index_urls': index_urls}
    from playwright.sync_api import sync_playwright
    # CDP attach (real Chrome daemon) if SCRAPE_USE_DAEMON=1 OR if CF env present
    use_daemon = os.environ.get('SCRAPE_USE_DAEMON', '') == '1'
    cf_cfg = _load_cf_for(index_url, src.get('src_id'))
    launch_kwargs = {'headless': True, 'args': ['--no-sandbox']}
    if os.path.exists(js_mod.CHROME_PATH):
        launch_kwargs['executable_path'] = js_mod.CHROME_PATH
    # load URL->file map from channel + scan posts/*.md for source: lines (cross-run dedup)
    url_to_fn = {}
    for url, fn in (ch.get('post_urls') or {}).items():
        url_to_fn[url] = fn
    if os.path.isdir(posts_dir):
        for root, _dirs, fns in os.walk(posts_dir):
            for fn in fns:
                if not fn.endswith('.md'):
                    continue
                fpath = os.path.join(root, fn)
                try:
                    with open(fpath, encoding='utf-8') as f:
                        for line in f:
                            if line.startswith('source:'):
                                url = line[len('source:'):].strip()
                                if url and url not in url_to_fn:
                                    url_to_fn[url] = os.path.relpath(fpath, posts_dir)
                                break
                except Exception:
                    pass
    posts_written = []
    written_urls = []
    tab_existing_n = {}  # tab subdir -> files already on disk there
    pw_obj = None
    try:
        if use_daemon:
            from chrome_daemon import is_alive as _daemon_alive
            if not _daemon_alive():
                raise RuntimeError('SCRAPE_USE_DAEMON=1 but chrome daemon not running. '
                                   f'Start: python3 chrome_daemon.py')
            pw_obj = sync_playwright().start()
            browser = pw.chromium.connect_over_cdp('http://127.0.0.1:9222')
            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
        else:
            pw_obj = sync_playwright().start()
            browser = pw_obj.chromium.launch(**launch_kwargs)
            ctx = browser.new_context(user_agent=common.BROWSER_UA)
            if cf_cfg:
                cookies_mod.inject_cf_clearance(ctx, cf_cfg['domain'], cf_cfg['value'])
            page = ctx.new_page()

        # 1. fetch each index URL + scroll, aggregate links (dedup)
        # rotate context every tab to avoid bot detection patterns (AMD ROCm, NVIDIA)
        links = []
        tab_map = {}   # post url -> tab subdir ('' = posts/ top level)
        tabs_no_update = 0
        for tab_idx, idx_url in enumerate(index_urls):
            if tab_idx > 0 and not use_daemon:
                # fresh context to break tracking patterns
                ctx.close()
                ctx = browser.new_context(
                    user_agent=common.BROWSER_UA,
                    locale='en-US',
                    timezone_id='America/New_York',
                )
                if cf_cfg:
                    cookies_mod.inject_cf_clearance(ctx, cf_cfg['domain'], cf_cfg['value'])
                page = ctx.new_page()
                time.sleep(_jit(1))  # gentle backoff
            try:
                page.goto(idx_url, wait_until='networkidle', timeout=TIMEOUT_MS)
            except Exception:
                try:
                    page.goto(idx_url, wait_until='domcontentloaded', timeout=TIMEOUT_MS * 2)
                except Exception as e:
                    print(f'  tab {idx_url} goto err: {str(e)[:80]}', flush=True)
                    continue
            time.sleep(_jit(3))  # let Cloudflare challenge JS complete
            # detect Cloudflare bot challenge
            body_text = page.inner_text('body')[:500]
            if 'Performing security verification' in body_text or 'Ray ID:' in body_text:
                print(f'  tab {idx_url} blocked by Cloudflare (skip)', flush=True)
                continue
            for _ in range(8):
                page.mouse.wheel(0, 1500)
                time.sleep(_jit(0.5))
            html = page.content()
            idx_links = _extract_post_links(html, idx_url)
            # per-tab head-check: this tab's newest post already local →
            # tab unchanged, contributes no links. When EVERY tab is
            # unchanged, short-circuit the whole channel (single-index
            # channels are the len==1 special case of this).
            if idx_links and idx_links[0] in url_to_fn:
                tabs_no_update += 1
                print(f'  head-check: newest post already local — tab unchanged '
                      f'({tabs_no_update}/{len(index_urls)})', flush=True)
                if tabs_no_update == len(index_urls):
                    if not use_daemon:
                        browser.close()
                    out.update(status='ok', mode='blog', posts=[], total_chars=0,
                               post_urls=url_to_fn, head_check='no_update')
                    meta_channels[ch_key] = out
                    return
                continue
            # dedup against previously seen links; per-tab cap = newest
            # MAX_POSTS of THIS tab (tabs don't share the quota)
            tab = _tab_name(idx_url) if len(index_urls) > 1 else ''
            seen_in_batch = {l for l in links}
            new_links = [l for l in idx_links[:MAX_POSTS]
                         if l not in seen_in_batch and l not in url_to_fn]
            for l in new_links:
                tab_map[l] = tab
            links.extend(new_links)
            print(f'  index {idx_url} -> {len(idx_links)} links ({len(new_links)} new, total={len(links)})', flush=True)
        if not links:
            # fallback to single-index URL behavior
            page.goto(index_url, wait_until='networkidle', timeout=TIMEOUT_MS)
            html = page.content()
            links = _extract_post_links(html, index_url)[:MAX_POSTS]
        # final ordered-preserving dedup — guard against tab-merging or
        # extractor edge-cases that pass duplicates (e.g. trailing-slash
        # near-duplicates slipping past seen-set before normalization).
        links = list(dict.fromkeys(links))
        print(f'  total {len(links)} post links across {len(index_urls)} index(es)', flush=True)

        # 2. visit each post (skip URLs already in url_to_fn = cross-run dedup)
        for i, url in enumerate(links):
            if url in url_to_fn:
                print(f'  [{i+1}/{len(links)}] skip (already fetched) {url}', flush=True)
                continue
            # rotate context every 20 posts to avoid bot detection (skipped in daemon mode)
            if not use_daemon and (len(posts_written) + len(written_urls)) > 0 and (len(posts_written) + len(written_urls)) % 20 == 0:
                ctx.close()
                ctx = browser.new_context(
                    user_agent=common.BROWSER_UA,
                    locale='en-US',
                    timezone_id='America/New_York',
                )
                if cf_cfg:
                    cookies_mod.inject_cf_clearance(ctx, cf_cfg['domain'], cf_cfg['value'])
                page = ctx.new_page()
                time.sleep(_jit(2))
            try:
                page.goto(url, wait_until=WAIT, timeout=15000)
                time.sleep(_jit(1))
                post_html = page.content()
                # detect Cloudflare challenge
                if 'Performing security verification' in post_html[:2000] or 'Ray ID:' in post_html[:2000]:
                    print(f'  [{i+1}/{len(links)}] skip (cf block) {url}', flush=True)
                    continue
                md = common.extract_md(post_html, url)
                if not md or len(md) < 100:
                    print(f'  [{i+1}/{len(links)}] skip (no md) {url}', flush=True)
                    continue
                # multi-tab SRC: file under posts/<tab>/NN_slug.md, numbering
                # restarts per tab; single-index SRC stays at posts/ top level
                tab = tab_map.get(url, '')
                tab_dir = os.path.join(posts_dir, tab) if tab else posts_dir
                os.makedirs(tab_dir, exist_ok=True)
                if tab not in tab_existing_n:
                    tab_existing_n[tab] = len([f for f in os.listdir(tab_dir)
                                               if f.endswith('.md')])
                fn = f'{tab_existing_n[tab]+1:02d}_{_slug(url)[:60]}.md'
                rel = f'{tab}/{fn}' if tab else fn
                with open(os.path.join(tab_dir, fn), 'w') as f:
                    f.write(f'# {_slug(url)}\n\nsource: {url}\n\n{md}\n')
                posts_written.append(rel)
                url_to_fn[url] = rel
                written_urls.append(url)
                print(f'  [{i+1}/{len(links)}] {len(md)}c {rel}', flush=True)
            except Exception as e:
                print(f'  [{i+1}/{len(links)}] error {url}: {e}', flush=True)
        if not use_daemon:
            browser.close()
        out.update(status='ok', mode='blog', posts=posts_written,
                   total_chars=sum(os.path.getsize(os.path.join(posts_dir, f))
                                   for f in posts_written),
                   post_urls=url_to_fn)
    except Exception as e:
        out.update(status='error', mode='blog', error=str(e)[:200])
    finally:
        if pw_obj is not None:
            try:
                pw_obj.stop()
            except Exception:
                pass
    meta_channels[ch_key] = out