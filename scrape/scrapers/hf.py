"""HuggingFace channel: model card / org model list via REST API."""
import json
import os
import re

from . import common

API = 'https://huggingface.co/api'
ORG_MODEL_CAP = 200


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

    if not ident:
        out.update(status='error', error=f'unparsed HF url {url}')
        meta_channels[ch_key] = out
        return

    parts = []
    # org or user?
    code, body = common.fetch_url(f'{API}/organizations/{ident}/overview', timeout=20)
    kind = 'org' if code == 200 else None
    if not kind:
        code, body = common.fetch_url(f'{API}/users/{ident}/overview', timeout=20)
        kind = 'user' if code == 200 else 'model'

    if kind in ('org', 'user'):
        parts += [f'# HuggingFace {kind}: {ident}', '']
        # model list
        mcode, mbody = common.fetch_url(
            f'{API}/models?author={ident}&limit={ORG_MODEL_CAP}&full=true', timeout=60)
        models = json.loads(mbody) if mcode == 200 and mbody else []
        parts += [f'models listed: {len(models)}', '']
        cursor[f'{ch_key}:models'] = {'count': len(models)}
        for mo in models:
            parts += [f"## {mo.get('id')}",
                      f"- downloads: {mo.get('downloads')}",
                      f"- likes: {mo.get('likes')}",
                      f"- pipeline: {mo.get('pipeline_tag')}",
                      f"- lastModified: {mo.get('lastModified')}",
                      f"- url: https://huggingface.co/{mo.get('id')}", '']
            card = (mo.get('cardData') or {})
            if card:
                keep = {k: card[k] for k in ('license', 'library_name', 'tags',
                                             'base_model', 'model_type') if k in card}
                if keep:
                    parts += [f"card: {json.dumps(keep, ensure_ascii=False)}", '']
        out.update(kind=kind, models=len(models))
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
        out.update(kind='model')

    fn = 'hf.md'
    with open(os.path.join(d, fn), 'w') as f:
        f.write('\n'.join(str(p) for p in parts))
    out.update(status='ok', output=fn)
    meta_channels[ch_key] = out
