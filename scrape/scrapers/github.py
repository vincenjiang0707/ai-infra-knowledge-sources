"""GitHub channel: repo meta, README, issues/pulls top-100, releases, changelog."""
import json
import os
import re

from . import common
from . import github_detail

CAP = 100
CHANGELOG_NAMES = ['CHANGELOG.md', 'CHANGES.md', 'HISTORY.md', 'NEWS.md']
RAW = 'https://raw.githubusercontent.com'


def run(src, ch_key, ch, meta_channels, cursor):
    """Scrape one github_repo channel. Mutates meta_channels + cursor."""
    url = ch['url']
    m = re.match(r'https://github\.com/([^/]+)/([^/]+)', url)
    owner, repo = m.group(1), m.group(2)
    d = common.src_dir(src['src_id'])
    out = {'type': 'github_repo', 'url': url}
    print(f'[{ch_key}] {owner}/{repo}', flush=True)
    # If this channel has never had detail fetched, force-refresh jsonl
    # even if cursor head-check would otherwise short-circuit. Otherwise
    # first-time-detail SRCs get stuck at "no update" forever.
    detail_dir = os.path.join(d, 'github_details', ch_key)
    detail_missing = not os.path.isdir(detail_dir)

    # 1. repo meta
    data, st = common.gh_api(f'repos/{owner}/{repo}')
    if st != 'ok':
        out.update(status=st, error=f'repos API {st}')
        meta_channels[ch_key] = out
        return
    branch = data.get('default_branch') or 'main'
    # fork 上游: 手工 override 优先, 否则取根仓库 (data.source, fork 链最顶层)
    upstream = ch.get('upstream_override') or (
        (data.get('source') or {}).get('full_name') if data.get('fork') else None)
    if ch.get('upstream_override'):
        out['upstream_override'] = ch['upstream_override']  # 回写持久化
    head = [f'# {owner}/{repo}', '',
            f'- stars: {data.get("stargazers_count")}',
            f'- forks: {data.get("forks_count")}',
            f'- open_issues: {data.get("open_issues_count")}',
            f'- default_branch: {branch}',
            f'- archived: {data.get("archived")}',
            f'- license: {(data.get("license") or {}).get("spdx_id")}',
            f'- pushed_at: {data.get("pushed_at")}',
            f'- homepage: {data.get("homepage")}']
    if upstream:
        head.append(f'- forked from: {upstream} (issues/PRs 从上游获取)')
    head.append('')

    # 2. README
    code, body = common.fetch_url(f'{RAW}/{owner}/{repo}/{branch}/README.md')
    readme_found = code == 200 and body
    if not readme_found:
        code, body = common.fetch_url(f'{RAW}/{owner}/{repo}/{branch}/readme.md')
        readme_found = code == 200 and body
    if readme_found:
        head += ['## README', '', body]
    out['readme'] = 'embedded' if readme_found else 'missing'
    with open(os.path.join(d, 'github_repo.md'), 'w') as f:
        f.write('\n'.join(head))
    out.update(status='ok', output='github_repo.md')

    # 3. issues (top-100 by updated desc, mirror web UI default sort)
    # head-check: 1 API call — if newest activity <= cursor, keep cached jsonl
    prev_c = cursor.get(f'{ch_key}:issues') or {}
    prev_i = prev_c.get('last_updated_at', '')
    # 上次若已回退到上游, head-check 也对上游做
    hc_tgt_i = prev_c.get('from') or f'{owner}/{repo}'
    head_i = 'zzz' if detail_missing else (_head_updated(hc_tgt_i, 'issues') or 'zzz')
    if prev_i and head_i <= prev_i and not detail_missing:
        out['issues'] = {'status': 'ok', 'count': 'cached',
                         'note': 'head-check: no update since last run'}
        print(f'  [{ch_key}] issues cached (head_check ok)', flush=True)
    else:
        print(f'  [{ch_key}] fetching issues top-{CAP} (head={head_i[:10]}, prev={prev_i[:10] or "—"})', flush=True)
        tgt = f'{owner}/{repo}'
        rows, st_i, last_upd = _list(d, f'repos/{tgt}/issues',
                                     'github_issues.jsonl',
                                     params='per_page=100&state=all&sort=updated&direction=desc',
                                     kind='issue', cap=CAP)
        # fork 仓库 issues 为空 → 回退到上游根仓库
        if st_i == 'ok' and not rows and upstream and upstream != tgt:
            print(f'  [{ch_key}] fork issues empty -> fallback to {upstream}', flush=True)
            tgt = upstream
            rows, st_i, last_upd = _list(d, f'repos/{upstream}/issues',
                                         'github_issues.jsonl',
                                         params='per_page=100&state=all&sort=updated&direction=desc',
                                         kind='issue', cap=CAP)
        out['issues'] = {'status': st_i, 'count': len(rows),
                         'note': f'top-{CAP} by updated_at desc (web default)'}
        if tgt != f'{owner}/{repo}':
            out['issues']['from'] = upstream
        if last_upd:
            cur = {'last_updated_at': last_upd}
            if tgt != f'{owner}/{repo}':
                cur['from'] = upstream
            cursor[f'{ch_key}:issues'] = cur
        if st_i == 'ok' and rows:
            _run_detail(d, ch_key, tgt, rows, 'issue', out, 'issues')

    # 4. pulls (top-100 by updated desc, mirror web UI default sort)
    prev_c = cursor.get(f'{ch_key}:pulls') or {}
    prev_p = prev_c.get('last_updated_at', '')
    hc_tgt_p = prev_c.get('from') or f'{owner}/{repo}'
    head_p = 'zzz' if detail_missing else (_head_updated(hc_tgt_p, 'pulls') or 'zzz')
    if prev_p and head_p <= prev_p and not detail_missing:
        out['pulls'] = {'status': 'ok', 'count': 'cached',
                        'note': 'head-check: no update since last run'}
        print(f'  [{ch_key}] pulls cached (head_check ok)', flush=True)
    else:
        print(f'  [{ch_key}] fetching pulls top-{CAP} (head={head_p[:10]}, prev={prev_p[:10] or "—"})', flush=True)
        tgt_p = f'{owner}/{repo}'
        rows_p, st_p, last_upd_p = _list(d, f'repos/{tgt_p}/pulls',
                                         'github_pulls.jsonl',
                                         params='per_page=100&state=all&sort=updated&direction=desc',
                                         kind='pr', cap=CAP)
        if st_p == 'ok' and not rows_p and upstream and upstream != tgt_p:
            print(f'  [{ch_key}] fork pulls empty -> fallback to {upstream}', flush=True)
            tgt_p = upstream
            rows_p, st_p, last_upd_p = _list(d, f'repos/{upstream}/pulls',
                                             'github_pulls.jsonl',
                                             params='per_page=100&state=all&sort=updated&direction=desc',
                                             kind='pr', cap=CAP)
        out['pulls'] = {'status': st_p, 'count': len(rows_p),
                        'note': f'top-{CAP} by updated_at desc (web default)'}
        if tgt_p != f'{owner}/{repo}':
            out['pulls']['from'] = upstream
        if last_upd_p:
            cur = {'last_updated_at': last_upd_p}
            if tgt_p != f'{owner}/{repo}':
                cur['from'] = upstream
            cursor[f'{ch_key}:pulls'] = cur
        if st_p == 'ok' and rows_p:
            _run_detail(d, ch_key, tgt_p, rows_p, 'pr', out, 'pulls')

    # 5. releases (all)
    print(f'  [{ch_key}] fetching releases', flush=True)
    rows_r, st_r, last_id = _list(d, f'repos/{owner}/{repo}/releases',
                                  'github_releases.jsonl',
                                  params='per_page=100', kind='release', cap=None)
    out['releases'] = {'status': st_r, 'count': len(rows_r)}
    if last_id:
        cursor[f'{ch_key}:releases'] = {'last_id': last_id}

    # 6. changelog: probe 4 filenames, else aggregate releases.body
    cl_src, cl_text = None, None
    for fn in CHANGELOG_NAMES:
        code, body = common.fetch_url(f'{RAW}/{owner}/{repo}/{branch}/{fn}')
        if code == 200 and body:
            cl_src, cl_text = fn, body
            break
    if cl_text is None:
        cl_src = 'releases.body'
        cl_text = _aggregate_releases(rows_r)
    with open(os.path.join(d, 'github_changelog.md'), 'w') as f:
        f.write(cl_text)
    out['changelog'] = {'status': 'ok', 'output': 'github_changelog.md',
                        'from': cl_src, 'probed': CHANGELOG_NAMES}

    meta_channels[ch_key] = out


def _head_updated(owner_repo, kind):
    """Head-check: newest updated_at for issues|pulls in 1 API call.

    owner_repo 形如 'owner/repo' (可能是 fork 上游, 由调用方决定).
    Returns None on API error (caller treats as 'changed' → full refresh).
    Issues API mixes PRs — that only makes the check conservative (more
    likely to refresh, never to miss activity)."""
    data, st = common.gh_api(f'repos/{owner_repo}/{kind}'
                             '?per_page=5&state=all&sort=updated&direction=desc')
    if st != 'ok' or not data:
        return None
    return max((it.get('updated_at') or '') for it in data)


def _list(d, api, fname, params, kind, cap):
    """Paginate gh api list; write JSONL; return (rows, status, cursor_val)."""
    rows, status, cursor_val = [], 'ok', None
    page = 1
    while True:
        data, st = common.gh_api(f'{api}?{params}&page={page}')
        if st != 'ok':
            status = st if not rows else 'partial'
            break
        if not data:
            break
        for it in data:
            row = _row(it, kind)
            if row:
                rows.append(row)
                if kind != 'release':
                    cursor_val = max(cursor_val or '', row['updated_at'])
        if cap and len(rows) >= cap:
            rows = rows[:cap]
            break
        if len(data) < 100:
            break
        page += 1
    if rows:
        with open(os.path.join(d, fname), 'w') as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
    if kind == 'release':
        cursor_val = rows[0]['id'] if rows else None
    return rows, status, cursor_val


def _row(it, kind):
    if kind == 'release':
        return {'id': it.get('id'), 'tag': it.get('tag_name'),
                'name': it.get('name'), 'published_at': it.get('published_at'),
                'prerelease': it.get('prerelease'), 'body_chars': len(it.get('body') or ''),
                'body': it.get('body') or ''}
    if kind == 'issue':
        if 'pull_request' in it:
            return None  # issues API includes PRs; filter
        return {'number': it.get('number'), 'title': it.get('title'),
                'state': it.get('state'), 'created_at': it.get('created_at'),
                'updated_at': it.get('updated_at'), 'closed_at': it.get('closed_at'),
                'labels': [l['name'] for l in it.get('labels', [])],
                'comments_count': it.get('comments'), 'is_pr': False,
                'body': it.get('body') or '',
                'url': it.get('html_url')}
    return {'number': it.get('number'), 'title': it.get('title'),
            'state': it.get('state'), 'created_at': it.get('created_at'),
            'updated_at': it.get('updated_at'), 'closed_at': it.get('closed_at'),
            'labels': [l['name'] for l in it.get('labels', [])],
            'comments_count': it.get('comments'),
            'is_pr': True, 'merged_at': it.get('merged_at'),
            'body': it.get('body') or '',
            'url': it.get('html_url')}


def _aggregate_releases(rows):
    head = [f'# Changelog (aggregated from releases.body)', '',
            f'> releases: {len(rows)}', '']
    for r in reversed(rows):  # oldest first
        head += [f"## {r['tag'] or r['name']} ({(r['published_at'] or '')[:10]})", '',
                 r['body'] or '(empty body)', '']
    return '\n'.join(head)


def _run_detail(d, ch_key, owner_repo, rows, kind, out, out_key):
    """Wire detail fetch into the main pipeline: migrate legacy flat files
    (one-time per SRC) then run per-item incremental fetch."""
    base = os.path.join(d, 'github_details')
    github_detail.migrate_legacy_flat(base, ch_key, owner_repo, kind, rows)
    ddir = os.path.join(base, ch_key)
    out[out_key]['details'] = github_detail.process_repo(
        owner_repo, ch_key, rows, kind, ddir)
