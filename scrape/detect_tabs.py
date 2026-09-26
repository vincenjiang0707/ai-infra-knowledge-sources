#!/usr/bin/env python3
"""Detect tab URLs on blog index pages (e.g. AMD ROCm / NVIDIA).

Run as one-shot to discover tab structure for a given URL:
  python3 detect_tabs.py https://rocm.blogs.amd.com/

Output: JSON list of tab URLs (excluding root).

Used to manually seed blog_topup channel.index_urls field.
"""
import json
import re
import subprocess
import sys
import os

CHROME = os.environ.get('SCRAPE_CHROME', '/home/jj/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome')

# text labels that suggest a category tab
TAB_HINT_LABELS = (
    'home', 'ai', 'hpc', 'data science', 'data-science',
    'systems', 'developers', 'developer', 'robotics',
    'tutorials', 'guides', 'news', 'research', 'blog',
    'about', 'archive', 'archives', 'category', 'topics',
)


def detect(index_url):
    """Visit page, look for tab-like nav links."""
    from playwright.sync_api import sync_playwright
    out = {'index': index_url, 'tabs': [], 'all_matching_links': []}
    with sync_playwright() as pw:
        launch = {'headless': True, 'args': ['--no-sandbox']}
        if os.path.exists(CHROME):
            launch['executable_path'] = CHROME
        browser = pw.chromium.launch(**launch)
        page = browser.new_context().new_page()
        try:
            page.goto(index_url, wait_until='networkidle', timeout=30000)
        except Exception as e:
            page.goto(index_url, wait_until='domcontentloaded', timeout=30000)
        time_sleep = 2
        import time as _t; _t.sleep(time_sleep)
        html = page.content()
        # find <a> tags whose text matches a tab hint AND href is sibling to root
        from urllib.parse import urljoin, urlparse
        base_netloc = urlparse(index_url).netloc
        base_dir = urlparse(index_url).path.rsplit('/', 1)[0] + '/'
        candidates = []
        for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>', html, re.I):
            href, text = m.group(1), m.group(2).strip()
            full = urljoin(index_url, href)
            if urlparse(full).netloc != base_netloc:
                continue
            if not text:
                continue
            t = text.lower()
            # match tab hints
            matched = False
            for h in TAB_HINT_LABELS:
                if t == h or t.startswith(h + ' ') or t == h + 's':
                    matched = True
                    break
            if not matched:
                continue
            # exclude pure root and non-html
            if full.rstrip('/') == index_url.rstrip('/'):
                continue
            if any(full.lower().endswith(s) for s in ('.xml', '.json', '.rss', '.atom', '.pdf')):
                continue
            candidates.append({'text': text, 'href': full})
            out['all_matching_links'].append({'text': text, 'href': full})
        # dedup by URL
        seen = set()
        uniq = []
        for c in candidates:
            if c['href'] not in seen:
                seen.add(c['href'])
                uniq.append(c)
        out['tabs'] = [c['href'] for c in uniq]
        browser.close()
    return out


def main():
    if len(sys.argv) < 2:
        print('usage: detect_tabs.py <index_url>')
        sys.exit(1)
    res = detect(sys.argv[1])
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()