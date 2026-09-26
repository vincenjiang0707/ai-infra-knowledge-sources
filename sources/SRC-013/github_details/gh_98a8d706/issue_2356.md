# [Issue #2356] guides(tiered-prefix-cache): duplicate `env` key in lmcache-connector/cpu patch silently discards the HF_TOKEN block

source: https://github.com/llm-d/llm-d/issues/2356
state: closed | updated: 2026-08-31T15:42:57Z
labels: 

## 正文

**Area:** guides / tiered-prefix-cache model server overlay
**Path:** Manifest (Kustomize patch)
**Severity:** medium — the manifest applies cleanly and no linter complains, but half of it is dead. The `HF_TOKEN` block in this patch never reaches the container.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

`guides/tiered-prefix-cache/modelserver/gpu/vllm/lmcache-connector/cpu/base/patch-vllm.yaml` declares the key `env` **twice** inside the same container mapping — at lines 17 and 28. YAML resolves duplicate keys by keeping the last one, so the first `env` block is discarded before the patch is ever applied:

```yaml
          args:
            - "Qwen/Qwen3-32B"
            # ...
          env:                                   # <-- line 17, discarded
            - name: HF_TOKEN
              valueFrom:
                secretKeyRef:
                  name: llm-d-hf-token
                  key: HF_TOKEN
          resources:
            limits:
              memory: 500Gi
            requests:
              memory: 500Gi
          env:                                   # <-- line 28, wins
            - name: LMCACHE_MAX_LOCAL_CPU_SIZE
              value: "100.0"
            - name: PYTHONHASHSEED
              value: "123"
            - name: PROMETHEUS_MULTIPROC_DIR
              value: "/tmp/lmcache_prometheus"
```

The practical impact is contained, because the base at `modelserver/gpu/vllm/base/patch-vllm.yaml` already supplies `HF_TOKEN` and the strategic merge is by element name. So the deployment works — but the patch does not do what it says, and anyone copying this overlay as a template for a base that does *not* supply `HF_TOKEN` gets a pod that cannot pull a gated model, with nothing in the manifest to explain why.

## Repro

1. `git checkout v0.9.0`
2. ```sh
   python3 -c "
   import yaml
   d=yaml.safe_load(open('guides/tiered-prefix-cache/modelserver/gpu/vllm/lmcache-connector/cpu/base/patch-vllm.yaml'))
   env=d['spec']['template']['spec']['containers'][0]['env']
   print([e['name'] for e in env])"
   ```
3. Output is `['LMCACHE_MAX_LOCAL_CPU_SIZE', 'PYTHONHASHSEED', 'PROMETHEUS_MULTIPROC_DIR']` — no `HF_TOKEN`.

Verified as the only occurrence across all 557 YAML files under `guides/` in this tag, so it is an isolated slip rather than a pattern.

## Expected

One `env` key per container mapping, listing all four variables.

## Actual

Two `env` keys; the first is silently dropped by the parser.

## Suggested fix

Merge the two blocks into a single `env` list.

## Scope

Worth a CI guard: a duplicate-key check over `guides/**/*.yaml` is a few lines with `yaml.compose_all` and catches this class of error, which neither `kubectl apply --dry-run` nor a schema validator reports. The existing `docs/ci/kustomize-dry-run.md` job would be a natural home for it.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree, by scanning every manifest for duplicate mapping keys. No secrets in this report.


## 评论 (1)

### varad-ahirwadkar · 2026-08-25

/assign
