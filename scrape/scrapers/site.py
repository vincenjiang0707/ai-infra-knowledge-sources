"""Site channel: feed discovery (RSS/Atom) → docs sitemap crawl → page extract."""
import json
import os
import re

from . import common

FEED_PROBES = ['feed.xml', 'atom.xml', 'rss.xml', 'index.xml', 'feed/', 'rss/']
POST_CAP = 500


def run(src, ch_key, ch, meta_channels, cursor):
    url = ch['url'].rstrip('/') + '/'
    d = common.src_dir(src['src_id'])
    out = {'type': ch['type'], 'url': ch['url']}

    # raw text manifests (llms.txt etc.)
    if ch['url'].rstrip('/').endswith(('.txt', '.md')):
        code, body = common.fetch_url(ch['url'])
        if code == 200 and body:
            fn = 'page.md'
            with open(os.path.join(d, fn), 'w') as f:
                f.write(f"source: {ch['url']}\n\n{body}")
            out.update(status='ok', output=fn, mode='raw', chars=len(body))
        else:
            out.update(status='blocked' if code in common.BLOCKED_HTTP else 'error',
                       http_code=code, mode='raw')
        meta_channels[ch_key] = out
        return

    feed_url = _cached_feed_url(d) or _discover_feed(url)
    if feed_url:
        out.update(mode='rss')
        _rss(d, src, feed_url, out, cursor, ch_key)
    elif _is_docs(ch['url']):
        from . import sitemap, menu
        if sitemap.try_run(src, ch_key, ch, meta_channels, cursor):
            return
        if menu.try_run(src, ch_key, ch, meta_channels, cursor):
            return  # menu wrote its own channel result
        _page_extract(d, ch, out)
    else:
        _page_extract(d, ch, out)
    meta_channels[ch_key] = out


def _page_extract(d, ch, out):
    code, html = common.fetch_url(ch['url'])
    if code != 200 or not html:
        out.update(status='blocked' if code in common.BLOCKED_HTTP else 'error',
                   http_code=code, mode='page')
        return
    md = common.extract_md(html, ch['url'])
    fn = 'page.md'
    with open(os.path.join(d, fn), 'w') as f:
        f.write(f"source: {ch['url']}\n\n{md}")
    out.update(status='ok', output=fn, mode='page', chars=len(md))


def _is_docs(url):
    u = url.lower()
    host = re.match(r'https?://([^/]+)', u).group(1)
    return (host.startswith('docs.') or '/docs' in u or '/guide' in u
            or '/learn/' in u or '/documentation' in u)


def _cached_feed_url(d):
    """Reuse feed_url recorded by a previous run (saves 7-probe discovery)."""
    p = os.path.join(d, 'feed_meta.json')
    if os.path.exists(p):
        try:
            return json.load(open(p)).get('feed_url')
        except Exception:
            return None
    return None


def _discover_feed(url):
    """Try <link rel=alternate> in HTML head, then common paths."""
    code, html = common.fetch_url(url, timeout=20)
    if code == 200 and html:
        m = re.search(
            r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]+href=["\']([^"\']+)'
            r'|<link[^>]+href=["\']([^"\']+)["\'][^>]+type=["\']application/(?:rss|atom)\+xml["\']',
            html[:20000], re.I)
        if m:
            href = m.group(1) or m.group(2)
            if href.startswith('http'):
                return href
            root = re.match(r'(https?://[^/]+)', url).group(1)
            return root + href if href.startswith('/') else url + href
    for p in FEED_PROBES:
        cand = url + p
        code, body = common.fetch_url(cand, timeout=15)
        if code == 200 and body and re.search(r'<(rss|feed)[ >]', body[:2000]):
            return cand
    return None


def _rss(d, src, feed_url, out, cursor, ch_key):
    import feedparser
    fp = feedparser.parse(feed_url)
    entries = fp.entries or []
    last_pub = ''
    for e in entries:
        pub = e.get('published', '') or e.get('updated', '')
        if pub > last_pub:
            last_pub = pub

    # head-check: newest entry link unchanged vs local feed_meta.json →
    # nothing new since last run, skip per-entry fetching entirely
    meta_path = os.path.join(d, 'feed_meta.json')
    new_first = entries[0].get('link', '') if entries else ''
    if new_first and os.path.exists(meta_path):
        try:
            old_first = ((json.load(open(meta_path)).get('entries') or [{}])[0]
                         .get('link', ''))
            if old_first == new_first:
                out.update(status='ok', output='feed_meta.json',
                           entries=len(entries), posts_fetched=0, posts_failed=0,
                           output_dir='posts/', head_check='no_update')
                if last_pub:
                    cursor[f'{ch_key}:rss'] = {'last_entry_published': last_pub}
                return
        except Exception:
            pass

    feed_meta = {
        'feed_url': feed_url,
        'title': fp.feed.get('title', ''),
        'link': fp.feed.get('link', ''),
        'updated': fp.feed.get('updated', ''),
        'entries_total': len(entries),
        'entries': [{'title': e.get('title', ''), 'link': e.get('link', ''),
                     'published': e.get('published', '')} for e in entries],
    }
    with open(meta_path, 'w') as f:
        json.dump(feed_meta, f, ensure_ascii=False, indent=1)

    posts_dir = os.path.join(d, 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    # cross-run dedup: entry slugs already on disk are not refetched
    local_slugs = set()
    for fn in os.listdir(posts_dir):
        if fn.endswith('.md') and '_' in fn:
            local_slugs.add(fn.split('_', 1)[1][:-3])
    fetched = failed = 0
    for e in entries[:POST_CAP]:
        link = e.get('link')
        if not link:
            continue
        if common.slugify(link) in local_slugs:
            continue  # already fetched in an earlier run
        pub = e.get('published', '') or e.get('updated', '')
        code, html = common.fetch_url(link, timeout=30)
        md = common.extract_md(html, link) if code == 200 and html else ''
        if md:
            pt = e.get('published_parsed') or e.get('updated_parsed')
            date = ('%04d%02d%02d' % pt[:3]) if pt else 'undated'
            fn = f"{date}_{common.slugify(link)}.md"
            with open(os.path.join(posts_dir, fn), 'w') as f:
                f.write(f"# {e.get('title', '')}\n\nsource: {link}\npublished: {pub}\n\n{md}")
            local_slugs.add(common.slugify(link))
            fetched += 1
        else:
            failed += 1
    out.update(status='ok' if (fetched or local_slugs) else 'error',
               output='feed_meta.json', entries=len(entries),
               posts_fetched=fetched, posts_failed=failed, output_dir='posts/')
    if last_pub:
        cursor[f'{ch_key}:rss'] = {'last_entry_published': last_pub}
