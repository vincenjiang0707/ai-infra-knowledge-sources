"""Menu crawl: fall back when sitemap/llms missing.

BFS from seed URL, same-origin only. Extract nav links from rendered HTML
(works on Docusaurus/MkDocs/Sphinx that fail to expose sitemap.xml).
Cap pages per SRC.
"""
import os
import re
import time
from urllib.parse import urljoin, urldefrag, urlparse

from . import common

CAP = 200
MAX_DEPTH = 3


def try_run(src, ch_key, ch, meta_channels, cursor):
    """Returns True if menu crawl produced output; False to let caller fallback."""
    seed = ch['url']
    base = urlparse(seed)
    origin = f'{base.scheme}://{base.netloc}'
    pages_dir = os.path.join(common.src_dir(src['src_id']), 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    out = {'type': 'menu', 'url': seed, 'mode': 'menu_bfs'}

    prev = (cursor.get(f'{ch_key}:menu') or {})
    visited = set(prev.get('visited', []))
    frontier = [seed]
    depth_idx = {seed: 0}
    fetched = failed = 0
    md_count = 0
    while frontier and fetched + failed < CAP:
        next_frontier = []
        for url in frontier:
            if url in visited or depth_idx.get(url, 0) >= MAX_DEPTH:
                continue
            code, html = common.fetch_url(url, timeout=30)
            visited.add(url)
            if code != 200 or not html:
                failed += 1
                continue
            fetched += 1
            md = common.extract_md(html, url)
            if md:
                fn = common.slugify(url) + '.md'
                with open(os.path.join(pages_dir, fn), 'w') as f:
                    f.write(f"source: {url}\n\n{md}")
                md_count += 1
            for href in _nav_links(html, url, origin):
                if href not in visited and href not in next_frontier and href not in frontier:
                    depth_idx[href] = depth_idx.get(url, 0) + 1
                    next_frontier.append(href)
            if (fetched + failed) % 20 == 0:
                time.sleep(0.3)
        frontier = next_frontier

    out.update(status='ok' if md_count else 'error',
               pages_fetched=fetched, pages_failed=failed,
               md_written=md_count, output_dir='pages/', cap=CAP)
    if visited:
        cursor[f'{ch_key}:menu'] = {'visited': sorted(visited)}
    meta_channels[ch_key] = out
    return md_count > 0


def _nav_links(html, base_url, base_url_str):
    """Extract same-origin links from entire HTML. Prioritize nav/aside/main
    regions by emitting their hrefs first (still BFS — order matters)."""
    origin = urlparse(base_url).netloc
    regions = []
    for tag in ('nav', 'aside', 'main'):
        for m in re.finditer(rf'<{tag}\b[^>]*>([\s\S]*?)</{tag}>', html, re.I):
            regions.append(m.group(1))
    blob = '\n'.join(regions) + '\n' + html

    out, seen = [], set()
    for href in re.findall(r'href=["\']([^"\']+)["\']', blob):
        href = href.strip()
        if not href or href.startswith(('#', 'mailto:', 'tel:', 'javascript:')):
            continue
        full = urldefrag(urljoin(base_url, href)).url
        p = urlparse(full)
        if p.netloc != origin:
            continue
        if re.search(r'\.(png|jpe?g|gif|svg|ico|css|js|woff2?|pdf|zip)(\?|$)',
                     p.path, re.I):
            continue
        if full not in seen:
            seen.add(full)
            out.append(full)
    return out