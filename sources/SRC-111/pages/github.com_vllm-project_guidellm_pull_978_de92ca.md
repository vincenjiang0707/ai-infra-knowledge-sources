source: https://github.com/vllm-project/guidellm/pull/978

# Update click to 8.4 - #978

## Conversation

A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2. Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers. We resolve this by bumping click to 8.4. In the AIPCC build base image, this binds to transformers 5.14.1, which does not have the CVEs at issue. I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1. A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

Jul 31, 2026


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 31, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Where could I find the AIPCC (or equivalent) Containerfile? Otherwise not much to see in the diffs.


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 31, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I did a basic test and it works for me.

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 31, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

I won't put the internal link here, but I can share it if you're curious. (You can access the internal wheels and look at the repo as long as you're in the Red Hat domain, but you can't see the container images because they're on a protected repo.) The main thing is that it uses |

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Aug 3, 2026

## Summary ## Details A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2. Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers. We resolve this by bumping click to 8.4. In the AIPCC build base image, this allows huggingface_hub 1.23 and transformers 5.14.1, which does not have the CVEs at issue. ## Test Plan - I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1. - A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image. ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Fri Jul 31 14:18:03 2026 -0400 Update click to 8.4 A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2. Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers. We resolve this by bumping click to 8.4. In the AIPCC build base image, this binds to transformers 5.14.1, which does not have the CVEs at issue. I ran a container build using (essentially) the AIPCC Containerfile, on the 3.5 builder base image (but copying in my local source and using `pip install ".[all]"`), and verified that it binds transformers 5.14.1. A local `trivy` scan shows no CRITICAL/HIGH CVEs on the resulting image. Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>]fdb89ab

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

## Details

A transitive dependency collision in the AIPCC build environment caused us to bind transformers < 5.0, and failing to resolve the transformers CVEs for which we released 0.7.2.

Basically, the crux was huggingface_hub: we have bound upstream to 1.16.0, while the AIPCC index jumps from 0.38 to 1.16.4. 1.16.4 added an explicit dependency on click 8.4, which caused us to bind 0.38 and an equally old transformers.

We resolve this by bumping click to 8.4. In the AIPCC build base image, this allows huggingface_hub 1.23 and transformers 5.14.1, which does not have the CVEs at issue.

## Test Plan

`pip install ".[all]"`

), and verified that it binds transformers 5.14.1.`trivy`

scan shows no CRITICAL/HIGH CVEs on the resulting image.## Related Issues

N/A

## Use of AI

## git log

commit

fdb89abAuthor: David Butenhof dbutenho@redhat.com

Date: Fri Jul 31 14:18:03 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com