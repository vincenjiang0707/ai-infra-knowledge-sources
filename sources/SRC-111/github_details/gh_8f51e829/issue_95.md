# [Issue #95] Have GuideLLM kick off a vLLM server automatically to avoid having the user install vLLM and assign the target themselves

source: https://github.com/vllm-project/guidellm/issues/95
state: open | updated: 2026-09-23T19:31:07Z
labels: internal

## 正文

**Description:**
The proposal here is to change the architecture of how GuideLLM runs so that when a user runs GuideLLM it automatically kicks off a vLLM server and supplies GuideLLM with the necessary data to run the benchmark. This also covers adding any necessary pass-through parameters to vLLM to GuideLLM so that the user can just run GuideLLM to do a full end-to-end benchmark on a model. This is a UX enhancement. 

**Acceptance Criteria:**
- Enable GuideLLM to kick off a vLLM server when GuideLLM is run
- Enable GuideLLM to accept the necessary pass-through arguments that need to go to vLLM:
-- model (required)
-- port (optional)
-- TBD

## 评论 (1)

### dagrayvid · 2025-03-10

I'm not sure that we should add orchestration of the vLLM server to the scope of GuideLLM, for a few reasons:

- Want the tool to stay agnostic of the runtime engine, we may want to add different backends to support other runtime engines.
- Don't want the tool to be opinionated about the platform that the runtime engine is deployed on. If we wanted to support model deployment we would likely want to support k8s, KServe, Podman, bare-metal, etc...
- Want to avoid scope-creep and keep GuideLLM focused on it's current focus which is doing load tests against a pre-deployed model endpoint.

Alternatives:
- A separate project focused on simplifying model deployment that supports all platforms we care about (k8s Deployment, kserve, Podman, local [`vllm serve`]). We could even try to keep a set of "known-good" model configurations in that repo
- Refer users to existing model deployment guides / mechanisms.
