source: https://docs.nvidia.com/dynamo/zh-CN/reference/components/profiler-configuration
lastmod: 2026-09-23T23:30:39.914Z

# Profiler Configuration Reference

Field reference for the Dynamo profiler CLI arguments — the SLA profiler entry point and the low-level per-endpoint profiler.

The Dynamo profiler has two entry points, each with its own arguments:

— the SLA profiler. Sweeps a model across tensor-parallel sizes and interpolates prefill/decode performance to recommend a deployment that meets your SLA. Takes a DynamoGraphDeploymentRequest (DGDR) spec plus a handful of operational flags.`python -m dynamo.profiler`

— the low-level per-endpoint profiler. Profiles a single already-running prefill or decode endpoint.`python -m dynamo.profiler.profile_endpoint`


For the profiling workflow and DGDR spec structure, see the [Profiler Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/overview). Field names, types, and defaults on this page come from [ __main__.py](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/profiler/__main__.py) and

[.](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/profiler/profile_endpoint.py)

`profile_endpoint.py`

## SLA profiler (`dynamo.profiler`

)

DynamoGraphDeploymentRequestSpec as an inline JSON string or a path to a JSON/YAML file. This defines the model, backend, and SLA targets to profile against. Startup fails if it is neither a valid file path nor valid JSON.

Path to the output results directory. The profiler writes plots, the interpolation data, `profile_sla.log`

, and a `profiler_status.yaml`

status file here.

Maximum seconds to wait for each trial deployment to become ready before failing.

Number of input-sequence-length (ISL) samples used to interpolate prefill performance. Higher values give a finer prefill curve at the cost of more profiling runs.

Number of samples used to interpolate decode performance across the KV-cache load range. Higher values give a finer decode curve at the cost of more profiling runs.

Skip deployments and benchmarking. Use this to validate the config and preview the planned sweep without provisioning GPUs.

## Per-endpoint profiler (`dynamo.profiler.profile_endpoint`

)

This entry point profiles a single running endpoint. It is normally invoked by the SLA profiler, but you can run it directly against an existing deployment.

Which phase to profile.

Allowed values: prefill decodeModel name to send with requests. Must match the model the endpoint serves.

Base URL of the endpoint to profile, for example `http://localhost:8000`

.

Number of GPUs backing the endpoint. Used to normalize the reported per-GPU performance.

Path to the tokenizer. When empty, the tokenizer is resolved from `--model_name`

.

Maximum KV-cache tokens for the endpoint. Used only in `decode`

mode to bound the KV-load sweep. Decode profiling requires an explicit positive value; the default `0`

is valid only for prefill mode and causes decode mode to fail validation.

Directory to save this endpoint’s profiling results.

Maximum context length to probe when generating request payloads.

Number of samples used to interpolate this endpoint’s results.

Attention data-parallel size of the endpoint. Set this for MoE models that run attention with data parallelism.