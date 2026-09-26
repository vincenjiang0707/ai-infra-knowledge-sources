# [Issue #2780] [Bug] With spec.mode unset and replicas > 1, a role-level PodAutoscaler seems to multiply the replica count by N

source: https://github.com/vllm-project/aibrix/issues/2780
state: open | updated: 2026-09-22T16:17:42Z
labels: kind/bug, area/orchestration

## 正文

### 🐛 Describe the bug

I was learning to use PodAutoscaler to autoscale one role of a StormService. I set `maxReplicas` to 10 and ended up with 30 Pods that never came back down. My StormService has no `spec.mode` and `replicas: 3`; the PodAutoscaler uses `subTargetSelector.roleName` and does not set the `autoscaling.aibrix.ai/storm-service-mode` annotation (the docs say it's deprecated).

Reading the code, it looks like the PA and the StormService controller disagree about which mode the service is in: the controller uses `ResolvedMode()` (`stormservice_types.go:102`), where `replicas > 1` means Replica; the PA uses `stormServiceScalingMode()` (`workload_scale.go:60`), which returns Pooled whenever the annotation is absent.

Once it decides Pooled, what the PA reads and what it writes don't seem to be the same quantity. It reads `status.roleStatuses[role].replicas` (`workload_scale.go:190`), which is the sum across all RoleSets (`stormservice/utils.go:447` accumulates it). It writes `spec.template.spec.roles[role].replicas` (`workload_scale.go:289`), and in Replica mode the template is copied to every RoleSet.

So the actual Pod count becomes "the value written × the number of RoleSets". On the next round the PA reads the inflated total, it doesn't match the desired value, and the value it writes can't bring the total down, so it never converges.

I searched the issues: #2449 (closed on Sep 20) says in its backward-compatibility section that when mode is omitted, `replicas > 1` should be treated as replica mode. The PA doesn't seem to follow that — I don't know if it was missed or if there's another reason.

I reproduced it on kind with `replicas: 3`, no mode, 2 decode per RoleSet, PA `maxReplicas: 10`, and the metric held above the target. Three things happen:

First, the replica count overshoots by 3x. decode Pods settle at 30 (the 10 that was written × 3 RoleSets), and the PA's own status reads `actualScale=30, desiredScale=10`.

Second, RoleSets are recreated over and over. I assumed this was something about my environment at first, so I ran a control: same setup, without the PA, 2.5 minutes produced zero RoleSet creates or deletes, generation stayed at 1 and the UIDs never changed; with the PA attached, the same 2.5 minutes produced somewhere between a hundred and a few hundred creates/deletes (124 and 311 on two runs), generation went up by ~90 every 10 seconds, the RoleSet UIDs differed on every sample, and decode Pods bounced between 4 and 14. The PA keeps rewriting the role replica count in the template (oscillating between 5 and 10), and every rewrite triggers a rebuild of all RoleSets. With a real engine each rebuild means reloading weights and capturing CUDA graphs, so it would be a continuous cold start (I don't have a GPU environment, so I didn't measure that part).

Third, the PA never settles. Since the value it reads never equals the desired value, `shouldScale` stays true. I counted `Successfully rescaled` a few times: 295 and 1616 lines per 30 seconds on different runs, so tens of reconciles per second, each one scraping metrics from every Pod and sending the apiserver a patch whose content hasn't changed. I watched for over ten minutes and it never stopped.

Steady-state logs from the first run (the one that settled at 30 Pods), one round every ~25ms:

```
I0913 10:30:52.084432 apa.go:97] "APA scaling up" currentPods=30 expectedPods=36
I0913 10:30:52.094093 podautoscaler_controller.go:914] "Successfully rescaled" PodAutoscaler="bug2/decode-pa" currentReplicas=30 desiredReplicas=10 reason="All metrics below target"
I0913 10:30:52.118153 apa.go:97] "APA scaling up" currentPods=30 expectedPods=36
I0913 10:30:52.128259 podautoscaler_controller.go:914] "Successfully rescaled" PodAutoscaler="bug2/decode-pa" currentReplicas=30 desiredReplicas=10 reason="All metrics below target"
```

I first assumed I had simply forgotten `spec.mode`, but after looking around the repo it seems easy for others to hit as well:

The logic has been like this since #1625 (in `da47edde` it already took the role branch whenever the `replica` annotation was absent). Back then the samples carried the annotation, so copying them was safe. #2617 removed the annotation from the samples, and the docs now mark it deprecated in favour of `spec.mode`.

Right now `samples/` has 20 StormService samples without `spec.mode`, 5 of which have `replicas > 1`:

```
samples/disaggregation/sglang/replica.yaml                            replicas=2
samples/orchestration/topology-policy/role-zone-preferred.yaml        replicas=3
samples/orchestration/topology-policy/role-zone-required.yaml         replicas=3
samples/orchestration/topology-policy/roleset-hostname-required.yaml  replicas=3
samples/orchestration/topology-policy/roleset-zone-preferred.yaml     replicas=3
```

I deployed the shape of `sglang/replica.yaml` (no mode, `replicas: 2`, `InPlaceUpdate`, prefill 2 / decode 1) and attached a PA with `roleName: decode` following `samples/autoscaling/stormservice-replica.yaml`, and it does hit the problem: the PA wrote 10 into the template's decode, each of the 2 RoleSets brought up 10, so 20 decode Pods against a `maxReplicas` of 10. The PA sat at `20/10`, with 93 RoleSet rebuilds in 90 seconds and 1318 rescales in 30 seconds.

One detail I found unnerving: the overshoot factor is exactly the number of RoleSets, and it doesn't always show. On the same deployment I first tried `maxReplicas: 6`; the PA wrote 3, the 2 RoleSets added up to exactly 6 Pods, which matched the limit, so it converged and looked completely fine. It only gets stuck when "value written × number of RoleSets" crosses the limit. Could some clusters already be in this state without anyone noticing?

The webhook doesn't seem to catch it either: the switch in `validateStormServiceMode` only matches an explicitly declared `Pooled` / `Replica` and skips an empty mode; the `/scale` validation added in #2661 reuses the same function, and its own comment notes that inferred pooled objects can still scale `spec.replicas`.

### Steps to Reproduce

Prerequisite: AIBrix controller-manager installed with `stormservice-controller` and `pod-autoscaler-controller` enabled. Below I use busybox running httpd to fake an inference engine; it only serves a fixed `vllm:num_requests_waiting 12` so the metric stays above target and the scaling behaviour is easy to watch. Replace `IMAGE` with any image in your environment that has sh and httpd — a real engine works the same way.

```bash
export IMAGE=busybox:1.36   # any image available in your environment

kubectl create ns bug2

cat <<EOF | kubectl apply -f -
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: llm
  namespace: bug2
spec:
  # spec.mode deliberately left out
  replicas: 3
  updateStrategy: {type: RollingUpdate}
  selector: {matchLabels: {app: llm}}
  template:
    metadata: {labels: {app: llm}}
    spec:
      roles:
      - name: prefill
        replicas: 1
        template:
          spec:
            terminationGracePeriodSeconds: 0
            containers:
            - name: engine
              image: $IMAGE
              command: ["sh", "-c", "mkdir -p /www; echo '# TYPE vllm:num_requests_waiting gauge' > /www/metrics; echo 'vllm:num_requests_waiting 12' >> /www/metrics; exec httpd -f -p 8000 -h /www"]
              ports: [{containerPort: 8000}]
              readinessProbe: {tcpSocket: {port: 8000}, periodSeconds: 1}
      - name: decode
        replicas: 2
        template:
          spec:
            terminationGracePeriodSeconds: 0
            containers:
            - name: engine
              image: $IMAGE
              command: ["sh", "-c", "mkdir -p /www; echo '# TYPE vllm:num_requests_waiting gauge' > /www/metrics; echo 'vllm:num_requests_waiting 12' >> /www/metrics; exec httpd -f -p 8000 -h /www"]
              ports: [{containerPort: 8000}]
              readinessProbe: {tcpSocket: {port: 8000}, periodSeconds: 1}
EOF

sleep 30
```

**Step 1 (control), no PA yet, confirm everything is quiet:**

```bash
for i in $(seq 1 6); do
  echo "$(date +%T) gen=$(kubectl -n bug2 get stormservice llm -o jsonpath='{.metadata.generation}') template.decode=$(kubectl -n bug2 get stormservice llm -o jsonpath='{.spec.template.spec.roles[?(@.name=="decode")].replicas}') rolesets=$(kubectl -n bug2 get roleset --no-headers | wc -l) decodePods=$(kubectl -n bug2 get pod -l role-name=decode --no-headers | wc -l)"
  sleep 10
done
echo "RoleSet creates/deletes in the last minute: $(kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=60s | grep -c rolesetoperation)"
```

Completely stable on my side, no rebuilds at all:

```
21:10:37 gen=1 template.decode=2 rolesets=3 decodePods=6
21:10:47 gen=1 template.decode=2 rolesets=3 decodePods=6
21:10:58 gen=1 template.decode=2 rolesets=3 decodePods=6
21:11:08 gen=1 template.decode=2 rolesets=3 decodePods=6
21:11:18 gen=1 template.decode=2 rolesets=3 decodePods=6
21:11:28 gen=1 template.decode=2 rolesets=3 decodePods=6
RoleSet creates/deletes in the last minute: 0
```

**Step 2, attach the PA (with roleName, without the annotation) and change nothing else:**

```bash
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: decode-pa
  namespace: bug2
spec:
  scaleTargetRef:
    apiVersion: orchestration.aibrix.ai/v1alpha1
    kind: StormService
    name: llm
  subTargetSelector: {roleName: decode}
  minReplicas: 1
  maxReplicas: 10
  scalingStrategy: APA
  metricsSources:
  - metricSourceType: pod
    protocolType: http
    port: "8000"
    path: /metrics
    targetMetric: num_requests_waiting
    targetValue: "10"
EOF

for i in $(seq 1 10); do
  echo "$(date +%T) spec.replicas=$(kubectl -n bug2 get stormservice llm -o jsonpath='{.spec.replicas}') template.decode=$(kubectl -n bug2 get stormservice llm -o jsonpath='{.spec.template.spec.roles[?(@.name=="decode")].replicas}') gen=$(kubectl -n bug2 get stormservice llm -o jsonpath='{.metadata.generation}') decodePods=$(kubectl -n bug2 get pod -l role-name=decode --no-headers | wc -l) PA=$(kubectl -n bug2 get podautoscaler decode-pa -o jsonpath='{.status.actualScale}/{.status.desiredScale}')"
  sleep 10
done
```

`maxReplicas` is 10, but decode Pods go to 30 (the PA writes 10 into the template, which is copied to all 3 RoleSets). The PA's status stays at 30/10, never matching and never coming down, and generation keeps climbing, which means the template is being rewritten again and again:

```
21:11:50 spec.replicas=3 template.decode=5  gen=4   decodePods=4  PA=4/5
21:12:00 spec.replicas=3 template.decode=5  gen=106 decodePods=10 PA=4/5
21:12:10 spec.replicas=3 template.decode=5  gen=199 decodePods=8  PA=14/10
21:12:21 spec.replicas=3 template.decode=5  gen=292 decodePods=4  PA=4/5
21:12:31 spec.replicas=3 template.decode=10 gen=384 decodePods=10 PA=4/5
21:12:41 spec.replicas=3 template.decode=5  gen=477 decodePods=8  PA=14/10
21:12:51 spec.replicas=3 template.decode=10 gen=570 decodePods=9  PA=4/5
21:13:02 spec.replicas=3 template.decode=5  gen=663 decodePods=10 PA=14/10
21:13:12 spec.replicas=3 template.decode=10 gen=756 decodePods=9  PA=4/5
21:13:22 spec.replicas=3 template.decode=5  gen=849 decodePods=5  PA=4/5
```

The Pod count keeps jumping because RoleSets are rebuilt before their Pods finish starting. On my first run (with the controller CPU-limited, so rebuilds were slower) it settled at 30 decode Pods with the PA reporting `actualScale=30 desiredScale=10` — that's the 10 written into the template times 3 RoleSets.

**Step 3, look at how much rebuilding and spinning is going on:**

```bash
echo "RoleSet creates/deletes (last 150s): $(kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=150s | grep -c rolesetoperation)"
echo "PA rescales (last 30s):              $(kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=30s | grep -c 'Successfully rescaled')"
kubectl -n aibrix-system logs deploy/aibrix-controller-manager --since=30s | grep 'Successfully rescaled' | tail -2
```

Compared with the 0 from step 1 the difference is obvious. The absolute numbers differ every run — across several runs I saw 124, 284 and 311 RoleSet operations and 295, 1616 and 1758 rescales, depending on machine speed and sampling — but the control is always 0. Either way it doesn't stop, and every round scrapes metrics from all Pods and sends a patch whose content hasn't changed:

```
RoleSet creates/deletes (last 150s): 284
PA rescales (last 30s):              1758
I0922 12:13:34.785672 podautoscaler_controller.go:914] "Successfully rescaled" PodAutoscaler="bug2/decode-pa" currentReplicas=14 desiredReplicas=10 reason="All metrics below target"
I0922 12:13:34.796956 podautoscaler_controller.go:914] "Successfully rescaled" PodAutoscaler="bug2/decode-pa" currentReplicas=14 desiredReplicas=10 reason="All metrics below target"
```

**Cleanup:**

```bash
kubectl delete ns bug2
```

**If you'd rather not spin up a cluster**, a unit test shows the same contradiction:

```go
ss.Spec.Mode = ""
ss.Spec.Replicas = ptr.To(int32(3))
ss.Status.RoleStatuses = []RoleStatus{{Name: "decode", Replicas: 12}} // sum over 3 RoleSets

ss.Spec.ResolvedMode()            // => Replica
stormServiceScalingMode(pa, ss)   // => Pooled
GetCurrentReplicasFromScale(...)  // => 12, the aggregated value
SetDesiredReplicas(ctx, pa, 13)   // => template decode becomes 13, spec.replicas stays 3
                                  //    rolled out to 3 RoleSets that's 39 Pods
```

### Expected behavior

When `spec.mode` is unset and `replicas > 1`, the PodAutoscaler should agree with the StormService controller and treat it as Replica: read and write `spec.replicas`, with `roleName` only selecting which Pods the metrics come from. That's also what #2449 states in its backward-compatibility section (mode omitted plus `replicas > 1` means replica mode), and what the comment in `samples/autoscaling/stormservice-replica.yaml` says about `roleName`.

About `maxReplicas` — I had this wrong at first. The API comment says "the maximum number of replicas to which the target can be scaled up", so it bounds the quantity being scaled: `spec.replicas` (the number of RoleSets) in Replica mode, and the target role's `replicas` in Pooled mode. So after the fix, `maxReplicas: 10` giving 10 RoleSets and 20 decode Pods is consistent with that definition and not an overshoot.

What actually feels wrong is that the PA loses control of the quantity it manages: it reads `actualScale=30`, writes `desiredScale=10`, the two never meet, and the value it writes can't bring the read value down. `actualScale` should be able to converge to `desiredScale`, and autoscaling shouldn't keep rebuilding RoleSets.

Of course, if you'd rather not guess when mode is missing, another outcome works for me too: when the PA sees `ResolvedReplicas() > 1` on the target and can't determine the mode, mark itself invalid and say in the conditions that `spec.mode` needs to be set, instead of silently treating it as Pooled. The PA already rejects the `HPA + roleName` combination outright, so that approach seems to have precedent.

### I tried a change (not sure if it's right)

Locally I made the "neither mode nor annotation" case fall back to `ss.Spec.ResolvedMode()`:

```go
 func stormServiceScalingMode(pa *autoscalingv1alpha1.PodAutoscaler, ss *orchestrationv1alpha1.StormService) orchestrationv1alpha1.StormServiceMode {
 	if ss.Spec.Mode != "" {
 		return ss.Spec.Mode
 	}
 	if pa.Annotations[AutoscalingStormServiceModeAnnotationKey] == "replica" {
 		return orchestrationv1alpha1.StormServiceReplicaMode
 	}
-	return orchestrationv1alpha1.StormServicePooledMode
+	return ss.Spec.ResolvedMode()
 }
```

The code comment says `replicas == 1` can't tell the two modes apart, which I get; but `replicas > 1` looks unambiguous, and I don't know why that case ends up as Pooled too.

I re-ran the same setup with the patched controller (`replicas: 3`, template decode 2, `maxReplicas: 10`):

```
21:13:59 spec.replicas=5  template.decode=2 gen=1115 decodePods=12 PA=8/8
21:14:10 spec.replicas=10 template.decode=2 gen=1117 decodePods=20 PA=10/10
21:14:20 spec.replicas=10 template.decode=2 gen=1117 decodePods=20 PA=10/10
... unchanged for the next two minutes ...
21:15:31 spec.replicas=10 template.decode=2 gen=1117 decodePods=20 PA=10/10

RoleSet creates/deletes (last 120s): 0
PA rescales (last 60s):              0
```

The PA changes `spec.replicas` instead of the template, converges in about 20 seconds, and after that there were 0 RoleSet creates/deletes in 120 seconds and 0 rescale calls in 60 seconds, with the template untouched.

The unit tests for `pkg/controller/podautoscaler` all pass. If this direction is acceptable I can open a PR and add tests: `stormServiceScalingMode` should return Replica when mode is unset, `replicas=3` and no annotation; plus one each for `GetCurrentReplicasFromScale` and `SetDesiredReplicas` asserting that `spec.replicas` is what changes and the role replicas in the template are left alone.

One more question while I'm here: should the 20 samples without `spec.mode` be updated as well? It looks low-risk and would save the next person some confusion.

### Environment

- AIBrix: main at `dcc8aa9a`. I checked current main too and `stormServiceScalingMode` still returns Pooled unconditionally
- Cluster: single-node kind v1.30.0, controller-manager built from source with only `pod-autoscaler-controller` and `stormservice-controller` enabled, plus `--disable-webhook`
- The inference engine is faked with busybox httpd serving a single `vllm:num_requests_waiting` metric, no GPU. This sits in the control plane's mode resolution and replica arithmetic; the engine only supplies a number, so a real vLLM wouldn't change how the PA computes or writes
- Related issues/PRs: #1625, #2449 (closed), #2450, #2617, #2661, #1619


### Area

Orchestration (controllers, CRDs)

## 评论 (3)

### github-actions[bot] · 2026-09-22

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### googs1025 · 2026-09-22

Confirmed: this is a real issue. The PodAutoscaler and the StormService controller currently resolve an omitted `spec.mode` differently. With `spec.replicas > 1`, the controller uses `ResolvedMode()` and treats the service as Replica, while the PA falls back to Pooled when the legacy annotation is absent. That makes the PA read an aggregate across all RoleSets but write a per-RoleSet template value, so `actualScale` cannot converge to `desiredScale` and repeated RoleSet rollouts are expected.

I see two reasonable ways to address it:

1. **Backward-compatible inference:** when `spec.mode` is unset and the legacy PA annotation is absent, fall back to `ss.Spec.ResolvedMode()`. The resolver should preserve the existing precedence for an explicitly present legacy annotation. This matches the compatibility contract from #2449/#2450. Tests should cover mode resolution plus both `GetCurrentReplicasFromScale` and `SetDesiredReplicas` for `replicas > 1`.

2. **Require an explicit mode for role-level autoscaling:** mark the PA invalid when its StormService target omits `spec.mode`, with a condition explaining that `mode: Replica` or `mode: Pooled` must be set. This removes ambiguity, especially if `spec.replicas` can cross 1, but is a stricter behavior change for existing objects.

I would prefer option 1 as the immediate compatibility fix, while continuing to recommend an explicit `spec.mode` for autoscaled StormServices. The `replicas == 1` transition is worth adding as a test/design case because inferred mode is inherently ambiguous at that boundary.

### btxu-db · 2026-09-22

I'll pick this up.
