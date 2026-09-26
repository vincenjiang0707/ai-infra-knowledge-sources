# [Issue #4455] [Feature] Support multiple Ray containers per Pod

source: https://github.com/ray-project/kuberay/issues/4455
state: open | updated: 2026-09-22T16:58:14Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

It may be beneficial to support creating multiple Ray workers on the same Pod created with KubeRay. 

There is more context in this PR: https://github.com/ai-on-gke/kuberay-tpu-webhook/pull/19, which supports multiple TPU containers with KubeRay, and specifically this comment: https://github.com/ai-on-gke/kuberay-tpu-webhook/pull/19#issuecomment-3808077486.

I was able to create a RayCluster with 2 workers, each with 2 Ray containers (so 4 Ray nodes total), and run a workload on it. However, in order to avoid port conflicts and pass the correct Ray resources it's necessary to manually construct a `ray start` command for the second container. The amount of manual intervention required by the user would be reduced if KubeRay updated the resource detection logic and port assignment to handle multiple containers automatically.

### Use case

TPU v7x introduces a dual-chiplet architecture where a standard 4-chip VM spans two distinct NUMA nodes. To optimize memory bandwidth and avoid cross-NUMA latency, v7x workloads can now run as multiple NUMA-aligned containers within a single Pod. This would entail multiple Ray containers on the same Pod created by KubeRay.

More context on the new accelerator: https://docs.cloud.google.com/tpu/docs/tpu7x

### Related issues

N/A

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (13)

### Future-Outlier · 2026-01-31

this is related to this https://github.com/ray-project/ray/issues/59551.
(single host, multi-node scenario)

### ryanaoleary · 2026-02-05

cc: @andrewsykim @Future-Outlier @rueian We're thinking about trying to include this support in v1.6 since multiple containers per Pod for TPU workloads (2 containers each requesting 2 chips) will be the most common deployment pattern for Ironwood (tpu7x) TPU.

I can share a design document once I figure out the scope of the change, but at a high level I think it would involve a new API in the RayCluster or WorkerGroup indicating the number of Ray containers, and then logic in `pod.go` to assign unique Ports and detect the Ray resources for each Pod. Does that sound doable for v1.6?

### Future-Outlier · 2026-02-05

Hi, @ryanaoleary 

1.	We are planning to release v1.6 on March 15, so I can’t guarantee this will be included.
2.	I’d be happy to take a look at this in the next two weeks.
3.	One concern I have is that Ray assumes single host / single node in many places, but this use case is single host with multiple nodes. I’m wondering whether there could be Ray-side bugs in this scenario.
4.	Have you tried this setup and confirmed it works? Specifically, running multiple Ray containers per Pod with this TPU. Before moving forward, I’d like to make sure this actually runs and doesn’t hit any Ray edge cases.


### ryanaoleary · 2026-02-06

> Hi, [@ryanaoleary](https://github.com/ryanaoleary)
> 
> 1. We are planning to release v1.6 on March 15, so I can’t guarantee this will be included.
> 2. I’d be happy to take a look at this in the next two weeks.
> 3. One concern I have is that Ray assumes single host / single node in many places, but this use case is single host with multiple nodes. I’m wondering whether there could be Ray-side bugs in this scenario.
> 4. Have you tried this setup and confirmed it works? Specifically, running multiple Ray containers per Pod with this TPU. Before moving forward, I’d like to make sure this actually runs and doesn’t hit any Ray edge cases.

@Future-Outlier Sounds good, and yeah I tested the setup in this comment: https://github.com/ai-on-gke/kuberay-tpu-webhook/pull/19#issuecomment-3808077486 running a simple test for JAX init, and one with Ray Train.

### ryanaoleary · 2026-02-06

> > Hi, [@ryanaoleary](https://github.com/ryanaoleary)
> > 
> > 1. We are planning to release v1.6 on March 15, so I can’t guarantee this will be included.
> > 2. I’d be happy to take a look at this in the next two weeks.
> > 3. One concern I have is that Ray assumes single host / single node in many places, but this use case is single host with multiple nodes. I’m wondering whether there could be Ray-side bugs in this scenario.
> > 4. Have you tried this setup and confirmed it works? Specifically, running multiple Ray containers per Pod with this TPU. Before moving forward, I’d like to make sure this actually runs and doesn’t hit any Ray edge cases.

 [@Future-Outlier](https://github.com/Future-Outlier) Sounds good, and yeah I tested the setup in this comment: [ai-on-gke/kuberay-tpu-webhook#19 (comment)](https://github.com/ai-on-gke/kuberay-tpu-webhook/pull/19#issuecomment-3808077486) running a simple test for JAX init, and one with Ray Train. It worked for both examples but I agree it could run into bugs with Ray for more complex examples.

### Future-Outlier · 2026-02-06

Hi, @ryanaoleary just an edge case comes to my mind.
this might not work properly with the history server project, is that ok in your usecase?
this is ray's problem, for more detail, you can see here.
https://github.com/ray-project/ray/issues/58880#issuecomment-3636959240


### Future-Outlier · 2026-02-06

Hi @ryanaoleary, if possible, please also let me know what the potential new API might look like in your mind.

### rueian · 2026-02-06

Hi @ryanaoleary, do you know where the "NUMA-aligned" for containers happens? Can't that be done inside one container? Such as setting affinities to processes?



### ryanaoleary · 2026-02-06

> Hi [@ryanaoleary](https://github.com/ryanaoleary), do you know where the "NUMA-aligned" for containers happens? Can't that be done inside one container? Such as setting affinities to processes?

NUMA alignment requires resource alignment across cpu, memory, TPUs and the NIC. The alignment can be done through creating containers that align on the NUMA boundaries and allowing the topology manager in the Kubelet to handle the scheduling. This is how frameworks like Jobset and XPK handle Ironwood. Alternatively, if we had the two worker processes run on the same pod (same Ray node, so sharing 1 Raylet) I think we could also try to ensure NUMA alignment through using `numactl` when the process starts but I haven't explored this option as much.

> if possible, please also let me know what the potential new API might look like in your mind.

I think it could look something like:
```
workerGroupSpecs:
- replicas: 0
  rayContainers: 2
  ...
  template:
      spec:
        containers:
        <2+ containers>
```
I think the controller would then just have to validate that `template.Spec.Containers` contains at least `rayContainers` containers, and it can construct the `ray start` arguments/set unique ports for the first `rayContainers` out of the total defined for the Pod.

> this might not work properly with the history server project, is that ok in your usecase?
this is ray's problem, for more detail, you can see here.

I think ideally it would work together, so maybe that's another reason we should try to get `numactl` to work within Ray when the worker process starts. Alternatively, it seems like your solution to write logs to `/tmp/ray/session_latest/{node_id}/` would work for the multi-container setup since each container would have it's own node id.

### rueian · 2026-02-06

>  I think we could also try to ensure NUMA alignment through using numactl when the process starts but I haven't explored this option as much.

Thanks for sharing! Happy to learn that. One more question: aren't multiple pods on the same host also NUMA-aligned?

> maybe that's another reason we should try to get numactl to work within Ray when the worker process starts.

I think that will be ideal, in the sense of avoiding unnecessary Raylet, but that may be much more difficult to implement than multiple containers in KubeRay.

### Future-Outlier · 2026-02-06

I'm also curious about how ray autoscaler is going to work in this case?

### ryanaoleary · 2026-02-06

> Thanks for sharing! Happy to learn that. One more question: aren't multiple pods on the same host also NUMA-aligned?

Yeah that's another potential workaround - but it'd require a change in Google Common Webhooks (GCW) since currently there's a requirement that Pods running on TPU request the full # of chips in the VM across all the containers in the Pod (so for a 4 chip VM all chips would need to be used by the same Pod). This is a restriction we could potentially loosen, in which case we could create multiple NUMA-aligned Pods to achieve the same behavior.

> I'm also curious about how ray autoscaler is going to work in this case?

The V2 autoscaler uses Pod names as the [cloud instance ID](https://github.com/ray-project/ray/blob/521cb0ece4d05773e59b295660eefd7f0b4f329d/python/ray/autoscaler/v2/instance_manager/cloud_providers/kuberay/cloud_provider.py#L550) which means it also wouldn't work for multiple Ray nodes per Pod. When one Ray node on a Pod is terminated, it would result in the Pod being deleted along with the rest of the nodes erroneously. We would have to update the v2 autoscaler logic to consider all Ray nodes on the Pod when making scaling decisions. For TPU though, this might not be a problem because Ray nodes on the same TPU slice are scaled atomically anyway, so if 1 was scaled down all should be scaled down.

I am looking into the other two workarounds (i.e. `numactl` when Ray creates the worker process, or the workaround of creating more single-container Pods that are NUMA-aligned) and will update this issue with a design doc / solution.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
