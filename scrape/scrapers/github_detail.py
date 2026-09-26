"""Per-item detail (comments + PR reviews) for github issues/pulls.

Two-tier storage:
  SRC-XXX/github_details/{ch_key}/
    _index_issue.jsonl      # cursor + counts for issue_NNN.md
    _index_pr.jsonl         # cursor + counts for pr_NNN.md
    issue_NNN.md            # appendable: 正文 / ## 评论 (N)
    pr_NNN.md               # appendable: 正文 / ## 评论 (N) / ## Review (N)

Why per-md and not jsonl-embedded: a single new comment is one API call
plus a small append to one md file. Blowing up jsonl to embed every
comment would force a whole-file rewrite per new comment.

Wired into scrapers/github.py:run() so the main pipeline populates detail
on every pass. Also callable standalone via detail_fetcher.py.

Schema for _index_{kind}.jsonl:
  {number, kind, file, comments, reviews, status, fetched_at,
   last_comment_id, last_review_id}   # last_* nullable; 0 / null → full refetch
"""
import json
import os
import re
import subprocess
import time

from . import common


def rate_wait():
    """Pause when gh core remaining < 100 until window reset + 10s cushion."""
    while True:
        try:
            r = subprocess.run(['gh', 'api', 'rate_limit', '--jq', '.resources.core'],
                               capture_output=True, text=True, timeout=15)
            c = json.loads(r.stdout or '{}')
            rem, reset = c.get('remaining', 5000), c.get('reset', 0)
            if rem >= 100:
                return
            wait = max(reset - time.time(), 5) + 10
            print(f'rate low ({rem}), sleep {wait/60:.1f}m', flush=True)
            time.sleep(wait)
        except Exception:
            time.sleep(30)


def _paged(path):
    """Paginate GitHub list endpoint. Stops on first empty/short page or error."""
    out, page = [], 1
    while True:
        rate_wait()
        data, st = common.gh_api(f'{path}?per_page=100&page={page}')
        if st != 'ok' or not data:
            break
        out += data
        if len(data) < 100:
            break
        page += 1
    return out, st


def fetch_comments(owner_repo, number):
    return _paged(f'repos/{owner_repo}/issues/{number}/comments')


def fetch_reviews(owner_repo, number):
    return _paged(f'repos/{owner_repo}/pulls/{number}/reviews')


def render(item, comments, reviews):
    kind = 'PR' if item.get('is_pr') else 'Issue'
    lines = [f"# [{kind} #{item['number']}] {item['title']}", '',
             f"source: {item['url']}",
             f"state: {item['state']} | updated: {item['updated_at']}",
             f"labels: {', '.join(item.get('labels') or [])}", '',
             '## 正文', '', item.get('body') or '(empty)', '',
             f'## 评论 ({len(comments)})', '']
    for c in comments:
        who = (c.get('user') or {}).get('login', '?')
        when = (c.get('created_at') or '')[:10]
        lines += [f"### {who} · {when}", '', c.get('body') or '', '']
    if item.get('is_pr') and reviews:
        lines += [f'## Review ({len(reviews)})', '']
        for rv in reviews:
            who = (rv.get('user') or {}).get('login', '?')
            when = (rv.get('submitted_at') or '')[:10]
            state = rv.get('state', '')
            lines += [f"### {who} · {when} · {state}", '', rv.get('body') or '(no text)', '']
    return '\n'.join(lines)


def atomic_write_jsonl(path, rows):
    """POSIX-atomic: write .tmp then os.replace()."""
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    os.replace(tmp, path)


def append_to_md(path, item, new_comments, new_reviews, total_c, total_r):
    """Append new comment/review blocks; bump header counters atomically."""
    with open(path) as f:
        text = f.read()
    text = re.sub(r'## 评论 \(\d+\)', f'## 评论 ({total_c})', text, count=1)
    if item.get('is_pr'):
        text = re.sub(r'## Review \(\d+\)', f'## Review ({total_r})', text, count=1)
    blocks = []
    for c in new_comments:
        who = (c.get('user') or {}).get('login', '?')
        when = (c.get('created_at') or '')[:10]
        blocks += [f"### {who} · {when}", '', c.get('body') or '', '']
    for rv in new_reviews:
        who = (rv.get('user') or {}).get('login', '?')
        when = (rv.get('submitted_at') or '')[:10]
        state = rv.get('state', '')
        blocks += [f"### {who} · {when} · {state}", '', rv.get('body') or '(no text)', '']
    text = text.rstrip() + '\n\n' + '\n'.join(blocks).rstrip() + '\n'
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        f.write(text)
    os.replace(tmp, path)


def load_index(idx_path):
    """Tolerate empty file (mid-write crash). Skips malformed lines."""
    idx = {}
    if os.path.exists(idx_path):
        with open(idx_path) as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                try:
                    e = json.loads(l)
                except json.JSONDecodeError:
                    continue
                idx[(e['kind'], e['number'])] = e
    return idx


def migrate_legacy_flat(ddir, ch_key, owner_repo, kind, kind_rows):
    """One-time: legacy github_details/{issue|pr}_N.md → ch_key/.

    Pre-channel-aware detail_fetcher.py dumped everything flat under one
    github_details/. This moves each repo's files into its own ch_key
    subdir. No-op once the per-(ch_key, kind) index exists.
    Per-kind migration: legacy rows are split into _index_issue.jsonl and
    _index_pr.jsonl so each kind's incremental fetch has its own cursor.
    """
    legacy_idx = os.path.join(ddir, '_index.jsonl')
    if not os.path.exists(legacy_idx):
        return
    new_ddir = os.path.join(ddir, ch_key)
    new_idx_path = os.path.join(new_ddir, f'_index_{kind}.jsonl')
    if os.path.exists(new_idx_path):
        return
    legacy = []
    with open(legacy_idx) as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            try:
                legacy.append(json.loads(l))
            except json.JSONDecodeError:
                continue
    legacy = [e for e in legacy if e.get('kind') == kind]
    by_num = {r['number']: r for r in kind_rows}
    rows = []
    for e in legacy:
        r = by_num.get(e['number'])
        if not r:
            continue
        m = re.match(r'https://github\.com/([^/]+)/([^/]+)', r.get('url', ''))
        if not m or f'{m.group(1)}/{m.group(2)}' != owner_repo:
            continue
        src_md = os.path.join(ddir, e['file'])
        dst_md = os.path.join(new_ddir, e['file'])
        if os.path.exists(src_md) and not os.path.exists(dst_md):
            os.makedirs(new_ddir, exist_ok=True)
            os.rename(src_md, dst_md)
        rows.append(e)
    if rows:
        os.makedirs(new_ddir, exist_ok=True)
        atomic_write_jsonl(new_idx_path, rows)


def process_repo(owner_repo, ch_key, jsonl_rows, kind, ddir):
    """Fetch per-item detail; append-only on re-runs.

    ddir: SRC-XXX/github_details/{ch_key}/
    Returns {fetched, appended, skipped}.
    """
    # Filter: for issues, only fetch if > 0 comments. PRs always (their
    # conversation lives on the reviews endpoint, comments_count is 0).
    todo = [r for r in jsonl_rows
            if kind != 'issue' or (r.get('comments_count') or 0) > 0]
    if not todo:
        return {'fetched': 0, 'appended': 0, 'skipped': 0}

    os.makedirs(ddir, exist_ok=True)
    idx_path = os.path.join(ddir, f'_index_{kind}.jsonl')
    idx = load_index(idx_path)

    fetched = appended = skipped = 0
    new_idx = []
    now_iso = common.now()
    for i, r in enumerate(todo, 1):
        n = r['number']
        existing = idx.get((kind, n))
        last_cid = (existing or {}).get('last_comment_id') or 0
        last_rid = (existing or {}).get('last_review_id') or 0
        # Hard short-circuit: cursor populated + nothing changed since fetch
        if (existing and existing.get('fetched_at')
                and (r.get('updated_at') or '') <= existing['fetched_at']
                and last_cid and last_rid):
            new_idx.append(existing)
            skipped += 1
            continue

        comments, st_c = fetch_comments(owner_repo, n)
        reviews = []
        if kind == 'pr':
            reviews, _ = fetch_reviews(owner_repo, n)

        # GitHub has no per-issue `since=`; dedupe locally by id
        new_c = [c for c in comments if (c.get('id') or 0) > last_cid]
        new_r = [rv for rv in reviews if (rv.get('id') or 0) > last_rid]

        fn = f'{kind}_{n}.md'
        path = os.path.join(ddir, fn)
        if not existing:
            with open(path, 'w') as f:
                f.write(render(r, comments, reviews))
            fetched += 1
            tag = f'fetched ({len(comments)}c/{len(reviews)}r)'
        elif new_c or new_r:
            append_to_md(path, r, new_c, new_r, len(comments), len(reviews))
            appended += 1
            tag = f'appended +{len(new_c)}c/+{len(new_r)}r'
        else:
            tag = 'no new'
        print(f'  [{ch_key}] {kind} #{n} [{i}/{len(todo)}] {tag}',
              flush=True)

        new_idx.append({
            'number': n, 'kind': kind, 'file': fn,
            'comments': len(comments), 'reviews': len(reviews),
            'status': st_c, 'fetched_at': now_iso,
            'last_comment_id': (max((c.get('id') or 0) for c in comments)
                                if comments else last_cid),
            'last_review_id': (max((rv.get('id') or 0) for rv in reviews)
                               if reviews else last_rid),
        })
    atomic_write_jsonl(idx_path, new_idx)
    return {'fetched': fetched, 'appended': appended, 'skipped': skipped}