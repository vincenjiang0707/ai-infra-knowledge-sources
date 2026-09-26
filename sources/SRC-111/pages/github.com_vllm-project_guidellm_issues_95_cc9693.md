source: https://github.com/vllm-project/guidellm/issues/95

**Description:**

The proposal here is to change the architecture of how GuideLLM runs so that when a user runs GuideLLM it automatically kicks off a vLLM server and supplies GuideLLM with the necessary data to run the benchmark. This also covers adding any necessary pass-through parameters to vLLM to GuideLLM so that the user can just run GuideLLM to do a full end-to-end benchmark on a model. This is a UX enhancement.

**Acceptance Criteria:**

- Enable GuideLLM to kick off a vLLM server when GuideLLM is run
- Enable GuideLLM to accept the necessary pass-through arguments that need to go to vLLM:

-- model (required)

-- port (optional)

-- TBD

Description:The proposal here is to change the architecture of how GuideLLM runs so that when a user runs GuideLLM it automatically kicks off a vLLM server and supplies GuideLLM with the necessary data to run the benchmark. This also covers adding any necessary pass-through parameters to vLLM to GuideLLM so that the user can just run GuideLLM to do a full end-to-end benchmark on a model. This is a UX enhancement.

Acceptance Criteria:-- model (required)

-- port (optional)

-- TBD