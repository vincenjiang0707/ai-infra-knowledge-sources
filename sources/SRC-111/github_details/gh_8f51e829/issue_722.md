# [Issue #722] Turn and Conversation Metrics Plan

source: https://github.com/vllm-project/guidellm/issues/722
state: open | updated: 2026-07-25T12:59:17Z
labels: 

## 正文

Here is an AI generated proposal for new turn and conversation metrics to add to GuideLLM:

# Conversation-Level and Turn-by-Turn Metrics

## Current State

Today, all metrics in `GenerativeMetrics.compile()` treat requests as a flat bag -- no grouping by `conversation_id` or awareness of `turn_index`. The raw data for grouping already exists (`RequestInfo.conversation_id`, `RequestInfo.turn_index`, `RequestTimings.*`), but nothing aggregates it.

---

## Turn-by-Turn Metrics

These are per-request metrics that become meaningful when **sliced by turn position**. The key insight: turn position affects performance (history grows, KV cache state changes, scheduling dependencies emerge).

### Timing metrics sliced by turn position

- **TTFT for first turns only** (`turn_index == 0`): Cold-start latency with no conversation history. This is the "first impression" latency.
- **TTFT for last turns only** (`turn_index == max for that conversation`): Latency with maximum history context. Shows worst-case TTFT as context grows.
- **TTFT by turn index** (distribution per index 0, 1, 2, ...): Shows how TTFT degrades (or stays flat with good prefix caching) as conversation progresses.
- **Request latency by turn position**: Same slicing as TTFT -- first, last, per-index. Captures total turn time, not just time-to-first-token.
- **ITL (inter-token latency) by turn position**: Does decoding speed degrade as history grows?

### Throughput metrics sliced by turn position

- **Output tokens/sec by turn position**: Does generation throughput drop with longer contexts?
- **Prompt tokens by turn position**: Quantifies context growth. First turn has minimal prompt; last turn has full history. Useful for understanding the "cost of history."

### Turn scheduling metrics

- **Turn queue/wait time by position**: Later turns in a conversation depend on earlier turns completing. How long do they wait?
- **Turn gap time**: Time between one turn's `request_end` and the next turn's `request_start` within the same conversation. Captures scheduling overhead for dependent turns.

---

## Conversation-Level Metrics

These aggregate across all turns of a single conversation, then produce distributions across all conversations.

### Time metrics

- **End-to-end conversation time**: Wall-clock from first turn's `request_start` (or `targeted_start`) to last turn's `request_end` (or `resolve_end`). The total time a "user" would experience.
- **Total server processing time**: Sum of `request_latency` across all turns in the conversation. Pure compute time.
- **Total idle/gap time**: `e2e_time - total_server_time`. Time spent not generating -- scheduling overhead, queue waits between turns, etc.
- **Percent time on server**: `total_server_time / e2e_time`. High values mean the server is the bottleneck; low values mean scheduling/queueing overhead dominates.
- **Percent time idle**: `1 - percent_on_server`. Useful for identifying whether multi-turn overhead is significant.
- **Average inter-turn gap**: Mean of gap times between consecutive turns. Captures the "think time" imposed by the system (not the user).

### Token metrics (per conversation)

- **Total prompt tokens**: Sum across turns. Shows the true cost of a conversation (history re-processing).
- **Total output tokens**: Sum across turns. Total useful generation.
- **Total tokens**: Combined.
- **Prompt token growth rate**: How much does prompt size increase per turn? (Linear = naive history append; sublinear = summarization/truncation.)
- **Effective conversation throughput**: `total_output_tokens / e2e_time`. Unlike per-request throughput, this accounts for inter-turn gaps and gives a realistic "useful output rate."

### Conversation success/completion metrics

- **Conversation completion rate**: Fraction of conversations where all turns completed successfully (no errors, no cancellations).
- **Turns completed per conversation**: Distribution. For errored conversations, shows how far they got.
- **First error turn index**: For conversations with errors, which turn failed?

### Conversation count/shape metrics

- **Turns per conversation**: Distribution of conversation lengths in the benchmark run.
- **Conversation count**: Total conversations in the measurement window.

---

### New schema objects needed

- **`ConversationMetrics`** (new `StandardBaseDict`): holds conversation-level distribution summaries (e2e time, server time, idle time, completion rate, etc.)
- **`TurnPositionMetrics`** (new `StandardBaseDict`): holds turn-position-sliced distributions (TTFT by position, latency by position, etc.)
- Both would be fields on `GenerativeMetrics`



### CSV output changes

New columns would be added to [`src/guidellm/benchmark/outputs/csv.py`](src/guidellm/benchmark/outputs/csv.py) in a new "Conversation Metrics" group, following the existing pattern of `_add_stats_for_metric`.

---

## Open Questions

- **Single-turn conversations**: When every conversation has exactly 1 turn, conversation metrics collapse to per-request metrics. Should we skip conversation metrics entirely for single-turn runs, or show them as a degenerate case?
- **Incomplete conversations**: If turn 2 of 5 errors and turns 3-5 are cancelled, how do we handle conversation e2e time? Use last attempted turn? Last completed turn?
- **Turn gap attribution**: The gap between turns includes scheduler queue time + multi-turn dependency wait. Should we try to separate these, or report the combined gap?


## 评论 (1)

### dbutenhof · 2026-05-07

Those look great

Open questions (top-of-mind first impressions):

- *Single-turn conversations* -- yeah. Simplicity vs consistency. First == Last, etc. Ultimately I fear that showing the degenerate per-turn breakdowns might be just annoying here.
- *Incomplete conversations* -- yeah, aggregating conversation (or "last turn") metrics when each conversation is at a different turn isn't likely to be helpful. Dropping back to the highest completed term? Well, maybe -- but it's not a reflection of the theoretical intent. Maybe do the per-turn metrics and warn that all conversations weren't completed?
- *Turn gap attribution* -- you mean separating engine gap from GuideLLM scheduling gap. It all factors in end-to-end time, so skipping GuideLLM time leaves gaps in the gap data, while silently aggregating it doesn't lead to engine performance metrics. Separating client latency from server latency might work. I suppose we could even report an end-to-end time excluding client scheduling latency?
