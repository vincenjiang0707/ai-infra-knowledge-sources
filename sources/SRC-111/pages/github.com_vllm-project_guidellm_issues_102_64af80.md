source: https://github.com/vllm-project/guidellm/issues/102

**Purpose:**

The purpose of this ticket is to support batch inference requests for GuideLLM. We will need to add in a batch-size parameter to enable the user to dictate the batch size of inference requests.

We will want to add non-streaming batched inferencing like this PR from llm-load-test [openshift-psap/llm-load-test#66](https://github.com/openshift-psap/llm-load-test/pull/66)

Acceptance Criteria:

- Add a
`batch-size`

parameter in for the user to dictate the batch size of inference requests
- This should be non-streaming batching
- Once set, send requests in batches as dictated by the parameter

Example:

`--batch-size=16, --batch-size=32 `


Purpose:The purpose of this ticket is to support batch inference requests for GuideLLM. We will need to add in a batch-size parameter to enable the user to dictate the batch size of inference requests.

We will want to add non-streaming batched inferencing like this PR from llm-load-test openshift-psap/llm-load-test#66

Acceptance Criteria:

`batch-size`

parameter in for the user to dictate the batch size of inference requestsExample:

`--batch-size=16, --batch-size=32`