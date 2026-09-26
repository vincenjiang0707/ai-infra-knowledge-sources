# [Issue #992] Implement full subagent WEKA trace replay

source: https://github.com/vllm-project/guidellm/issues/992
state: closed | updated: 2026-09-04T21:36:25Z
labels: priority-high, feature

## 正文

Complete WEKA format replay with full tool calling and branching conversation support.

Some references:

* https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/weka_trace_replay.md
* https://github.com/ai-dynamo/aiperf/pull/1070

## 评论 (1)

### QHarshil · 2026-09-01

I have been looking at this and measured a few things against the reference traces first. Posting what I found plus two design questions, since the answers change how this should be built.

@SkiHatDuckie you mentioned in #1012 that you would finish the WEKA replay if you found the time. Are you still planning to take this? I do not want to duplicate your work. If you are, I am happy to leave it with you and just contribute the smaller pieces.

First, something that is not really part of this issue. No trace that follows the format spec loads today, because validation requires the trace's column set to equal the required set:

```
DataNotSupportedError: The columns in features (['t', 'in', 'out', 'hash_ids'])
must be identical as the columns in the dataset:
['t', 'type', 'model', 'in', 'out', 'hash_ids', 'input_types', 'output_types', 'stop']
```

That hits the reference trace from the spec and the cc-traces-weka-no-subagents-051226 dataset that trace_replay.md links to. I opened #1072 for that. With it, the non-subagent reference trace loads and the subagent one then fails on the nested records, which is this issue.

The measurements below are against sample_trace_with_subagent.json from the spec repo (90 inference requests across the parent and four subagents) and the HF dataset (949 conversations, 136,118 requests).

1. The recorded prompt already contains the whole conversation. `in` is the full input for that request (64 * len(hash_ids) is approximately `in`, and sum(in) equals totals.parent_tokens.input exactly), and create_prompt synthesizes all of it. The linear chain in trace_common gives every turn a `full` parent edge, so the backend prepends walk-back history on top of a prompt that already has it. Through the pipeline on a three request trace:

```
main_0: recorded in=8  history_pairs=0 words_sent=8
main_1: recorded in=12 history_pairs=1 words_sent=20
main_2: recorded in=16 history_pairs=2 words_sent=36
```

Over the first 50 conversations of the HF dataset the median conversation sends 30x more input than was recorded. The aggregate is 554x, because the inflation grows with turn count and the longest conversation has 1,973 requests. That figure is the sum over every request of its recorded input plus the recorded input of every earlier request in the conversation, divided by total recorded input. It counts request text only, so it is a lower bound.

2. Turn shapes. Across the 90 requests:

```
tool_result -> text+tool_use, stop=tool_use : 60
tool_result -> tool_use,      stop=tool_use : 19
tool_result -> text,          stop=end_turn :  5
text        -> text+tool_use, stop=tool_use :  4
text        -> thinking+tool_use, tool_use  :  2
```

Only the five in the third row map onto tool_response_injection, and none are standard. Since TurnType is a single discriminator and tool_response_injection forces tool_choice="none", "consume a tool result and emit another tool call" has no representation. If tool flows are meant to be replayed faithfully, I think the input kind and the expected output need to be separate fields, with turn_type left alone for existing datasets.

3. hash_id_scope is a file level field we currently ignore. It is "global" in the subagent sample and "local" across all 949 HF conversations. Global means the ID namespace is shared across conversations in the file, so resetting the table per conversation is wrong for those. Within the sample, the parent uses IDs 1 to 761 and each of the four subagents starts at 762. Every pair of subagents shares exactly 164 IDs, so a per-scope table would give the same block different text. block_size is also a file level field we take from config.

4. Nested request timestamps restart at 0.0, so a child's absolute offset is subagent.t + child.t.

5. subagent_type is null in all four subagents of the sample, and input_types, output_types and stop are absent from the entire HF corpus, so none of those can be relied on.

Two questions.

The first is what to do about 1. Two options I can see:

- Use `new` edges for trace requests. Ordering is unchanged, since dag.py builds in_degree from every edge regardless of history_context. The `new` context is already documented for this case in conversation.py: "the consumer node's prompt already embeds the expected output, so no runtime data flow is needed". The cost is that history_len and turn_index become 0 for every trace request instead of 0, 1, 2 and so on.
- Keep the semantic edges and separate the dependency metadata from whether history is serialized into the request body. That keeps the turn metadata but adds a concept.

The first is smaller and looks like the abstraction that is already there, but the second is the only one that preserves the reported turn metadata, so I would rather you pick.

The second question is about subagent joins. The obvious compilation is that the parent's next request depends on every subagent leaf through `last`. The recording does not quite agree: main request [7] is at t=337.0, while the last request of subagent a87d76ff is at 217.311 + 123.0 = 340.3. So the recorded execution overlaps the nominal return. Should recorded timestamps stay authoritative, with nesting only carrying ownership, cache scope and the timestamp origin, or do you want nesting compiled into a hard fork and join barrier?

Once those are settled the rest is fairly mechanical and I am happy to do it.

