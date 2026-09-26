source: https://github.com/vllm-project/guidellm/issues/1078

### Bug Description

When a `warmup`

is configured in the profile all requests that overlap the main phase are used for metric calculations even if that request only slightly overlaps. For example:

In this figure requests 1 and 2 are excluded but requests 3-7 are included because they are still active after the warmup ends. Most other tools will exclude 1-7 because they fall partially outside the main phase. This works for latencies at the cost of some valid samples but does not work for throughput metrics since the entire population is required to calculate throughput.

### Expected Behavior

The solution is to look at individual token events rather then full requests when determining if the event falls in-bounds. We should credit events based on their end time, so in the above example 1-6 would be omitted from first token / prefill metrics, but 7 would be counted because its first token event falls in-bounds.

### Steps to Reproduce

Any run with warmup has this issue, but the above example is specifically for a concurrent run.

### Operating System

N/A

### Python Version

N/A

### GuideLLM Version

main

### Installation Method

pip install guidellm

### Installation Details

*No response*

### Error Messages or Stack Traces

### Additional Context

*No response*

## Bug Description

When a

`warmup`

is configured in the profile all requests that overlap the main phase are used for metric calculations even if that request only slightly overlaps. For example:In this figure requests 1 and 2 are excluded but requests 3-7 are included because they are still active after the warmup ends. Most other tools will exclude 1-7 because they fall partially outside the main phase. This works for latencies at the cost of some valid samples but does not work for throughput metrics since the entire population is required to calculate throughput.

## Expected Behavior

The solution is to look at individual token events rather then full requests when determining if the event falls in-bounds. We should credit events based on their end time, so in the above example 1-6 would be omitted from first token / prefill metrics, but 7 would be counted because its first token event falls in-bounds.

## Steps to Reproduce

Any run with warmup has this issue, but the above example is specifically for a concurrent run.

## Operating System

N/A

## Python Version

N/A

## GuideLLM Version

main

## Installation Method

pip install guidellm

## Installation Details

No response## Error Messages or Stack Traces

## Additional Context

No response