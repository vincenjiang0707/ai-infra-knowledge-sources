source: https://github.com/vllm-project/guidellm/pull/596

# vLLM Python Backend - #596

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)Feb 17, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Core handling of vLLM seems good, the rest is mostly cleanup and minor fixes. There are a lot of dead codepaths that likely exist due to this PR being started before [#478](https://github.com/vllm-project/guidellm/pull/478). A lot of converting to/from `/v1/chat/completions`

format can be removed. Multimodel probably needs bit more work. Audio should be easy to fix but image/video don't seem implemented; this can be a later follow-up PR. Both plain and chat template formats need fixes, see respective comments; neither should be difficult.

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/__init__.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-a547d33bd218c6cdfff0392dfb92b424a48886ddd65a90c860c209918fde1e4d)

[src/guidellm/backends/__init__.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-a547d33bd218c6cdfff0392dfb92b424a48886ddd65a90c860c209918fde1e4d)Outdated

[src/guidellm/benchmark/schemas/generative/entrypoints.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-01f13cfce729be3e9362e2f146eb8fe7ccef973cf9780236a3ad24fbd0f49ade)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Feb 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

My eyes are starting to glaze over, in the middle of `vllm.py`

, so I need a break. Might as well post what I've got so far and start fresh later...

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Feb 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

More comments / questions / rambling

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm_response.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-ceb464f6268b43029fe14087d2ccfdcb028a70e8591148bb8cb032d168dfe75e)Outdated

[Containerfile.vllm](https://github.com/vllm-project/guidellm/pull/596/files#diff-5b27b672bc83c96acebb4aa9a8c1ef7f11365693faf11d5deb19e8cab6bf5b52)

[Containerfile.vllm](https://github.com/vllm-project/guidellm/pull/596/files#diff-5b27b672bc83c96acebb4aa9a8c1ef7f11365693faf11d5deb19e8cab6bf5b52)Outdated

[Containerfile.vllm](https://github.com/vllm-project/guidellm/pull/596/files#diff-5b27b672bc83c96acebb4aa9a8c1ef7f11365693faf11d5deb19e8cab6bf5b52)

[Containerfile.vllm](https://github.com/vllm-project/guidellm/pull/596/files#diff-5b27b672bc83c96acebb4aa9a8c1ef7f11365693faf11d5deb19e8cab6bf5b52)

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ad0015a71c267cf17e6ce15a5062f60ae69e7df7..a595ae22ca32a233118ed5b8257612fe2600271e)the feat/vllm-python branch from

[to](https://github.com/vllm-project/guidellm/commit/ad0015a71c267cf17e6ce15a5062f60ae69e7df7)

`ad0015a`


`a595ae2`

[Compare](https://github.com/vllm-project/guidellm/compare/ad0015a71c267cf17e6ce15a5062f60ae69e7df7..a595ae22ca32a233118ed5b8257612fe2600271e)

February 23, 2026 23:42


**commented**

[jaredoconnell](https://github.com/jaredoconnell)Feb 24, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Addressed doc comments.

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Feb 25, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Comments just on the final commit. GitHub's "changed since last review" is useless across a rebase, and I'm not anxious to go through each of your massive list of commits.

(My preferred mode is to squash on my side so each update on a PR is a single neat commit ... I get not everyone likes to work that way, but a long list of commits with rebases is *really* hard to re-review...)

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/806c028f19e198861ba2757fc80a2ad37e86a0de..ab512e962ad59f1346d9c6432f083b693c89c71a)the feat/vllm-python branch from

[to](https://github.com/vllm-project/guidellm/commit/806c028f19e198861ba2757fc80a2ad37e86a0de)

`806c028`


`ab512e9`

[Compare](https://github.com/vllm-project/guidellm/compare/806c028f19e198861ba2757fc80a2ad37e86a0de..ab512e962ad59f1346d9c6432f083b693c89c71a)

March 4, 2026 01:09


**commented**

[jaredoconnell](https://github.com/jaredoconnell)Mar 5, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I addressed almost all requested changes. It's much simpler now. Much less dead code.

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/benchmark/schemas/generative/entrypoints.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-01f13cfce729be3e9362e2f146eb8fe7ccef973cf9780236a3ad24fbd0f49ade)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[jaredoconnell](https://github.com/jaredoconnell)marked this pull request as ready for review

March 6, 2026 05:25


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Few more minor nits and comments. Not final review, still working though `vllm.py`

but so far looking pretty good. Haven't tested latest version yet.

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated

[Containerfile.vllm](https://github.com/vllm-project/guidellm/pull/596/files#diff-5b27b672bc83c96acebb4aa9a8c1ef7f11365693faf11d5deb19e8cab6bf5b52)

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/596/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)

[tox.ini](https://github.com/vllm-project/guidellm/pull/596/files#diff-ef2cef9f88b4fe09ca3082140e67f5ad34fb65fb6e228f119d3812261ae51449)Outdated

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Mar 11, 2026

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/596/files#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)

|
This pull request has merge conflicts that must be resolved before it can be |

|
You can do this by running: |

[sjmonson](https://github.com/sjmonson)added a commit that referenced this pull request

Mar 13, 2026

## Summary Adds formatting check to CI jobs and runs formatting against all files to ensure CI passes. ## Related Issues - Blocked by[#596]- Blocked by[#590]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes AI-assisted code completion - [ ] Includes code generated by an AI application - [ ] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`)

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/dc3492d6204c65c7debb057f40f45c295936881e..cc1f09bc768a6c2b212346aee5a734578db763fe)the feat/vllm-python branch from

[to](https://github.com/vllm-project/guidellm/commit/dc3492d6204c65c7debb057f40f45c295936881e)

`dc3492d`


`cc1f09b`

[Compare](https://github.com/vllm-project/guidellm/compare/dc3492d6204c65c7debb057f40f45c295936881e..cc1f09bc768a6c2b212346aee5a734578db763fe)

March 13, 2026 18:15

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/cc1f09bc768a6c2b212346aee5a734578db763fe..110ea1f7615b6bc7ec5b6fe5ba768666cda40159)the feat/vllm-python branch from

[to](https://github.com/vllm-project/guidellm/commit/cc1f09bc768a6c2b212346aee5a734578db763fe)

`cc1f09b`


`110ea1f`

[Compare](https://github.com/vllm-project/guidellm/compare/cc1f09bc768a6c2b212346aee5a734578db763fe..110ea1f7615b6bc7ec5b6fe5ba768666cda40159)

March 13, 2026 18:30


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 13, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

You overrode Jared's protections on the column field accesses. I'm making comments, but also approving on the assumption that you did this out of certain knowledge that I (and apparently Jared) lack about about the input predicates -- particularly, that the column values really can never be `None`

. So ... you're sure? 😁

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files/172e17571f04a83ee26a2ff3e2b12d098b9c7ff4#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/596/files/172e17571f04a83ee26a2ff3e2b12d098b9c7ff4#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

|
Not able to reproduce the unit test failures locally but can reproduce e2e failures. Seems like vLLM being present in the env is causing a few tests to time out. |

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

This design uses pydantic for the validation, since pydantic is used extensively in GuideLLM. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

This led to it requiring the model field Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Also includes some other improvements, and fixed test not passing. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Implemented a new base class for BackendArgs and improved documentation Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/172e17571f04a83ee26a2ff3e2b12d098b9c7ff4..22957cee927a13dd3ad5b4779c92137561a2757d)the feat/vllm-python branch from

[to](https://github.com/vllm-project/guidellm/commit/172e17571f04a83ee26a2ff3e2b12d098b9c7ff4)

`172e175`


`22957ce`

[Compare](https://github.com/vllm-project/guidellm/compare/172e17571f04a83ee26a2ff3e2b12d098b9c7ff4..22957cee927a13dd3ad5b4779c92137561a2757d)

March 13, 2026 20:18

Signed-off-by: Samuel Monson <smonson@redhat.com>


**reviewed**

[sjmonson](https://github.com/sjmonson)Mar 13, 2026

[tox.ini](https://github.com/vllm-project/guidellm/pull/596/files/756c3a82141ebe470def06bdb3530f37fa0dda5c#diff-ef2cef9f88b4fe09ca3082140e67f5ad34fb65fb6e228f119d3812261ae51449)Outdated


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 13, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 13, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

This PR is a bit too large at this point so pushing for a merge. There will have to be a few follow-up like:

- Confirm that having vLLM installed does not affect other backends
- Improvements to
`guidellm.extras`

to lazy load large optional extras - Cleanup of argument parsing code
- Multi-turn support

[sjmonson](https://github.com/sjmonson)added a commit that referenced this pull request

Mar 16, 2026

## Summary Drop vLLM extras group and instruct users to install vLLM separately. ## Details Had planned to put this in[#596]but wanted to give[@jaredoconnell]a chance to respond. The main reasons to have an `extras` group is if multiple packages are needed to make an optional feature work or a specific version is needed. vLLM is neither of those things. Not having a vLLM extras group will simplify a lot of things on the locking side for the low cost of asking a user to do `pip install vllm guidellm` instead of `pip install guidellm[vllm]`. In fact, the vLLM backend container image does not even use the extras group since it is easier to just install GuideLLM into an existing vLLM image. ## Related Issues - Closes[#634]- Closes[#633]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes AI-assisted code completion - [ ] Includes code generated by an AI application - [ ] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`)

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

The VLLM Python backend is an alternative to the traditional client-server setup by utilizing the Python API rather than the HTTP API.

## Details

`--backend vllm_python`

## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)