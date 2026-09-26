# [Issue #2323] [RFE]: Add persistent backoff recovery mechanism for IB resiliency port recovery

source: https://github.com/NVIDIA/nccl/issues/2323
state: open | updated: 2026-08-19T09:42:52Z
labels: enhancement

## 正文

### Please provide the below details to ensure we understand your needs

## Background

NCCL currently provides IB resiliency support through the `p2p_resiliency` module.
The current recovery mechanism uses `IB_RESILIENCY_PORT_RECOVERY_ATTEMPTS_MAX` to limit the number of recovery attempts for an unhealthy physical port.

This works well for transient failures, but it may not handle long-duration physical failures in modern NIC configurations, such as scenarios where a failed optical module cannot be replaced for several hours or even days.

## Problem Scenario

Some CX8 NIC configurations can expose multiple RDMA devices while NCCL may treat them as a single logical NIC through its NIC merging mechanism.

For example:
```text
                 CX8 NIC
                    |
          +---------+---------+
          |                   |
       RDMA PF0            RDMA PF1
          |                   |
          |                   |
   Switch Port A       Switch Port B
```


Assume one RDMA PF encounters a physical link failure:

- The remote switch side optical module fails.
- The link cannot recover until the optical module is replaced.
- The replacement process may take several hours or even days.

During this period, NCCL resiliency will continuously attempt recovery.
Once the number of retries exceeds: IB_RESILIENCY_PORT_RECOVERY_ATTEMPTS_MAX  the device/PF is marked as permanently failed.

However, after the physical issue is fixed and the optical module is replaced, the port is actually healthy again, but NCCL will no longer try to recover it.

This results in a permanently degraded NCCL communication topology even though the underlying hardware has recovered.

## Current Behavior
As mentioned in the issue #2157 

The current recovery logic is bounded by the retry count:

failure -->recovery attempt -->retry count exceeds limit  --> mark port as permanently failed

The retry limit is useful to avoid excessive recovery attempts, but it does not distinguish between:

- a transient failure (seconds/minutes)
- a planned hardware replacement (hours/days)

## Proposed Enhancement

Could we introduce a persistent backoff-based recovery mechanism in the `p2p_resiliency` module instead of relying only on `IB_RESILIENCY_PORT_RECOVERY_ATTEMPTS_MAX`?

The idea is:

- Keep the failed port in a recoverable state.
- After each failed recovery attempt, increase the retry interval using a  backoff policy.
- Continue trying recovery periodically without permanently disabling the port.

Example:

Failure detected

Attempt 1 retry after 1 minute

Attempt 2 retry after 5 minutes

Attempt 3 retry after 30 minutes

Attempt 4 retry after several hours

...

Port becomes healthy
automatically restore the device


Possible implementation options:

1. Add a configurable recovery backoff interval:
IB_RESILIENCY_PORT_RECOVERY_BACKOFF_ENABLE
IB_RESILIENCY_PORT_RECOVERY_BACKOFF_MAX_INTERVAL

2. Keep `IB_RESILIENCY_PORT_RECOVERY_ATTEMPTS_MAX` as a short-term protection
   mechanism, but allow long-term recovery attempts after the limit is reached.

3. Store recovery state persistently within the resiliency module rather than
   permanently transitioning the port into an unrecoverable state.

## Benefits

This would improve resilience for large-scale AI/HPC clusters where:

- optical module replacement can take significant time;
- operators may repair hardware without restarting NCCL jobs;

The goal is not to increase aggressive retry behavior, but to provide a long-lived recovery mechanism for failures that are expected to eventually
recover.

Would the NCCL team consider adding such a persistent backoff recovery mechanism to the IB resiliency framework?

## 评论 (7)

### xiaofanl-nvidia · 2026-08-09

++ @raminudelman @jynv to review and consider this. 

### 525309178 · 2026-08-12

@jynv Could you please help review and consider this scenario? If this is a valid direction, I can provide an initial plan within the PR.

### jynv · 2026-08-14

@525309178 Thanks for the RFE. We are considering the persistent recovery mechanism to help applications recover from failures with long MTTRs. Exponential backoff reduces overhead during failures, but it can also delay recovery detection. Therefore we are considering heartbeat-based mechanism to detect recovery more promptly.

### 525309178 · 2026-08-19

@jynv hi，I have a preliminary design. Could you take a look?

## Proposed design

I am considering extending the current IB port recovery mechanism with an optional **persistent recovery** mode for long-duration physical link failures.

The intention is to keep the existing fast recovery path unchanged for transient failures, while allowing an existing communicator to retry recovery after a port has been unavailable for minutes or hours.

### 1. Keep the existing fast recovery burst

The current recovery protocol and `NCCL_IB_RESILIENCY_PORT_RECOVERY_ATTEMPTS_MAX` would still be used for short-term recovery.

A sequence of immediate recovery attempts is treated as one **recovery burst**:

```text
Recovery attempt
      |
      +-- success --> Recovered
      |
      +-- failure, attempts < ATTEMPTS_MAX
      |                  |
      |                  +--> retry immediately
      |
      +-- attempts exhausted
                         |
                         v
                       Backoff
```

With persistent recovery disabled, exhausting `ATTEMPTS_MAX` would keep the current behavior and transition to `Failed`.

### 2. Add a Backoff state

When persistent recovery is enabled, exhausting one recovery burst would not destroy the recovery context.

Instead, the context enters a new `Backoff` state:

```text
Fast recovery burst
        |
        v
     Backoff
        |
   deadline expires
        |
        v
 PrepareAttempt
        |
        v
 new recovery burst
```

The retry interval would use exponential backoff with jitter. My proposed defaults are:

```text
initialBackoff = 1 second
maxBackoff     = 1 hour
backoffLevel   = 0, 1, 2, ...

cap = min(maxBackoff, initialBackoff << backoffLevel)
jitter = 75% ... 100%
delay = cap * jitter
```

For example, the nominal retry sequence would be approximately `1s, 2s, 4s, 8s, ...`, eventually capped at `1h`, with each interval reduced by a deterministic 75%-100% jitter factor to avoid synchronized retries across ranks.

While in `Backoff`, the failed device remains excluded from `activeQps`, and no active recovery CQ polling or QP operations are performed.

This keeps the recovery overhead low even if the physical link remains unavailable for a long time.

### 3. Receiver-side passive listening

One concern is that the sender and receiver may detect the failure at different times, so independently scheduled recovery bursts may not overlap.

To avoid requiring synchronized retry timers, my current proposal is:

* the **sender** periodically initiates recovery attempts after its backoff expires;
* once the **receiver** has a usable recovery QP, it enters a lightweight `PassiveListen` state;
* the receiver periodically polls the recovery CQ, with a proposed default interval of **500 ms**;
* receiving a valid Alive message moves it back into the normal active recovery handshake.

Conceptually:

```text
Sender                         Receiver

Backoff                        PassiveListen
   |                                |
deadline expires                    | low-frequency CQ poll
   |                                |
   v                                |
PrepareAttempt                      |
   |                                |
   +---------- Alive -------------> |
                                    v
                               AliveMessages
                                    |
                              ACK / Final ACK
```

An empty passive poll would not count as a failed recovery attempt. The proposed **500 ms** passive-poll interval is intentionally much shorter than the existing recovery protocol timeouts, while still avoiding continuous busy polling. It also matches the current default Alive-message batch interval.

### 4. Compatibility

The proposal is intended to preserve the existing behavior when persistent recovery is disabled.

It also does not change the normal data-path failover behavior:

* healthy devices continue carrying traffic;
* the failed device stays outside `activeQps`;
* only the lifetime and scheduling of the recovery context are extended.

### Questions for maintainers

Before implementing this, I would like feedback on a few design choices:

1. Does extending `ATTEMPTS_MAX` into a per-burst retry limit make sense, or would a separate persistent-recovery limit be preferable?
2. Is keeping failed recovery contexts alive for the communicator lifetime acceptable?
3. Does the sender-active / receiver-passive model look reasonable for handling asymmetric failure detection?
4. Would it be better to reuse the current recovery thread with a deadline queue, or keep long-term recovery scheduling separate from the existing fast recovery path?

### sjeaugey · 2026-08-19

Hi @525309178,

I'm not sure I understand the use case.

> This works well for transient failures, but it may not handle long-duration physical failures in modern NIC configurations, such as scenarios where a failed optical module cannot be replaced for several hours or even days.

So we would keep the job running, spinning at 100% power consumption and blocking lots of GPUs, to wait for one module to be replaced? If it's one hour, maybe it's ok? But days ... that doesn't seem reasonable to me. You should stop the job and restart it on a set of functional nodes, or when the system is functional again.

The one use case I could see is a planned maintenance, e.g. we need to replace a switch. Basically, I don't want jobs to fail, just be paused until the change is complete -- 15 minutes to an hour. But that's quite a different starting point, for which there could be better controlled alternatives like some sort of suspend / resume.

Let me know if I'm missing a use case. Thanks!

### 525309178 · 2026-08-19

Hi @sjeaugey 
Thanks for the feedback. I think the use case I had in mind is slightly different from a job being paused and waiting for the failed link to be repaired.

In the configuration I am considering, multiple physical NIC/PF paths are merged into one logical NIC. If one PF or its corresponding switch path goes down, the healthy PF(s) can continue carrying traffic, so the training job can keep making progress, although potentially with reduced network bandwidth.

For a long-running training job that may run for several days, we may not want to terminate and restart the whole job just because one redundant network path is temporarily unavailable.

For example:

```text
        Logical NIC
        /         \
      PF0         PF1
       |           |
   Switch A    Switch B
```

If the optical module on the `PF0 -> Switch A` path fails, traffic can fail over to `PF1`, and the job can continue running. The intent of persistent recovery is not to keep the job idle while waiting for PF0 to come back. It is to allow NCCL to periodically retry the failed path in the background and automatically restore PF0 once the physical issue is fixed.

The repair time can sometimes be hours, or in some operational environments even longer, for reasons such as spare-part availability or internal replacement/approval procedures. In that case, restarting a multi-day training job solely because one redundant path has been unavailable for longer than the current recovery window may be undesirable.

That said, I agree that waiting indefinitely should probably not be the default behavior. This could be an opt-in mode, and we could also consider a configurable maximum persistent-recovery duration if that better matches the expected NCCL behavior.

So the main use case I am targeting is:

**keep the job running on the remaining healthy network path(s), and allow the failed path to rejoin automatically after it is repaired**, rather than pausing the whole job until maintenance completes.


### sjeaugey · 2026-08-19

My bad. Understood. This is about running in degraded mode and then having link recovery once the issue is fixed. Arguably, in many cases, running in degraded mode for long periods of time could be seen as not very efficient, but ok, that makes more sense. Sorry, I failed to properly read the original description.

