source: https://github.com/vllm-project/guidellm/issues/216

When running a guidellm benchmark with --rate-type concurrent against an Ollama server at high concurrency rates, the resulting report can contain negative values for time_to_first_token_ms and other time-based metrics.

This seems to occur when the Ollama server is under heavy load and may not be returning a valid streaming response for some requests, causing an issue in how guidellm calculates the timing for those requests.

### To Reproduce

Set up an Ollama server and configure it for high parallelism (OLLAMA_NUM_PARALLEL=32).

Load a model such as llama3.1:8b-instruct-fp16.

Run a guidellm benchmark with a high concurrency rate (--rate 128).

Inspect the output JSON file.

### Faulty Output JSON Example:

The following is an extract from a benchmarks.json file generated during a high-concurrency test, showing the negative values:

```
"time_to_first_token_ms": {
"successful": {
"mean": -1715507074412.1443,
"median": -1750878354510.5388,
"mode": -1750878498066.5781,
"variance": 6.067968657158425e+22,
"std_dev": 246332471614.24792,
"min": -1750878498066.5781,
"max": 89488.18135261536,
"count": 99,
"total_sum": -169835200366802.25
}
}
```


A temporary patch was suggested by [@sjmonson](https://github.com/sjmonson) that adds error handling to the _iterative_completions_request function in src/guidellm/backend/openai.py.

This patch checks if first_iter_time or last_iter_time were ever set. If not (which happens when the server is overloaded and sends no data back for a request), it raises a ValueError instead of proceeding with faulty time calculations.

I can confirm that after applying this patch locally, the issue was resolved. Error requests were correctly marked as errors, and the benchmark only produced positive time values.

Here is the diff for the temporary fix:

```
diff --git a/src/guidellm/backend/openai.py b/src/guidellm/backend/openai.py
index 4eb6ae0..0748213 100644
--- a/src/guidellm/backend/openai.py
+++ b/src/guidellm/backend/openai.py
@@ -630,6 +630,9 @@ class OpenAIHTTPBackend(Backend):
response_prompt_count = usage["prompt"]
response_output_count = usage["output"]
+ if first_iter_time is None or last_iter_time is None:
+ raise ValueError("No iterations received for request: {}", request_id)
+
logger.info(
"{} request: {} with headers: {} and params: {} and payload: {} completed"
"with: {}",
```


When running a guidellm benchmark with --rate-type concurrent against an Ollama server at high concurrency rates, the resulting report can contain negative values for time_to_first_token_ms and other time-based metrics.

This seems to occur when the Ollama server is under heavy load and may not be returning a valid streaming response for some requests, causing an issue in how guidellm calculates the timing for those requests.

## To Reproduce

Set up an Ollama server and configure it for high parallelism (OLLAMA_NUM_PARALLEL=32).

Load a model such as llama3.1:8b-instruct-fp16.

Run a guidellm benchmark with a high concurrency rate (--rate 128).

Inspect the output JSON file.

## Faulty Output JSON Example:

The following is an extract from a benchmarks.json file generated during a high-concurrency test, showing the negative values:

A temporary patch was suggested by @sjmonson that adds error handling to the _iterative_completions_request function in src/guidellm/backend/openai.py.

This patch checks if first_iter_time or last_iter_time were ever set. If not (which happens when the server is overloaded and sends no data back for a request), it raises a ValueError instead of proceeding with faulty time calculations.

I can confirm that after applying this patch locally, the issue was resolved. Error requests were correctly marked as errors, and the benchmark only produced positive time values.

Here is the diff for the temporary fix: