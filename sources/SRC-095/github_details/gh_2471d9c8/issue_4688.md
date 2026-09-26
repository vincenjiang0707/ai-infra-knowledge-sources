# [Issue #4688] [Refactor] [history server] Enable stateless flushing by decoupling identity state from EventCollector

source: https://github.com/ray-project/kuberay/issues/4688
state: open | updated: 2026-09-23T04:42:24Z
labels: stale

## 正文

## Goal

Make EventCollector **identity-stateless**, which means it no longer needs to track identity state internally (specifically the [session name](https://github.com/ray-project/ray/blob/dc6e3dc8deea0e3eadc393f75dcc9775f66f9cc5/src/ray/protobuf/public/events_base_event.proto#L102) and [node ID](https://github.com/ray-project/ray/blob/dc6e3dc8deea0e3eadc393f75dcc9775f66f9cc5/src/ray/protobuf/public/events_base_event.proto#L118)). Instead, it reads these values directly from each incoming event.

> Both `session_name` and `node_id` are base fields present in every Ray event.

## Motivation

1. **Single source of truth:** `session_name` and `node_id` come directly from the raw event, which is always the most accurate source.
2. **Data-driven routing:** Storage path is determined by the event itself, not by whatever the collector happens to have cached.
3. **Simpler, predictable flushing:** Flush logic is based on time, buffer size, or shutdown; not on identity transitions that may be hard to anticipate or test.

## Problem

Today, `EventCollector` stores `currentSessionName` and `currentNodeID` as internal state. Every time an event arrives, it checks whether the event's identity matches the stored state. If it does not, the collector flushes the old buffer and updates its internal state before writing.

This creates an unwanted coupling between two separate concerns:

- **WHERE to write:** The storage path, derived from the event's identity
- **WHEN to write:** The flush trigger, currently fired by identity changes (e.g., session or node ID change)

In other words, a storage routing decision is driving flush timing, and they should not be tied together.

```text
# Current Design (identity-stateful)

Event ──▶ EventCollector ──▶ check currentSessionName / currentNodeID
              │                       │
              │  state mismatch?  ────▶ flush old buffer + update state
              │                       │
              └───────────────────────▶ write to path derived from internal state
```

## Proposed Solution

- Read `session_name` and `node_id` directly from each event to determine where to write (no internal state needed)
- Flushing timing: Fire on a timer (periodic flushing), when the buffer is full (not supported yet), or on shutdown

```text
# Proposed Design (identity-stateless)

Event ──▶ EventCollector ──▶ read event.session_name + event.node_id
              │                       │
              │                       ▼
              └───────────────────────▶ write to path derived from event fields

Flush triggers: periodic | buffer size | shutdown (decoupled from identity)
```

## Compared to Spark

The Spark counterpart is `EventLoggingListener` and one `EventLoggingListener` instance is bound to an application attempt, which has a **fixed** log file path. That means the identity has been fixated since constructed, so there is no need to detect runtime identity transitions. If identity (application attempt) changes, a new instance is created, following the classic **immutable identity pattern**.

In KubeRay, identities can change within the lifecycle of one collector sidecar (i.e., one `EventCollector` processes events from multiple sessions and nodes), so we need to handle identity states differently.


## 评论 (9)

### JiangJiaWei1103 · 2026-04-09

Hi @chiayi @Future-Outlier,

Please take a look when you get a chance. Since you are also planning the event processor for beta, I would like to share my recent survey and writeup in this [doc](https://docs.google.com/document/d/1gimiX833QLVuUCJeN58954ydLsH9pK2bkZ_SvYP9f2U/edit?usp=sharing). I hope it is useful context.

I am also considering opening a new epic issue to track beta progress and follow-ups. Happy to be looped into the offline discussion if there is an opportunity. Thanks!

### chiayi · 2026-04-09

Thank you @JiangJiaWei1103! So from my understanding, I believe there are a few reasons why identity transition was used:
1. Difficulty of detecting when the ray container shuts down, whether from crash or some graceful shutdown. 
2. Isolate the sessions, so that collector only needs to know one session at a time and limit the need to append to files.
3. By flushing every transition/hour, we are essentially partitioning the events into smaller, potentially more manageable files. (But I'm thinking now that it could also be beneficial to have more compact/larger files).

I do like the approach of having a single source of truth and think that this could be a good direction to go in. But I have a few questions:
1. With the collector being stateless, does that mean there could be multiple different sessions/node_ids events in one buffer? Or is the plan to have separate buffers?
2. How will this approach take care of when the ray container crashes? And also ensure that the those "terminated" ray sessions events are flushed when the ray container restarts?
3. Are we still sticking with the same file structure for where we will write the events? Or is there a new file strcuture that you are proposing?

Please let me know if I misunderstood anything, and I will also take a look at the doc as well, thanks! 

We also have a bi-weekly meetings specific to history server! @Future-Outlier can provide more information and add you to it. 

### JiangJiaWei1103 · 2026-04-10

Thanks for the detailed context. Let me address your three reasons, then answer the questions.

### On the original reasons for identity transition

#### 1. Difficulty of detecting Ray container shutdown

Detection becomes unnecessary with a stateless collector: the storage path is derived per-event from its own `session` and `node_id`, so a crashed container's events still flush to the correct path. The only cost is slightly higher **flush latency** for the old session.

#### 2. Isolating sessions to avoid appending to files

This invariant is currently violated for `node_events/`. The file naming or flush model needs to change regardless of statefulness. I can reproduce it if helpful!

#### 3. Partitioning into smaller files

Stateless preserves the same hour-key granularity. The only difference: a single hour partition may materialize as multiple files that the reader merges (see Q3).

### Questions

#### Q1. Will a stateless collector hold events from multiple sessions / node IDs in one buffer?

Yes. Paths are derived per-event, so one buffer is sufficient. The one code change: expand the `flushEventsInternal` grouping key to:

- node events: `(sessionName, nodeID, hourKey)`
- job events: `(sessionName, nodeID, jobID, hourKey)`

#### Q2. How do we handle Ray container crash / restart and ensure terminated sessions get flushed?

Correctness no longer depends on crash detection. Events from terminated sessions sit in the buffer until the next flush and land at the correct path. Worst-case latency can be bounded by two mechanisms:

- Periodic flush: Time-bound (currently 1h, tunable)
- Size-threshold flush: Memory-bound (not yet implemented)

Note on the postStart hook https://github.com/ray-project/kuberay/issues/4654: A stateless `EventCollector` can decouple from node ID, but the log collector still depends on it.

#### Q3. Same file structure?

Multi-flush requires collision-safe naming. I would go with a flush identifier suffix:

- `node_events`: `…/node_events/{nodeID}-{hourKey}-{flushSeq}`
- `job_events`:  `…/job_events/{jobID}/{nodeID}-{hourKey}-{flushSeq}
`

`flushSeq` can be a monotonic counter or `UnixNano`. The storage reader already iterates over all files under a prefix, so it just needs to merge arrays within the same hour bucket and no schema change is needed.

The alternative, read-modify-write append, is conceptually simpler but adds **IO latency** and might break under concurrent collectors (potential **race conditions**).

### Future-Outlier · 2026-04-13

cc @KunWuLuan @ChenYi015 to take a look

### chiayi · 2026-04-13

@JiangJiaWei1103 Thank you for the detailed response and answer! 

I just have one more clarification on my side. Since different sessions will be in one buffer, is there logic for finding out if the event should be flushed or not? Or is that what you mean by `worst-case latency can be bounded` so that flushes happens often enough?

### KunWuLuan · 2026-05-06

Hi, @JiangJiaWei1103 , there is another reaon for why we store the `node_id` in memory:

The `node_id` is not contained in the ray events before this issue [#58879](https://github.com/ray-project/ray/issues/58879).

cc @Future-Outlier 

### JiangJiaWei1103 · 2026-05-06

@chiayi sorry for the late reply on this issue. My original intention is to preserve only two drivers for flushing:

1. Periodic trigger by time
2. Trigger by memory usage

As we are revisiting the collector design in today's meeting, I think we can continue discussing based on @KunWuLuan's new design. WDYT? Thanks!

### JiangJiaWei1103 · 2026-05-06

@KunWuLuan Thanks for providing the context!

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
