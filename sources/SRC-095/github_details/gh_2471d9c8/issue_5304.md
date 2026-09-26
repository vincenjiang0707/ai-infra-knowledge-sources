# [Issue #5304] [Feature] Forward Kubernetes Pod events for autoscaler-driven remediation

source: https://github.com/ray-project/kuberay/issues/5304
state: open | updated: 2026-09-22T23:23:19Z
labels: enhancement

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.

### KubeRay Component

ray-operator

### Description

Extend the selective Kubernetes event forwarder introduced in [#4978](https://github.com/ray-project/kuberay/pull/4978) to support events involving Ray-managed Pods.

The current Node event forwarder re-emits selected infrastructure events onto the affected `RayCluster` and `RayJob` resources. Pod-level events could provide additional, actionable signals that are not always represented by Node events—for example volume-mount failures, container/runtime failures, or device-related problems affecting an individual Ray Pod.

The forwarded signal should also have a stable, structured contract that an autoscaler or a separate remediation controller can consume. Event forwarding and remediation should remain separate concerns: forwarding is observational, while any destructive action must be explicitly enabled and policy-driven.


### Use case

Pod events can enable targeted recovery from infrastructure failures that the Ray autoscaler cannot currently observe directly.

Examples:

1. **NFS or volume-mount timeout**

   If a Ray worker Pod repeatedly receives `FailedMount` or `FailedAttachVolume` events because an NFS mount timed out, Ray autoscaler can delete the Pods. 

2. **Problematic GPU node**

   If Pod- or Node-level signals indicate persistent GPU/device failures, Ray autoscaler could "cordon" the affected Ray Pod to avoid scheduling Ray actors/tasks to the Ray Pod and wait for the K8s cluster admin cordon / drain the node. 

This could reduce the time that Ray workloads remain stuck because of Kubernetes infrastructure failures, while keeping remediation behavior opt-in and auditable.

### Related issues

- [#4978 — Forward Kubernetes Node infrastructure events to Ray custom resources](https://github.com/ray-project/kuberay/pull/4978)

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### kevin85421 · 2026-09-16

This may need more discussions. It would be helpful to align with the community before working on it.

### kevin85421 · 2026-09-17

On second thought, if we want to handle issues such as Pods failing to mount NFS, perhaps KubeRay should delete the Pod and emit an event instead of letting the Ray Autoscaler handle it. My thinking is that KubeRay should own the Pod lifecycle until the container starts running; once the Pod is running, the Ray Autoscaler should take over.

I’m still not entirely sure whether KubeRay should handle this kind of infrastructure issue, since it isn’t directly related to either Ray or KubeRay. For node-level issues, infrastructure components such as NPD and NVSentinel are dedicated to detecting and remediating them. However, I’m not aware of any community component that handles similar issues at the Pod level.

The NFS mount issue is pretty common in our environment but I am not sure whether this is also common for other users.

### richabanker · 2026-09-22

I am a bit confused by 

> Extend the selective Kubernetes event forwarder introduced in https://github.com/ray-project/kuberay/pull/4978 to support events involving Ray-managed Pods

The k8s_provider module in upstream Ray for collecting and exporting Platform Events, already has a [pod_event_watcher](https://github.com/ray-project/ray/blob/167c1808265ba9a56eef6b653e1c1ddce84ba6b6/python/ray/dashboard/modules/platform_events/providers/k8s_provider.py#L423-L486), so currently any events emitted for k8s pods are being consumed as RayEvents by the Ray Dashboard head and streamed into the Ray dashboard.  Did you mean an extension on this existing feature?

One clarification regarding 
> The current Node event forwarder re-emits selected infrastructure events onto the affected RayCluster and RayJob resources.

We decided in the [implementation of the Node-event forwarder](https://github.com/ray-project/kuberay/pull/4978#discussion_r3945094177) that we'd re-emit the events onto the affected *RayCluster only*

Also, I definitely agree that making failure signals more actionable is a great direction. However, we should be cautious about driving destructive or disruptive actions (such as pod deletion or cordoning) directly off raw Kubernetes events, since the K8s events API is lossy, sampled, and subject to aggressive TTL expiration (default 1 hour) and API server rate limits ([ref](https://kubernetes.io/docs/reference/kubernetes-api/core/event-v1/#Event)). But maybe we could take a more cautious path of only taking some action if a huge influx of some certain type of critical failure like event is seen or surfacing them as a Condition on the custom resource status first? 

Before we dive into that though, would like to clarify the scope of what this issue is trying to address? Is it:
1. to re-emit Pod-level events onto RayCluster for external consumers/controllers ?
2. about Remediation ownership (KubeRay Operator vs. Ray Autoscaler vs. Generic K8s Tooling)? First, how do we even meaningfully consume these signals to drive a safe and reasonable action?
