# [Issue #1082] Add conversation-level concurrency for realistic multi-turn user and agent workloads

source: https://github.com/vllm-project/guidellm/issues/1082
state: open | updated: 2026-09-10T16:40:12Z
labels: 

## 正文

### Problem Statement

GuideLLM's concurrent profile controls the number of in-flight requests, not the number of active conversations or users.

For multi-turn workloads, GuideLLM releases a concurrency slot after each response. While that conversation is waiting for its configured requeue delay ("think time"), GuideLLM schedules requests from other conversations to keep every request slot occupied.

As a result, a benchmark configured with concurrency `N` can represent more than `N` users or agents. This makes it difficult to model workloads such as 10,000-40,000 concurrently active user or agent sessions, where:

- Each session has at most one request in flight.
- A session remains active during think time between turns.
- Think time should not allow another conversation to take that session's concurrency slot.
- The number of in-flight requests may fall below the configured number of concurrent sessions.

### Proposed Solution

Add a conversation-level concurrency mode for multi-turn benchmarks.

In this mode, each concurrency slot represents one conversation for its entire lifetime:

1. Assign a conversation to a slot.
2. Send one turn and wait for its response.
3. Keep the slot reserved during the conversation's requeue delay.
4. Send the next turn from the same conversation.
5. Release the slot only when the conversation completes, fails, or is cancelled.
6. Assign a new conversation to the released slot.

The existing request-concurrency behavior should remain available and unchanged.

This could be exposed as either:

- A new profile, such as `--profile conversation`, or
- An explicit concurrency unit, such as `--profile concurrent --concurrency-unit conversation`.

The selected terminology should clearly distinguish concurrent requests from concurrent conversations/users.

#### Acceptance criteria

- Configuring conversation concurrency to `N` starts no more than `N` conversations simultaneously.
- A conversation retains its slot during inter-turn requeue delays.
- Only one request per conversation can be in flight at a time.
- Think time may reduce current request concurrency below `N`.
- A slot is released when its conversation completes, errors, or is cancelled.
- Existing request-level concurrent benchmarks retain their current behavior.
- Results identify whether concurrency represents requests or conversations.
- The behavior works with both trace-provided and synthetic requeue delays.

### Alternatives Considered

The existing concurrent profile can approximate server-side request concurrency, but not a fixed population of active users or agents. Increasing request concurrency or adding workers does not solve this semantic difference.

A request-rate profile can model aggregate traffic, but it does not preserve a bounded number of independently progressing multi-turn sessions.

Setting requeue delays already models think time between turns, but currently another conversation can use the released request slot during that delay.

### Usage Examples

```bash
guidellm benchmark run \
  --target "http://localhost:8000" \
  --model "my-model" \
  --request-format /v1/chat/completions \
  --profile concurrent \
  --concurrency-unit conversation \
  --rate 10000 \
  --data "prompt_tokens=200,output_tokens=100,turns=4"
```

In this example, GuideLLM would maintain up to 10,000 active conversations. Each conversation would execute its turns sequentially and retain its slot during its configured think time.

### Additional Context

This supports customer scenarios involving one agent per employee or customer, with populations of approximately 10,000-40,000 concurrently active sessions.

The delay-generation mechanism itself already exists: real-world traces can provide arbitrary delays, and synthetic workloads can use configured delay distributions. The requested change is specifically to retain ownership of a concurrency slot for the full conversation rather than releasing it between turns.


## 评论 (1)

### LOGO127 · 2026-09-09

Hi @acalhounRH, I'd like to help with this if it is not already assigned. I checked main `8bdb96c`: `_process_requests_loop` releases its semaphore after each node task, and `_get_next_ready_node` can dequeue a new graph while an existing graph's next node is think-time gated.

A small local characterization invokes the unmodified selector and DAG state with a controlled clock and stubbed IPC: with a 30-second requeue delay it selects a new graph while the original is unfinished; without a delay it selects the original child. This verifies the admission seam, not a complete benchmark or a global concurrency bound. The current request-concurrency behavior should remain unchanged.

Before proposing an implementation, could we confirm two ownership boundaries?

1. Does one conversation mean one complete `ConversationGraph`, including all its agents/branches? The acceptance criterion of at most one in-flight request per conversation would serialize otherwise parallel ready DAG branches in the new mode. Is that intended?
2. Should the conversation limit be one global admission budget across workers, retained from graph admission through think time until completion/error/cancellation, separately from the existing request limit? That would avoid multiplying the configured population by worker count.

I can prepare an opt-in design and multi-worker lifecycle tests once the graph semantics and preferred configuration surface are agreed. I would not try to approximate this by increasing request concurrency or silently changing the existing concurrent profile. Investigation and any proposed implementation are Codex-assisted; no implementation or PR has been published.

