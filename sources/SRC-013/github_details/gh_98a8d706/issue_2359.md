# [Issue #2359] docs(README): version badge still says 0.8 at the v0.9.0 tag, and "four core themes" introduces five bullets

source: https://github.com/llm-d/llm-d/issues/2359
state: closed | updated: 2026-09-11T16:38:37Z
labels: 

## 正文

**Area:** repository README
**Path:** Docs
**Severity:** low — cosmetic, but it is the first page anyone reads, and the version badge is the fastest way to answer "what is the current release?"
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

Two small inconsistencies in `README.md` at the v0.9.0 tag:

1. **Version badge is a release behind.** Line 14 renders `Version-0.8`:
   ```markdown
   [![Release Status](https://img.shields.io/badge/Version-0.8-yellow)](https://github.com/llm-d/llm-d/releases)
   ```
   A visitor landing on the default branch after the 0.9.0 cut reads 0.8 as the current version.

2. **"four core themes" introduces five bullets.** Line 24 says "Our offerings are organized into four core themes:" and the list that follows has five entries: Intelligent Routing, Advanced KV-Cache Management, Serving Large Models, Operational Excellence, and Batch Processing.

## Repro

1. `git checkout v0.9.0`
2. `grep -n 'Version-0.8\|four core themes' README.md`
3. `grep -c '^\* \*\*\[' README.md` → `5`

## Expected

The badge tracks the current release, and the count matches the list.

## Actual

Badge says 0.8 at the 0.9.0 tag; the sentence says four and the list has five.

## Suggested fix

Either change the count to five, or drop the number ("Our offerings are organized into the following themes:") so the sentence stops going stale each time a theme is added. For the badge, the shields.io endpoint can read the latest release automatically:

```markdown
[![Release Status](https://img.shields.io/github/v/release/llm-d/llm-d?label=Version)](https://github.com/llm-d/llm-d/releases)
```

which removes this from the release checklist entirely.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree. No secrets in this report.


## 评论 (1)

### oforiwaasam · 2026-08-24

/assign
