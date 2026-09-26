"""Shared: meta json io, state machine, slug, http helpers."""
import hashlib
import json
import os
import re
import subprocess
import time
from datetime import datetime, timezone

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    '..')  # scrape/ sits directly under knowledge-sources/
ROOT = os.path.normpath(ROOT)

BLOCKED_HTTP = (401, 403, 404)

# realistic desktop UA shared by all fetchers (curl, playwright contexts)
BROWSER_UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def slugify(url):
    """Stable filesystem slug from URL."""
    s = re.sub(r'^https?://', '', url.strip('/'))
    s = re.sub(r'[^A-Za-z0-9._-]+', '_', s)
    h = hashlib.md5(url.encode()).hexdigest()[:6]
    return f"{s[-80:]}_{h}"


def src_dir(src_id):
    d = os.path.join(ROOT, 'sources', src_id)
    os.makedirs(d, exist_ok=True)
    return d


def load_meta(src_id):
    p = os.path.join(ROOT, 'sources', src_id, '_meta.json')
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None


def save_meta(src_id, meta):
    p = os.path.join(ROOT, 'sources', src_id, '_meta.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)


def http_classify_error(err):
    """Map error to channel status: blocked vs error."""
    s = str(err)
    for code in BLOCKED_HTTP:
        if f'HTTP {code}' in s or f'{code}' in re.findall(r'\b\d{3}\b', s[:200] or ''):
            if f'HTTP {code}' in s:
                return 'blocked'
    return 'error'


def fetch_url(url, timeout=30):
    """curl fetch, returns (status_code, body|None)."""
    try:
        r = subprocess.run(
            ['curl', '-sL', '--max-time', str(timeout), '-w', '\n%{http_code}',
             '-A', BROWSER_UA, url],
            capture_output=True, text=True, timeout=timeout + 10)
        body, _, code = r.stdout.rpartition('\n')
        return int(code or 0), (body if int(code or 0) == 200 else None)
    except Exception:
        return 0, None


def extract_md(html, url):
    import trafilatura
    return trafilatura.extract(html, url=url, output_format='markdown',
                               include_links=True) or ''


def combine_status(channels):
    """SRC status from channel statuses."""
    sts = [c.get('status') for c in channels.values()] or ['not_fetched']
    if all(s == 'ok' for s in sts):
        return 'success'
    if any(s == 'ok' for s in sts):
        return 'partial'
    if all(s == 'blocked' for s in sts):
        return 'blocked'
    return 'not_fetched'


def gh_api(path, accept='application/vnd.github+json'):
    """gh api call; returns (data|None, status_str). Sleep 0.1s after each."""
    try:
        r = subprocess.run(['gh', 'api', path, '-H', f'Accept: {accept}'],
                           capture_output=True, text=True, timeout=60)
        time.sleep(0.1)
        if r.returncode != 0:
            err = (r.stderr or '').strip()
            for code in BLOCKED_HTTP:
                if f'HTTP {code}' in err:
                    return None, 'blocked'
            return None, 'error'
        return json.loads(r.stdout), 'ok'
    except Exception as e:
        return None, f'error'
