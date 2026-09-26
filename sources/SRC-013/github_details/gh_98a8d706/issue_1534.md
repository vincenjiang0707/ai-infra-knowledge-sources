# [Issue #1534] [Batch] Graduate Async Processor to Production

source: https://github.com/llm-d/llm-d/issues/1534
state: open | updated: 2026-08-25T12:13:14Z
labels: help wanted, release/v0.9

## 正文

SUMMARY:
- [ ] move repo from llm-d-incubation to llm-d
- [ ] release out of llm-d
- [ ] make guide "production quality"

## 评论 (5)

### ahg-g · 2026-05-16

/assign @shimib 

### shimib · 2026-08-03

@ahg-g can you update the status on this issue? looks like i don't have permissions

### UgaTheDev · 2026-08-24

Took a look at where this stands:

- **Move repo**: done — `llm-d-incubation/llm-d-async` now redirects to `llm-d/llm-d-async`.
- **Release out of llm-d**: shipping — `llm-d-async` has releases through v0.9.0 with full CI (build-images, e2e-tests, trivy scan). The remaining release-artifact checkboxes (container image, release tag + notes, E2E tests passing) look like they're already tracked under the "Async Processor" section of #2131, so that's probably the better place to close those out rather than duplicating them here.
- **Guide production quality**: `guides/asynchronous-processing/` in this repo reads as fairly complete (prereqs, Helm install, multi-tenant variant, pointer to an ops guide for sizing) — no obvious gaps jumped out.

@shimib @ahg-g — is there a specific bar for "production quality" on the guide you had in mind that's not met yet, or can this be closed out with #2131 tracking the rest?


### shimib · 2026-08-24

@UgaTheDev this can be closed

### UgaTheDev · 2026-08-25

Agreed on closing — I don't have write access here, so I can't do it myself.

@ahg-g could you close this one out? You assigned it originally, and shimib flagged
above that he doesn't have permissions either.

For the record, the remaining release-artifact boxes (container image, release tag +
notes, E2E tests passing) are already tracked under the "Async Processor" section of
#2131, so nothing is lost by closing this rather than migrating the checklist.

