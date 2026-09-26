source: https://github.com/vllm-project/guidellm/pull/874

# Loosen torchcodec requirement - #874

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 30, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

What happened here? The ARM64 fix got backported to 0.12???

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/05c66207d4ef5ae11802bc4bbb803925231a4cc0..a5cbf0f3670dfcf383098b434a04e7abcb1b048b)the fix/torchcodec_bump branch from

[to](https://github.com/vllm-project/guidellm/commit/05c66207d4ef5ae11802bc4bbb803925231a4cc0)

`05c6620`


`a5cbf0f`

[Compare](https://github.com/vllm-project/guidellm/compare/05c66207d4ef5ae11802bc4bbb803925231a4cc0..a5cbf0f3670dfcf383098b434a04e7abcb1b048b)

July 1, 2026 13:40


[sjmonson](https://github.com/sjmonson)changed the title

Jul 1, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

Just for documentation sake: Its possible to build earlier versions of torchcodec for aarch64 there we just not packages available. By locking to a minimum of 0.12 a user's local pip will resolve properly for the intended platform. |

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

July 1, 2026 13:59

|
Queued — the merge queue status continues in |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

[uv.lock](https://github.com/vllm-project/guidellm/pull/874/files/a5cbf0f3670dfcf383098b434a04e7abcb1b048b#diff-84321598744d84dbee2318e634c74c9aae39a1c253f1c4bd17ebf9ef2f807b11)

| { name = "torchcodec", version = "0.13.0", source = { registry = "https://download.pytorch.org/whl/cpu" }, marker = "platform_machine == 'arm64' and sys_platform == 'darwin'" }, | ||
| { name = "torchcodec", version = "0.13.0+cpu", source = { registry = "https://download.pytorch.org/whl/cpu" }, marker = "platform_machine != 'arm64' or sys_platform != 'darwin'" }, |

There was a problem hiding this comment.

Shouldn't this be relaxed, too?

There was a problem hiding this comment.

No and it can't be. `uv.lock`

is always the exact wheel as it exists on the target index. AIPCC already has to rebuild (or ignore) the `uv.lock`

as it targets PYPI and the PyTorch index.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

## Summary Torchcodec no longer requires a strict PyTorch version. Downstream builds of GuideLLM only have torchcodec 0.11 available so make that our minimum. ## Details As of 0.12, `torchcodec` has switched to using the PyTorch 2.11 stable ABI ([meta-pytorch/torchcodec#1260]) which means that we no longer have to lock version-to-version. Due to the downstream requirement (see above) we lock to a minimum of `torchcodec` 0.12 which requires `torch==2.11`. Technically this means that a user could end up with a broken install if they bump torch past 2.11 without bumping torchcodec but that is unlikely. ## Test Plan Testing with any audio dataset should verify that this works. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 30 18:15:57 2026 -0400 Bump torchcodec (for the final time) Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Signed-off-by: Samuel Monson <smonson@redhat.com>]a5cbf0f

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Torchcodec no longer requires a strict PyTorch version. Downstream builds of GuideLLM only have torchcodec 0.11 available so make that our minimum. ## Details As of 0.12, `torchcodec` has switched to using the PyTorch 2.11 stable ABI ([meta-pytorch/torchcodec#1260]) which means that we no longer have to lock version-to-version. Due to the downstream requirement (see above) we lock to a minimum of `torchcodec` 0.12 which requires `torch==2.11`. Technically this means that a user could end up with a broken install if they bump torch past 2.11 without bumping torchcodec but that is unlikely. ## Test Plan Testing with any audio dataset should verify that this works. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 30 18:15:57 2026 -0400 Bump torchcodec (for the final time) Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Signed-off-by: Samuel Monson <smonson@redhat.com>]a5cbf0f

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Torchcodec no longer requires a strict PyTorch version. Downstream builds of GuideLLM only have torchcodec 0.11 available so make that our minimum.

## Details

As of 0.12,

`torchcodec`

has switched to using the PyTorch 2.11 stable ABI (meta-pytorch/torchcodec#1260) which means that we no longer have to lock version-to-version. Due to the downstream requirement (see above) we lock to a minimum of`torchcodec`

0.12 which requires`torch==2.11`

. Technically this means that a user could end up with a broken install if they bump torch past 2.11 without bumping torchcodec but that is unlikely.## Test Plan

Testing with any audio dataset should verify that this works.

## Use of AI

## git log

commit

a5cbf0fAuthor: Samuel Monson smonson@redhat.com

Date: Tue Jun 30 18:15:57 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com