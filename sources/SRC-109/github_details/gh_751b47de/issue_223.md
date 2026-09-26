# [Issue #223] AUTH KEY or OPEN_API_KEY util missing

source: https://github.com/triton-inference-server/perf_analyzer/issues/223
state: closed | updated: 2025-07-18T12:47:31Z
labels: 

## 正文

### Description
I am trying to use the `genai-perf` tool to benchmark an endpoint that requires an `Authorization` Bearer token or even OPEN_API_KEY. However, the tool does not seem to support passing custom headers using the `--headers` argument, resulting in the following error:


## 评论 (4)

### the-david-oy · 2024-12-17

Thanks for using GenAI-Perf! Please see this section: https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/README.md#authentication.

That's the current approach. We may consider making it a main argument in the future.

### Yokesh-RS · 2024-12-20

HI , but which version is this supported ..I'm using nvcr.io/nvidia/tritonserver:24.10-py3-sdk



![image](https://github.com/user-attachments/assets/c1546d4c-5b93-46d0-9ac4-93b7d45502b0)



### the-david-oy · 2024-12-20

Please follow the documentation for 24.12: https://github.com/triton-inference-server/perf_analyzer/blob/r24.12/genai-perf/README.md#authentication.

Based on your request and the requests of other users, we recognized that this feature is being used more and added it as a native arg in the last few days. Starting in 25.01, this will work out of the box. The documentation on the main branch has been updated, since the code there has also been updated.

Until 25.01 is released, you have to use superuser mode, which requires appending `--` before the superuser args (e.g. `-- 
 -H...`). We recognize this is confusing and was only intended for superusers who want to pass arguments directly to PA.

### psydok · 2025-07-18

@Yokesh-RS Can you tell me, please, is it working for you? I'm testing for nvcr.io/nvidia/tritonserver:25.03-py3-sdk. The title doesn't convey anything
