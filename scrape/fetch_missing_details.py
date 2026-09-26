#!/usr/bin/env python3
"""遍历含 github 链接但无 github_details/ 子目录的 SRC,调用主流程抓 detail。

主流程 scrape.py 已通过 _run_detail 自动接入 detail 抓取,无需单独跑
detail_fetcher.py。首次接入会一次性消耗 API(每个 issue 1 call + 每个
PR 2 calls),之后增量只追新评论。

用法:
    python3 scrape/fetch_missing_details.py                # 全量扫描
    python3 scrape/fetch_missing_details.py SRC-028 SRC-029  # 指定 SRC
    python3 scrape/fetch_missing_details.py --limit 10     # 限 N 个
    python3 scrape/fetch_missing_details.py --dry-run      # 只列出,不跑
"""
import argparse
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRAPE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scrape.py')


def find_missing():
    """SRC 列表 = 含 github_repo 通道 且 完全无 github_details/ 子目录
    且 gh 通道从未成功跑过 (meta 中 issues.status=ok 视为已成功 —
    避免 issues/pulls count=0 的仓库因无目录而每批重跑)."""
    src_dir = os.path.join(ROOT, 'sources')
    missing = []
    for sid in sorted(os.listdir(src_dir)):
        meta = os.path.join(src_dir, sid, '_meta.json')
        if not os.path.exists(meta):
            continue
        m = json.load(open(meta))
        gh = [(k, v) for k, v in m.get('channels', {}).items()
              if v.get('type') == 'github_repo']
        if not gh:
            continue
        # 有顶层 github_details/ 目录 → 已完成
        if os.path.isdir(os.path.join(src_dir, sid, 'github_details')):
            continue
        # 无目录但所有 gh 通道 issues.status=ok (含 count=0) → 已成功, 跳过
        if all(v.get('issues', {}).get('status') == 'ok' for _, v in gh):
            continue
        missing.append(sid)
    return missing


def detail_state(sid):
    """当前 SRC 中哪些 gh 通道已有 / 缺 detail 子目录."""
    src_dir = os.path.join(ROOT, 'sources', sid)
    meta = os.path.join(src_dir, '_meta.json')
    if not os.path.exists(meta):
        return None
    m = json.load(open(meta))
    chs = [(k, v.get('url', '')) for k, v in m.get('channels', {}).items()
           if v.get('type') == 'github_repo' and v.get('url')]
    return [(k, os.path.isdir(os.path.join(src_dir, 'github_details', k))) for k, _ in chs]


def run_one(sid):
    t0 = time.time()
    try:
        r = subprocess.run(
            [sys.executable, '-u', SCRAPE, sid],
            capture_output=True, text=True, timeout=900,
        )
        dt = round(time.time() - t0, 1)
        return (r.returncode == 0, dt,
                (r.stdout or '')[-500:],
                (r.stderr or '')[-500:])
    except subprocess.TimeoutExpired:
        return False, 900.0, '', 'timeout 900s'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('srcs', nargs='*', help='指定 SRC;不传 = 扫描所有缺失')
    ap.add_argument('--limit', type=int, default=0, help='最多跑 N 个 (0=全部)')
    ap.add_argument('--dry-run', action='store_true', help='只列出,不调 scrape.py')
    ap.add_argument('--force', action='store_true',
                    help='先删 SRC 下的 github_details/ 子目录(强制 detail 重抓)')
    args = ap.parse_args()

    sids = args.srcs or find_missing()
    if args.limit:
        sids = sids[:args.limit]

    print(f'target: {len(sids)} SRCs', flush=True)
    if args.dry_run:
        for s in sids:
            print(f'  {s}', flush=True)
        return

    success = failed = empty = 0
    for i, sid in enumerate(sids, 1):
        before = detail_state(sid) or []
        if args.force:
            # wipe existing detail dirs so detail_missing=True forces refresh
            import shutil
            ddir = os.path.join(ROOT, 'sources', sid, 'github_details')
            if os.path.isdir(ddir):
                shutil.rmtree(ddir)
                print(f'  wiped {ddir}', flush=True)
            before = detail_state(sid) or []
        print(f'[{i}/{len(sids)}] {sid} ...', flush=True)
        ok, dt, out, err = run_one(sid)
        after = detail_state(sid) or []
        new_dirs = sum(1 for (k1, b), (k2, a) in zip(before, after) if not b and a)
        flag = 'OK' if ok else 'FAIL'
        detail_msg = f' detail: +{new_dirs} dir' if new_dirs else (' detail: NONE' if ok else '')
        print(f'  [{flag}] {dt}s{detail_msg}', flush=True)
        if err.strip():
            print(f'  err: {err.strip()[-200:]}', flush=True)
        if ok and new_dirs == 0:
            empty += 1
        elif ok:
            success += 1
        else:
            failed += 1

    print(f'\ntotal: {success} ok (with detail), {empty} ok-but-no-detail, {failed} fail',
          flush=True)


if __name__ == '__main__':
    main()