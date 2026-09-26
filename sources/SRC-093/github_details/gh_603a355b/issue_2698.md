# [Issue #2698] [Docs] Add Chinese localization and language switching for the documentation site

source: https://github.com/vllm-project/aibrix/issues/2698
state: open | updated: 2026-09-10T11:06:27Z
labels: kind/documentation, help wanted

## 正文

## Feature Description and Motivation

 provide a Chinese version for the entire [AIBrix documentation site](https://aibrix.readthedocs.io/latest/)

A site-wide Chinese localization would make AIBrix more accessible to Chinese-speaking users and contributors, improve onboarding, and reduce the effort required to understand concepts, deployment guides, API references, and troubleshooting documentation.

## Use Case

Chinese-speaking users who are evaluating, deploying, or contributing to AIBrix currently need to translate the documentation page by page. A consistent official Chinese version would provide a more coherent reading experience across the whole documentation site.

## Proposed Solution

Consider adding Chinese localization for the documentation site with a visible language switcher, for example:

- Add a `中文` / `English` switcher in the documentation header or navigation.
- Use a stable localized URL structure such as `https://aibrix.readthedocs.io/zh-CN/latest/`.
- Translate the existing documentation progressively, starting with Getting Started, Installation, Architecture, and core user guides.
- Preserve matching navigation and page structure between English and Chinese where possible.
- Define a lightweight synchronization process so translated pages stay aligned with the English source, including a way to identify pages that need updates.
- Reuse any localization support already available in the current documentation toolchain.



## 评论 (1)

### FAUST-BENCHOU · 2026-09-10

/assign @FAUST-BENCHOU 
