source: https://github.com/vllm-project/guidellm/pull/1155

# Implement `copies`

feature for synthetic traces - #1155

Open

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 6 commits into

Open

[jaredoconnell](https://github.com/jaredoconnell) wants to merge 6 commits into

[jaredoconnell](https://github.com/jaredoconnell)wants to merge 6 commits into

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 17, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Just comments, really -- nothing's a blocker; but I'll hold off a bit on approving just so in case Sam approves we don't auto-merge before you see the comments/questions here. 😁

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/1155/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[docs/guides/trace_replay.md](https://github.com/vllm-project/guidellm/pull/1155/files#diff-d1919f3fd587a605342ebbc06efb54fb7f3c1c0c0c94750935e927f956a242a5)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Sep 18, 2026

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9b884edd087541dad7a1d25b2321cfecfa66974a..84bcabf913136f067999114280824bf1c8624140)the feat/synthetic-trace-copies branch from

[to](https://github.com/vllm-project/guidellm/commit/9b884edd087541dad7a1d25b2321cfecfa66974a)

`9b884ed`


`84bcabf`

[Compare](https://github.com/vllm-project/guidellm/compare/9b884edd087541dad7a1d25b2321cfecfa66974a..84bcabf913136f067999114280824bf1c8624140)

September 19, 2026 02:30


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Cleaner ... a couple of minor follow-ups on the hash table rework.

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/1155/files#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 23, 2026

Contributor

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

This allows you to increase the apparent size of the dataset for long-running benchmarks. Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/284e963b760a6fcf07aa57e8fdaefbb4d8b9488c..2654056165bb2e1f945880f98a5bed27cd35e21c)the feat/synthetic-trace-copies branch from

[to](https://github.com/vllm-project/guidellm/commit/284e963b760a6fcf07aa57e8fdaefbb4d8b9488c)

`284e963`


`2654056`

[Compare](https://github.com/vllm-project/guidellm/compare/284e963b760a6fcf07aa57e8fdaefbb4d8b9488c..2654056165bb2e1f945880f98a5bed27cd35e21c)

September 23, 2026 22:22


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 24, 2026

Contributor

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This allows you to increase the apparent size of the dataset for long-running benchmarks.

## Details

`copy`

option.## Test Plan

You can test with all synthetic trace formats. Here is a command I used to test it, along with the attached file I used.


`guidellm run --backend "kind=openai_http,target=http://localhost:8000,request_format=/v1/chat/completions,validate_backend=false,model=Qwen/Qwen3-0.6B" --tokenizer "kind=huggingface_auto,model=Qwen/Qwen3-0.6B" --profile kind=replay --data "kind=trace_synthetic,source.kind=json_file,source.path=replay_stall_delayed_requests.jsonl,max_wait=1,max_session_wait=1,copies=4,min_concurrent_sessions=4" --constraint kind=max_duration,seconds=60`

## Related Issues

## Use of AI

## git log

commit

a512271Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 16 18:06:23 2026 -0400

commit

420e975Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 16 18:43:08 2026 -0400

commit

d9891a4Author: Jared O'Connell joconnel@redhat.com

Date: Fri Sep 18 21:47:35 2026 -0400

commit

e6d896aAuthor: Jared O'Connell joconnel@redhat.com

Date: Fri Sep 18 21:54:29 2026 -0400

commit

ccddae1Author: Jared O'Connell joconnel@redhat.com

Date: Fri Sep 18 22:28:24 2026 -0400

commit

2654056Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 23 13:45:44 2026 -0400

Generated-by: Cursor AI Grok 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com