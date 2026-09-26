# [Issue #2434] [Bug :bug:]: TPU related nightly test has been failing for about one month

source: https://github.com/llm-d/llm-d/issues/2434
state: open | updated: 2026-09-13T08:25:41Z
labels: bug

## 正文

### Contact Details

_No response_

### What happened?
TPU related nightly test has been failing for about one month including Optimized baseline, Precise Prefix Cache Routing, P/D Disaggregation. Example:  https://github.com/llm-d/llm-d/actions/workflows/nightly-e2e-optimized-baseline-gke-acc-tpu-vllm-x.yaml. You can see full list here https://github.com/llm-d/llm-d/blob/main/release/README.md


### Version

n/a

### Area

Optimized baseline
Precise Prefix Cache Routing
P/D Disaggregation


### Relevant log output

```shell
Dynamic TPU request parameters calculated:
  CHIPS_TO_REQUEST: 16
  ACCELERATOR: tpu-v6e-slice
  TOPOLOGY: 2x4
  CHIPS_PER_VM: 8
  VMS: 2
job.batch/tpu-request-job created
timed out waiting for the condition on pods/tpu-request-job-lzjvt
timed out waiting for the condition on pods/tpu-request-job-zbwmn
Error: Process completed with exit code 1.
```

## 评论 (4)

### capri-xiyue · 2026-09-03

@rlakhtakia  Can you help investigate why we keep failing to request tpu resources?

### ItsRoy69 · 2026-09-05

I've gone through the failing TPU nightlies (Optimized Baseline, Precise Prefix Cache Routing, P/D Disaggregation) and the reusable workflow in `llm-d-infra`.
The failure happens during TPU resource provisioning:

- Workflow requests a `tpu-v6e-slice` with topology `2x4` (16 chips → 2 VMs × 8 chips).
- A `tpu-request-job` is created.
- The pods (`tpu-request-job-*`) never become Ready and the wait times out.

Happy to work on this issue and work on llm-infra

Can anyone assign this issue to me so I can drive the triage and the CI-side fixes?

### modelpath-dev · 2026-09-10

I will take this issue. Please assign it to me.

The TPU-related nightly test has been failing for about a month. The logs show a timeout waiting for the condition on TPU request job pods. I will first check the configuration in the nightly-e2e-optimized-baseline-gke-acc-tpu-vllm-x.yaml file. I will also review the TPU setup and any recent changes in the related code. The fix may involve adjusting the timeout settings or verifying the TPU resource availability.


### modelpath-dev · 2026-09-13

I will take a look at the TPU resource provisioning issue. Please assign this issue to me. I will start by reviewing the configuration and any recent changes that might have affected the TPU setup.

