# [Issue #2353] guides: CRD installer reads `GATEWAY_API_INFERENCE_EXTENSION_VERSION` while env.sh and the guides export `GAIE_VERSION`

source: https://github.com/llm-d/llm-d/issues/2353
state: open | updated: 2026-08-23T16:41:31Z
labels: 

## 正文

**Area:** guides / gateway CRD installation
**Path:** CLI (helper script) + Docs
**Severity:** medium — the default works, so this is invisible until someone pins a different GAIE version. Then they get v1.5.0 installed while believing they installed what they asked for.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

There are two different environment variable names for "which Gateway API Inference Extension version to install", and the one the guides tell you to export is not the one the installer script reads.

- `guides/env.sh:16` exports **`GAIE_VERSION`** (default `v1.5.0`) and derives `GAIE_URL` from it. This is the variable every guide sources and references.
- `guides/recipes/gateway/install-gateway-crds.sh:45` reads **`GATEWAY_API_INFERENCE_EXTENSION_VERSION`** (default `v1.5.0`).

Because both defaults are `v1.5.0`, the mismatch is silent today. Override `GAIE_VERSION` to test a different GAIE release and the script still installs `v1.5.0`, with no warning.

## Repro

1. `git checkout v0.9.0`
2. `grep -n 'GAIE_VERSION' guides/env.sh` → `export GAIE_VERSION=${GAIE_VERSION:-v1.5.0}`
3. `grep -n 'INFERENCE_EXTENSION_VERSION' guides/recipes/gateway/install-gateway-crds.sh` →
   `GATEWAY_API_INFERENCE_EXTENSION_VERSION=${GATEWAY_API_INFERENCE_EXTENSION_VERSION:-"v1.5.0"}`
4. Follow any guide's prerequisites, `export GAIE_VERSION=v1.4.0`, then run the CRD installer script.
5. The applied manifest URL still contains `v1.5.0`.

## Expected

One variable name decides the installed GAIE version, and it is the one the guides document.

## Actual

Two names for the same setting. The documented one has no effect on the script.

## Probable root cause

`env.sh` introduced the short `GAIE_VERSION` alias later; the recipe script kept the original long name and was never reconciled.

## Suggested fix

In `guides/recipes/gateway/install-gateway-crds.sh`, honour the shorter name with the long one as fallback:

```sh
GATEWAY_API_INFERENCE_EXTENSION_VERSION=${GAIE_VERSION:-${GATEWAY_API_INFERENCE_EXTENSION_VERSION:-"v1.5.0"}}
```

Same consideration applies to `GATEWAY_API_VERSION`, which happens to match by name today.

## Scope

`docs/infrastructure/gateway/install-crds.md` sets `GAIE_VERSION=v1.5.0` locally and builds the URL by hand, so it is internally consistent — but it teaches the name that the script ignores.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree and cross-checking documented environment variables against the scripts that consume them. No secrets in this report.


## 评论 (1)

### AniketR10 · 2026-08-23

@paulohenriquevn  would like to work on this please assign, thanks!
