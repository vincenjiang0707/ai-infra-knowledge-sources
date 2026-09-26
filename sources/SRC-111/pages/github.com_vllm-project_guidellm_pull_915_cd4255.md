source: https://github.com/vllm-project/guidellm/pull/915

# Add example: benchmarking with local tokenizer and custom JSONL dataset - #915

## Conversation

|
Hi |

[miglis](https://github.com/miglis)

[force-pushed](https://github.com/vllm-project/guidellm/compare/7de165ac96a6bf035d328f42fc099b539d83bae7..ef4aa0241c47c5f2975fcf44c425efcfd5161748)the docs/jsonl-example branch from

[to](https://github.com/vllm-project/guidellm/commit/7de165ac96a6bf035d328f42fc099b539d83bae7)

`7de165a`


`ef4aa02`

[Compare](https://github.com/vllm-project/guidellm/compare/7de165ac96a6bf035d328f42fc099b539d83bae7..ef4aa0241c47c5f2975fcf44c425efcfd5161748)

July 8, 2026 11:44


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 8, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

There's some overlap with the `practice_on_vllm_simulator.md`

example -- for example it talks about downloading a tokenizer to run locally, although it doesn't specify the particular files.

Generally, more concrete examples are good. My comments are generally in areas where you're either too abstract or unnecessarily over-specified (like using unnecessary options to specify defaults or values inconsistent with your example)...

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)


**previously requested changes**

[sjmonson](https://github.com/sjmonson)Jul 8, 2026

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

[miglis](https://github.com/miglis)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5366e5f8d45ffa6d30b058cc075a10ca525317b1..a6930641f51956abb34e716b02f8b86c018c22c2)the docs/jsonl-example branch from

[to](https://github.com/vllm-project/guidellm/commit/5366e5f8d45ffa6d30b058cc075a10ca525317b1)

`5366e5f`


`a693064`

[Compare](https://github.com/vllm-project/guidellm/compare/5366e5f8d45ffa6d30b058cc075a10ca525317b1..a6930641f51956abb34e716b02f8b86c018c22c2)

July 9, 2026 13:55

|
Hi |

…L dataset Adds docs/examples/custom-jsonl-dataset.md, showing how to run GuideLLM against an OpenAI-compatible endpoint using only local tokenizer files (tokenizer.json, tokenizer_config.json, special_tokens_map.json) and a custom JSONL prompt dataset. Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

To keep example so readers understand the options exists. Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

[miglis](https://github.com/miglis)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1f841f9832cd84ef6f795d0f3aee0e50ac781d2a..e2e7c63ca3bb1c981bdcd800be68a9df400c5dba)the docs/jsonl-example branch from

[to](https://github.com/vllm-project/guidellm/commit/1f841f9832cd84ef6f795d0f3aee0e50ac781d2a)

`1f841f9`


`e2e7c63`

[Compare](https://github.com/vllm-project/guidellm/compare/1f841f9832cd84ef6f795d0f3aee0e50ac781d2a..e2e7c63ca3bb1c981bdcd800be68a9df400c5dba)

July 9, 2026 14:04

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

… 3 can be ignored Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 10, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This is improving -- sorry, but still a few more problems.

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files/aaa9cc90c3c259621915fab75b0f03a610f2a331#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files/aaa9cc90c3c259621915fab75b0f03a610f2a331#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files/aaa9cc90c3c259621915fab75b0f03a610f2a331#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)Outdated

|
By the way, you need to fix your file formatting: ```
run markdown formatter...................................................Failed
- hook id: mdformat
- files were modified by this hook
``` So, when you're making further changes, ```
$ pip install pre-commit
$ pre-commit install
$ pre-commit run
``` It will give you a message like the CI's message above ... only in this case, the modified files are in your local branch. Add the changes to your git index, then you can re-run |

Replaced with commands to run guidellm manually. Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Merge the "copy only these three files" statement with the Mistral-family caveat into one coherent paragraph, removing the contradiction between them. Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>

Signed-off-by: Michael Stucki <michael.stucki99@gmail.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 13, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

One somewhat awkward sentence could be clarified.

And while I'm basically happy about removing the extra steps of the containerized deployment and the unnecessary default options, I also feel just a little bad that I pushed you away from what you were trying to do. (Just a little: but... "sorry".)

[docs/examples/custom-jsonl-dataset.md](https://github.com/vllm-project/guidellm/pull/915/files/b6661cba90b4af195838df94a4aaeb3aca28da79#diff-fdc89e475628675766b8b4227964a73e311059d851f6741c6fe00b69fb64cb27)


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 15, 2026

###
**
**[SkiHatDuckie](https://github.com/SkiHatDuckie)
left a comment

**left a comment**

[SkiHatDuckie](https://github.com/SkiHatDuckie)

There was a problem hiding this comment.

I've got no complaints.

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

|
|

## ☑️ Command
|

[dbutenhof](https://github.com/dbutenhof)dismissed

[sjmonson](https://github.com/sjmonson)’s

[stale review](https://github.com#pullrequestreview-4655215656)

July 15, 2026 18:40

The substance of Sam's comment has been met.

|
|

## ✅ Pull request refreshed |

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

benchmarking with local tokenizer and custom JSONL dataset

Adds docs/examples/custom-jsonl-dataset.md, showing how to run GuideLLM against an OpenAI-compatible endpoint using only local tokenizer files (tokenizer.json, tokenizer_config.json, special_tokens_map.json) and a custom JSONL prompt dataset.

## Use of AI

## git log

commit

166f012Author: Michael Stucki michael.stucki99@gmail.com

Date: Wed Jul 8 13:39:29 2026 +0200

commit

b065f94Author: Michael Stucki michael.stucki99@gmail.com

Date: Thu Jul 9 15:30:50 2026 +0200

commit

cd6507aAuthor: Michael Stucki michael.stucki99@gmail.com

Date: Thu Jul 9 15:54:17 2026 +0200

commit

c5b3c2cAuthor: Michael Stucki michael.stucki99@gmail.com

Date: Thu Jul 9 16:02:51 2026 +0200

commit

e2e7c63Author: Michael Stucki michael.stucki99@gmail.com

Date: Thu Jul 9 16:03:26 2026 +0200

commit

ed1b8ecAuthor: Michael Stucki michael.stucki99@gmail.com

Date: Fri Jul 10 11:23:46 2026 +0200

commit

ebf524bAuthor: Michael Stucki michael.stucki99@gmail.com

Date: Fri Jul 10 11:31:17 2026 +0200

commit

aaa9cc9Author: Michael Stucki michael.stucki99@gmail.com

Date: Fri Jul 10 11:34:29 2026 +0200

commit

0c26bd2Author: Michael Stucki michael.stucki99@gmail.com

Date: Sun Jul 12 20:36:06 2026 +0200

commit

160c905Author: Michael Stucki michael.stucki99@gmail.com

Date: Sun Jul 12 20:42:16 2026 +0200

commit

d2d5707Author: Michael Stucki michael.stucki99@gmail.com

Date: Sun Jul 12 20:46:12 2026 +0200

commit

b6661cbAuthor: Michael Stucki michael.stucki99@gmail.com

Date: Sun Jul 12 20:58:42 2026 +0200

Signed-off-by: Michael Stucki michael.stucki99@gmail.com