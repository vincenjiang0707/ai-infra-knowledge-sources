source: https://github.com/vllm-project/guidellm/pull/949

# Added more useful error messages for kind inputs - #949

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 22, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

You missed `cli/preprocess/dataset.py`

-- although there are more registry-backed options after [#943](https://github.com/vllm-project/guidellm/pull/943) goes in. (Will this work for the positional `data`

argument? 🤔)

I'm about done for the day, but I'll pull this and experiment first thing tomorrow. Sounds like a great add for 0.7.2.

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/608538849401fbd0f86599419f1f5aff205843fa..858153815e25d7c1de7fb7d34ed09b7289596868)the feat/improved-kind-errmsg branch from

[to](https://github.com/vllm-project/guidellm/commit/608538849401fbd0f86599419f1f5aff205843fa)

`6085388`


`8581538`

[Compare](https://github.com/vllm-project/guidellm/compare/608538849401fbd0f86599419f1f5aff205843fa..858153815e25d7c1de7fb7d34ed09b7289596868)

July 22, 2026 21:22

Good point. I approved and merged your PR, rebased this onto it, and tested that command. Without adding the |

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d0eb233e49c60a76dbf714cb21bab7d6a861201c..0dfd6dfcb334d7d0609c330a31296a0afa7a08a3)the feat/improved-kind-errmsg branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/d0eb233e49c60a76dbf714cb21bab7d6a861201c)

`d0eb233`


`0dfd6df`

[Compare](https://github.com/vllm-project/guidellm/compare/d0eb233e49c60a76dbf714cb21bab7d6a861201c..0dfd6dfcb334d7d0609c330a31296a0afa7a08a3)

July 22, 2026 21:35

[src/guidellm/utils/click_pydantic.py](https://github.com/vllm-project/guidellm/pull/949/files#diff-08fbd9ea74f7b34cb6c2062e00cd577a32a656d1b88ba344bbb2643ea440e2e5)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 22, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This is great coverage for the registry options! Unfortunately it doesn't help for the positional dataset on `preprocess dataset`

, which just says "Error: Missing argument 'DATA'."

It's not using the registry model decorator because that was hardcoded to prepend the `--`

... but I suppose I should have reworked that chain instead of just using the low-level parser directly.

Probably not worth the time right now, since I really want to launch 0.7.2 ... but it probably won't be hard.

|
Queued — the merge queue status continues in |


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 23, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

Other than the one comment, I didn't see anything else that seemed off.


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 23, 2026


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 23, 2026

[src/guidellm/cli/reexport.py](https://github.com/vllm-project/guidellm/pull/949/files#diff-ee02b313f143746629ae654ff25951e2c86086d22c1dcfe26ff372af49518d11)Outdated


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 23, 2026

[src/guidellm/cli/benchmark/from_file.py](https://github.com/vllm-project/guidellm/pull/949/files#diff-504b2ce74c3c7dfc5cd7284acd22d0bc777b932a69f36d947569e13b564452d9)

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/82b5785f2a8c2408379283a0bbfc637e0f263913..d4c4afa321b83aa270b9cbdb303ef59f75c41a4e)the feat/improved-kind-errmsg branch from

[to](https://github.com/vllm-project/guidellm/commit/82b5785f2a8c2408379283a0bbfc637e0f263913)

`82b5785`


`d4c4afa`

[Compare](https://github.com/vllm-project/guidellm/compare/82b5785f2a8c2408379283a0bbfc637e0f263913..d4c4afa321b83aa270b9cbdb303ef59f75c41a4e)

July 23, 2026 17:00

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d4c4afa321b83aa270b9cbdb303ef59f75c41a4e..0f84a0731b1460039abf4f16e2d1a94402c3069d)the feat/improved-kind-errmsg branch from

[to](https://github.com/vllm-project/guidellm/commit/d4c4afa321b83aa270b9cbdb303ef59f75c41a4e)

`d4c4afa`


`0f84a07`

[Compare](https://github.com/vllm-project/guidellm/compare/d4c4afa321b83aa270b9cbdb303ef59f75c41a4e..0f84a0731b1460039abf4f16e2d1a94402c3069d)

July 23, 2026 17:00


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 23, 2026

|
GitHub Actions are definitely having problems in several PRs ... we're hung up on dependency installation before even getting to the actual tests. I guess I'm going to add to the merge queue and hope for the best, and just monitor through the afternoon. 🤬 |

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This adds a more useful error message to all

`kind`

-based discriminator inputs.I found the refactor to the

`kind`

system reduced the user friendliness of the CLI. I find this to be a huge improvement.## Details

`cls=RegistryAwareCommand`

that intersects all errors to determine if it's a kind based error, and if so it shows the expected format and the valid`kind`

values.Inputs to

`guidellm run`

and the error message created:Just

`--constraint`

Without the key-value pair format (

`--constraint nodict`

)Without the kind field ( --constraint nokind=test)

With an invalid kind value (--constraint kind=wrong)

Does not affect when you correctly input the kind (--constraint kind=max_duration)

Example with different CLI options (from-file and --output)

## Test Plan

`constraint`

or`output`

## Use of AI

## git log

commit

a762c9cAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Jul 22 16:19:22 2026 -0400

commit

47bd6d4Author: Jared O'Connell joconnel@redhat.com

Date: Wed Jul 22 17:34:01 2026 -0400

commit

0f84a07Author: Jared O'Connell joconnel@redhat.com

Date: Thu Jul 23 11:45:37 2026 -0400

Generated-by: Cursor AI

Signed-off-by: Jared O'Connell joconnel@redhat.com