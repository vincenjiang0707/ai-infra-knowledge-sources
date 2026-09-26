# [Issue #2088] Create a new llm-d repository to host inference server API extensions

source: https://github.com/llm-d/llm-d/issues/2088
state: open | updated: 2026-08-31T17:53:27Z
labels: tier/production

## 正文

[RFC](https://github.com/vllm-project/vllm/issues/38147) was opened in vLLM to create endpoints to retrieve data to be used by llm-d for routing, scheduling etc. vLLM pushed back lately where they would prefer to limit new endpoints primarily because vLLM core is becoming increasingly complex especially with all the additional front end changes.
@hickeyma implemented an [endpoint framework](https://docs.vllm.ai/en/latest/design/endpoint_plugins/) in this [vLLM PR](https://github.com/vllm-project/vllm/pull/47454). Instead now of adding the API endpoints needed by llm-d directly to vLLM, they will be implemented instead as endpoint plugins in llm-d and passed to vLLM server on startup.
A draft API endpoint plugin, allowing llm-d to access vLLM configuration data, is [here](https://github.com/hickeyma/vllm-server-introspection).

Need a new llm-d repository to host API extensions for vLLM (and possibly others).
The API extenstions need to be packaged and available in inference server deployments.

While currently supported by vLLM, the repo should be engine agnostic (`api-extensions` sounds good).

cc: @vMaroon @hickeyma 

## 评论 (11)

### ahg-g · 2026-07-29

looks good to me, do we want it in incubation for now?

### elevran · 2026-07-30

in `llm-d`, not incubation

### hickeyma · 2026-08-04

Thanks @ahg-g and @elevran. Once the repo is created, do you mind adding the link to the issue?

### ahg-g · 2026-08-10

Another question, will we able to support sglang as well?

### elevran · 2026-08-10

@ahg-g it requires the model server to enable the pluggability. @hickeyma did it for vllm - I don't know if slgang support that as well.
@hickeyma are you aware of existing or plans for this type of functionality on sglang?

From a repo name perspective we kept it model server agnostic and will host vllm specific extensions under a `vllm` directory, not the top-level.


### hickeyma · 2026-08-13

> @hickeyma are you aware of existing or plans for this type of functionality on sglang?

Off hand, I don't know but I can investigate it. 

In the meantime, can we get the repo created as I want to follow on and close out existing PRs in vLLM?

### davidgs · 2026-08-19

What would you like the repo called?

### elevran · 2026-08-19

Let's use `api-extensions` (add `llm-d-` prefix if that's required)

### davidgs · 2026-08-19

This repo has been created, but it is bare-bone. Please make sure that it has the following files added ASAP:
- CONTRIBUTING.md
-  MAINTAINERS.md
- OWNERS
- SECURITY.md
- .gitignore (appropriate for the codebase)

For proper examples, you can look in this or other llm-d repos. 

### elevran · 2026-08-20

thanks @davidgs 
@hickeyma - you're good to go.

### hickeyma · 2026-08-31

Thanks @davidgs and @elevran for driving this on. Pushed PR https://github.com/llm-d/llm-d-api-extensions/pull/2.
