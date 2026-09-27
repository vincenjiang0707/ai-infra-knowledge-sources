"""HuggingFace channel: model card / org model list via REST API."""
import json
import os
import re
import time

from . import common

API = 'https://huggingface.co/api'
# full=true + limit>100 → WAF connection drop; ?page= ignored with full=true.
# So: list WITHOUT full=true at limit=1000 (single request, all models),
# then fetch raw README for the top README_CAP by downloads (rate limit 500/300s).
LIST_LIMIT = 1000
README_CAP = 100


def _fetch_readme(repo_id):
    """Raw model card README. Try main then master. None if absent/blocked."""
    for branch in ('main', 'master'):
        code, body = common.fetch_url(
            f'https://huggingface.co/{repo_id}/raw/{branch}/README.md', timeout=30)
        if code == 200 and body and body.strip():
            return body, f'https://huggingface.co/{repo_id}'
    return None, None


def _store_post(d, repo_id, readme):
    """Write posts/<repo_id>.md in blog post format (# title / source: url / body).
    Returns filename if newly written or changed, else None (dedup across runs)."""
    posts_dir = os.path.join(d, 'posts')
    os.makedirs(posts_dir, exist_ok=True)
    fname = repo_id.replace('/', '_') + '.md'
    path = os.path.join(posts_dir, fname)
    page_url = f'https://huggingface.co/{repo_id}'
    text = f'# {repo_id}\n\nsource: {page_url}\n\n{readme}\n'
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
    out = {'type': 'hf', 'url': ch['url']}
    m = re.match(r'https://huggingface\.co/([^/]+)$', url)
    ident = m.group(1) if m else None
    if ident in ('models', 'blog', 'papers', 'discuss', 'docs', 'spaces', 'datasets'):
        # special listing/blog pages: feed discovery or page extract
        from . import site
        site.run(src, ch_key, ch, meta_channels, cursor)
        return

    common.clog(src, ch_key, f"hf {ident}")
    if not ident:
        out.update(status='error', error=f'unparsed HF url {url}')
        meta_channels[ch_key] = out
        return

    parts = []
    # org or user? (overview endpoints occasionally 401 transiently — retry once)
    code, body = common.fetch_url(f'{API}/organizations/{ident}/overview', timeout=20)
    if code == 401:
        time.sleep(2)
        code, body = common.fetch_url(f'{API}/organizations/{ident}/overview', timeout=20)
    kind = 'org' if code == 200 else None
    if not kind:
        code, body = common.fetch_url(f'{API}/users/{ident}/overview', timeout=20)
        if code == 401:
            time.sleep(2)
            code, body = common.fetch_url(f'{API}/users/{ident}/overview', timeout=20)
        kind = 'user' if code == 200 else 'model'

    if kind in ('org', 'user'):
        parts += [f'# HuggingFace {kind}: {ident}', '']
        # full list, single request, no full=true (WAF drops limit>100 with it)
        mcode, mbody = common.fetch_url(
            f'{API}/models?author={ident}&limit={LIST_LIMIT}', timeout=60)
        if mcode == 401:  # transient — one retry
            time.sleep(2)
            mcode, mbody = common.fetch_url(
                f'{API}/models?author={ident}&limit={LIST_LIMIT}', timeout=60)
        models = json.loads(mbody) if mcode == 200 and mbody else []
        if mcode != 200:
            out.update(status='blocked' if mcode in common.BLOCKED_HTTP else 'error',
                       http_code=mcode)
            meta_channels[ch_key] = out
            return
        parts += [f'models listed: {len(models)}', '']
        cursor[f'{ch_key}:models'] = {'count': len(models)}
        posts_written = []
        for mo in models:
            repo_id = mo.get('id')
            parts += [f"## {repo_id}",
                      f"- downloads: {mo.get('downloads')}",
                      f"- likes: {mo.get('likes')}",
                      f"- pipeline: {mo.get('pipeline_tag')}",
                      f"- lastModified: {mo.get('lastModified')}",
                      f"- url: https://huggingface.co/{repo_id}", '']
            card = (mo.get('cardData') or {})
            if card:
                keep = {k: card[k] for k in ('license', 'library_name', 'tags',
                                             'base_model', 'model_type') if k in card}
                if keep:
                    parts += [f"card: {json.dumps(keep, ensure_ascii=False)}", '']
        # model card bodies -> posts/<repo>.md, top README_CAP by downloads
        # (big orgs have hundreds of derivative quant uploads; only majors carry signal)
        top = sorted(models, key=lambda m: m.get('downloads') or 0, reverse=True)[:README_CAP]
        for mo in top:
            repo_id = mo.get('id')
            readme, _ = _fetch_readme(repo_id)
            if readme:
                fn = _store_post(d, repo_id, readme)
                if fn:
                    posts_written.append(fn)
            else:
                common.clog(src, ch_key, f"hf readme missing: {repo_id}")
        out.update(kind=kind, models=len(models), posts=posts_written)
        if posts_written:
            cursor[f'{ch_key}:readme_posts'] = {'count': len(posts_written)}
    else:
        # single model card
        mcode, mbody = common.fetch_url(f'{API}/models/{ident}', timeout=30)
        if mcode != 200 or not mbody:
            out.update(status='blocked' if mcode in common.BLOCKED_HTTP else 'error',
                       http_code=mcode)
            meta_channels[ch_key] = out
            return
        mo = json.loads(mbody)
        parts += [f"# HuggingFace model: {ident}", '',
                  f"- downloads: {mo.get('downloads')}",
                  f"- likes: {mo.get('likes')}",
                  f"- lastModified: {mo.get('lastModified')}", '',
                  mo.get('description') or '', '']
        posts_written = []
        readme, _ = _fetch_readme(ident)
        if readme:
            fn = _store_post(d, ident, readme)
            if fn:
                posts_written.append(fn)
        out.update(kind='model', posts=posts_written)

    fn = 'hf.md'
    with open(os.path.join(d, fn), 'w') as f:
        f.write('\n'.join(str(p) for p in parts))
    out.update(status='ok', output=fn)
    common.clog(src, ch_key, f"hf {out.get('kind', '')} -> ok")
    meta_channels[ch_key] = out
