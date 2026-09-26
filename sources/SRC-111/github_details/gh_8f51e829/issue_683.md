# [Issue #683] Enable AIPCC builds of GuideLLM

source: https://github.com/vllm-project/guidellm/issues/683
state: closed | updated: 2026-06-17T13:50:05Z
labels: internal, build

## 正文

Before we can integrate GuideLLM with downstream RHAI, we need to

- [ ] Understand the AIPCC onboarding process
- [x] Make sure all dependencies are built (or request they be added)
- [x] Set up the AIPCC build of GuideLLM artifacts
- [ ] Determine how to integrate those artifacts into our build/release process

This is also a dependency for Eval Hub support (#653)

## 评论 (2)

### dbutenhof · 2026-04-03

Interestingly, AIPCC has already "onboarded" GuideLLM and is building a `guidellm` wheel (I believe only with `[recommended]` extras), including v0.6.0, under rocm, cuda, and cpu variations. The wheels seem to be publicly accessible (outside the firewall) although without being certain of the proprieties I won't post a URL on GitHub.

The next step is figuring out what's involved in getting a container built in the AIPCC pipeline.

### dbutenhof · 2026-06-17

I'm going to mark this "done", although the current state for RHAI 3.5 EA1 is "partial success". We've got a GuideLLM container, albeit built without our extras, which means no multimodal support. Both the `recommended` and `all` extras depend on the `blobfile` tokenizer, which has not previously been built in the AIPCC index. This has been added (currently in AIPCC staging) and will be available for 3.5 EA2, allowing us to upgrade to `guidellm[all]==0.6.0`.

Releasing with 0.7.0 is a possibility, but we're concerned about the first release being the massively refactored 0.7.0 CLI and thinking that releasing the stable/familiar 0.6.0 for 3.5 and upgrading for 3.6 probably makes more sense.

Note that the Eval Hub team owns their GuideLLM adapter, but they expect to build on top of our container image, adding a layer for their SDK. This is unlikely for 3.5.
