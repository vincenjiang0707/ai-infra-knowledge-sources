# [Issue #4033] [Feature] add `ttlSeconds` field to `RayClusterSpec`

source: https://github.com/ray-project/kuberay/issues/4033
state: open | updated: 2026-09-24T04:46:05Z
labels: enhancement

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

It would be nice it there was a `ttlSeconds` field in `RayClusterSpec` that would allow the `KubeRay` controller to automatically cleanup old `RayCluster` instances. 

### Use case

I would like to have a staging-like environment where a `RayCluster` can be shared across multiple data processing steps - for faster startup time. 

When a new step runs, it would check whether there is already a `RayCluster` available to run on. If there isn't, it would create one. However, it's channeling to determine whether a step should *delete* a `RayCluster`, because it's unclear whether there are going to be other steps targeting the same cluster launched soon. 

Therefore, the only reliable cleanup mechanism can be implemented on the controller side (I mean, I could make a custom external schedule, but that's inferior UX), similarly how `RayJobSpec` has `ttlSecondsAfterFinished`. 

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (23)

### andrewsykim · 2025-09-02

We've discussed this feature in the past and I _think_ it makes sense, but can you share why you couldn't use RayJob? RayJob would be more efficiency since the cluster would be deleted immediately. 

### danielgafni · 2025-09-02

I don't want to delete the `RayCluster`, I want to reuse it across multiple steps to avoid unnecessary (in a dev/staging environment) waiting. I don't know when exactly would the next step be launched, so I just want to have some buffer time when the `RayCluster` is still available.   

I would use a `RayJob` in a production environment where I want the steps to be isolated and reliable.   

### andrewsykim · 2025-09-02

This makes sense, are you open to adding a PR for this feature? I'm happy to review it. 

### danielgafni · 2025-09-02

I don't really know any Go but can try doing it with the help of my friend Claude  

### kevin85421 · 2025-09-03

The behavior seems strange to me. In #4036, the RayCluster is deleted when the time reaches `CreationTimestamp + Spec.TTLSeconds` no matter how many jobs are running in the RayCluster. What happens if a Ray job is submitted to a RayCluster, and the cluster is deleted before the job finishes because it has expired?

Is terminating the RayCluster after it has been idle (with no running Ray jobs) for a period of time the ideal behavior for your use case? @owenowenisme is working on moving the queries of Ray dashboards into a background goroutine pool and then implementing idle termination: https://github.com/ray-project/kuberay/issues/2999#issuecomment-2649335659.

### kevin85421 · 2025-09-03

cc @rueian @Future-Outlier PTAL and share your thoughts if you have any.

### Future-Outlier · 2025-09-03

I agree that https://github.com/ray-project/kuberay/issues/2998 this is make more sense, since it will complex the logic in RayJob when a Ray job is submitted to a RayCluster, and the RayCluster is going to be deleted, but we also want to provide an option for users to configure that this RayCluster will wait for RayJob to finish.

I also super agree that "the RayCluster is deleted when the time reaches CreationTimestamp + Spec.TTLSeconds no matter how many jobs are running in the RayCluster"
This is super dangerous for most of users.

We should keep the controller's logic simple in summary.

### danielgafni · 2025-09-03

For my use case it would be sufficient, since I'd also bump ttlSeconds with each job submission, ensuring there is enough cluster lifetime left to complete the job. 

However, I agree that for most users this might not be desired.

The main goal I'm pursuing here is the reusal of (ephemeral) RayCluster across multiple jobs. So it doesn't make sense to wait for just one job to finish. 

Could we consider tracking multiple jobs instead? Not sure how feasible that would be. 

An alternative approach would be to allow RayJob to cleanup the cluster it targets with clusterSelector. Then we could create multiple RayJob instances running on the same cluster, and the controller could delete it once the last ttlSecondsAfteeFinished expires. 

### kevin85421 · 2025-09-03

Thank you for the reply!


> since I'd also bump ttlSeconds with each job submission, ensuring there is enough cluster lifetime left to complete the job.

This approach seems hacky to me.

> The main goal I'm pursuing here is the reusal of (ephemeral) RayCluster across multiple jobs. So it doesn't make sense to wait for just one job to finish.
> Could we consider tracking multiple jobs instead? Not sure how feasible that would be.

“Idle” means that there are no running Ray jobs in the cluster. It does not refer to just a single Ray job.

> An alternative approach would be to allow RayJob to cleanup the cluster it targets with clusterSelector. 

This is also not good behavior for me. In HTTPMode, the underlying assumption is that the cluster isn't owned by the CR, so we should not use the RayJob CR to manage the RayCluster. If we do, it feels like an abstraction leak to me.


### danielgafni · 2025-09-03

> “Idle” means that there are no running Ray jobs in the cluster. It does not refer to just a single Ray job.

Oh great, that's even better then! Sure, let's track the idle status rather than the cluster creation timestamp. 

### andrewsykim · 2025-09-03

Tracking idle status would require us to connect to the Ray cluster and perdiocally list jobs, which I thought we were trying to avoid? Not just jobs but also client sessions that may have created tasks / actors. Seems like a lot of complexity we would have to add in RayCluster controller.  

I think allowing users to set their own TTL is a reasonable use-case separate from terminating idle clusters after a timeout. It's up to the user to ensure their jobs completed within the TTL and I think that's ok. I think this is also generally useful for platform teams that may want to timebox the life of Ray clusters without necessarily caring about what job runs there. If you care about job completion you should use RayJob anyways. 

### andrewsykim · 2025-09-03

> I also super agree that "the RayCluster is deleted when the time reaches CreationTimestamp + Spec.TTLSeconds no matter >how many jobs are running in the RayCluster"
> This is super dangerous for most of users.

> We should keep the controller's logic simple in summary.

@Future-Outlier I think these two statements are countering each other. Deleting a cluster after a TTL is actually very simple, compared to trying to track idle clusters. 

Can you also expand on why it's dangerous? The feature is not on by default, a user is opting into the TTL so they understand a cluster is deleted regardless of the timeout. If a users finds it "dangerous" they do not need to enable the feature. 

### owenowenisme · 2025-09-03

@andrewsykim 
To track if cluster is idling, we currently do need to List job and filter if there existing running job on the cluster, but we will eventually create an endpoint in Ray DashBoard to know if cluster is idling.

### owenowenisme · 2025-09-03

And also IMO, using TTL have 2 downside
- User need to know how long the job will need to run, which doesn't seemed flexible
- User will be hard to use existing RayCluster, since they might reach TTL when running jobs

### kevin85421 · 2025-09-03

> Tracking idle status would require us to connect to the Ray cluster and perdiocally list jobs, which I thought we were trying to avoid?

We want to avoid communication between KubeRay and the Ray data plane. The main reason is to prevent blocking a single reconciliation, which could cause other CRs to wait longer for reconciliation. Therefore, we have several potential options:

* Option 1. @owenowenisme is working on moving the queries of Ray dashboards into a background goroutine pool. The main motivation for this one is mainly for RayJob, but it also makes communication between KubeRay and Ray dashboards acceptable because it will not block reconciliations.

* Option 2: Ask the Ray head Pod (possibly the Ray Autoscaler) to annotate itself with idle time.

Option 2 avoids communication between KubeRay and the Ray dashboard and is more scalable, but its implementation is more complex. Hence, it may make sense to start with Option 1, along with proper stress tests.

> Seems like a lot of complexity we would have to add in RayCluster controller.

Regarding the complexity concern, it may not be that complex if we already have a background goroutine pool for RayJob. Depending on the design of the goroutine pool, the implementation of idle termination should be fairly straightforward.

> Not just jobs but also client sessions that may have created tasks / actors.

In my understanding, both are Ray jobs, regardless of whether they are submitted via `ray job submit` or the Ray client. You can also submit a job via the Ray client and list the jobs to verify.

> I think allowing users to set their own TTL is a reasonable use-case separate from terminating idle clusters after a timeout. It's up to the user to ensure their jobs completed within the TTL and I think that's ok.

I may need more concrete use cases for this. Anyscale doesn’t support TTL, but it has supported idle termination for years, and it works quite well.


### andrewsykim · 2025-09-03

I think we should consider TTL and idle termination as two separate features and use-cases. 

1. TTL is useful for platform teams that want to give a Ray cluster to a data scientist on a time limit. Deleting the cluster even if there is a running job is desired behavior in this case. Automatically deleting it when idle could be undesirable as the data scientist may submit jobs with idle gaps between them.  
2. Terminating idle cluster is a cost savings feature that can be used by both platform team or ML engineer that create the Ray cluster themselves.

### kevin85421 · 2025-09-03

> TTL is useful for platform teams that want to give a Ray cluster to a data scientist on a time limit. Deleting the cluster even if there is a running job is desired behavior in this case.

In theory, this is possible, but we may need more evidence before moving forward with an API change. My only experience with this kind of behavior is from when I started a free trial for a SaaS service, and the vendor provided a limited period for the trial. I tried to do some investigations. Anyscale, [Databricks](https://docs.databricks.com/aws/en/compute/clusters-manage#terminate-a-compute), and [Snowflake](https://docs.snowflake.com/en/user-guide/warehouses-overview#auto-suspension-and-auto-resumption), to the best of my knowledge, only support idle termination and do not have TTL.

Does GKE Autopilot support terminating a node with a TTL or similar behaviors?

I’m not saying this is impossible. We can revisit it once we have enough signals. If the use case can be addressed by idle termination, we should go with idle termination, especially idle termination is a top item on the wish list. For TTL, we can revisit it when more use cases arise.

### andrewsykim · 2025-09-03

> I’m not saying this is impossible. We can revisit it once we have enough signals. If the use case can be addressed by idle termination, we should go with idle termination, especially idle termination is a top item on the wish list. For TTL, we can revisit it when more use cases arise.

I'm not opposed to the idle termination feature, in fact I had proposed something similar a few years ago to automatically delete Ray clusters once all jobs are completed https://github.com/ray-project/kuberay/issues/1740 :) I think we should build it. 

But again these are two separate features / use-cases. Implementing idle termination will not remove the need for TTLs as I mentioned above. Without mentioning specific names, I know of a few GKE users that have built their own TTL logic using annotations so I personally I think there's enough signal for this use-case. The initial use-case that @danielgafni mentioned for TTL is another data point as well. 

### kevin85421 · 2025-09-03

> But again these are two separate features / use-cases. Implementing idle termination will not remove the need for TTLs as I mentioned above.

Thank you. I understand the points you mentioned. We can ask users to open an issue for their TTL use cases and discuss them later. TTL doesn’t add significant complexity, and we should be open to implementing it once we have sufficient use cases.

> The initial use-case that @danielgafni mentioned for TTL is another data point as well.

In this use case, we need to patch the RayCluster CR's `ttlSeconds` with each job submission, so I think idle termination is a better solution.

My point is that if idle termination is a feature requested by many users to address the issue, we should implement it and revisit the TTL feature once we gather more information.

### andrewsykim · 2025-09-03

sounds good to me, let's revisit this later. I will review the idle termination feature from @owenowenisme as well

### danielgafni · 2025-09-03

I agree that idle termination is better suited for my use case, and is a great feature to have in general. 

I also think ttl as a separate feature makes sense.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### danielgafni · 2026-09-22

bumping this 
