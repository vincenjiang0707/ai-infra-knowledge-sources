source: https://github.com/vllm-project/guidellm/pull/936

# Handle repeated `--output`

specifications consistently across run and from-file - #936

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

Contributor

|
Hi |

Both `guidellm run` and `benchmark from-file` collected outputs in a dict keyed by output kind, so repeating a kind (two json specs, two plot specs, etc.) overwrote earlier entries: run never generated the duplicate, and from-file generated both files but reported only the last. Resolve, generate, and report outputs from an ordered list in both paths so every --output is generated and reported. Signed-off-by: Pragadeesh122 <pragan189@gmail.com>

[Pragadeesh122](https://github.com/Pragadeesh122)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e0766c8c68418e26127ad68411819a8d775c4c83..bfffc67b13f7a8be30753a6450edf6e7ecb1cf7a)the fix/933-output-list-handling branch from

[to](https://github.com/vllm-project/guidellm/commit/e0766c8c68418e26127ad68411819a8d775c4c83)

`e0766c8`


`bfffc67`

[Compare](https://github.com/vllm-project/guidellm/compare/e0766c8c68418e26127ad68411819a8d775c4c83..bfffc67b13f7a8be30753a6450edf6e7ecb1cf7a)

July 17, 2026 21:02


[dbutenhof](https://github.com/dbutenhof)added

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jul 17, 2026

[dbutenhof](https://github.com/dbutenhof)requested review from

[SkiHatDuckie](https://github.com/SkiHatDuckie),

[dbutenhof](https://github.com/dbutenhof),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)

July 17, 2026 21:17


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 20, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 20, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This makes sense. I tested it and I can confirm that it works as intended.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

`--output`

may be specified multiple times, but two specs of thesame kindwere handled inconsistently and lossily. Both entrypoints collected outputs/results in a`dict`

keyed by output`kind`

, which cannot hold two outputs of the same kind:`guidellm run`

overwrote at resolve time, so a repeated kind (e.g.`--output kind=json,path=a.json --output kind=json,path=b.json`

) wasnever generated— only the last survived.`guidellm benchmark from-file`

generated both files butreported only the last.This is most visible with the new

`plot`

output from the issue, e.g.`--output kind=plot,dpi=72,path=plot.png --output kind=plot,dpi=300,path=plot.pdf`

.This change resolves, generates, and reports outputs from an ordered list in both paths, so every

`--output`

is generated and reported, consistently.## Details

`resolve_output_formats`

now returns an ordered`list[GenerativeBenchmarkerOutput]`

(one entry per spec, repeated kinds preserved) instead of a`dict[str, GenerativeBenchmarkerOutput]`

keyed by kind.`benchmark_generative_text`

(run) and`reimport_benchmarks_report`

(from-file) finalize and report over that list, collecting an ordered`list[tuple[str, Any]]`

of`(kind, result)`

.`dict[str, Any]`

to`list[tuple[str, Any]]`

. This is a public-API shape change, but unavoidable: a dict keyed by kind cannot represent duplicate kinds. The only in-repo consumers of the return value are tests (updated here); the two CLI callers discard it, and user-facing reporting happens inside the functions.`src/guidellm/benchmark/entrypoints.py`

and its tests; no new public types.## Test Plan

`tests/unit/benchmark/test_entrypoints.py`

:`resolve_output_formats`

preserves duplicate kinds as an ordered list.`tests/unit/entrypoints/test_benchmark_from_file_entrypoint.py`

to the list-shaped results and added a regression test: two same-kind outputs with different paths are both generatedandboth reported, in order.`tox -e lint-check`

and`tox -e type-check`

pass.`tox -e test-unit`

passes for these changes (the only failure observed locally was an unrelated, pre-existing`MaxDurationConstraint`

timing test that passes in isolation).`guidellm benchmark from-file benchmarks.json --output kind=json,path=a.json --output kind=json,path=b.json`

→ both`a.json`

and`b.json`

are created and both are reported in the console summary.## Related Issues

`--output`

lists #933## git log

commit

bfffc67Author: Pragadeesh122 pragan189@gmail.com

Date: Fri Jul 17 11:21:15 2026 -0500

Signed-off-by: Pragadeesh122 pragan189@gmail.com