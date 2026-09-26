source: https://github.com/vllm-project/guidellm/issues/197

Often when we benchmark a new model or hardware, the goal is to determine the max RPS or tokens per second that the server can sustain under a certain SLO. We should add a new feature similar to the "sweep" but instead of doing linearly spaced constant RPS runs, it should do something like a binary search to try to find the peak load which the server can handle while meeting a defined latency SLO.

We would need to support some config options for the SLO, to support p99 or p95 ITL and TTFT.

I have a rough PoC of this in progress on this branch: [https://github.com/dagrayvid/guidellm/tree/goodput](https://github.com/dagrayvid/guidellm/tree/goodput), but wanted to open this issue to discuss the idea further and track progress.

Often when we benchmark a new model or hardware, the goal is to determine the max RPS or tokens per second that the server can sustain under a certain SLO. We should add a new feature similar to the "sweep" but instead of doing linearly spaced constant RPS runs, it should do something like a binary search to try to find the peak load which the server can handle while meeting a defined latency SLO.

We would need to support some config options for the SLO, to support p99 or p95 ITL and TTFT.

I have a rough PoC of this in progress on this branch: https://github.com/dagrayvid/guidellm/tree/goodput, but wanted to open this issue to discuss the idea further and track progress.