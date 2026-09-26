source: https://github.com/vllm-project/guidellm/pull/753

# CLI profile refactor - #753

[mergify[bot]](https://github.com/mergify[bot])merged 6 commits into

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[documentation](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adocumentation)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

May 29, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)May 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

The way this is currently written each `ProfileArgs`

is essentially a duplicate of its `Profile`

without its business logic. That is going to be hard to maintain going forward because we will have to maintain identical fields between Args and Profiles. Instead I recommend looking at converting `Profiles`

to a normal non-pydantic registry. See `BackendRegistry`

or `DataLoaderRegistry`

(after [#754](https://github.com/vllm-project/guidellm/pull/754)) for examples.

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)May 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Forgot one thing. There is a bunch of migration code in the CLI run function:

[guidellm/src/guidellm/cli/benchmark/run.py](https://github.com/vllm-project/guidellm/blob/8fdbd2862d1ca0405e947e40e55e21740c6fb02d/src/guidellm/cli/benchmark/run.py#L345-L364)

Lines 345 to 364
in
[8fdbd28](https://github.com/vllm-project/guidellm/commit/8fdbd2862d1ca0405e947e40e55e21740c6fb02d)

If you add the following then you can update `BenchmarkGenerativeTextArgs`

to store the profile args rather then profile name and avoid changing the existing CLI usage.

`kwargs["profile"] = {"kind": kwargs.pop("profile", sweep)}`


**commented**

[dbutenhof](https://github.com/dbutenhof)Jun 1, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

The way this is currently written each ProfileArgs is essentially a duplicate of its Profile without its business logic.


Yeah; I'd started out turning Profile into a plain class, but ran into problems ... and without noticing I'd forgotten to remove the Pydantic registry mixin, I let Cursor try to fix them. Which it did by completing the Pydantic infrastructure. I let it stand to get some other things straightened out "first", and then never remembered to fix it.

store the profile args rather then profile name and avoid changing the existing CLI usage.


Well, I started out with code to transparently promote a `str`

to `{"kind": str}`

, and decided it made more sense to require the kind to be explicit. I suppose it's not entirely similar to the new data deserializer since you *can* specify a profile without additional parameters.

Anyway, I spent today doing most of the rework, which got messier than I'd expected. I'll resume tomorrow morning, and hopefully have another tested commit up ...

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b1e613051bbfaefa49c7e286f104df7416a7f3d1..618936f69e537b083e22bbc43b06510dc3280c50)the refactor/schema/profile branch from

[to](https://github.com/vllm-project/guidellm/commit/b1e613051bbfaefa49c7e286f104df7416a7f3d1)

`b1e6130`


`618936f`

[Compare](https://github.com/vllm-project/guidellm/compare/b1e613051bbfaefa49c7e286f104df7416a7f3d1..618936f69e537b083e22bbc43b06510dc3280c50)

June 2, 2026 15:55

Use CLI to construct a ProfileArgs instance, which is then used to build the Profile. Like datasets and backends, we now identify a profile "kind", as `--profile kind=constant[,param=value...]`; directly specified parameters supercede inherited global CLI values like `--rate`. Use more meaningful aliases for the global "rate" to match the previous internal names (e.g., "sweep_size"). This also exposes previously hidden parameters like the sweep's `strategy_type` to run poisson instead of constant async. Manually tested all profiles, including Replay. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

- Remove Pydantic aspect of Profile class, holding a reference to ProfileArgs. - Remove constraints from ProfileArgs, to isolate construction and remove some report serialization issues. - Change ProfileArgs deserialization to "forbid" unknown keys. We have two classes of profile parameter that aren't "universal": - data and data_samples are used only by Replay: we remove these from other ProfileArgs -- this will be refactored later. - Although random_seed isn't used by all profiles, it's a global used throughout GuideLLM, so we promote this to the base ProfileArgs for convenience. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/618936f69e537b083e22bbc43b06510dc3280c50..f49f3b7545e7997d00be3740cf70b06fbef6f7d3)the refactor/schema/profile branch from

[to](https://github.com/vllm-project/guidellm/commit/618936f69e537b083e22bbc43b06510dc3280c50)

`618936f`


`f49f3b7`

[Compare](https://github.com/vllm-project/guidellm/compare/618936f69e537b083e22bbc43b06510dc3280c50..f49f3b7545e7997d00be3740cf70b06fbef6f7d3)

June 2, 2026 16:28


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 2, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Few more nits. Also I forgot to mention earlier but in the original proposal I moved `warmup`

and `cooldown`

config into the `ProfileArgs`

(see [#724](https://github.com/vllm-project/guidellm/issues/724)) since currently they are fed directly into the scheduler. We can tackle that later though if we just want to get this in to unblock other work.

[src/guidellm/benchmark/profiles/profile.py](https://github.com/vllm-project/guidellm/pull/753/files/9f24445ada63ac0d72671a56e75772e330800d67#diff-2e999c6d89e5329280d36c7fbb7827a638815dc4f28123dddcc40abfe9587bab)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/753/files/9f24445ada63ac0d72671a56e75772e330800d67#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/753/files/9f24445ada63ac0d72671a56e75772e330800d67#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)Outdated

- move random_seed to Profile - formalize abstraction of Profile with ABC Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 3, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 3, 2026

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[dbutenhof](https://github.com/dbutenhof)added a commit to dbutenhof/guidellm that referenced this pull request

Jun 5, 2026

This follows up on a discussion in[vllm-project#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)added a commit to dbutenhof/guidellm that referenced this pull request

Jun 6, 2026

This follows up on a discussion in[vllm-project#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 8, 2026

## Summary Continuing CLI refactoring: modify the Profile classes to use ProfileArgs instances built from `kind=<name>` payloads like backends and datasets. ## Details Use CLI to construct a ProfileArgs instance, which is then used to build the Profile. Like datasets and backends, we now identify a profile "kind", as `--profile kind=constant[,param=value...]`; directly specified parameters supercede inherited global CLI values like `--rate`. Use more meaningful aliases for the global "rate" to match the previous internal names (e.g., "sweep_size"). This also exposes previously hidden parameters like the sweep's `strategy_type` to run poisson instead of constant async. ## Test Plan Manually tested all profiles, including Replay. ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue May 26 15:24:51 2026 -0400 CLI profile refactor Use CLI to construct a ProfileArgs instance, which is then used to build the Profile. Like datasets and backends, we now identify a profile "kind", as `--profile kind=constant[,param=value...]`; directly specified parameters supercede inherited global CLI values like `--rate`. Use more meaningful aliases for the global "rate" to match the previous internal names (e.g., "sweep_size"). This also exposes previously hidden parameters like the sweep's `strategy_type` to run poisson instead of constant async. Manually tested all profiles, including Replay. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]6b3d675[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 2 09:27:53 2026 -0400 Review comments & cleanup - Remove Pydantic aspect of Profile class, holding a reference to ProfileArgs. - Remove constraints from ProfileArgs, to isolate construction and remove some report serialization issues. - Change ProfileArgs deserialization to "forbid" unknown keys. We have two classes of profile parameter that aren't "universal": - data and data_samples are used only by Replay: we remove these from other ProfileArgs -- this will be refactored later. - Although random_seed isn't used by all profiles, it's a global used throughout GuideLLM, so we promote this to the base ProfileArgs for convenience. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]9f24445[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 2 12:13:06 2026 -0400 Odd .. CI "pre-commit" check found something local pre-commit didn't. Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]f49f3b7[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 2 19:54:56 2026 -0400 More review changes - move random_seed to Profile - formalize abstraction of Profile with ABC Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]2c64d1a[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 2 19:59:17 2026 -0400 Just in case the CI went crazy due to pre-commit updates ... Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]744b3ec

[dbutenhof](https://github.com/dbutenhof)added a commit to dbutenhof/guidellm that referenced this pull request

Jun 9, 2026

This follows up on a discussion in[vllm-project#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)added a commit to dbutenhof/guidellm that referenced this pull request

Jun 9, 2026

This follows up on a discussion in[vllm-project#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 9, 2026

## Summary Let `BenchmarkGenerativeTextArgs` build the `ProfileArgs` embedded object. ## Details This is a refactoring that follows up on a discussion during review of[#753]. The key was to shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on a built loader by the time we need it. Now we can fully build ProfileArgs up front. ## Test Plan Ensure proper parsing of profile parameters, particularly, - [x] merging of global rate & rampup into `ProfileArgs` dict - [x] proper handling of global `--rate` with aliased `ProfileArgs` parameters E.g.: - uv run guidellm benchmark --target http://<vllm> --max-seconds 10 --profile kind=replay,time_scale=0.3 --data kind=trace_synthetic,path=${HOME}/replay.jsonl --rate 5 - uv run guidellm benchmark --target http://<vllm> --max-seconds 10 --data "kind=synthetic_text,prompt_tokens=256,output_tokens=128" --rate 5 --profile kind=async ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Fri Jun 5 02:03:41 2026 -0400 Build ProfileArgs in BenchmarkGenerativeTextArgs This follows up on a discussion in]3e27713[#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit[Author: David Butenhof <dbutenho@redhat.com> Date: Fri Jun 5 15:04:53 2026 -0400 Pull random_seed back out of kwargs Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]66d9025[Author: David Butenhof <dbutenho@redhat.com> Date: Fri Jun 5 20:12:36 2026 -0400 Fix a typo Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]c3cf2d0[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 8 08:45:01 2026 -0400 Complain about duplicate rates More consistent behavior than ignoring one. Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]a11f2dd[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 9 16:21:31 2026 -0400 Fix merge queue test breakage (Yeah, that's why we *have* a merge queue!) Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]f240157

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 11, 2026

## Summary Uses a new format with a `kind` discriminator and separate args classes. Includes translation layer for the old CLI format to use the new constraints format. ## Details - For the CLI refactor - Does not expose the new format to the CLI yet. That will be a part of the refactor. - As discussed, I removed aliases for the constraints. We can discuss if I chose the right option for each. I chose `max_duration` instead of `max_seconds` since it's more generic and with the follow up refactor we can do `--constraint kind=max_duration,seconds=120`, which would enable `--constraint kind=max_duration,minutes=2`, or in the new format `--constraint max_duration seconds=120` ## Test Plan - Run the tests - Run benchmarks as usual ## Related Issues - Relates to[#753]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 9 14:22:47 2026 -0400 Refactor constraints Uses a new format with a kind discriminator and separate args classes. Includes translation layer for the old CLI format to use the new constraints format. Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]d6a2313[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 9 15:57:43 2026 -0400 Remove constraint aliases Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]04c6960[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 10 11:56:26 2026 -0400 Address review comments Remove old create method, remove unnecessary comments, and remove unnecessary static function. Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]03046f3[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 10 13:11:01 2026 -0400 Simplify constraints code paths and fix tests and CI Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]1e73fca[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 10 13:26:28 2026 -0400 Fix unit tests Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]f813642[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 10 17:51:12 2026 -0400 Remove legacy pathways and replace "enabled" for oversaturation constraint Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]f89bd7b[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 10 17:54:39 2026 -0400 Address review comments Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]05ca95f

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Continuing CLI refactoring: modify the Profile classes to use ProfileArgs instances built from

`kind=<name>`

payloads like backends and datasets.## Details

Use CLI to construct a ProfileArgs instance, which is then used to build the Profile.

Like datasets and backends, we now identify a profile "kind", as

`--profile kind=constant[,param=value...]`

; directly specified parameters supercede inherited global CLI values like`--rate`

.Use more meaningful aliases for the global "rate" to match the previous internal names (e.g., "sweep_size"). This also exposes previously hidden parameters like the sweep's

`strategy_type`

to run poisson instead of constant async.## Test Plan

Manually tested all profiles, including Replay.

## Related Issues

## Use of AI

Assisted-by: Cursor

## git log

commit

6b3d675Author: David Butenhof dbutenho@redhat.com

Date: Tue May 26 15:24:51 2026 -0400

commit

9f24445Author: David Butenhof dbutenho@redhat.com

Date: Tue Jun 2 09:27:53 2026 -0400

commit

f49f3b7Author: David Butenhof dbutenho@redhat.com

Date: Tue Jun 2 12:13:06 2026 -0400

commit

2c64d1aAuthor: David Butenhof dbutenho@redhat.com

Date: Tue Jun 2 19:54:56 2026 -0400

commit

744b3ecAuthor: David Butenhof dbutenho@redhat.com

Date: Tue Jun 2 19:59:17 2026 -0400

Assisted-by: Cursor

Signed-off-by: David Butenhof dbutenho@redhat.com