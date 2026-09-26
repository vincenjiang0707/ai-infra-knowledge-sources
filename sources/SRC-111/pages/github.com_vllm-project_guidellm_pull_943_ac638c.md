source: https://github.com/vllm-project/guidellm/pull/943

# Update `guidellm preprocess dataset`

syntax to 0.7.x CLI style - #943

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jul 21, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Overall it looks good.

Instead of ignoring those tests, we should address the root of the problem. It appears that it's due to a change in resolution order in Pytnon 3.11.

Here is what AI recommends doing to fix this:

Instead of passing a string path to [@patch](https://github.com/patch), import the target module directly in your test file and use patch.object. This completely avoids string path resolution issues across Python versions:

Yeah, I hadn't tried |

Convert the CLI to a more modern form matching "run". This includes full registry specifications for dataset, tokenizer, and random seed. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Merge data config and short prompt handling into a clean registry class to modernize the interface along the lines of "run". Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

This allows limiting the number of samples we preprocess, which can be useful for extremely large datasets. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

Python 3.10 (which we still use in the CI) has problems with the mocking in a few new tests. Cursor came up with a messy and inelegant workaround that disrupted the product code imports: instead I'm just conditionally disabling the two failing tests until we bump the CI to 3.12. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b8879016e271959d2f7507d063e41316abe8f25a..0cef790b0aa70a063b310c65439383ae43172cc0)the feature/preprocess branch from

[to](https://github.com/vllm-project/guidellm/commit/b8879016e271959d2f7507d063e41316abe8f25a)

`b887901`


`0cef790`

[Compare](https://github.com/vllm-project/guidellm/compare/b8879016e271959d2f7507d063e41316abe8f25a..0cef790b0aa70a063b310c65439383ae43172cc0)

July 22, 2026 13:03

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I'll formally approve once you respond to my comments, since I don't want to trigger the auto-merge.

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/943/files/0cef790b0aa70a063b310c65439383ae43172cc0#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[src/guidellm/cli/preprocess/__init__.py](https://github.com/vllm-project/guidellm/pull/943/files/0cef790b0aa70a063b310c65439383ae43172cc0#diff-87b45d4d49ccc5b3b8c444c07e10003315c7b2123c3219c8d7af70aa41604333)

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 22, 2026

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/943/files/eda955dc0605c8ec737ad73bc3962a25cd6d30fa#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)

|
Queued — the merge queue status continues in |

[src/guidellm/data/entrypoints.py](https://github.com/vllm-project/guidellm/pull/943/files/eda955dc0605c8ec737ad73bc3962a25cd6d30fa#diff-580af024efad5f14fb7a7d2e179ed181d73642bc23f89037c732b99d5459cdc2)Outdated

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 22, 2026


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 22, 2026

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

GuideLLM 0.7.0 made massive changes to the

`run`

subcommand but left`preprocess dataset`

behind. Update and streamline the CLI style.## Details

`--strategy`

.`--data-loader`

as a way to supply a limit on the number of preprocessed samples. (I chose to let Cursor skip implementing the parallelism and shuffle options largely because the agent analysis was concerned about the amount of refactoring that would require. Since we didn't control parallelism before, and we can always shuffle later when we use the preprocessed dataset, this seemed acceptable.)## Test Plan

`guidellm preprocess dataset kind=huggingface,source=wikimedia/wikipedia,load_kwargs.split=train,load_kwargs.name=20231101.es out.jsonl --tokenizer kind=huggingface_auto,model=Qwen/Qwen3-0.6B,load_kwargs.use_fast=false --strategy kind=concatenate,delimiter=+,prompt_tokens=128,output_tokens=256,prompt_tokens_max=512,prompt_tokens_min=64 --seed kind=static,value=49 --data-loader kind=pytorch,samples=2048`

`guidellm preprocess dataset kind=huggingface,source=wikimedia/wikipedia,load_kwargs.split=train,load_kwargs.name=20231101.es out.jsonl --tokenizer kind=huggingface_auto,model=Qwen/Qwen3-0.6B,load_kwargs.use_fast=false --strategy kind=pad,pad=x,prompt_tokens=128,output_tokens=256,prompt_tokens_max=512,prompt_tokens_min=64 --seed kind=static,value=49 --data-loader kind=pytorch,samples=2048`

`guidellm preprocess dataset kind=huggingface,source=wikimedia/wikipedia,load_kwargs.split=train,load_kwargs.name=20231101.es out.jsonl --tokenizer kind=huggingface_auto,model=Qwen/Qwen3-0.6B,load_kwargs.use_fast=false --strategy kind=error,prompt_tokens=128,output_tokens=256,prompt_tokens_max=512,prompt_tokens_min=64 --seed kind=static,value=49 --data-loader kind=pytorch,samples=2048`

(fails with short prompt)`guidellm preprocess dataset kind=huggingface,source=wikimedia/wikipedia,load_kwargs.split=train,load_kwargs.name=20231101.es out.jsonl --tokenizer kind=huggingface_auto,model=Qwen/Qwen3-0.6B,load_kwargs.use_fast=false --strategy kind=ignore,prompt_tokens=128,output_tokens=256,prompt_tokens_max=512,prompt_tokens_min=64 --seed kind=static,value=49 --data-loader kind=pytorch,samples=2048`

(succeeds with many WARNING messages)## Related Issues

## N/A

## Use of AI

## git log

commit

2f793dfAuthor: David Butenhof dbutenho@redhat.com

Date: Fri Jul 17 08:48:05 2026 -0400

commit

511776dAuthor: David Butenhof dbutenho@redhat.com

Date: Fri Jul 17 16:38:34 2026 -0400

commit

d335fd8Author: David Butenhof dbutenho@redhat.com

Date: Fri Jul 17 16:57:15 2026 -0400

commit

c4bfcd7Author: David Butenhof dbutenho@redhat.com

Date: Tue Jul 21 14:57:32 2026 -0400

commit

0cef790Author: David Butenhof dbutenho@redhat.com

Date: Wed Jul 22 09:00:57 2026 -0400

commit

eda955dAuthor: David Butenhof dbutenho@redhat.com

Date: Wed Jul 22 14:30:45 2026 -0400

commit

6d5e083Author: David Butenhof dbutenho@redhat.com

Date: Wed Jul 22 16:56:56 2026 -0400

Assisted-by: Cursor

Signed-off-by: David Butenhof dbutenho@redhat.com