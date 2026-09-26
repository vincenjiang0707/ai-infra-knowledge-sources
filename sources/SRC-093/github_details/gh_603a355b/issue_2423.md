# [Issue #2423] [Question] v0.7.0 Redis request count sync pattern — per-pod in-memory counting with periodic Redis sync vs. direct Redis operations — real-time accuracy concerns

source: https://github.com/vllm-project/aibrix/issues/2423
state: closed | updated: 2026-09-21T21:27:32Z
labels: 

## 正文

We understand that v0.7.0 introduced syncing request counts (runningRequests) to Redis, but from what we can tell (please correct us if we're wrong), the pattern appears to be:

1. Each pod does ±1 counting locally in memory via atomic.AddInt32
2. Periodically, the in-memory count is batch-synced/flushed to Redis

Rather than doing direct INCR/DECR operations on Redis.

Our concerns:

If this is a periodic-sync approach:

1. Significant real-time lag: Within the sync interval (even 1-10 seconds), the values in Redis are always stale. In LLM inference scenarios where requests complete in sub-second to seconds, this means the routing algorithm is making decisions on outdated data.
2. Contradiction with least-request routing: The fundamental premise of least-request routing is that runningRequests reflects the current load on each Pod. A seconds-old snapshot undermines this premise — potentially even worse than purely local counting (which at least has zero network delay).
3. Atomicity regression: Moving from atomic.AddInt32 (nanosecond-scale, lock-free) to periodic sync (second-scale, network overhead) is a trade-off that adds global visibility but sacrifices timeliness.

Questions:
1. What was the design rationale behind this approach? Is it primarily for sharing request counts across multiple gateway instances?
2. Have you done comparative testing (pure local counting vs. periodic Redis sync) on routing quality metrics such as P50/P99 TTFT and load distribution fairness?
3. Have you considered direct INCR/DECR on Redis (with pipeline batching to reduce network overhead), or a hybrid approach where local atomic counts are used for real-time routing decisions while Redis serves asynchronously for monitoring/recovery?

## 评论 (5)

### varungup90 · 2026-07-07

Hi @allswell00,

Thanks for raising these excellent points! You've accurately identified the core architectural trade-offs we are navigating here.

To clarify the current implementation: when `AIBRIX_STATESYNC_ENABLED` is turned on, the default sync period is actually **100ms** rather than in the order of seconds. That said, I completely agree with your concern—in ultra-high-throughput scenarios, even a 100ms window can introduce noticeable real-time lag for dynamic routing algorithms like least-request.

### Design Rationale & Current Approach

The initial motivation behind this periodic sync pattern was to share the *entire* local gateway state (including both `runningRequests` and the prefix-cache map) across multiple gateway instances.

Thinking through your feedback, there is a clear distinction in consistency requirements between these states:

* **Prefix-cache mapping:** Eventual consistency via a 100ms periodic sync is highly effective and acceptable.
* **Request counts:** For dynamic load balancing, a 100ms stale window can absolutely lead to sub-optimal routing decisions and hot-spotting under high concurrency. Utilizing direct Redis `INCR`/`DECR` atomic operations makes much more sense here.

### Next Steps

Before making a definitive architectural change, I plan to run a set of benchmark tests to evaluate:

1. The latency overhead of direct Redis `INCR`/`DECR` operations under load (including pipelining/batching potential).
2. The performance limits of the current periodic sync approach (i.e., how low we can safely push the sync interval below 100ms without overwhelming the network/Redis).

I will share the benchmark findings right here as soon as they are ready so we can align on the best path forward (whether that is a hybrid approach or fully moving request counts to direct Redis operations). Stay tuned!

### rayne-Li · 2026-07-10

@allswell00 @varungup90 
> Contradiction with least-request routing: The fundamental premise of least-request routing is that runningRequests reflects the current load on each Pod. A seconds-old snapshot undermines this premise — potentially even worse than purely local counting (which at least has zero network delay).

is least-request still use pod.metrics in cache instead of redisClient to get running_request?

<img width="1025" height="473" alt="Image" src="https://github.com/user-attachments/assets/07153be1-af82-4934-b193-2e177310e744" />

only powerOfTwo strategy use redisClient to get running_request?

### varungup90 · 2026-07-10

@rayne-Li To answer your question about how `least-request` interacts with `pod.metrics` vs. the `redisClient`:

Yes, `least-request` still reads from the local metrics cache (`r.cache.GetMetricValueByPod`) rather than hitting Redis directly on every routing decision. However, when state sync is enabled, that cached value isn't purely local—it is actually a globally aggregated total computed by a background synchronization loop.

Here is the exact implementation detail showing how the global sync updates the local cache:

```go
// syncRunningRequestsGlobally computes the cross-gateway running request count for a pod and
// stores it so GetMetricValueByPod returns the global total. It reads the in-memory snapshot
// cache (populated every 100ms by initGatewaySnapshotSync — no Redis call here), sums
// requests_running from all other gateway instances, then adds this gateway's own local
// atomic counter (always fresher than the Redis snapshot for the local instance).
func (c *Store) syncRunningRequestsGlobally(pod *Pod) {
	raw := c.gatewaySnapshotCache.Load()
	if raw == nil {
		return
	}
	snapshotCache := raw.(map[string][]map[string]string)

	var remoteRunning float64
	podKey := utils.GeneratePodKey(pod.Namespace, pod.Name)
	for _, fields := range snapshotCache[podKey] {
		// Skip our own outdated snapshot in Redis; we want to use the fresh local atomic count instead
		if fields["gateway_instance_id"] == gatewayPodName {
			continue
		}
		running, _ := strconv.ParseFloat(fields["requests_running"], 64)
		remoteRunning += running
	}

	// Read the ultra-fresh local atomic counter (zero network delay)
	localRunning := float64(atomic.LoadInt32(&pod.runningRequests))
	total := localRunning + remoteRunning
	klog.V(5).InfoS("running requests aggregation", "pod", pod.Name, "local", localRunning, "remote", remoteRunning, "total", total)

	totalValue := &metrics.SimpleMetricValue{Value: total}
	metrics.EmitMetricToPrometheus(&types.RoutingContext{}, pod.Pod, metrics.RealtimeNumRequestsRunning, totalValue, nil)
	
	// This updates the local pod.metrics cache that least-request queries
	if err := c.updatePodRecord(pod, "", metrics.RealtimeNumRequestsRunning,
		metrics.PodMetricScope, totalValue); err != nil {
		klog.V(4).ErrorS(err, "failed to update global running requests", "pod", pod.Name)
	}
}

```

### Key Takeaways from this Pattern:

1. **Least-Request Strategy:** It fetches from the local cache (`r.cache`), but that cache contains `total` (`localRunning` + `remoteRunning`).
2. **The Stale Window:** While the `localRunning` component is perfectly real-time (atomic lock-free lookups), the `remoteRunning` component comes from the `gatewaySnapshotCache`, which is bound to the ~100ms stale Redis sync interval.
3. **PowerOfTwo Strategy Divergence:** You are correct that the `powerOfTwo` implementation handles this differently at the moment. Its pattern has diverged from `least-request`, and it's on my TODO list to converge and refactor it so that all routing algorithms follow an aligned, consistent state-sharing pattern.

### varungup90 · 2026-09-18

https://github.com/vllm-project/aibrix/pull/2749

### varungup90 · 2026-09-21

Now read/write for request is synchronous. Other takeaways are also addressed.
