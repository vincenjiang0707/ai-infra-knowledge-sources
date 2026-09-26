# [Issue #588] --max-requests with --rate-type=sweep causes first stage to run all requests synchronously, resulting in extremely long runtimes

source: https://github.com/vllm-project/guidellm/issues/588
state: closed | updated: 2026-07-21T20:10:07Z
labels: priority-high, internal, cli

## 正文

### Bug Description


When using --rate-type=sweep combined with --max-requests=N, the first synchronous stage of the sweep runs ALL N requests sequentially before moving to parallel stages. This results in unexpectedly long benchmark runtimes, especially with larger request counts.
Observed Behavior
A benchmark configured with --max-requests=1000 --rate-type=sweep took ~7 hours to complete on H100 GPUs, when users expected it to complete in minutes.
Root Cause
The sweep profile's first stage runs requests synchronously (one at a time). The --max-requests parameter applies to each stage, causing all 1000 requests to be processed sequentially in stage 1 alone before any parallel stages begin.


### Expected Behavior

Either:
--max-requests should be the total requests across all sweep stages, not per-stage
The synchronous stage should have a separate, smaller limit
Documentation should clearly warn against using high --max-requests values with sweep mode

### Steps to Reproduce

apiVersion: batch/v1
kind: Job
metadata:
  name: guidellm-benchmark
spec:
  template:
    spec:
      containers:
      - name: guidellm
        image: quay.io/jhurlocker/guidellm:latest
        args:
          - benchmark
          - --target=http://my-llm-service:8080/v1
          - --model=granite-33-8b-instruct
          - --rate-type=sweep
          - --max-requests=1000    # <-- This causes the issue
          - --data=/mnt/prompts/prefix-prompts.csv
          - --output-path=/results/output.json

### Operating System

OpenShift (RHOAI 3.0)

### Python Version

OpenShift (RHOAI 3.0)

### GuideLLM Version

latest

### Installation Method

pip install guidellm

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

Suggested Improvements
Documentation: Add a warning to the README/docs that --max-requests with sweep mode runs synchronously in the first stage
CLI Warning: Emit a warning when --max-requests > 100 is used with --rate-type=sweep
Design Change: Consider making the synchronous stage use a smaller, fixed request count (e.g., 50-100) regardless of --max-requests
Environment
GuideLLM version: latest
Hardware: NVIDIA H100 GPUs
Platform: OpenShift (RHOAI 3.0)

## 评论 (2)

### dbutenhof · 2026-02-04

Thank you!

> The synchronous stage should have a separate, smaller limit

We have a plan (#575) to address a way to parameterize the various stages independently. This is currently planned for v0.7.0 as it's a breaking CLI change. We'll discuss potentially less radical alternatives.

> Documentation should clearly warn against using high --max-requests values with sweep mode

A small documentation change to warn about this may be more feasible in the short term.

### dbutenhof · 2026-07-21

Resolved in 0.7.1, which allows `--constraint kind=max_requests --override constraints[0].count=10,100,1000` which sets the constraint on the first strategy (sychronous) to 10 requests, the second (throughput) to 100, and each of the subsequent strategies (the constant sweep) to 1000.
