source: https://docs.nvidia.com/dynamo/dev/advanced-customizations/conditional-disaggregation
lastmod: 2026-09-24T19:58:16.636Z

# Conditional Disaggregation

**Experimental.** Validate/tune conditional disaggregation against your workload before using it in production.

Conditional disaggregation enables a hybrid of aggregated and disaggregated request routing. The router may serve a request `prefill worker -> decode worker`

, or it may send the request directly to a decode worker and the backend runs local prefill plus decode there.

For workloads with a high degree of KV reusage on long-ISL requests, e.g. multi-turn / agentic conversation scenarios, conditional disaggregation can help your deployment maintain predictable SLA. Compared to unconditional disaggregation, it reduces memory pressure / TTFT on prefill workers by optimizing reuse of *decode-worker* KV cache; compared to unconditionally aggregated deployments, it avoids the heavy ITL penalty incurred by co-scheduling heavy prefill workload onto decode workers.

Enable conditional disaggregation with `--router-conditional-disagg`

on the frontend:

Tune the policy with `--router-conditional-disagg-config`

. For example:

## Backend Requirements

Conditional disaggregation requires decode-worker KV visibility. The router uses decode-side KV events to estimate effective ISL and decide whether local prefill+decode is cheaper than remote prefill.

Configure workers as follows:

If decode workers do not publish KV events, the router cannot accurately assess bypass conditions.

Append these additional flags to tune the conditional disaggregation policy:

For ISL-based policies, `effective ISL`

is the request prompt length after subtracting the selected decode worker’s cached prefix overlap. The absolute threshold limits the number of prompt tokens the decode worker may need to compute locally. The ratio threshold limits that local work as a fraction of the raw prompt length. These thresholds measure both “how much compute does this request require” (absolute) and “how compute/memory-bound is this request, due to the ratio of its computed / cached KV cache” (ratio), respectively.

As a tuning starting point, we recommend choosing thresholds based on your workload’s expected effective-ISL and the `effective ISL : raw ISL`

ratio distribution. For example, with `isl_bounding`

, setting the absolute threshold to p25 of the workload’s effective ISL would make the absolute-threshold check pass for roughly 25% of requests.

The config fields map to these policy settings:

The available policies are: