source: https://github.com/vllm-project/guidellm/commit/39383552962841086d05e25c37b58a83ef06c758

# Commit 3938355

authored

Update click to 8.4 (

## Summary
## Details
A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2.
Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers.
We resolve this by bumping click to 8.4. In the AIPCC build base image, this allows huggingface_hub 1.23 and transformers 5.14.1, which does not have the CVEs at issue.
## Test Plan
- I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1.
- A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image.
## Related Issues
N/A
---
- [x] "I certify that all code in this PR is my own, except as noted below."
## Use of AI
- [ ] Includes code generated or substantially modified by an AI agent
- [ ] Includes tests generated or substantially modified by an AI agent
> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([#978](https://github.com/vllm-project/guidellm/pull/978))[https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md)) file. --- # git log commit

[Author: David Butenhof <dbutenho@redhat.com> Date: Fri Jul 31 14:18:03 2026 -0400 Update click to 8.4 A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2. Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers. We resolve this by bumping click to 8.4. In the AIPCC build base image, this binds to transformers 5.14.1, which does not have the CVEs at issue. I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1. A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image. Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>](https://github.com/vllm-project/guidellm/commit/fdb89ab0ce2a942ad34364428840cac91ac80b14)

`fdb89ab`1 parent[05d3afb]commit 3938355

4 files changed

Lines changed: 69 additions & 77 deletions

## File tree

- src/guidellm/utils
- tests/unit/cli

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`59` | `59` |
| |
`60` | `60` |
| |
`61` | `61` |
| |
`62` |
| `-` | |
| `62` | `+` | |
`63` | `63` |
| |
`64` | `64` |
| |
`65` | `65` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`95` | `95` |
| |
`96` | `96` |
| |
`97` | `97` |
| |
`98` |
| `-` | |
| `98` | `+` | |
`99` | `99` |
| |
`100` | `100` |
| |
`101` | `101` |
| |
|

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`112` | `112` |
| |
`113` | `113` |
| |
`114` | `114` |
| |
`115` |
| `-` | |
| `115` | `+` | |
`116` | `116` |
| |
`117` | `117` |
| |
`118` | `118` |
| |
|

## 0 commit comments