# [Issue #4575] [Feature] Adopt the Gateway API Inference Extension with KubeRay

source: https://github.com/ray-project/kuberay/issues/4575
state: open | updated: 2026-09-22T16:58:48Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

The [Gateway API Inference Extension](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/) is a Kubernetes specification that allows cloud-native Gateways (e.g. Istio, Envoy Gateway, kgateway, etc.) to perform optimized load balancing across model server endpoints. This allows users to use standard Gateway API resources to be able to route across different models (even based on the body of the prompt) while taking into account utilization data from serving engines like vllm. Serving frameworks like [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo/tree/main/deploy/inference-gateway) and [llm-d](https://llm-d.ai/docs/guide/Installation/inference-scheduling) adopt this standard, and kuberay can as well. The first step would be to create an Endpoint Picker (EPP) service that is aware of kuberay context and is likely a part of the kuberay framework itself.

I'm not a kuberay expert, but I'm pretty well-versed in Gateway API and proxies, so I'm happy to help provide any and all context that I can.  

/cc @alimaazamat @ericdbishop 

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (13)

### andrewsykim · 2026-03-10

Thanks for opening the issue! @spencer-p is already exploring this and will probably share a proposal soon

### andrewsykim · 2026-03-10

> The first step would be to create an Endpoint Picker (EPP) service that is aware of kuberay context and is likely a part of the kuberay framework itself.

I don't think kuberay is the right framework to integrate with EPP, it may have to be in the Ray Serve layer because KubeRay is not aware of the model server ports. And it's unlikely we can use port 8000 on the nodes as it won't be compatible with extensiosn 

### jackfrancis · 2026-03-10

cc @alimaazamat 

### alimaazamat · 2026-03-10

@andrewsykim @spencer-p Is the proposal about using EPP with Gateway API in Ray Serve? I agree this can be a Ray Serve issue but just wondering if the proposal is covering this in Ray Serve?

### spencer-p · 2026-03-11

On a high level, there's two architectures to consider:

 1. Ray could work with the [reference endpoint picker implemented here](https://github.com/kubernetes-sigs/gateway-api-inference-extension).
    - This may involve making ray more amenable to the EPP and/or making the EPP more amenable to Ray,
    - but the low hanging fruit is to pipe through vLLM metrics and use existing scorers.
 3. Ray could fulfill the role of the endpoint picker by wrapping the [llm request routing policies](https://docs.ray.io/en/latest/serve/llm/architecture/routing-policies.html) or a [custom request router in ray](https://docs.ray.io/en/latest/serve/advanced-guides/custom-request-router.html) in an endpoint on the ray head that serves the [envoy proxy ext-proc protocol](https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ext_proc/v3/external_processor.proto).
    - This is probably a significant lift in the Ray Serve api.

And then from the kuberay side, we may want to give ray-operator the ability to provision at least the InferencePool and HealthCheckPolicy objects, if not the rest of the gateway objects, for ease of use.

My preference is to see how far we can take the first option to start. I imagine the second option could be very powerful but will require a fair bit of alignment from everyone to land.

### alimaazamat · 2026-03-11

@keithmattix had pointed out an issue with the first option is that GAIE is proposing removing that reference endpoint picker and making each implementation (such as Ray) build their own

### alimaazamat · 2026-03-11

Two things from my end:
- Why not use Ray Serve metrics for EPP routing instead of vLLM? I'm not opposed just curious because Ray Serve sits in front of vLLM info and would aggregate that info with replicas? Is it just more advantageous to use vLLM metrics?
- In a previous KubeRay community I believe we need to still suppport Ingress even though it is deprecated in favor of Gateway API just because users are still using it and migrating over will take some time. Problem here is that using Ingress to call out to an EPP to make routing decisions hasn't been done before by an Ingress controller before. So we should maybe just start with just making this work with Gateway API.

### spencer-p · 2026-03-11

> Why not use Ray Serve metrics for EPP routing [...]

I was thinking using the reference EPP as an example could be a simpler/easier way to demonstrate what's possible here and inform more decision making. I wasn't aware that EPP would be deprecated, and I would certainly agree that an EPP with knowledge of Ray specific metrics would be a bit more interesting.

However there is a bit of a decision point about whether that EPP should be external to the RayCluster (i.e. in a Deployment) or not. Managing a deployment alongside the RayService might run counter to the pythonic/ray way of doing things (writing a request router that runs in the ray serve data path). Or maybe it turns out those are separate personas and customers are happy separating those concerns.

> hasn't been done before by an Ingress controller before ... So we should maybe just start with just making this work with Gateway API.

Agreed.

### alimaazamat · 2026-03-11

Good point. Yeah, llm-d and Dynamo both implement EPP as an external deployment which seems to be the norm. But to keep it internal to Ray would make sense to get Ray info like replicas. 
So now our arch options to consider are:
1. Ray has an external EPP that uses vLLM metrics
2. Ray has an internal EPP with Ray Serve metrics

Let me know if I understood this correctly.
Thanks for exploring this and looking forward to the proposal!

### Future-Outlier · 2026-03-13

cc @win5923 to take a look, since you are investigating ingress and gateway usecases

### spencer-p · 2026-03-23

Here's my thoughts on a couple scenarios that could play out re Gateway and Ray.

**My opinion** is that using an EPP with Ray is a lot of work for really unclear
benefit. Performance improvements should be brought to Ray directly, not
externalized. However, multi-cluster request routing is an interesting angle to
explore for kuberay and cloud providers.

---

 ## Option 0: **No Ray Endpoint Picker**.

- Ray already provides users a [Custom Request Router](https://docs.ray.io/en/latest/serve/advanced-guides/custom-request-router.html)
  api. This is more idiomatic to Ray than an external K8s deployment for
  endpoint picking.
- Any features of an external endpoint picker could be reimplemented in Ray. For
  example, [this guide and custom request router does that](https://github.com/llm-d-incubation/py-inference-scheduler).
- There's no need for service discovery since Ray knows where all the services
  are.

You can create a gateway in front of Ray with a plain old Service pretty easily.
The only thing that Ray on K8s can't do for itself is multi-cluster routing.

## Option 1: **Bolstered support for multi-cluster routing**.

Because Ray can't do multi cluster routing, there's an interesting opportunity
for the next level of abstraction to manage directing traffic between multiple ray clusters.
For example, [I wrote a guide for body based routing between two rayclusters](
https://github.com/spencer-p/ray-inference-gateway-guide/tree/main/body-based-routing).
I think spillover to lower cost clusters based on high level metrics (like total
CPU usage, etc) could be an interesting use case as well.

This is something that may be preferable to manually configure, but maybe
KubeRay can help with provisioning some of the boilerplate.

## Option 2a: **A Ray aware endpoint picker.**

Hypothetically we could write an endpoint picker that watches Ray's metrics on
8080 and the deployment config on `/api/serve/applications`, etc, and can make
routing decisions. But there's a number of caveats:

1. Ray serve replicas are not fungible. Inside any given ray replica might be
   any number of serve replicas, and often none of them are an ingress replica.
   So this endpoint picker needs to track which ingress replicas are on which
   nodes and which path prefixes they serve to direct traffic accordingly.
2. Deployments are multi-tier. A simple LLM deployment might have one
   OpenAIIngress and multiple LLMServers. An EPP would want to direct traffic to
   an LLMServer with capacity, but it has to go through the ingress first. So we
   need *two seperate headers* added to the request, one to route the request to
   the ingress and another to hint to Ray Serve which replica (actor) to choose
   after it goes through the ingress.
3. And what if it's more than two tiers? Some customers run workloads that pass
   a request through multiple models. By the time a request routes through the
   first tiers, whatever decision the EPP made 30s+ ago is probably outdated.
   And are we writing a header with a comma separated list of actors to route
   to? This is why Ray makes the next routing decision in Python when it's
   needed, in real time.
4. The endpoint picker would have limited visibility into Ray internals (since
   it is only using the external API and metrics).

Some of this HTTP header grunt work is probably weird enough that we'd want to
build the support into Ray Serve.

I wrote a [guide to using the reference endpoint picker and vLLM with
Ray](https://github.com/spencer-p/ray-inference-gateway-guide/tree/main/external-epp),
which involves a custom request router reading HTTP headers. This example only
really makes sense for single-replica workers.

## Option 2b: **Ray is the endpoint picker.**

This is like #2 above but we expose the CustomRequestRouters' logic as an ext
proc compatible endpoint from the ray head. This probably looks really appealing
to folks that love Ray custom request routers as well as inference gateway, if
those people exist. It's also probably a ton of work in upstream Ray and has
similar downsides as outlined above.




### alimaazamat · 2026-03-24

Yeah I like leaning into option 1, it can align with kuberay federation https://github.com/ray-project/kuberay/issues/4561 

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
