"""GitHub org channel: repo list via REST API + raw README per repo.

Replaces the old site.run snapshot of the org HTML page (needs JS/login, produced
noise like "Prevent this user from interacting..."). API list is unauthenticated
(60 req/h per IP — one list call per org page, READMEs come from
raw.githubusercontent.com which is NOT rate-limited).
"""
import json
import os
import re
import time

from . import common

API = 'https://api.github.com'
REPO_CAP = 100  # max repos per org to list & fetch READMEs for
# non-org paths on github.com — fall back to site snapshot
SPECIAL_PATHS = ('trending', 'topics', 'explore', 'collections', 'features', 'about', 'pricing')


def _api_get(path, timeout=30):
    """GET api.github.com with one transient-retry. Returns (code, body_json|None)."""
    code, body = common.fetch_url(f'{API}{path}', timeout=timeout)
    if code in (403, 429, 401):  # transient throttle — one retry
        time.sleep(3)
        code, body = common.fetch_url(f'{API}{path}', timeout=timeout)
    if code == 200 and body:
        try:
            return code, json.loads(body)
        except ValueError:
            return code, None
    return code, None


def _fetch_readme(full_name, branch):
    """Raw README from raw.githubusercontent.com (no API rate limit). main file name variants."""
    for fn in ('README.md', 'readme.md', 'README.rst', 'README'):
        code, body = common.fetch_url(
            f'https://raw.githubusercontent.com/{full_name}/{branch}/{fn}', timeout=30)
        if code == 200 and body and body.strip():
            return body
    return None


def _store_post(d, full_name, readme):
    """posts/<org>_<repo>.md in the shared post format. Returns fname if written/changed."""
    posts_dir = os.path.join(d, 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    fname = full_name.replace('/', '_') + '.md'
    path = os.path.join(posts_dir, fname)
    page_url = f'https://github.com/{full_name}'
    text = f'# {full_name}\n\nsource: {page_url}\n\n{readme}\n'
    if os.path.exists(path):
        with open(path) as f:
            if f.read() == text:
                return None
    with open(path, 'w') as f:
        f.write(text)
    return fname


def run(src, ch_key, ch, meta_channels, cursor):
    url = ch['url'].rstrip('/')
    d = common.src_dir(src['src_id'])
    out = {'type': 'github_org', 'url': ch['url']}
    m = re.match(r'https://github\.com/([^/]+)$', url)
    ident = m.group(1) if m else None
    if not ident or ident.lower() in SPECIAL_PATHS:
        # not an org home (e.g. github.com/trending) — keep old page snapshot behavior
        from . import site
        site.run(src, ch_key, ch, meta_channels, cursor)
        return

    common.clog(src, ch_key, f"gh_org {ident}")
    # org first, then personal user account
    code, repos = _api_get(f'/orgs/{ident}/repos?per_page=100&sort=pushed')
    if code == 404:
        code, repos = _api_get(f'/users/{ident}/repos?per_page=100&sort=pushed')
    if code != 200 or repos is None:
        out.update(status='blocked' if code in common.BLOCKED_HTTP else 'error',
                   http_code=code)
        meta_channels[ch_key] = out
        return

    repos = repos[:REPO_CAP]
    if not repos:
        # GitHub returns 200 [] for a non-existent user's repos — empty means
        # wrong org name or an empty personal account, not a successful scrape
        out.update(status='error', http_code=code,
                   error=f'no repos for {ident} (empty user or wrong org name; check URL)')
        meta_channels[ch_key] = out
        return
    parts = [f'# GitHub org: {ident}', '', f'repos listed: {len(repos)}', '']
    for r in repos:
        parts += [f"## {r.get('full_name')}",
                  f"- stars: {r.get('stargazers_count')}",
                  f"- forks: {r.get('forks_count')}",
                  f"- language: {r.get('language')}",
                  f"- pushed_at: {r.get('pushed_at')}",
                  f"- branch: {r.get('default_branch')}",
                  f"- url: https://github.com/{r.get('full_name')}", '']
        desc = (r.get('description') or '').strip()
        if desc:
            parts += [f"desc: {desc}", '']
    cursor[f'{ch_key}:repos'] = {'count': len(repos)}

    posts_written = []
    for r in repos:
        full_name = r.get('full_name')
        branch = r.get('default_branch') or 'main'
        if r.get('archived') or r.get('fork'):
            continue  # skip forks/archived: README is someone else's
        readme = _fetch_readme(full_name, branch)
        if readme:
            fn = _store_post(d, full_name, readme)
            if fn:
                posts_written.append(fn)
        else:
            common.clog(src, ch_key, f"gh_org readme missing: {full_name}")

    with open(os.path.join(d, 'gh.md'), 'w') as f:
        f.write('\n'.join(str(p) for p in parts))
    out.update(status='ok', kind='org', repos=len(repos), posts=posts_written,
               output='gh.md')
    common.clog(src, ch_key, f"gh_org {ident} -> ok repos={len(repos)} posts={len(posts_written)}")
    meta_channels[ch_key] = out
