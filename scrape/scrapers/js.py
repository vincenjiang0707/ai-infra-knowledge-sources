"""JS-rendered page scraper: playwright headless chromium.

Use when site.py:_page_extract fails to retrieve meaningful content
(SPA shell with empty body — e.g. Nuxt SSR returning shell only).
"""
import os, time
from . import common

TIMEOUT_MS = 45000

# Allow pointing at an already-installed chromium (puppeteer / system chrome)
# when playwright's CDN-hosted binary can't be installed in this env.
CHROME_PATH = os.environ.get('SCRAPE_CHROME') or \
    '/home/jj/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome'


def run(src, ch_key, ch, meta_channels, cursor):
    url = ch['url']
    d = common.src_dir(src['src_id'])
    out = {'type': 'js', 'url': url}
    from playwright.sync_api import sync_playwright
    try:
        launch_kwargs = {'headless': True, 'args': ['--no-sandbox']}
        if os.path.exists(CHROME_PATH):
            launch_kwargs['executable_path'] = CHROME_PATH
        with sync_playwright() as pw:
            browser = pw.chromium.launch(**launch_kwargs)
            ctx = browser.new_context(user_agent=common.BROWSER_UA)
            page = ctx.new_page()
            page.goto(url, wait_until='networkidle', timeout=TIMEOUT_MS)
            # give SPA hydration a moment
            time.sleep(2)
            html = page.content()
            text = page.inner_text('body')
            browser.close()
        if not html:
            out.update(status='error', mode='js')
        else:
            from . import common as C
            md = C.extract_md(html, url)
            if md and len(md) > 200:
                fn = 'page.md'
                with open(os.path.join(d, fn), 'w') as f:
                    f.write('# ' + src.get('name', '') + '\n\nsource: ' + url + '\n\n' + md + '\n')
                out.update(status='ok', output=fn, mode='js', chars=len(md))
            else:
                out.update(status='error', mode='js', chars=len(text), reason='no_md')
    except Exception as e:
        out.update(status='error', mode='js', error=str(e)[:200])
    meta_channels[ch_key] = out
