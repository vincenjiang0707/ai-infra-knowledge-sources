# [Issue #4286] [Feature] Sync rayjob or raycluster annotation to podgroup

source: https://github.com/ray-project/kuberay/issues/4286
state: open | updated: 2026-09-22T16:57:40Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Users have made modifications to the community-based volcano, and the custom feature interacts with the scheduler through the annotation of the podgroup. At this time, they need to support passing the annotation on the rayjob or raycluster to the podgroup resource

### Use case

For example, some experimental switches or scheduling preference attributes will be attached to the annotation to trigger the scheduler behavior. This ability can prevent users from having to modify kuberay's code to pass it through to podgroup. Special annotation can be specially processed into podGroup's spec

### Related issues

_No response_

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (10)

### dushulin · 2025-12-17

cc @kevin85421  @Future-Outlier PTAL, Thanks!

### seanlaii · 2025-12-17

I am interested in this. Could you provide some links regarding these features in volcano? Thanks!

### win5923 · 2025-12-17

Hi @dushulin, which feature are you using? We could handle this in a similar way to https://github.com/ray-project/kuberay/pull/4105



### dushulin · 2025-12-22

> Hi [@dushulin](https://github.com/dushulin), which feature are you using? We could handle this in a similar way to [#4105](https://github.com/ray-project/kuberay/pull/4105)

@win5923 @seanlaii Thanks for reply, our inner volcano version use annotation aie.io/best_schedule_unit=32 which configured on podgroup.scheduling.volcano.sh cr. Tells the scheduler how many pods to distribute under one unit
In the future, we may have other annotations for the interaction between the controller and the scheduler, and each time we modify the controller code adaptation is costly. If these annotations can be passed from upper cr to pg without other side effects, I think this feature will be very useful in many scenarios
And I implemented a pr. If you think this feature is in line with the community building philosophy, I will submit a pr. to you for review.

### win5923 · 2025-12-25

SG

### dushulin · 2025-12-25

I will submit a pr this week, help review

### seanlaii · 2025-12-26

Hi @dushulin , I agree that we might need a way to pass the annotations/labels to the `podGroup`. 
I would like to know if this pattern is common when using `volcano`: using annotations/labels of `podGroup` to control the scheduling behavior?
Thanks!

### Future-Outlier · 2026-01-03

todo: we should make sure is this a common pattern or not, thank you!

### dushulin · 2026-01-05

> Hi [@dushulin](https://github.com/dushulin) , I agree that we might need a way to pass the annotations/labels to the `podGroup`. I would like to know if this pattern is common when using `volcano`: using annotations/labels of `podGroup` to control the scheduling behavior? Thanks!

Sorry for late reply, I mainly consider it from two aspects: 1. In cloud-native development, one of the main ways for controller components to interact and transfer information is set information on labels and annotations. Therefore, in the internally maintained version of volcano, many beta features will be written on annotations. 2. Volcano officials also use annotations extensively to control scheduling behavior, such as volcano.sh/queue-name, volcano.sh/priorityClassName, etc.

cc @Future-Outlier We can discuss together whether it is appropriate to pass all rayclusters or rayjob annotations

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
