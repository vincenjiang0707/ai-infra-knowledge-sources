# [Issue #4720] [Bug] Autoscaler accumulates stale headgroup instances when ray-head container restarts without autoscaler container restarting

source: https://github.com/ray-project/kuberay/issues/4720
state: open | updated: 2026-09-23T04:42:34Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

Others, ray-operator

### What happened + What you expected to happen

### Versions
- KubeRay: v1.4.2
- Ray: 2.54.1
- Autoscaler: v2

### What happened

When the `ray-head` container restarts (due to liveness probe failure or crash) while
the `autoscaler` sidecar container keeps running, the autoscaler accumulates stale
headgroup instances in its in-memory state that are permanently stuck in an infinite
`TERMINATING → TERMINATION_FAILED → TERMINATING` loop.

Each `ray-head` restart generates a new `ray_id`. The autoscaler registers a new
headgroup instance for the new `ray_id` but cannot clean up the old one — because
the pod (same `cloud_instance_id`) still exists in Kubernetes and cannot be
"terminated" via the API. After N restarts of `ray-head`, there are N stale
headgroup instances looping every 300s indefinitely with no self-recovery.

**Root cause**: The autoscaler holds its instance state entirely in memory. When
`ray-head` restarts, only that container's state is reset — the `autoscaler`
container continues running with its stale state intact.

In our case: `ray-head` restarted 4 times (`Restart Count: 4`), `autoscaler` never restarted (`Restart Count: 0`), resulting in 4 stale headgroup instances looping simultaneously.


### What you expected to happen

Either:
1. The autoscaler should detect that the new `ray_id` belongs to the same
   `cloud_instance_id` (pod name) and replace the stale instance rather than
   creating a new one, OR
2. The autoscaler container should have a liveness probe that fails when
   `ray-head` restarts, so both containers restart together and state is
   consistent


### Steps to reproduce

1. Trigger a restart of the `ray-head` container only (e.g. via liveness probe failure, OOM, or manual `kubectl exec` kill) — autoscaler container must NOT restart
2. Repeat step 2 a few times
3. Observe autoscaler logs — a new headgroup instance is created per restart, old ones never reach `TERMINATED`


### Logs
[kube_ray_logs_autoscaler_incident.csv](https://github.com/user-attachments/files/26784545/kube_ray_logs_autoscaler_incident.csv)

```
timestamp                    | transition               | instance_id                          | ray_id                                                   | cloud_instance_id
-----------------------------+--------------------------+--------------------------------------+----------------------------------------------------------+----------------------
2026-04-11 13:53:23          |                          | c490a3ac-de06-464c-bd50-f08efb5af9ca |                                                          |
2026-04-11 13:53:28          | ALLOCATED->RAY_RUNNING   | c490a3ac-de06-464c-bd50-f08efb5af9ca |                                                          | ray-kuberay-head-hkxwm
2026-04-12 18:11:32          | RAY_RUNNING->RAY_STOPPED | c490a3ac-de06-464c-bd50-f08efb5af9ca | cc9f27f8576867505438cbe332d30fd28873b7290e04a501c0935dfe | ray-kuberay-head-hkxwm
2026-04-12 18:11:32          | RAY_STOPPED->TERMINATING | c490a3ac-de06-464c-bd50-f08efb5af9ca | cc9f27f8576867505438cbe332d30fd28873b7290e04a501c0935dfe | ray-kuberay-head-hkxwm
2026-04-12 18:11:38          | ALLOCATED->RAY_RUNNING   | 3ec3901b-f708-46c8-ac8a-0a116e8e5acf | 5909dc51001bf3cb8e47299d906f05860d18bb66c6d244b9c0f2f613 | ray-kuberay-head-hkxwm  ← restart #1: new instance_id, new ray_id, same cloud_instance_id
2026-04-13 15:28:51          | ALLOCATED->RAY_RUNNING   | 90b39587-2ca9-4751-8683-6faba537e5a5 | 49900bf1faf5fa562f892ccce7d54f4f1a4c952e87918afc3be98ebe | ray-kuberay-head-hkxwm  ← restart #2
2026-04-13 15:28:51          | RAY_RUNNING->RAY_STOPPED | 3ec3901b-f708-46c8-ac8a-0a116e8e5acf | 5909dc51001bf3cb8e47299d906f05860d18bb66c6d244b9c0f2f613 | ray-kuberay-head-hkxwm
2026-04-13 15:28:51          | RAY_STOPPED->TERMINATING | 3ec3901b-f708-46c8-ac8a-0a116e8e5acf | 5909dc51001bf3cb8e47299d906f05860d18bb66c6d244b9c0f2f613 | ray-kuberay-head-hkxwm
2026-04-13 16:45:54          | ALLOCATED->RAY_RUNNING   | b9616161-c737-4181-95a4-b63c7d496b16 | edfe4e6ee1ad0bdf04a5a5a2286162bc6d64d447c280ddbb6557301e | ray-kuberay-head-hkxwm  ← restart #3
2026-04-13 16:45:54          | RAY_RUNNING->RAY_STOPPED | 90b39587-2ca9-4751-8683-6faba537e5a5 | 49900bf1faf5fa562f892ccce7d54f4f1a4c952e87918afc3be98ebe | ray-kuberay-head-hkxwm
2026-04-13 16:45:54          | RAY_STOPPED->TERMINATING | 90b39587-2ca9-4751-8683-6faba537e5a5 | 49900bf1faf5fa562f892ccce7d54f4f1a4c952e87918afc3be98ebe | ray-kuberay-head-hkxwm
2026-04-13 16:49:15          | ALLOCATED->RAY_RUNNING   | 62e377da-943a-46ba-84d7-bd69cc0afe08 | 45f424f4d9567b164e2caa9e598574dcfb2355bdea39e28543c89a0e | ray-kuberay-head-hkxwm  ← restart #4 (current)
2026-04-13 16:49:15          | RAY_RUNNING->RAY_STOPPED | b9616161-c737-4181-95a4-b63c7d496b16 | edfe4e6ee1ad0bdf04a5a5a2286162bc6d64d447c280ddbb6557301e | ray-kuberay-head-hkxwm
2026-04-13 16:49:15          | RAY_STOPPED->TERMINATING | b9616161-c737-4181-95a4-b63c7d496b16 | edfe4e6ee1ad0bdf04a5a5a2286162bc6d64d447c280ddbb6557301e | ray-kuberay-head-hkxwm
```

### Additional notes

- `ray.io/ft-enabled: true` is set on the cluster (GCS fault tolerance via Redis)
- The issue persists across days with no self-healing
- The head pod itself is healthy and serving traffic throughout

### Reproduction script

N/A

### Anything else

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (4)

### fscnick · 2026-04-18

Hi @Future-Outlier , I'd like to help with this.

### fscnick · 2026-04-25

Hi @izolin-defy ,

Would you mind to share the yaml file that encounters this issue?

Do you enable the per-container restart feature in the cluster?  I tried to reproduce it but it would restart the pod, `Restart Count` does not accumulate.

However, in autoscaler v1 the `Restart Count` could accumulate but the content of log seems not like the content you mentioned. There is no status transition as you mentioned.

### fscnick · 2026-04-28

After a bit of investigation, I still not able to reproduce this issue.

Once the container reaches the `Terminated`, the pod would be deleted.
https://github.com/ray-project/kuberay/blob/318759482e8312ed4a0d75af90f9a61a1b1b3c77/ray-operator/controllers/ray/raycluster_controller.go#L1194-L1202

If the restartPolicy is not `Never`, it would not delete the pod. However, it could only be `Never` if the autoscaler v2 is enabled.
https://github.com/ray-project/kuberay/blob/318759482e8312ed4a0d75af90f9a61a1b1b3c77/ray-operator/controllers/ray/utils/validation.go#L218-L221

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
