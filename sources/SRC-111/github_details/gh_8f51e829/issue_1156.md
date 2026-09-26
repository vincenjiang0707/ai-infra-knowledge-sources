# [Issue #1156] Discuss bilingual (English/Chinese) documentation support

source: https://github.com/vllm-project/guidellm/issues/1156
state: closed | updated: 2026-09-22T01:58:49Z
labels: 

## 正文

## Summary

Are there plans to support bilingual English/Chinese documentation for GuideLLM?

There is a large and growing community of Chinese-speaking developers and users using GuideLLM. Providing Chinese documentation alongside the existing English documentation would make the project easier to adopt, promote, and share, while also helping more users understand the project and contribute to the community.

I would be happy to take responsibility for contributing and maintaining the Chinese documentation.

## Proposed contribution plan

- Keep the Chinese documentation in the same documentation site and repository, with a structure and navigation consistent with the English documentation.
- Start with the most important sections, such as installation, getting started, benchmark usage, and core guides.
- Submit one small chapter or section at a time, so that each change is easy to review and discuss.
- Keep the Chinese version aligned with the English source, updating translations when the corresponding English documentation changes.
- Follow the project’s existing documentation style, terminology, formatting, and contribution workflow.

## Questions

- Is bilingual English/Chinese documentation within the project’s roadmap or scope?
- Where would maintainers prefer the Chinese documentation to live?
- Are there any translation conventions or review requirements I should follow?

If the maintainers and community agree with this direction, I can start by preparing the first small documentation contribution.


## 评论 (3)

### sjmonson · 2026-09-17

None of the core GuideLLM team speak Chinese so it is not on our roadmap, but we would open to the idea. The overall proposal makes sense to me. We don't have a process or structure for multilingual so a few other things need to be figured out as well:

1. Do we need to reorganize our docs to support multiple languages? Currently we use `mkdocs` to publish documentation to https://vllm-project.github.io/guidellm/ I assume some changes may be needed to support multilingual.
2. How do we manage drift between documentation in different languages? For example if an English speaker want to change docs do we require them to use AI to generate matching Chinese docs or do we try to track the drift and encourage bilingual Chinese speakers to separately improve the documentation?
3. How we make it possible for English speaking maintainers to review Chinese documentation changes and for Chinese speaking maintainers to review English documentation changes?
4. Should we also find a way to localize GuideLLM's output and docstrings?

(2) and (3) could be solved in a lot of different ways, I would be curious if you have been involved in any other open source project that handled this well who we could learn from. One possible approach is creating some reusable AI skills which individuals can run with their own AI harnesses. (4) seems very difficult to me so maybe out of scope for the initial plan?

### tangming1996 · 2026-09-20

Thanks — these are exactly the right concerns. I agree that we should solve the maintenance and review model before adding a large amount of translated content.

I am willing to own not only the initial translations, but also the supporting tooling and the ongoing drift triage. I would suggest starting with a deliberately small, reversible pilot.

### 1. Documentation structure and deployment

English should remain the canonical source, and the existing English URLs should not change.

For the first PR, I would create a technical proof of concept with only one or two translated pages. Before choosing a permanent structure, I would verify the alternatives against GuideLLM's existing documentation stack, including MkDocs Material, Mike versioning, `gen-files`, `api-autonav`, search, link checking, and the current deployment workflows.

The acceptance criteria for that PR would include:

- no changes to existing English URLs;
- a working language selector;
- successful English and Chinese builds;
- working links, navigation, search, and versioned deployment;
- a clear fallback or notice for pages that have not been translated;
- no requirement to reorganize the English documentation unless the POC demonstrates a strong technical reason and the maintainers agree.

I would document the chosen structure and its tradeoffs in the PR instead of introducing a large translation tree immediately.

### 2. Managing translation drift

I do not think English contributors should be required to update Chinese documentation or generate translations with AI as part of an English documentation PR.

Instead, each translated page should have an explicit mapping to its canonical English source and record the English source revision it was translated from. A small validation tool can then detect when the English source has changed.

My proposed behavior is:

- English-only PRs are never blocked by missing Chinese updates.
- Source changes produce a non-blocking stale-translation report for the Chinese maintainers.
- A stale Chinese page clearly links to the current English version and is marked as potentially outdated.
- Changes to a Chinese page must pass stricter checks: valid source mapping, current source revision, documentation build, links, and structural checks.
- Missing translations fall back to English or remain absent rather than silently presenting outdated Chinese content as current.

I would be the initial owner of reviewing these drift reports and submitting the follow-up updates.

### 3. Cross-language review

I think review should be split by responsibility rather than requiring every reviewer to be bilingual:

- English-speaking maintainers review the site architecture, technical claims, commands, code examples, links, and possible regressions to the English site.
- Chinese-speaking reviewers review meaning, terminology, and language quality.
- Automated checks verify source mappings, headings, links, code blocks, commands, and documentation builds.
- Each translation PR includes the English source revision and a concise English review summary. An AI-generated back-translation can be included as additional review evidence, but it should not replace human review.

I can act as the initial Chinese-language owner. Before expanding beyond the pilot, I will also try to recruit at least one additional Chinese-speaking reviewer so that the process does not depend permanently on one person.

### 4. AI-assisted workflow and existing projects

There are useful ideas we can borrow from other projects:

- Kubernetes keeps localized content in mirrored paths, assigns language-specific ownership, tracks upstream changes with scripts, and requires human review of machine-generated translations.
- FastAPI uses language-specific terminology/prompts and AI-assisted translation, followed by review from native speakers.

A reusable GuideLLM translation skill could eventually help produce drafts, apply the glossary, detect structural differences, and generate back-translations for review. I would treat that as an assistive tool rather than the source of truth, and introduce it only after the terminology and review rules are agreed.

### 5. Initial scope

I agree that localizing CLI output, logs, error messages, and docstrings should be out of scope initially. Auto-generated API reference documentation should also remain in English.

The pilot would cover only user-facing documentation, beginning with the landing page and one getting-started page. Later pages would be submitted one at a time. After a few pages, we can evaluate the actual maintenance and review cost before deciding whether to expand.

If the Chinese documentation ever becomes unmaintained, the stale-page mechanism and English fallback provide a safe degradation path, and the Chinese build can be disabled without affecting the canonical English documentation.

For context, I have already contributed across both GuideLLM documentation and implementation, with eight PRs merged, so I am familiar with the project's testing and review workflow.

I’ve submitted a small design/POC PR containing the build integration, maintenance policy, terminology guidance, automated checks, and an example translation—not a bulk translation: [PR #1164](https://github.com/vllm-project/guidellm/pull/1164).

### tangming1996 · 2026-09-22

Thank you — I’ll work with @[zhiyingfang2022](https://github.com/zhiyingfang2022) on the Chinese documentation effort. She is my colleague and works on product design for our LLM platform. She also maintains our company’s documentation site and has extensive experience with documentation planning, writing, review, and long-term maintenance. Together, we can help ensure that the Chinese documentation remains technically accurate, consistent, and sustainable as it grows.

Also, does the community currently have any documentation reviewer roles or openings? @@[zhiyingfang2022](https://github.com/zhiyingfang2022) and I would be happy to help with the initial review and maintenance of the documentation, especially while the Chinese documentation effort is getting established.
