source: https://github.com/vllm-project/guidellm/pull/1016

# Move entrypoint configs to top-level `schemas`

submodule - #1016

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/42b8d523cf0987276063213917c182269660089c..c85cf11c3e09600372aaa9a798dab7aa5d20805c)the fix/schema_split branch from

[to](https://github.com/vllm-project/guidellm/commit/42b8d523cf0987276063213917c182269660089c)

`42b8d52`


`c85cf11`

[Compare](https://github.com/vllm-project/guidellm/compare/42b8d523cf0987276063213917c182269660089c..c85cf11c3e09600372aaa9a798dab7aa5d20805c)

August 11, 2026 15:32

Move core schema files (base, info, request, request_stats, response, statistics, tool_call) into schemas/base/ subdirectory. Move conversation_graph.py to scheduler/schemas/ where it belongs. Update all internal and external imports accordingly. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Move BackendArgs, OpenAIHTTPBackendArgs, OpenAIWebSocketBackendArgs, and VLLMPythonBackendArgs into schemas/backends/ subpackage. Original backend implementation files now import Args from the centralized schemas module. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Move all data-related Args classes (deserializers, preprocessors, finalizers, loaders, tokenizers) into centralized schemas/data/ module. Original files become thin re-exports. HuggingFaceDataArgs.source uses Any type to avoid heavy datasets import in schema layer. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Move all benchmark Args classes (profiles, outputs, metrics, random), BenchmarkScenario, BenchmarkArgs, TransientPhaseConfig, and scenario JSON files into centralized schemas/benchmark/ module. Original files become thin re-exports. SchedulerState gated behind TYPE_CHECKING in TransientPhaseConfig. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Point pure-Args imports in cli/ and benchmark/entrypoints.py to guidellm.schemas.* canonical locations. Mixed imports (Args + impl classes from same module) left on re-export paths for stability. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Replace guidellm.logger with stdlib logging in schemas/backends/ vllm_python.py. Verified: importing all schemas/ submodules does not load datasets, torch, transformers, vllm, pandas, or faker. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Strip out shims that re-export Args classes from within each submodule. Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: Claude Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Opus removed a lot of comments while moving things. This commit restores them as they were. Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/623782e61cf5b848de38e37fd14ef2a99fd0d5d1..3cdefb25e803a3db31572fe0f447e3a8cdbda3d1)the fix/schema_split branch from

[to](https://github.com/vllm-project/guidellm/commit/623782e61cf5b848de38e37fd14ef2a99fd0d5d1)

`623782e`


`3cdefb2`

[Compare](https://github.com/vllm-project/guidellm/compare/623782e61cf5b848de38e37fd14ef2a99fd0d5d1..3cdefb25e803a3db31572fe0f447e3a8cdbda3d1)

August 24, 2026 18:57

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

August 24, 2026 20:40

|
|


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Aug 24, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

That's a lot -- but the patterns are relatively simple. The moves look valid, and the tests pass, so I'm not going to waste an enormous amount of time comparing every line of the code I'll trust has just moved. 😆

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Aug 25, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

This is very helpful towards our goal of fixing the circular dependencies. Due to it being large relocation refactor like this, I didn't review every line, but I reviewed the new organization, and skimmed the code.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Aug 26, 2026

## Summary Add a CI utility which enforces a clean import hierarchy in GuideLLM. ## Details GuideLLM have fairly strict requirements on which sub-modules can import from which other sub-modules. This tool ensures that the import ordered is respected. Note that currently there is an import on main which violates the rules; it will be fixed in[#1016]. ## Test Plan - Run `tox -e lint-check` ## Related Issues - Blocked by[#1016]- Relates to[#1046]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Aug 24 16:38:32 2026 -0400 Add import-linter config Import-linter is a tool for codifying dependency ordering. We have had a few cases where the contracts between submodules have been broken, running this tool as a part of CI should ensure that does not happen. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]c86a85c[Author: Samuel Monson <smonson@redhat.com> Date: Mon Aug 24 16:53:42 2026 -0400 Add import-lint to tox lint-check Signed-off-by: Samuel Monson <smonson@redhat.com> commit]0c94e0b[Author: Samuel Monson <smonson@redhat.com> Date: Wed Aug 26 11:00:22 2026 -0400 Add a lint rule to avoid slow imports in workers Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Signed-off-by: Samuel Monson <smonson@redhat.com>]808dc83

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Aug 27, 2026

## Summary The builtin scenarios files were missed during the migration in[#1016]. This PR both fixes the packaging code to point to the new location and replaces the scenarios. ## Details Moving the scenarios was on my TODO list but I forgot before undrafting the PR. Since I was doing a scenarios PR anyways I decided to replace our super out-of-date scenarios with ones that at least make some sense. The new ones are not perfect, they are mostly oriented for enterprise size model-deployments and very abstract to use-cases so I think there should be a followup to fully solve[#563]. ## Test Plan Run one of the new built-ins: `guidellm run -c rhaiis/concurrent-8k-1k-equal --backend kind=openai_http,target=[http://127.0.0.1:8000`]and confirm that the benchmark at least starts. ## Related Issues - Related to[#563]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Aug 27 14:38:29 2026 -0400 Move scenarios to correct location Signed-off-by: Samuel Monson <smonson@redhat.com> commit]c3286dc[Author: Samuel Monson <smonson@redhat.com> Date: Thu Aug 27 15:24:23 2026 -0400 Add RHAIIS Regression Scenarios Add a bunch of builtin scenarios that are used in RHAIIS regression testing. This is a first step in hopefully keeping a more up-to-date scenario catalog. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]150a464[Author: Samuel Monson <smonson@redhat.com> Date: Thu Aug 27 15:29:06 2026 -0400 Drop the old builtin scenarios The old Chat and RAG scenarios are super dated and do not accurately reflect modern workloads. The only reason we kept them around was to keep some kind of builtin workload available. Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Signed-off-by: Samuel Monson <smonson@redhat.com>]05e2394

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Moves all

`*Args`

classes and subclasses into the top-level`schemas`

submodule in perpetration for lazy loading the major submodules.## Details

One of the main blockers for #559 is that loading some of our heavier dependencies takes a significant amount of time when spawning new threads. Some of these dependencies (datasets and pytorch) are impossible defer in the data processing pathway, but are not necessary to run backend workers. Thus, this PR takes some initial steps to decouple loading the main submodules (backends, data, scheduler, benchmark) from importing the base package.

## Test Plan

Since there are no functional changes just running the tests should be sufficient.

## Related Issues

## Use of AI

## git log

commit

0280467Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 20:50:02 2026 +0000

commit

ac19804Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 20:56:21 2026 +0000

commit

3cc6591Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 21:02:40 2026 +0000

commit

a8b14f7Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 21:26:12 2026 +0000

commit

4183bf4Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 21:39:14 2026 +0000

commit

38648dbAuthor: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 21:41:51 2026 +0000

commit

9939a38Author: Samuel Monson smonson@redhat.com

Date: Fri Aug 7 21:43:59 2026 +0000

commit

6aaa50aAuthor: Samuel Monson smonson@redhat.com

Date: Mon Aug 10 23:29:29 2026 +0000

commit

55d0cfbAuthor: Samuel Monson smonson@redhat.com

Date: Mon Aug 10 23:29:59 2026 +0000

commit

3cdefb2Author: Samuel Monson smonson@redhat.com

Date: Tue Aug 11 17:12:24 2026 +0000

Generated-by: Claude Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com