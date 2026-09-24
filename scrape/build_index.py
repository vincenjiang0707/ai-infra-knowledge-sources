"""Build static index.html + _index.json for knowledge-sources/.

Reads _registry.json + sources/*/_meta.json + sources/*/<subdirs>/ to produce:
  - index.html      (human-browseable directory, collapsible tree, L1/L2/L3)
  - _index.json     (machine-readable SRC + file map, for skills)

Grouping: primary = category, with status filter (top toggle).
Layers: L1 category list -> L2 SRC list -> L3 SRC sub-file list -> L4 .md links.
Idempotent. Run manually: python3 scrape/build_index.py [--regen].
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


# ---------- filesystem scan ----------

# subdirs + file-globs we surface at L3 per channel type
SUB_FILE_MAP = {
    'github_repo': [
        ('github_repo.md', 'README'),
        ('github_issues.jsonl', 'issues.jsonl'),
        ('github_pulls.jsonl', 'pulls.jsonl'),
        ('github_releases.jsonl', 'releases.jsonl'),
        ('github_changelog.md', 'CHANGELOG'),
        ('github_details/', 'details/'),
    ],
    'site_sitemap': [
        ('pages/', 'pages/'),
    ],
    'site_menu': [
        ('pages/', 'pages/'),
    ],
    'blog': [
        ('feed_meta.json', 'feed_meta'),
        ('page.md', 'index.md'),
        ('posts/', 'posts/'),
    ],
    'rss': [
        ('feed_meta.json', 'feed_meta'),
        ('posts/', 'posts/'),
    ],
    'hf': [
        ('hf.md', 'overview'),
    ],
    'js': [
        ('page.md', 'index.md'),
    ],
    'reference': [],  # no fetch
    'academic': [
        ('page.md', 'paper'),
    ],
    'blocked': [],
}


def scan_src(src_id, registry_entry):
    """Return dict: {src_id, status, subdir, files:[relpath, label]}."""
    d = os.path.join(ROOT, 'sources', src_id)
    files = []
    if os.path.isdir(d):
        for name in sorted(os.listdir(d)):
            full = os.path.join(d, name)
            if os.path.isfile(full):
                files.append((f'{name}', name))
            elif os.path.isdir(full):
                # surface as dir entry (click to list)
                sub_listing = sorted(os.listdir(full))
                if sub_listing:
                    files.append((f'{name}/', f'{name}/ ({len(sub_listing)} files)'))
    return {
        'src_id': src_id,
        'status': registry_entry.get('status', 'unknown'),
        'files': files,
    }


# ---------- builders ----------

CSS = """
:root {
  --bg: #fafafa;
  --fg: #1a1a1a;
  --muted: #777;
  --line: #e5e5e5;
  --accent: #2563eb;
  --ok: #16a34a;
  --partial: #d97706;
  --blocked: #dc2626;
  --code-bg: #f4f4f5;
}
* { box-sizing: border-box; }
body { font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
       color: var(--fg); background: var(--bg); margin: 0; padding: 24px 32px; max-width: 1200px; }
header { border-bottom: 1px solid var(--line); padding-bottom: 16px; margin-bottom: 16px; }
h1 { margin: 0 0 4px; font-size: 22px; }
.meta { color: var(--muted); font-size: 12px; }
.controls { margin: 12px 0; display: flex; gap: 8px; flex-wrap: wrap; }
.controls button { font: inherit; padding: 4px 10px; border: 1px solid var(--line);
                   background: #fff; cursor: pointer; border-radius: 4px; }
.controls button.active { background: var(--accent); color: #fff; border-color: var(--accent); }
.category { margin: 16px 0 8px; padding: 8px 0; border-top: 1px solid var(--line); }
.category h2 { margin: 0 0 8px; font-size: 15px; cursor: pointer; user-select: none; }
.category h2::before { content: "▸ "; color: var(--muted); transition: transform .1s; display: inline-block; }
.category.open h2::before { content: "▾ "; }
.src-list { display: none; padding-left: 12px; }
.category.open .src-list { display: block; }
.src-row { padding: 6px 8px; border-left: 3px solid transparent; margin: 2px 0; }
.src-row:hover { background: #f0f0f0; }
.src-row details { margin-top: 4px; }
.src-row summary { cursor: pointer; list-style: none; }
.src-row summary::-webkit-details-marker { display: none; }
.src-row summary::before { content: "▸ "; color: var(--muted); display: inline-block; width: 14px; }
.src-row details[open] summary::before { content: "▾ "; }
.src-name { font-weight: 500; }
.src-id { color: var(--muted); font-family: ui-monospace, SFMono-Regular, monospace; font-size: 12px; margin-left: 6px; }
.src-url { color: var(--muted); font-size: 11px; margin-left: 8px; word-break: break-all; }
.badge { display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px;
         text-transform: uppercase; margin-left: 6px; vertical-align: middle; }
.badge.success { background: #dcfce7; color: var(--ok); }
.badge.partial { background: #fef3c7; color: var(--partial); }
.badge.blocked { background: #fee2e2; color: var(--blocked); }
.badge.not_fetched { background: #f3f4f6; color: var(--muted); }
.file-list { padding: 4px 0 4px 20px; font-size: 12px; }
.file-list a { color: var(--accent); text-decoration: none; margin-right: 12px; }
.file-list a:hover { text-decoration: underline; }
.dim { opacity: .35; pointer-events: none; }
footer { margin-top: 32px; padding-top: 16px; border-top: 1px solid var(--line);
         color: var(--muted); font-size: 11px; }
code { background: var(--code-bg); padding: 1px 4px; border-radius: 3px; font-size: 12px; }
"""


def render_html(registry, file_map):
    """registry: list of dicts; file_map: {src_id: scan_src dict}."""
    # group by category, preserve order of first appearance
    by_cat = defaultdict(list)
    cat_order = []
    for r in registry:
        c = r.get('category') or '未分类'
        if c not in by_cat:
            cat_order.append(c)
        by_cat[c].append(r)

    counts = defaultdict(int)
    for r in registry:
        counts[r.get('status', 'unknown')] += 1

    out = []
    out.append('<!doctype html>')
    out.append('<html lang="zh-CN">')
    out.append('<head>')
    out.append('<meta charset="utf-8">')
    out.append('<title>AI Infra Knowledge Sources — 索引</title>')
    out.append(f'<style>{CSS}</style>')
    out.append('</head><body>')
    out.append('<header>')
    out.append('<h1>AI Infra Knowledge Sources — 索引</h1>')
    out.append('<div class="meta">')
    out.append(f'共 {len(registry)} 个来源 · 抓取快照 {now()} · ')
    out.append(f'success {counts.get("success", 0)} / partial {counts.get("partial", 0)} / blocked {counts.get("blocked", 0)} / 其他 {counts.get("not_fetched", 0)}')
    out.append('</div>')
    # status filter
    out.append('<div class="controls" id="status-filter">')
    out.append('<button data-status="all" class="active">全部</button>')
    for s in ('success', 'partial', 'blocked', 'not_fetched'):
        out.append(f'<button data-status="{s}">{s} ({counts.get(s, 0)})</button>')
    out.append('</div>')
    out.append('</header>')

    # categories
    for cat in cat_order:
        items = by_cat[cat]
        out.append(f'<div class="category open" data-cat="{escape(cat)}">')
        out.append(f'<h2>{escape(cat)} <span class="meta">({len(items)})</span></h2>')
        out.append('<div class="src-list">')
        for r in items:
            sid = r['src_id']
            sc = file_map.get(sid, {'files': []})
            files = sc['files']
            status = r.get('status', 'unknown')
            url = ''
            chs = r.get('channels') or {}
            if chs:
                first_ch = next(iter(chs.values()))
                url = first_ch.get('url', '')
            out.append(f'<div class="src-row" data-status="{status}">')
            out.append('<details>')
            name = escape(r.get('name') or sid)
            out.append(f'<summary><span class="src-name">{name}</span>')
            out.append(f'<span class="src-id">{sid}</span>')
            out.append(f'<span class="badge {status}">{status}</span>')
            if url:
                out.append(f'<a class="src-url" href="{escape(url)}" target="_blank" rel="noopener">{escape(url)}</a>')
            out.append('</summary>')
            # L3 sub-file list (scan_src already includes _meta.json if present)
            if files:
                out.append('<div class="file-list">')
                for rel, label in files:
                    href = f'./sources/{sid}/{rel}'
                    out.append(f'<a href="{escape(href)}">{escape(label)}</a>')
                out.append('</div>')
            else:
                out.append('<div class="file-list meta">（无子文件 / blocked）</div>')
            out.append('</details>')
            out.append('</div>')
        out.append('</div>')  # src-list
        out.append('</div>')  # category

    out.append('<footer>')
    out.append('静态生成 · 不抓原网 · 内容版权见各原链接 · 生成时间 ' + now())
    out.append('</footer>')

    # JS: status filter + category toggle
    js = """
<script>
(function(){
  // category toggle
  document.querySelectorAll('.category h2').forEach(h=>{
    h.addEventListener('click',()=>h.parentElement.classList.toggle('open'));
  });
  // status filter
  const btns=document.querySelectorAll('#status-filter button');
  btns.forEach(b=>b.addEventListener('click',()=>{
    btns.forEach(x=>x.classList.remove('active'));
    b.classList.add('active');
    const s=b.dataset.status;
    document.querySelectorAll('.src-row').forEach(r=>{
      r.classList.toggle('dim', s!=='all' && r.dataset.status!==s);
    });
  }));
})();
</script>
"""
    out.append(js)
    out.append('</body></html>')
    return '\n'.join(out)


def build_index_json(registry, file_map):
    """Machine-readable: minimal SRC + file map for skills."""
    out = []
    for r in registry:
        sid = r['src_id']
        sc = file_map.get(sid, {'files': []})
        chs = r.get('channels') or {}
        url = ''
        ch_type = ''
        if chs:
            first_ch = next(iter(chs.values()))
            url = first_ch.get('url', '')
            ch_type = first_ch.get('type', '')
        out.append({
            'src_id': sid,
            'name': r.get('name') or sid,
            'category': r.get('category') or '未分类',
            'status': r.get('status', 'unknown'),
            'scrape_type': r.get('scrape_type', ''),
            'channel_type': ch_type,
            'url': url,
            'files': [{'path': f'sources/{sid}/{rel}', 'label': lbl} for rel, lbl in sc['files']],
            '_meta': f'sources/{sid}/_meta.json',
        })
    return {
        'generated_at': now(),
        'source_count': len(out),
        'sources': out,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--regen', action='store_true', help='force rebuild even if exists')
    args = ap.parse_args()

    reg_path = os.path.join(ROOT, '_registry.json')
    if not os.path.exists(reg_path):
        print(f'ERR: _registry.json not found at {reg_path}', file=sys.stderr)
        sys.exit(1)
    with open(reg_path) as f:
        registry = json.load(f)

    file_map = {r['src_id']: scan_src(r['src_id'], r) for r in registry}

    html = render_html(registry, file_map)
    html_path = os.path.join(ROOT, 'index.html')
    with open(html_path, 'w') as f:
        f.write(html)
    print(f'wrote {html_path} ({len(html)} bytes)')

    idx = build_index_json(registry, file_map)
    idx_path = os.path.join(ROOT, '_index.json')
    with open(idx_path, 'w') as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)
    print(f'wrote {idx_path} ({len(file_map)} sources)')


if __name__ == '__main__':
    main()