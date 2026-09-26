source: https://github.com/vllm-project/guidellm/pull/789

# [v0.7 CLI Refactor] New internal top-level args / CLI - #789

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/603beaee038267a3e37e91da6bcd0985ce7d9ff4..1232555faf8db186f9e51dc0d79a5814a3563461)the refactor/schema/cli branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/603beaee038267a3e37e91da6bcd0985ce7d9ff4)

`603beae`


`1232555`

[Compare](https://github.com/vllm-project/guidellm/compare/603beaee038267a3e37e91da6bcd0985ce7d9ff4..1232555faf8db186f9e51dc0d79a5814a3563461)

June 15, 2026 16:34

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1232555faf8db186f9e51dc0d79a5814a3563461..e8567509f0f56fc2298df2a7622fc68ab71bf071)the refactor/schema/cli branch from

[to](https://github.com/vllm-project/guidellm/commit/1232555faf8db186f9e51dc0d79a5814a3563461)

`1232555`


`e856750`

[Compare](https://github.com/vllm-project/guidellm/compare/1232555faf8db186f9e51dc0d79a5814a3563461..e8567509f0f56fc2298df2a7622fc68ab71bf071)

June 15, 2026 18:02

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e8567509f0f56fc2298df2a7622fc68ab71bf071..b4088fa1248c2c51f6bc67cf03e72828194d305d)the refactor/schema/cli branch from

[to](https://github.com/vllm-project/guidellm/commit/e8567509f0f56fc2298df2a7622fc68ab71bf071)

`e856750`


`b4088fa`

[Compare](https://github.com/vllm-project/guidellm/compare/e8567509f0f56fc2298df2a7622fc68ab71bf071..b4088fa1248c2c51f6bc67cf03e72828194d305d)

June 15, 2026 18:08

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b4088fa1248c2c51f6bc67cf03e72828194d305d..22d591364d27080bb47809b1f5602d8172f57e6c)the refactor/schema/cli branch from

[to](https://github.com/vllm-project/guidellm/commit/b4088fa1248c2c51f6bc67cf03e72828194d305d)

`b4088fa`


`22d5913`

[Compare](https://github.com/vllm-project/guidellm/compare/b4088fa1248c2c51f6bc67cf03e72828194d305d..22d591364d27080bb47809b1f5602d8172f57e6c)

June 15, 2026 19:24

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

June 15, 2026 19:30

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

So when you say "remaining items on this PR", you actually mean "follow-up PRs before the results are useful"??

This confused me, until I discovered why overriding multiple `profile.rate`

values doesn't work -- it's not me, it's the code, and the unchecked item "Adapter for multi-benchmark (overrides) to fall back to multi-rate" suggests that's intentional.

In a way I really don't like abandoning the ideal that "each merged PR results in a consistent and usable product": we've already seen a few "bugs on 0.6.0, try `main`

", which won't be viable in many cases with this PR as it stands. But in the name of expediency, (and given this is already pretty big and deep), if you think that's the cleanest way forward, let's move on.

A couple of comments, though

-
your design shows

`--constraint max_duration seconds=60`

, but the actual param name in`MaxDurationConstraintArgs`

is`max_duration`

-- so the CLI syntax becomes`--constraint max_duration max_duration=60`

, which is awkward and redundant. Similar,`--constraint max_requests max_num=1000`

could be`--constraint max_requests count=1000`

or even`num=1000`

. -
I still haven't figured out the syntax for constraint

*overrides*, or else something's not working that I can't quite pinpoint. Whatever I've tried, oddly, breaks in`spec.constraint`

(`BenchmarkArgs`

) deserialization even though the parsed product is clearly under`.benchmarks`

.

Sorry I was in a hurry when I wrote that. I think everything tier 0/1 needs to land in this PR. The rest can probably be follow up. For now "Adapter for multi-benchmark" will probably just be a hack to convert multiple ProfileArgs into one with a rate list, just to get us to par with main.
Yeah this is due to
Not 100% sure what you mean. One thing I did forget though is that overrides are not validated until |

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

OK, that definitely qualifies as an ugly hack, but it does allow me to `--profile async max_concurrency=20 --override profile.rate 5,10,20`

and it works.

Constraint overrides are completely broken, but that's OK since it would have been a completely new feature.

Probably the "worst" consequence (for compatibility) is that given the way the parser works there's now no way to specify multiple rates *without* using `--override`

-- or a full JSON `--profile async '{"rate":[5,10]}'`

(which I wasn't sure would work, but apparently it does properly merge the `kind`

with the payload even though I failed to notice where that happened. 😁 I'm suitably impressed!)

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/789/files/1b65bbf3fb57efd9aa0c6d1b947b3e02623ecfad#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)

|
|
||
|
|
||
| _SKIP_FIELDS: frozenset[str] = frozenset({"profile"}) | ||
| _PROFILE_RATE_FIELDS: frozenset[str] = frozenset({"rate", "streams"}) |

There was a problem hiding this comment.

This has a few minor but perhaps interesting implications. When I split the CLI profile params from the old global `--rate`

, I used the old internal profile names. While it's true only async and concurrent support *lists* of "rates", `--rate`

also used to stand in for replay's `time_scale`

, sweep's `sweep_size`

, and throughput's `max_concurrency`

. All of which *accept* a list and simply discard all but the first value.

I'm not sure I care what happens with `--profile sweep '' --override profile.sweep_size 5,10,20`

in our new CLI -- but in your previous commit this would actually work, and now it'll fail with a spectacular stack trace ("Differing profile field 'sweep_size' cannot be merged."). Maybe that's good, and it doesn't really matter that it's a "cultural" change from before, I think... but, just to complicate things, I'm pointing it out.

[src/guidellm/benchmark/outputs/csv.py](https://github.com/vllm-project/guidellm/pull/789/files/3d376cfe938c56bf9387275360e3b4a2cb87d0f0#diff-75560721d3398336f7853516ad23e59a86e8562b65b5379cc5548650227fdc2f)

| class CSVBenchmarkOutputArgs(BenchmarkOutputArgs): | ||
| kind: Literal["csv"] = Field( | ||
| default="csv", | ||
| description="The kind of output.", |

There was a problem hiding this comment.

This description doesn't add value.

Maybe use "The discriminator to specify this kind of output"

[src/guidellm/benchmark/schemas/profiles.py](https://github.com/vllm-project/guidellm/pull/789/files/1b65bbf3fb57efd9aa0c6d1b947b3e02623ecfad#diff-246d796e56894c8df927cca5742656d8f0d2e8c5def7790228ddbd777b938d69)

| def _fail_on_duplicate_rate(cls, data: Any, key: str) -> Any: | ||
| """Fail if both "rate" and <key> are specified. | ||
|
|
||
| Some profile alias "rate" and a more specific key; if the user enters | ||
| both, either directly or via the global "--rate" option, we should fail. | ||
|
|
||
| for example: | ||
|
|
||
| "--profile kind=concurrent,streams=2.0 --rate 3" | ||
| "--profile kind=concurrent,streams=2,rate=3" | ||
|
|
||
| Pydantic won't resolve all cases consistently, so we need to fail explicitly. | ||
|
|
||
| :param data: The data to validate | ||
| :param key: The key to check for duplicate rate | ||
| :return: The data | ||
| """ | ||
| if isinstance(data, dict) and all(key in data for key in ("rate", key)): | ||
| raise ValueError(f"Both 'rate' and '{key}' cannot be specified.") | ||
| return data |

There was a problem hiding this comment.

Shall we retire `rate`

with the new format?

There was a problem hiding this comment.

This check is not profile-specific. But `async|constant|poisson`

still uses `rate`

because that was what the profile class used before (and I didn't instantly have a better alternative). While `concurrent`

uses `streams`

-- again because that was the previous internal name. Those are the only two profiles that support multi-strategy values and therefore allow the override repetition we're managing here. (So we could make it smarter and only allow `streams`

for `concurrent`

and `rate`

for the `async`

family; but this is a temporary hack anyway.)

As I mentioned elsewhere, before the new commit, the other profiles (aside from `synchronous`

which is picky) would accept a list of values but only use the first: with this change, they'll now *fail* if you specify multiple values. Which is probably fine, but it's a change we should be aware of.

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 17, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 17, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good as long as the following problems are addressed promptly:

- Improve the descriptions
- Fix the performance problem. This PR makes the startup time go up from ~6 seconds to around ~16 seconds. It's unacceptable.

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 22, 2026

## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Depends on #788

## TODO

Remaining items on this PR (in increasing priority)

## Tier 0

`BenchmarkGenerativeText`

## Tier 1

## Tier 2

## Tier 3

`guidellm config`

`guidellm explain`

`guidellm run -c config_builtin -c my_custom.yaml --backend ...`

`guidellm benchmark from-file`

to use new format## Summary

Implements the new internal format and

`guidellm run`

based off of #724.## Details

TODO

## Test Plan

TODO

## Related Issues

## Use of AI

## git log

commit

b6aecd2Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 4 15:40:27 2026 -0400

commit

3fed00cAuthor: Samuel Monson smonson@redhat.com

Date: Fri Jun 5 15:54:02 2026 -0400

commit

8a15a7dAuthor: Samuel Monson smonson@redhat.com

Date: Fri Jun 12 14:11:40 2026 -0400

commit

3fd07c3Author: Samuel Monson smonson@redhat.com

Date: Fri Jun 5 21:07:41 2026 +0000

commit

3c895b5Author: Samuel Monson smonson@redhat.com

Date: Fri Jun 12 14:18:40 2026 -0400

commit

76eb426Author: Samuel Monson smonson@redhat.com

Date: Fri Jun 12 19:28:10 2026 +0000

commit

7bc150fAuthor: Samuel Monson smonson@redhat.com

Date: Fri Jun 12 16:44:16 2026 -0400

commit

31932f2Author: Samuel Monson smonson@redhat.com

Date: Fri Jun 5 15:03:47 2026 -0400

commit

6a8cc64Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 16:58:48 2026 +0000

commit

548c7f6Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 11:00:39 2026 -0400

commit

346b91dAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 17:13:11 2026 +0000

commit

4cc2b94Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 15:18:23 2026 -0400

commit

3120b87Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 15:19:41 2026 -0400

commit

22d5913Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 15:21:01 2026 -0400

commit

759e0dcAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 18:44:58 2026 -0400

commit

3d376cfAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 15 18:51:02 2026 -0400

commit

20f3d08Author: Samuel Monson smonson@redhat.com

Date: Tue Jun 16 17:25:58 2026 +0000

commit

1b65bbfAuthor: Samuel Monson smonson@redhat.com

Date: Tue Jun 16 15:49:34 2026 -0400

commit

e6fdcfeAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jun 17 11:19:07 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com