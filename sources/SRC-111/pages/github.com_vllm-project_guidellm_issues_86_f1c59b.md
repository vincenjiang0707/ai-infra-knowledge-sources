source: https://github.com/vllm-project/guidellm/issues/86

**Description:** The purpose of this ticket is to surface vLLM specific scheduler metrics to provide users with a full array of data on the vLLM service running.

**User Story:**

As a ml developer, I want to be able to see the vLLM specific scheduler metrics so that I can ensure that my benchmarks are taking full advantage of what vLLM has to offer and that my service is running optimally before I move to production.

**Acceptance Criteria:**

- Stream the metrics from Prometheus to the output format script:
- Queue size
- KV cache usage
- Requests in Waiting, Swap, Running
- Create a new CLI output table dedicated for the vLLM specific metrics:
-

Description:The purpose of this ticket is to surface vLLM specific scheduler metrics to provide users with a full array of data on the vLLM service running.User Story:As a ml developer, I want to be able to see the vLLM specific scheduler metrics so that I can ensure that my benchmarks are taking full advantage of what vLLM has to offer and that my service is running optimally before I move to production.

Acceptance Criteria: