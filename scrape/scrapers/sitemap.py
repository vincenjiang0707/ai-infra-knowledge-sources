"""Sitemap channel: sitemap.xml (index-aware) + page crawl with lastmod cursor."""
import os
import re
import time
import xml.etree.ElementTree as ET

from . import common

PAGE_CAP = 2000
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def try_run(src, ch_key, ch, meta_channels, cursor):
    """Attempt sitemap crawl. Returns False if no sitemap found (caller falls
    back to single-page extract)."""
    url = ch['url'].rstrip('/')
    d = common.src_dir(src['src_id'])
    out = {'type': 'sitemap', 'url': ch['url']}

    pages, mode = _find_pages(url)
    if pages is None:
        return False  # no sitemap anywhere -> caller fallback
    out['mode'] = mode

    prev = (cursor.get(f'{ch_key}:sitemap') or {})
    prev_lastmod = prev.get('lastmod', '')
    pages_dir = os.path.join(d, 'pages')
    os.makedirs(pages_dir, exist_ok=True)
    # stale-cursor guard: prior runs may have set cursor['lastmod'] but never
    # persisted the actual pages (e.g. an error path that bailed before the
    # write). If disk has zero .md files but cursor says "all covered", treat
    # the cursor as suspect and refetch.
    on_disk = sum(1 for f in os.listdir(pages_dir) if f.endswith('.md'))
    if prev_lastmod and on_disk == 0 and pages:
        prev_lastmod = ''
    todo = [p for p in pages if not prev_lastmod or (p[1] or '') > prev_lastmod]
    todo = todo[:PAGE_CAP]
    out['pages_total'] = len(pages)

    fetched = failed = 0
    max_lastmod = prev_lastmod
    # head-check: previous cursor already covers every page — nothing to do,
    # short-circuit with ok status (mirrors blog.py head-check pattern).
    # Without this, fetched=0 falls through to status='error' below even
    # though nothing actually failed.
    if pages and not todo:
        out.update(status='ok', pages_fetched=0, pages_failed=0,
                   output_dir='pages/', cap=PAGE_CAP, head_check='no_update')
        meta_channels[ch_key] = out
        return True
    for loc, lastmod in todo:
        code, html = common.fetch_url(loc, timeout=30)
        md = common.extract_md(html, loc) if code == 200 and html else ''
        if md:
            with open(os.path.join(pages_dir, common.slugify(loc) + '.md'), 'w') as f:
                f.write(f"source: {loc}\nlastmod: {lastmod}\n\n{md}")
            fetched += 1
            if lastmod and lastmod > max_lastmod:
                max_lastmod = lastmod
        else:
            failed += 1
        if (fetched + failed) % 50 == 0:
            time.sleep(0.5)

    out.update(status='ok' if (fetched or prev_lastmod) else 'error',
               pages_fetched=fetched, pages_failed=failed,
               output_dir='pages/', cap=PAGE_CAP)
    if max_lastmod:
        cursor[f'{ch_key}:sitemap'] = {'lastmod': max_lastmod}
    meta_channels[ch_key] = out
    return True


def _find_pages(url):
    """Probe sitemap candidates. Returns (pages, mode) or (None, None)."""
    origin = re.match(r'https?://[^/]+', url).group(0)
    cands = [f'{url}/sitemap.xml', f'{origin}/sitemap.xml',
             f'{url}/sitemap_index.xml', f'{origin}/sitemap_index.xml']
    seen = set()
    for sm_url in cands:
        if sm_url in seen:
            continue
        seen.add(sm_url)
        code, body = common.fetch_url(sm_url, timeout=30)
        if code == 200 and body:
            pages = _parse_sitemap(sm_url, body, depth=0)
            # keep pages under the channel's path scope when root sitemap
            if sm_url.startswith(origin) and not sm_url.startswith(url):
                scope = url + '/'
                pages = [p for p in pages if p[0].startswith(scope)]
            if pages:
                return pages, 'sitemap.xml'
    # llms.txt manifest fallback (same dir + origin)
    for base in (url, origin):
        code, txt = common.fetch_url(f'{base}/llms.txt', timeout=20)
        if code == 200 and txt and len(txt) > 100:
            pages = _from_llms_txt(base, txt)
            if pages:
                return pages, 'llms.txt'
    return None, None


def _parse_sitemap(sm_url, body, depth):
    """Recursive sitemap index parse. Returns [(loc, lastmod)]."""
    pages = []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return pages
    tag = root.tag.split('}')[-1]
    if tag == 'sitemapindex':
        if depth > 2:
            return pages
        for sm in root.findall('s:sitemap', NS):
            loc = sm.findtext('s:loc', default='', namespaces=NS)
            if not loc:
                continue
            code, sub = common.fetch_url(loc, timeout=30)
            if code == 200 and sub:
                pages += _parse_sitemap(loc, sub, depth + 1)
    else:
        for u in root.findall('s:url', NS):
            loc = u.findtext('s:loc', default='', namespaces=NS)
            lastmod = u.findtext('s:lastmod', default='', namespaces=NS)
            if loc:
                pages.append((loc, lastmod))
    return pages


def _from_llms_txt(base, txt):
    pages = []
    for m in re.finditer(r'^\s*[-*]?\s*\[?([^\]\n]+?)\]?\s*:\s*(https?://\S+)',
                         txt, re.M):
        title, loc = m.group(1), m.group(2)
        pages.append((loc, ''))
    return pages
