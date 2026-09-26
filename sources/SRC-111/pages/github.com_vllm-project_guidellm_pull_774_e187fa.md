source: https://github.com/vllm-project/guidellm/pull/774

# Build ProfileArgs in BenchmarkGenerativeTextArgs - #774

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Jun 5, 2026


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 5, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Small nit but not really blocking. Otherwise looks good.

[src/guidellm/benchmark/profiles/asynchronous.py](https://github.com/vllm-project/guidellm/pull/774/files#diff-5e2311a4fbd8afc3bb3cf7f32311b7144d5a067f46506309dbaa6a2ca73aa3c8)Outdated

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/38e625145d0f5288cb17a16c7190d20043b6188e..fecc715d0675d31c1213be0550b004bed269c0e9)the refactor/redata branch from

[to](https://github.com/vllm-project/guidellm/commit/38e625145d0f5288cb17a16c7190d20043b6188e)

`38e6251`


`fecc715`

[Compare](https://github.com/vllm-project/guidellm/compare/38e625145d0f5288cb17a16c7190d20043b6188e..fecc715d0675d31c1213be0550b004bed269c0e9)

June 5, 2026 19:08

[src/guidellm/benchmark/profiles/throughput.py](https://github.com/vllm-project/guidellm/pull/774/files#diff-59dd73352976d490feb98be3d2b68ad4559b00f77724ed8c7f5a381b083d2f47)Outdated

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/774/files#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)

| profile=args.profile, | ||
| rate=args.rate, | ||
| random_seed=args.random_seed, | ||
| rampup=args.rampup, |

There was a problem hiding this comment.

Is the rampup field this was referencing still used anywhere?

There was a problem hiding this comment.

It's referenced in `ProfileArgs`

. (Which, as Sam pointed out earlier, is really weird because it's a completely different path from warmup & cooldown, and shouldn't be -- but that's beyond the scope of this PR.) Anyway, it *was* needed because we built `ProfileArgs`

here; but we no longer do.

There was a problem hiding this comment.

It probably makes sense to create an issue then to note the odd design and retirement of that pathway.

There was a problem hiding this comment.

Yeah, we'd talked about unifying the paths for all of these; an issue makes sense, but when I started to think about writing one I got hung up on details and didn't get far.

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/fecc715d0675d31c1213be0550b004bed269c0e9..e4792f64ec501708f082d94df39d5e2325610832)the refactor/redata branch from

[to](https://github.com/vllm-project/guidellm/commit/fecc715d0675d31c1213be0550b004bed269c0e9)

`fecc715`


`e4792f6`

[Compare](https://github.com/vllm-project/guidellm/compare/fecc715d0675d31c1213be0550b004bed269c0e9..e4792f64ec501708f082d94df39d5e2325610832)

June 6, 2026 00:20


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 6, 2026

[src/guidellm/benchmark/profiles/concurrent.py](https://github.com/vllm-project/guidellm/pull/774/files#diff-669b161868bd7dc88be40e19fbb46f6657669d8c2745c889cd4cb5d62266f237)Outdated

[src/guidellm/benchmark/profiles/replay.py](https://github.com/vllm-project/guidellm/pull/774/files#diff-a6f16a84fe8992b6eca2a66b350f9fc57a827247cfe85620a71b92638713f190)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 8, 2026

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a98c255b7cad79c8f7eb72f0803303edd5646746..fc006405761c0298297ae0c77a506b8ddef0dffb)the refactor/redata branch from

[to](https://github.com/vllm-project/guidellm/commit/a98c255b7cad79c8f7eb72f0803303edd5646746)

`a98c255`


`fc00640`

[Compare](https://github.com/vllm-project/guidellm/compare/a98c255b7cad79c8f7eb72f0803303edd5646746..fc006405761c0298297ae0c77a506b8ddef0dffb)

June 9, 2026 13:22


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 9, 2026

## Merge Queue Status
This pull request spent
|

|
|

|
^ |

|
|

## Merge Queue Status
This pull request spent
|

This follows up on a discussion in[vllm-project#753]. Shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on built loader. Now we can fully build ProfileArgs up front. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

More consistent behavior than ignoring one. Signed-off-by: David Butenhof <dbutenho@redhat.com>

(Yeah, that's why we *have* a merge queue!) Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/fc006405761c0298297ae0c77a506b8ddef0dffb..f240157a121895d7bfb3d085c6687244215d1eb4)the refactor/redata branch from

[to](https://github.com/vllm-project/guidellm/commit/fc006405761c0298297ae0c77a506b8ddef0dffb)

`fc00640`


`f240157`

[Compare](https://github.com/vllm-project/guidellm/compare/fc006405761c0298297ae0c77a506b8ddef0dffb..f240157a121895d7bfb3d085c6687244215d1eb4)

June 9, 2026 20:22

|
|

## Merge Queue Status🛑 Queue command has been cancelled |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 9, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Let

`BenchmarkGenerativeTextArgs`

build the`ProfileArgs`

embedded object.## Details

This is a refactoring that follows up on a discussion during review of #753.

The key was to shuffle data/data_samples from ReplayProfileArgs to ReplayProfile so that we can rely on a built loader by the time we need it. Now we can fully build ProfileArgs up front.

## Test Plan

Ensure proper parsing of profile parameters, particularly,

`ProfileArgs`

dict`--rate`

with aliased`ProfileArgs`

parametersE.g.:

## Related Issues

N/A

## Use of AI

## git log

commit

3e27713Author: David Butenhof dbutenho@redhat.com

Date: Fri Jun 5 02:03:41 2026 -0400

commit

66d9025Author: David Butenhof dbutenho@redhat.com

Date: Fri Jun 5 15:04:53 2026 -0400

commit

c3cf2d0Author: David Butenhof dbutenho@redhat.com

Date: Fri Jun 5 20:12:36 2026 -0400

commit

a11f2ddAuthor: David Butenhof dbutenho@redhat.com

Date: Mon Jun 8 08:45:01 2026 -0400

commit

f240157Author: David Butenhof dbutenho@redhat.com

Date: Tue Jun 9 16:21:31 2026 -0400

Assisted-by: Cursor

Signed-off-by: David Butenhof dbutenho@redhat.com