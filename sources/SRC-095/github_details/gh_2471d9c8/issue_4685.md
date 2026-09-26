# [Issue #4685] [Bug] RayService worker liveness probe does not check Serve health endpoint, leading to silent failures and unrecoverable deployments

source: https://github.com/ray-project/kuberay/issues/4685
state: closed | updated: 2026-09-23T08:04:32Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

ray-operator

### What happened + What you expected to happen

The default liveness probe generated for RayService worker pods only checks the local raylet health:
```
wget --tries 1 -T 2 -q -O- http://localhost:52365/api/local_raylet_healthz | grep success
```
However, the readiness probe checks both the raylet and the Ray Serve health endpoint:
```
wget --tries 1 -T 2 -q -O- http://localhost:52365/api/local_raylet_healthz | grep success &&
wget --tries 1 -T 10 -q -O- http://localhost:8000/-/healthz | grep success
```
We're wondering if there's a good reason the /-/healthz check is not included in the liveness probe as well?

**What happened to us**

We experienced a production outage caused by this exact scenario. We have a GPU worker group with minReplicas: 1 and maxReplicas: 1, meaning there is always exactly one GPU worker pod running. On that GPU worker we run a single Ray Serve deployment replica (num_gpus: 1) that requires the GPU.

1. The Ray Serve replica running on the GPU worker pod entered a stuck unhealthy state. We are not sure of the exact root cause.
2. As a result, the /-/healthz endpoint on port 8000 stopped responding correctly, causing the readiness probe to fail.
3. The pod was marked NotReady by K8s but was never restarted because the liveness probe only checks the raylet, which was still healthy.
4. With the only GPU worker pod stuck and maxReplicas: 1 preventing a new one from being provisioned, the Ray Serve deployment became permanently unrecoverable.
5. Manual intervention was required, deleting the GPU worker pod triggered K8s to create a fresh one, and everything recovered immediately.

We worked around this by adding the /-/healthz check to our liveness probe:

```yaml
livenessProbe:
  exec:
    command:
      - bash
      - '-c'
      - >-
        wget --tries 1 -T 2 -q -O-
        http://localhost:52365/api/local_raylet_healthz | grep success &&
        wget --tries 1 -T 10 -q -O- http://localhost:8000/-/healthz | grep success
  initialDelaySeconds: 30
  timeoutSeconds: 15
  periodSeconds: 5
  failureThreshold: 3
```

But we wanted to raise this in case there's a deliberate reason it was left out? or whether this is something that could benefit others as a default? Is there a specific reason that the livenessprobe does not call `wget /healthz`?

**Environment**

KubeRay version: v1.5.0
Ray version: 2.54.0
K8s: EKS v1.33


### Reproduction script

Unfortunately I was not able to reproduce the exact issue. I could not find a way to make our GPU Ray Serve deployment get stuck.

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (4)

### Future-Outlier · 2026-04-11

cc @JiangJiaWei1103 to take a look and leave your thought

### JiangJiaWei1103 · 2026-04-11

Will look into this issue and provide my thoughts here, thx.

### JiangJiaWei1103 · 2026-04-14

Hi @nielstenboom,

The following summarizes my thoughts on this issue:

### Conclusion

We generally do not recommend including proxy actor health checks in the worker liveness probe in KubeRay. Instead, we suggest defining a custom liveness probe like what you did in your case as a workaround.

### Why

- **Flaky liveness behavior**:  
  Liveness probes run independently from readiness probes. If not carefully configured, they may start failing before the Serve application is successfully deployed, requiring careful tuning of `initialDelaySeconds`.

- **False positive restarts**:  
  Liveness probes cannot distinguish between transient failures (e.g., proxy actor restart, network glitches) and irrecoverable failures (e.g., deadlocks). As a result, transient conditions may trigger unnecessary container restarts.

- **Risk of cascading failures**:  
  In large clusters, aggressive or misconfigured liveness probes can lead to widespread restarts (`CrashLoopBackOff`), amplifying system instability, as mentioned in the Kubernetes docs [1].

### Context of Probing Design

https://github.com/ray-project/kuberay/pull/1808 outlines the probing design in KubeRay. In summary:

- **Avoiding circular dependency**:  
  Proxy actor health checks are not included in the head Pod readiness or liveness probes, since the Serve application is only deployed after the head Pod reaches the `Ready` state.

- **Distributed health checks for scalability**:  
  To reduce load on the KubeRay operator and improve scalability, proxy actor health checks are offloaded from the RayService controller (control plane) to kubelet (data plane) via readiness probes.

### Handling Stuck Workers

For scenarios where a worker becomes stuck due to proxy actor issues, it is generally preferable to handle recovery at a higher level (e.g., sidecar, external monitoring systems) rather than relying on liveness probes. This allows more controlled and context-aware recovery strategies.

### References

[1] https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/  
[2] https://kubernetes.recipes/recipes/deployments/liveness-readiness-probes/

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
