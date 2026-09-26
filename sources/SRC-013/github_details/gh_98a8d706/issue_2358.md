# [Issue #2358] docs(well-lit-paths): optimized-baseline links observability references with one `../` too few (dead links)

source: https://github.com/llm-d/llm-d/issues/2358
state: closed | updated: 2026-08-24T14:26:56Z
labels: 

## 正文

**Area:** docs / well-lit-paths (optimized-baseline)
**Path:** Docs
**Severity:** low — two dead links on the entry-point guide of the recommended path. They point readers looking for observability at a directory that does not exist.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

`docs/well-lit-paths/foundations/optimized-baseline.md:46` links the shared PromQL and metrics references with one `../` too few:

```markdown
backed by the shared [PromQL](../operations/observability/promql.md) and
[metric](../operations/observability/metrics.md) references.
```

From `docs/well-lit-paths/foundations/`, `../operations/` resolves to `docs/well-lit-paths/operations/`, which does not exist. The targets live at `docs/operations/observability/`.

`pd-disaggregation.md:48`, in the same directory and in the same sentence pattern, gets it right:

```markdown
backed by the shared [PromQL](../../operations/observability/promql.md#prefilldecode-disaggregation) and
[metric](../../operations/observability/metrics.md) references.
```

## Repro

1. `git checkout v0.9.0`
2. `grep -n 'operations/observability' docs/well-lit-paths/foundations/optimized-baseline.md docs/well-lit-paths/foundations/pd-disaggregation.md`
3. `ls docs/well-lit-paths/operations/` → no such directory.

## Expected

Both links resolve to `docs/operations/observability/`.

## Actual

Both 404 on the site and fail to resolve in the repo.

## Suggested fix

Change `../operations/observability/` to `../../operations/observability/` on line 46, matching the sibling page.

## Scope

A relative-link checker over `docs/**` in CI would catch this class of error. The repo already runs a link checker for the website (`link-checker.config.json.example` in `llm-d.github.io`), so extending it to relative links in the source tree may be enough.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree; every internal link was resolved against the tree. No secrets in this report.


## 评论 (1)

### varad-ahirwadkar · 2026-08-24

/assign
