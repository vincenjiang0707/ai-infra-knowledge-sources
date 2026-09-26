source: https://github.com/vllm-project/guidellm/pull/799

# Simplify constraint parameter names - #799

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jun 16, 2026

|
Draft because I quickly pushed the basic renaming -- but more work is needed for the current CLI and for unit testing. I wouldn't mind early feedback on the parameter names, especially for the oversaturation parameters (which I left alone having no better ideas right now...) |

|
The proposal seems good. I'm open to your proposed rename of "mode". Sam and I came up with those mode names, and your proposed names are a little more explicit, so that's helpful. |

|
I think these all sound good including the |

[dbutenhof](https://github.com/dbutenhof)marked this pull request as ready for review

June 16, 2026 22:31


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 17, 2026


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 17, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

There are some new merge conflicts due to the CLI refactor PR being merged.

Yeah -- I started working on that after the meeting, but I wanted to get out hiking. I'm nearly ready to push another commit. |

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9b5ff84c5715cd70be823f5a8e160ad5424815fa..705b15ca9141450f22509a3b3f48744b72d3a50e)the refactor/constraint branch from

[to](https://github.com/vllm-project/guidellm/commit/9b5ff84c5715cd70be823f5a8e160ad5424815fa)

`9b5ff84`


`705b15c`

[Compare](https://github.com/vllm-project/guidellm/compare/9b5ff84c5715cd70be823f5a8e160ad5424815fa..705b15ca9141450f22509a3b3f48744b72d3a50e)

June 17, 2026 20:52

|
I'm seeing repeated local e2e failures -- but if there's any code problem I can fix, I can't see any sign of it in the output. Looks like server timeouts, and I'm reluctant to just blindly mess with the timeouts. |

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/705b15ca9141450f22509a3b3f48744b72d3a50e..4bfc3ef2d9f00a8c54c623d6b8600b5599a77040)the refactor/constraint branch from

[to](https://github.com/vllm-project/guidellm/commit/705b15ca9141450f22509a3b3f48744b72d3a50e)

`705b15c`


`4bfc3ef`

[Compare](https://github.com/vllm-project/guidellm/compare/705b15ca9141450f22509a3b3f48744b72d3a50e..4bfc3ef2d9f00a8c54c623d6b8600b5599a77040)

June 17, 2026 21:59

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4bfc3ef2d9f00a8c54c623d6b8600b5599a77040..3c1a3f8be1da866c0ff93e7752241292662113d6)the refactor/constraint branch from

[to](https://github.com/vllm-project/guidellm/commit/4bfc3ef2d9f00a8c54c623d6b8600b5599a77040)

`4bfc3ef`


`3c1a3f8`

[Compare](https://github.com/vllm-project/guidellm/compare/4bfc3ef2d9f00a8c54c623d6b8600b5599a77040..3c1a3f8be1da866c0ff93e7752241292662113d6)

June 17, 2026 23:09

|
|

## Merge Queue Status🛑 Queue command has been cancelled |


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 18, 2026


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 18, 2026

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/3c1a3f8be1da866c0ff93e7752241292662113d6..6e6627524051803459eb8fe02c2a4854066b6c88)the refactor/constraint branch from

[to](https://github.com/vllm-project/guidellm/commit/3c1a3f8be1da866c0ff93e7752241292662113d6)

`3c1a3f8`


`6e66275`

[Compare](https://github.com/vllm-project/guidellm/compare/3c1a3f8be1da866c0ff93e7752241292662113d6..6e6627524051803459eb8fe02c2a4854066b6c88)

June 18, 2026 02:15

|
The E2E tests timed out again. |

## Merge Queue Status
This pull request spent
|

Signed-off-by: David Butenhof <dbutenho@redhat.com>

e2e isn't succeeding. I don't see any error indications that don't look like timeouts, so I'm hoping I got all the real problems. Signed-off-by: David Butenhof <dbutenho@redhat.com>

So the over-saturation e2e test fails because I missed an "active" test in the scheduler. I like ENUMs. Why don't we use ENUMs? Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6e6627524051803459eb8fe02c2a4854066b6c88..f2442994ed4cdb41f9c9878bb2847b459614604a)the refactor/constraint branch from

[to](https://github.com/vllm-project/guidellm/commit/6e6627524051803459eb8fe02c2a4854066b6c88)

`6e66275`


`f244299`

[Compare](https://github.com/vllm-project/guidellm/compare/6e6627524051803459eb8fe02c2a4854066b6c88..f2442994ed4cdb41f9c9878bb2847b459614604a)

June 18, 2026 08:25

More than that. Took me hours to finally realize that I broke one of the test cases with the oversaturation "mode" change. Too many literal "active" strings scattered through the code, and I missed one I should have changed ... but the constant timeouts kept me from discovering that. |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 18, 2026

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

## Summary With the new CLI constraint syntax, specifying `--constraint max_requests max_requests=<n>` is awkward. Simplify the parameter names to be more expressive, like `--constraint max_requests count=<n>` ## Details - `--constraint max_duration seconds=60` - `--constraint max_requests count=1000` - `--constraint max_errors count=10` - `--constraint max_error_rate rate=0.1,window=100` - `--constraint max_global_error_rate rate=0.2,minimum=10` - `--constraint over_saturation mode=enforce,min_seconds=30,max_window_seconds=120,moe_threshold=2,minimum+ttft=2.5,maximum_window_ratio=0.75,minimum_window_size=5,confidence=0.95` > **NOTES** - I didn't rename the parameters for "over_saturation" -- there are a lot and the meanings are fairly specific. ## Test Plan - [ ] Manually test that constraints are parsed correctly - [x] Unit tests have been appropriately updated. ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 16 13:39:29 2026 -0400 Simplify constraint parameter names Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]f1f8a14[Author: David Butenhof <dbutenho@redhat.com> Date: Wed Jun 17 16:49:08 2026 -0400 Fix rebase e2e isn't succeeding. I don't see any error indications that don't look like timeouts, so I'm hoping I got all the real problems. Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]25e8f92[Author: David Butenhof <dbutenho@redhat.com> Date: Thu Jun 18 04:24:58 2026 -0400 I hate literal string values So the over-saturation e2e test fails because I missed an "active" test in the scheduler. I like ENUMs. Why don't we use ENUMs? Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>]f244299

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

## Summary With the new CLI constraint syntax, specifying `--constraint max_requests max_requests=<n>` is awkward. Simplify the parameter names to be more expressive, like `--constraint max_requests count=<n>` ## Details - `--constraint max_duration seconds=60` - `--constraint max_requests count=1000` - `--constraint max_errors count=10` - `--constraint max_error_rate rate=0.1,window=100` - `--constraint max_global_error_rate rate=0.2,minimum=10` - `--constraint over_saturation mode=enforce,min_seconds=30,max_window_seconds=120,moe_threshold=2,minimum+ttft=2.5,maximum_window_ratio=0.75,minimum_window_size=5,confidence=0.95` > **NOTES** - I didn't rename the parameters for "over_saturation" -- there are a lot and the meanings are fairly specific. ## Test Plan - [ ] Manually test that constraints are parsed correctly - [x] Unit tests have been appropriately updated. ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 16 13:39:29 2026 -0400 Simplify constraint parameter names Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]f1f8a14[Author: David Butenhof <dbutenho@redhat.com> Date: Wed Jun 17 16:49:08 2026 -0400 Fix rebase e2e isn't succeeding. I don't see any error indications that don't look like timeouts, so I'm hoping I got all the real problems. Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]25e8f92[Author: David Butenhof <dbutenho@redhat.com> Date: Thu Jun 18 04:24:58 2026 -0400 I hate literal string values So the over-saturation e2e test fails because I missed an "active" test in the scheduler. I like ENUMs. Why don't we use ENUMs? Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>]f244299

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary With the new CLI constraint syntax, specifying `--constraint max_requests max_requests=<n>` is awkward. Simplify the parameter names to be more expressive, like `--constraint max_requests count=<n>` ## Details - `--constraint max_duration seconds=60` - `--constraint max_requests count=1000` - `--constraint max_errors count=10` - `--constraint max_error_rate rate=0.1,window=100` - `--constraint max_global_error_rate rate=0.2,minimum=10` - `--constraint over_saturation mode=enforce,min_seconds=30,max_window_seconds=120,moe_threshold=2,minimum+ttft=2.5,maximum_window_ratio=0.75,minimum_window_size=5,confidence=0.95` > **NOTES** - I didn't rename the parameters for "over_saturation" -- there are a lot and the meanings are fairly specific. ## Test Plan - [ ] Manually test that constraints are parsed correctly - [x] Unit tests have been appropriately updated. ## Related Issues N/A --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Tue Jun 16 13:39:29 2026 -0400 Simplify constraint parameter names Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]f1f8a14[Author: David Butenhof <dbutenho@redhat.com> Date: Wed Jun 17 16:49:08 2026 -0400 Fix rebase e2e isn't succeeding. I don't see any error indications that don't look like timeouts, so I'm hoping I got all the real problems. Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]25e8f92[Author: David Butenhof <dbutenho@redhat.com> Date: Thu Jun 18 04:24:58 2026 -0400 I hate literal string values So the over-saturation e2e test fails because I missed an "active" test in the scheduler. I like ENUMs. Why don't we use ENUMs? Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Signed-off-by: David Butenhof <dbutenho@redhat.com>]f244299

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

With the new CLI constraint syntax, specifying

`--constraint max_requests max_requests=<n>`

is awkward. Simplify the parameter names to be more expressive, like`--constraint max_requests count=<n>`

## Details

`--constraint max_duration seconds=60`

`--constraint max_requests count=1000`

`--constraint max_errors count=10`

`--constraint max_error_rate rate=0.1,window=100`

`--constraint max_global_error_rate rate=0.2,minimum=10`

`--constraint over_saturation mode=enforce,min_seconds=30,max_window_seconds=120,moe_threshold=2,minimum+ttft=2.5,maximum_window_ratio=0.75,minimum_window_size=5,confidence=0.95`

## Test Plan

## Related Issues

N/A

## Use of AI

## git log

commit

f1f8a14Author: David Butenhof dbutenho@redhat.com

Date: Tue Jun 16 13:39:29 2026 -0400

commit

25e8f92Author: David Butenhof dbutenho@redhat.com

Date: Wed Jun 17 16:49:08 2026 -0400

commit

f244299Author: David Butenhof dbutenho@redhat.com

Date: Thu Jun 18 04:24:58 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com