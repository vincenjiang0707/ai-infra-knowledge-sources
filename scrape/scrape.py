#!/usr/bin/env python3
"""Entry: parse _registry.json, dispatch SRC channels, 2-way concurrency.

Usage:
  python3 scrape.py                     # all sources, incremental
  python3 scrape.py SRC-003 SRC-140     # specific sources
  python3 scrape.py --retry-blocked     # also retry blocked/not_fetched
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scrapers import HANDLERS
from scrapers import common


def process(src, retry_blocked=False):
    src_id = src['src_id']
    t0 = time.time()
    meta = common.load_meta(src_id) or {}
    prev_status = meta.get('status')

    # incremental skip: blocked/not_fetched stay skipped; success re-runs so
    # channels do cheap head-checks (newest item already local → short-circuit,
    # see blog/site/github head-check paths). Sitemap/menu use their cursors.
    if prev_status in ('blocked', 'not_fetched') and not retry_blocked:
        return {'src_id': src_id, 'status': prev_status, 'skipped': True,
                'new_posts': 0, 'head_check': False,
                'total_posts': _count_disk_posts(src_id)}

    meta_channels = {}
    cursor = dict(meta.get('cursor') or {})  # seed with previous cursor so handlers can head-check
    if src.get('blocked_reason'):
        # PDF pre-flagged: no network request
        meta_channels['pdf_flag'] = {'type': 'none', 'status': 'blocked',
                                     'reason': src['blocked_reason']}
    else:
        for ch_key, ch in (src.get('channels') or {}).items():
            handler = HANDLERS.get(ch['type'])
            if not handler:
                meta_channels[ch_key] = {'type': ch['type'], 'status': 'error',
                                         'error': f'no handler for {ch["type"]}'}
                continue
            try:
                handler(src, ch_key, ch, meta_channels, cursor)
            except Exception as e:
                meta_channels[ch_key] = {'type': ch['type'], 'status': 'error',
                                         'error': repr(e)[:300]}

    meta.update({
        'src_id': src_id,
        'name': src.get('name', ''),
        'category': src.get('category', ''),
        'priority': src.get('priority', ''),
        'scrape_type': src.get('scrape_type', ''),
        'blocked_reason': src.get('blocked_reason'),
        'status': common.combine_status(meta_channels),
        'started_at': meta.get('started_at') or common.now(),
        'finished_at': common.now(),
        'duration_seconds': round(time.time() - t0, 1),
        'attempts': meta.get('attempts', 0) + 1,
        'channels': meta_channels,
        'cursor': {**meta.get('cursor', {}), **cursor},
        'notes': meta.get('notes', ''),
    })
    common.save_meta(src_id, meta)
    new_posts = _new_content(meta_channels)
    return {'src_id': src_id, 'status': meta['status'],
            'duration': meta['duration_seconds'], 'skipped': False,
            'new_posts': new_posts,
            'head_check': any(c.get('head_check') == 'no_update'
                              for c in meta_channels.values()),
            'total_posts': _count_disk_posts(src_id)}


def _count_disk_posts(src_id):
    """Recursive .md count under posts/ (top level + tab subdirs)."""
    d = os.path.join(common.ROOT, 'sources', src_id, 'posts')
    if not os.path.isdir(d):
        return 0
    return sum(len([f for f in fns if f.endswith('.md')])
               for _r, _d, fns in os.walk(d))


def _new_content(meta_channels):
    """Count content items written by THIS run across channel types."""
    n = 0
    for c in meta_channels.values():
        n += len(c.get('posts') or [])      # blog: files written this run
        n += c.get('posts_fetched') or 0    # rss
        n += c.get('pages_fetched') or 0    # sitemap / menu
    return n


def _outcome(r):
    """Classify a per-SRC run result: new | no_update | failed | skipped."""
    if r.get('skipped'):
        return 'skipped'
    if r.get('status') in ('error', 'blocked', 'not_fetched'):
        return 'failed'
    if r.get('new_posts', 0) > 0:
        return 'new'
    return 'no_update'


def _write_run_log(results, registry_size, scope):
    """Persist per-run report: _runs/RUN-<ts>.json + history.jsonl line."""
    run_id = common.now()
    for r in results:
        r['outcome'] = _outcome(r)
    by = {}
    for r in results:
        by[r['outcome']] = by.get(r['outcome'], 0) + 1
    run_log = {
        'run_id': run_id,
        'scope': scope or 'all',
        'registry_size': registry_size,
        'srcs_ran': len(results),
        'summary': {
            'new_posts_total': sum(r.get('new_posts', 0) for r in results),
            **{f'srcs_{k}': v for k, v in by.items()},
        },
        'srcs': sorted(results, key=lambda r: r['src_id']),
    }
    runs_dir = os.path.join(common.ROOT, '_runs')
    os.makedirs(runs_dir, exist_ok=True)
    fname = 'RUN-' + run_id.replace('-', '').replace(':', '') + '.json'
    with open(os.path.join(runs_dir, fname), 'w') as f:
        json.dump(run_log, f, ensure_ascii=False, indent=1)
    with open(os.path.join(runs_dir, 'history.jsonl'), 'a') as f:
        f.write(json.dumps({'run_id': run_id, 'scope': run_log['scope'],
                            **run_log['summary']}, ensure_ascii=False) + '\n')
    _merge_day_log(runs_dir, run_id[:10], run_log)
    return run_log


def _merge_day_log(runs_dir, day, run_log):
    """Fold this run into the day file: same-day runs merge per SRC —
    new_posts accumulate, latest status/outcome wins, newest total_posts kept."""
    day_path = os.path.join(runs_dir, f'DAY-{day}.json')
    day_log = {'day': day, 'runs': [], 'srcs': {}}
    if os.path.exists(day_path):
        try:
            day_log = json.load(open(day_path))
        except Exception:
            pass
    day_log['runs'].append(run_log['run_id'])
    srcs = day_log['srcs']
    for r in run_log['srcs']:
        sid = r['src_id']
        if sid in srcs:
            old = srcs[sid]
            old['new_posts'] = old.get('new_posts', 0) + r.get('new_posts', 0)
            old['head_check'] = old.get('head_check') or r.get('head_check')
            # latest-run fields win (run order = insertion order in results)
            old.update({k: v for k, v in r.items()
                        if k not in ('new_posts', 'head_check')})
        else:
            srcs[sid] = dict(r)
    # re-classify: any accumulated new_posts during the day => 'new'
    for s in srcs.values():
        s['outcome'] = 'new' if s.get('new_posts', 0) > 0 and \
            s.get('status') not in ('error', 'blocked', 'not_fetched') \
            else _outcome(s)
    by = {}
    for s in srcs.values():
        by[s['outcome']] = by.get(s['outcome'], 0) + 1
    day_log['summary'] = {
        'new_posts_total': sum(s.get('new_posts', 0) for s in srcs.values()),
        **{f'srcs_{k}': v for k, v in by.items()},
    }
    with open(day_path, 'w') as f:
        json.dump(day_log, f, ensure_ascii=False, indent=1)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    retry_blocked = '--retry-blocked' in sys.argv
    reg_path = os.path.join(common.ROOT, '_registry.json')
    with open(reg_path) as f:
        registry = json.load(f)

    if args:
        want = {a.upper() for a in args}
        registry = [s for s in registry if s['src_id'] in want]
        missing = want - {s['src_id'] for s in registry}
        if missing:
            print(f'unknown: {sorted(missing)}')
            sys.exit(1)

    # simple first: github single-channel, then multi-channel, then rest
    def order(s):
        n_ch = len(s.get('channels') or {})
        is_gh = s.get('scrape_type') == 'github_repo'
        return (0 if is_gh and n_ch == 1 else 1 if is_gh else 2, n_ch)
    registry.sort(key=order)

    results = []
    with ThreadPoolExecutor(max_workers=2) as ex:
        futs = {ex.submit(process, s, retry_blocked): s for s in registry}
        for fut in as_completed(futs):
            r = fut.result()
            results.append(r)
            skip = ' (skip)' if r.get('skipped') else ''
            dur = r.get('duration')
            print(f"{r['src_id']}: {r['status']}{skip} {dur}s" if dur else
                  f"{r['src_id']}: {r['status']}{skip}", flush=True)

    from collections import Counter
    print('\n' + json.dumps(dict(Counter(r['status'] for r in results)), ensure_ascii=False))
    run_log = _write_run_log(results, len(registry), ' '.join(args) or 'all')
    s = run_log['summary']
    print(f"run log: _runs/RUN-{run_log['run_id'].replace('-', '').replace(':', '')}.json"
          f" (day: _runs/DAY-{run_log['run_id'][:10]}.json)")
    print(f"new posts: {s['new_posts_total']} | "
          f"srcs new: {s.get('srcs_new', 0)} / "
          f"no_update: {s.get('srcs_no_update', 0)} / "
          f"failed: {s.get('srcs_failed', 0)} / "
          f"skipped: {s.get('srcs_skipped', 0)}")
    for r in run_log['srcs']:
        if r['outcome'] == 'new':
            print(f"  +{r['new_posts']:>3} {r['src_id']}")


if __name__ == '__main__':
    main()
