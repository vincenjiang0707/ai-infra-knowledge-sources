# [Issue #4823] [Feature] Ray GPU Failure Correlation Component

source: https://github.com/ray-project/kuberay/issues/4823
state: open | updated: 2026-09-23T04:43:02Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.

CC: @ganeshkumarashok for coming up with using Xid errors + NPD in Ray and also working on this

### Description
NPD: https://github.com/kubernetes/node-problem-detector

An optional, standalone Kubernetes controller `ray-failure-correlator` that watches RayJob / RayCluster failures and joins them with node-level evidence (NPD events, NodeConditions, kubelet termination reasons) to attribute a root cause (HardwareFailure, InfraFailure, ApplicationFailure, Unknown).

A working end-to-end prototype (NPD with Xid kernel-monitor rules + a stand-alone Python correlator + a no-GPU in-process simulator) WIP: 


### Use case

When a Ray job on a GPU node hits a hardware fault (e.g. NVIDIA Xid 79, "GPU has fallen off the bus"), CUDA returns a generic error code, Ray wraps it as RayTaskError, and KubeRay records [status.reason: AppFailed]. The failure is misleading as an application bug.

The real signal lives in dmesg on the node.
If NPD gets configured with Xid rules it would have it in Node.status.conditions (GPUHealthy=False) and Kubernetes Events (Warning NvidiaXid79).  But currently nothing automatically joins those signals to the failed RayJob.

The Kubernetes API server has both:
the failure object ([RayJob.status](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html), terminated pod) + node-level evidence (Events, NodeConditions)
so a controller with access to both could do the join and correlate

### Related issues


_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (11)

### andrewsykim · 2026-05-11

@alimaazamat thanks for opening this issue. BTW @richabanker is working on bringing Kubernetes events into Ray Dashboard (see initial PR https://github.com/ray-project/ray/pull/62314) and we plan to extend that to also cover events from other sources like NPD and custom operators. Would be great to collaborate in this area and figure out a way to bring GPU failure events directly into Ray Dashboard. 

### andrewsykim · 2026-05-11

As a starting point, we should check if NPD is capable of emitting Kubernetes events about GPU failures. And then in KubeRay we may need a controller similar to what you suggested like `ray-failure-correlator` that adds a reference to the RayCluster or emits another event with the correct object ref that is ingested into Ray Dashboard. 

### richabanker · 2026-05-11

I dont think there's an oss plugin in the NPD added yet for detection of GPU failures which are surfaced as node events. The current list only includes these https://github.com/kubernetes/node-problem-detector/tree/master/config/plugin. We'd need to first add a plugin that does this.

cc @SergeyKanzhelev in case you know if there are plans to add one

### alimaazamat · 2026-05-11

Thanks so much @andrewsykim @richabanker 
The existing [kernel-monitor plugin](https://github.com/kubernetes/node-problem-detector/blob/master/config/kernel-monitor.json) already tails /dev/kmsg and emits Node warning events. So, I think that can use XID errors from the kernel ring buffer? (I'm still learning so bear with me)
So no new plugin needed but was thinking to add rules/functionality for Xid/GPU rules


### alimaazamat · 2026-05-11

The rules/functionality would maybe be a JSON rule file in `config/`https://github.com/kubernetes/node-problem-detector/tree/master/config for system-log-monitor.
https://github.com/kubernetes/node-problem-detector/tree/master/config/plugin is only for custom-plugin-monitor
So Xid errors would be in kmsg would be for system-log-monitor


### ganeshkumarashok · 2026-05-11

For more context: this feature was inspired by a conversation I had with AnyScale during RayDay Seattle, where they shared challenges of differentiating ray failures from the underlying platform issues (GPU hardware failures), or version compatibility issues (ex: Pytorch compatibility with cuda version installed on the node). 

At Azure Kubernetes Service, we have GPU NPD:  https://learn.microsoft.com/en-us/azure/aks/gpu-health-monitoring, where we run separate custom plugins for NPD, with GPU health checks largely similar to https://github.com/Azure/azurehpc-health-checks/. 

One of the challenges with the design of GPU NPD is that some of the GPU health checks are hardware/GPU VM instance specific. Example: GPU count health checks which check for the expected number of GPUs and let's say if `nvidia-smi` returns 7 instead of 8 GPUs, then a `GPUMissing` node condition can be returned. Supporting those GPU-instance specific checks without hardcoding is challenging.

To start off, for kuberay, we could support GPU checks like XID errors or clock throttling failures which are surfaced similarly across all Nvidia GPUs, which means they don't need GPU-instance type specific hardcording (although there will be GPU vendor differences between say how Nvidia and AMD surface the errors).

### ganeshkumarashok · 2026-05-12

GPU NPD feature request for reference: https://github.com/kubernetes/node-problem-detector/issues/833. It's been open for a few years. 

### andrewsykim · 2026-05-12

@ganeshkumarashok makes a lot of sense and reflects similar pain points we hear from GKE users. The challenge will be generalizing this to work on any Kubernetes platform providing GPUs. I'm definitely open to exploring if there's anything more we should be doing in KubeRay for this.  

### SergeyKanzhelev · 2026-05-12

From requirements perspective, I am wondering if this KEP: https://github.com/kubernetes/enhancements/issues/4680 made the situation better for Ray? Do you need failing devices on Nodes in Node status or Pods in Pod Status? Failing devices on nodes will be removed from the allocatable so there is already a signal. Having it in Pod Status gives some extra information WHY the pod failed.

### richabanker · 2026-05-12

> From requirements perspective, I am wondering if this KEP: [kubernetes/enhancements#4680](https://github.com/kubernetes/enhancements/issues/4680) made the situation better for Ray? Do you need failing devices on Nodes in Node status or Pods in Pod Status? Failing devices on nodes will be removed from the allocatable so there is already a signal. Having it in Pod Status gives some extra information WHY the pod failed.

We are not necessarily looking for Pod/Node status surfacing GPU failures (partly since I am not sure how much detail about the failure those would include, but it might still be nice to have to use this info for pod scheduling/autoscaling decisions in Ray or KubeRay). For starters, we are looking to have a corresponding K8s event generated for GPU failures as detected by NPD that we could then surface in the Ray Dashboard (primary debugging tool used by Ray users) for failure detection at all levels (Ray / K8s / Hardware(GPU))


### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
