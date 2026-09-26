# [Issue #2795] [Feature][ModelClaim] Divide a card's KV again as its engines and their load change

source: https://github.com/vllm-project/aibrix/issues/2795
state: open | updated: 2026-09-24T03:11:15Z
labels: kind/feature, area/orchestration

## 正文

### 🚀 Feature Description and Motivation

Part of #2290, item 2 (the KV-budget arbiter).

#2647 divides a card between its engines only when a model lands on it. After that, the limits stay as they were set:

- Room freed when an engine leaves or fails goes to nobody. It waits for the next model placed on that card.
- A share does not follow load. A busy engine keeps the share it got at placement. An idle one keeps more than it needs.
- A sleeping engine keeps its whole share, though it serves nothing.

This issue proposes dividing a card again as its engines and their load change. It covers the share part of item 2.

### Use Case

Three models share one GPU in a warm pool. Their traffic shifts during the day. One of them is deleted, and the pool's idle policy (#2460) puts another to sleep.

Today, the model still serving keeps the share it got when the last model landed. With this change, it gets the room the other two no longer use, within about 10 seconds. When the sleeping model wakes, the card is divided again.

### Proposed Solution

Keep the division from #2647. Each engine keeps what it holds, and the spare is shared by weight. Change when it runs, and two of its rules.

- **When the engines on a card change, divide it on the next reconcile.** A model is placed, removed or fails, an engine sleeps or wakes, or a declaration changes. Every move is carried out, and each claim whose limit moves gets a `KVLimitSet` Event.
- **Follow load every 10 seconds.** A card is divided at most once per 10 seconds, with the weight placement uses: 1 plus requests in flight, capped at 4. The plan is carried out only if some limit moves by at least max(512 MiB, 1% of the card). These divisions are logged, with no Events.
- **A sleeping engine keeps only its floor.** Its weight is 0. If every engine on a card is asleep, the spare stays unassigned until one wakes.
- **Shrink, confirm, then grow.** A lower limit does not free pages already mapped. So no engine grows until each engine that shrank reads back at or below its new limit.
- **Read each runtime once per reconcile.** After a write, the read-back replaces that reading.

This also covers two follow-ups from the #2647 review: the single reading per reconcile above, and giving the room back to the neighbours when an `Activate` fails after a division.

There is no API change. The pool annotation's `reclaim` policy (#2453) does a similar job with a capacity set by hand. It already stands down where a claim holds a limit, and this change leaves it as it is.

Out of scope, for later:

- Per-model minimum, maximum and priority.
- Squeezing busy neighbours, or putting idle ones to sleep, to make room for a model.
- Metrics for these divisions (#2455).

The code is written and tested on an H20. It builds on #2647, and I will open its PR after #2647 is merged. Until then, the seven commits are here: https://github.com/Zeyu-ZEYU/AIBrix/compare/zeyu...zeyu-pr2-online-kv

### Area

Orchestration (controllers, CRDs)


## 评论 (3)

### github-actions[bot] · 2026-09-23

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### bolubo · 2026-09-23

Today the division only runs on the placement path: the claim placing a new engine calls `makeRoomOnPod`, which divides the card and records each engine's limit on its claim. The proposal adds two triggers but not the actor for the periodic division. With each claim's reconcile as the vehicle (the controller already requeues every 10s), a card with N claims would be divided N times per tick, so the once-per-10-seconds floor holds per claim, and the per-card interval depends on claim phases. A per-card actor would need a new gate and its own restart semantics. Which is intended, and what detects a changed engine set for the change-triggered path?

Two more things. One is the sequencing of `shrink, confirm, then grow`. In the current #2647 head (`bc841a9d`), one arrangement writes the whole batch (shrinks first by `writeOrder`, then grows) and reads back once; if the confirm fails, the placement refuses the card and tries the next one. The new rule would need the writes split into two batches with a read-back between them, or a wait across rounds. The confirm is a snapshot condition: the segment at the new limit and mapped KV at or below it. An engine that keeps taking KV can cross its planned ceiling between the plan and the read-back. The rule reads as one barrier over every shrinker, so a single laggard can hold all growth. How long may that wait last, and what surfaces a shrinker that never reads back, given that the load-following divisions are logged with no Events?

The other is sleep. `kvExtraWeight` floors the weight at 1 by design, and `engineOnPod` carries no sleep state, so `weight is 0` needs a new input to the planner. Also, the current plan spends the card exactly; leaving the spare unassigned when every engine sleeps is a different outcome: floor-only limits, or the last division left standing? What marks an engine asleep for the planner, and which of these three belongs here rather than on the #2290 list?

### Zeyu-ZEYU · 2026-09-24

Thanks. An implementation on top of #2647 answers these and passes its tests on an H20. It becomes a PR once #2647 merges: https://github.com/Zeyu-ZEYU/AIBrix/compare/zeyu...zeyu-pr2-online-kv

**Who divides.** Each claim's reconcile, as today. A per-card gate allows one division per card every 10 seconds, however many claims sit on it. Every placed claim requeues every 10 seconds in any phase, so any of them drives it. The gate is in memory, so after a restart each card is divided by its first round, without Events.

**What counts as a change.** Claim status, not the runtime: each instance's claim, state (awake, asleep or failed) and declared figures, from the account's fresh claim list. If that differs from what the card was last divided for, the card is divided on the next pass. The change stays pending until that division succeeds. Placement records what it divided for, so its newcomer is not a change.

**Shrink, confirm, then grow.** Two batches in one pass, each read back, with no waiting across rounds. An unconfirmed shrink stops growth for that pass and changes no record. The laggard stays routable, since it is held to no more than its record. The next round re-plans from a fresh reading, counting what the laggard has mapped as held. So the plan follows the laggard rather than waits, and each failed try delays growth by one round at most. Three failed tries in a row raise one Warning `KVLimitFailed` on each claim on the card, which surfaces a shrink that never takes.

**Sleep.** The planner reads the engine phase from the runtime snapshot, as the health loop does to mark a claim Sleeping. A sleeping engine weighs 0 and keeps what it holds, normally its floor. With every engine asleep, each keeps what it holds, and the spare stays unassigned. A wake is a change, so the card is divided again at once.

All three belong here, since online division is not safe without them. The #2290 list keeps priority, minimum and maximum, squeezing neighbours, and metrics.

