# [Issue #4341] [Feature] Report RayJob Progress and Job Metrics via the CR

source: https://github.com/ray-project/kuberay/issues/4341
state: open | updated: 2026-09-22T16:57:44Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

It would be nice to report some kind of Job progress via the RayJob CR, whether it's epochs or a percentage based metric so users can view how far along their Jobs are. If added to the CR this would allow the progress to be reported in UIs like Ray Dashboard, Kuberay Dashboard, and other custom dashboards.

I would be happy to submit a PR(s) for this if others agree we need this and an implementation can be decided upon!

I have a vague idea that I've seen this mentioned elsewhere before so this might be a duplicate

#### What we could include
- Progress
    - Estimated Time Remaining
    - Steps
    - Epochs
- Metrics
    - Loss
    - Accuracy
    - Total Batches
    - Total Samples

### Use case

Just some example use cases I can think of
- I have a custom UI for RayJobs that shows information from the RayJob CRs present on the cluster. I would like to show some kind of progress in the UI of how a running RayJob is going. I would need to fetch this via the CR.
- I am going to submit a medium priority job but there is one lower priority job running. It is at 90% (or 90/100 epochs) found via the CR, and so I might want to wait to submit my higher priority job so that we don't lose that progress. This is especially useful as checkpointing needs to be manually configured via the training script, so if the low priority job is preempted, it won't necessarily be checkpointed.

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (5)

### Future-Outlier · 2026-01-06

1. I guess maybe something like kubeflow evaluator might be similar to this
2. does spark operator has similar thing?
3. does flink operator has similar thing?

cc @win5923 @machima @AndySung320 @400Ping @justinyeh1995 @troychiu @seanlaii to take a look

### Future-Outlier · 2026-01-06

Hi, @kryanbeane can you explain why Ray Dashboard right now is not good enough?
If we introduce this, we might increase the burden of kuberentes API server right?

### kryanbeane · 2026-01-06

Hey, thanks @Future-Outlier 
Yeah Kubeflow Evaluator is where I've gotten this from.

The Ray Dashboard doesn't give any indication of how long might be left for a running Job.

> we might increase the burden of kuberentes API server right?

Yes I guess we would. Whether it would be to a significant degree I'm not sure. 

### Future-Outlier · 2026-01-10

I just discussed with @seanlaii and @rueian 
we think maybe add metrics in ray train might make more sense, what do you think?
@kryanbeane 


### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
