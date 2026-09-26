# [Issue #3962] [Proposal] OpenEval Import/Export Support

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3962
state: closed | updated: 2026-08-21T06:56:21Z
labels: 

## 正文

## Overview

We have launched [OpenEval](https://github.com/adhabnr-ux/openeval) (v1.0.0-rc.1), an open standard (Apache 2.0) for portable LLM evaluation datasets. Every eval framework uses incompatible formats — OpenEval provides a standard JSON format + converters + SDKs (TypeScript + Python).

## What We're Proposing

Add `to_openeval()` and `from_openeval()` methods (~50-100 lines using our SDK).

## Resources

- **Spec:** https://github.com/adhabnr-ux/openeval/blob/main/spec/SPEC.md
- **npm SDK:** `npm install @openeval/sdk`
- **PyPI SDK:** `pip install openeval`

We would love to collaborate.

## 评论 (2)

### adhabnr-ux · 2026-07-30

Update: OpenEval packages are now published! `pip install openeval-sdk`. Active responses from Inspect AI, CrewAI, and Arize. Would love to collaborate.

### adhabnr-ux · 2026-08-21

Closing this in favor of #4022, opened after I'd actually built and tested a real adapter against this package (including two real discrepancies found between `result_schema.py`'s docstrings and the installed 0.4.12 behavior) — this one was an early, generic template posted before that work. Apologies for the duplicate; #4022 has the substantive proposal.
