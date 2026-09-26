# [Issue #476] Adding scaling down to 0 case Gateway handling 

source: https://github.com/vllm-project/aibrix/issues/476
state: open | updated: 2026-09-25T01:06:52Z
labels: area/autoscaling, area/gateway, kind/feature

## 正文

### 🚀 Feature Description and Motivation

The autoscaler should support scaling down to 0. When a new request arrives, we should have an activator component intercepts the request and initializes a new pod. Right now, we will simply get the following error if the number of replicas is 0 for a model inference request.

```
error on getting pods for model llama2-7b
```

### Use Case

_No response_

### Proposed Solution

_No response_

## 评论 (9)

### newhans · 2025-05-29

Being able to scale down from 1 to 0 and scale up from 0 to 1 is a fundamental capability of HPA. We can enhance our elasticity component by adding conditional scaling statements, triggered by QPS or other metrics? @Jeffwan 

### halittiryaki · 2025-09-07

so is scale up from 0 pods currently not supported?

the docs provides an example with `minReplicas: 0` but mentions that this is needed for the optimizer based scaler, and an additional label `model.aibrix.ai/min_replicas: "1"` to keep one alive still.

but didn't find a clear state statement, that scaling up from 0 pods is not supported for any scaler component.

### dafu-wu · 2025-09-16

@Jeffwan Hi, scaling up from 0 pods is not supported yet?

### sadath-12 · 2025-09-28

Any update on this ?

### Jeffwan · 2025-09-30

@halittiryaki  @dafu-wu @sadath-12 do you have strong needs for this feature? The problem is the activation needs to be handled separately, it would be super slow and I doubt whether that's super helpful. let me know your thoughts and we can prioritize it for basic autoscalers. 

### halittiryaki · 2025-09-30

@Jeffwan it will be super helpful for a scenario where gpu resources are very limited, but the amount of models for various autom. tasks are high. scale to 0 will allow me to schedule inference based queries efficiently.

for my use cases, rps based scale to 0 would be sufficient. is it possible to integrate with the knative scheduler, like:
https://knative.dev/docs/serving/autoscaling/rps-target/


### Jeffwan · 2025-10-01

@halittiryaki i just like to confirm on the client side behavior. Let's say the replica is 0 now, do you expect the proxy hold the request, until the node is up and then forward the request? or the request can be discarded at the same time, the client will retry. once the node is up, the request pass? 


in your case, we have an experiment work ongoing to load/unload base model. but the maturity is not enough. In that case, let's assume we can swap the base model directly. would it be helpful?

### halittiryaki · 2025-10-09

> do you expect the proxy hold the request

yes. some client will be 3rd party in my case, without retry

> In that case, let's assume we can swap the base model directly

The challenge here would be to eventually re-schedule the pod to a different node, if the requested model / resources are not available on the node where the pod is currently scheduled. Also, maybe another issue will be resource leakage over time?

how about following approach of introducing a `model.aibrix.ai/priority` label for deployments?

A currently 0-scaled higher prio deployment, gives a <= prio and >0 scaled deployment `x` time configurable by `terminationGracePeriodSeconds` or a new label `model.aibrix.ai/scale-down-grace-period`, to free up resources / scale down.


### bolubo · 2026-09-25

Hi all. We would like to pick this up if nobody else is actively on it.

Short plan: when a request arrives for a model that has no ready pods because it was scaled to zero, the gateway should trigger an activation for that model and hold the request until a pod becomes ready, then route normally. This matches the hold behavior discussed earlier in this thread. The hold has a bounded timeout, and if the model does not come up in time, the gateway falls back to 503 with Retry-After. The gateway's existing ext_proc and route timeouts are 600s, which leaves room for a bounded hold.

@zhangjyr @nwangfw you are listed as the assignees here. If either of you is still planning to work on this, please let us know. Otherwise we will start with the gateway side and follow up with the autoscaler coordination.

One design point we would love input on: should the gateway scale the target directly when it sees the first request, or should it only record the activation and let the autoscaler own the 0 to 1 transition?

