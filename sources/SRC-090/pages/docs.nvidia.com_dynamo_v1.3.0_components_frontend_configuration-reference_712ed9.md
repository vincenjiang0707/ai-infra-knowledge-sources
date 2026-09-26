source: https://docs.nvidia.com/dynamo/v1.3.0/components/frontend/configuration-reference
lastmod: 2026-09-24T19:58:16.636Z

# Frontend Configuration Reference

This page documents all configuration options for the Dynamo Frontend (`python -m dynamo.frontend`

).

Every CLI argument has a corresponding environment variable. CLI arguments take precedence over environment variables.

## HTTP & Networking

The Rust HTTP server also reads these environment variables (not exposed as CLI args):

## Router

This is the canonical CLI and environment-variable reference for the frontend’s
embedded router. The [Router Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing) explains deployment
modes and behavior, while [Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning)
explains when to adjust these settings.

### Routing and Readiness

### KV Scoring and Cache Locality

### KV State and Indexers

### Active Load and Queueing

## AIC Prefill Load Model

These options are used only when `--router-mode kv`

is combined with `--router-prefill-load-model aic`

.

When enabled, the frontend’s embedded KV router predicts one expected prefill duration per admitted request, using the selected worker’s overlap-derived cached prefix. The router then decays only the oldest active prefill request on each worker for prompt-side load accounting.

For MoE models, AIC requires `aic_tp_size * aic_attention_dp_size == aic_moe_tp_size * aic_moe_ep_size`

. For Kimi-style TP-only MoE runs, set `--aic-moe-tp-size`

to the same value as `--aic-tp-size`

, with `--aic-moe-ep-size 1`

and `--aic-attention-dp-size 1`

.

## Fault Tolerance

The deprecated `--admission-control`

and `DYN_ADMISSION_CONTROL`

settings are accepted but ignored
with a startup warning and no longer gate these thresholds. See
[Request Rejection](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-rejection#migrate-from-admission-control)
for migration instructions.

## Model Discovery

## Infrastructure

## KServe gRPC

See the [Frontend Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/frontend/frontend-guide) for KServe message formats and integration details.

## Monitoring

## Tokenizer

## Experimental

## HTTP Endpoints

The frontend exposes the following HTTP endpoints:

### OpenAI-Compatible

### Anthropic (Experimental)

### Infrastructure

### Frontend feature switches

Environment variables controlling frontend extensions. Extensions are enabled by default. When deploying, consider whether each is needed for your use case; if not, disable it to prevent accidental abuse.

Set an env value of `1`

/ `true`

/ `yes`

/ `on`

(case-insensitive) to disable the extension.

### Endpoint Path Customization

All endpoint paths can be overridden via environment variables:

## See Also

[Frontend Overview](https://docs.nvidia.com/dynamo/v1.3.0/components/frontend)— quick start and feature matrix[Frontend Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/frontend/frontend-guide)— KServe gRPC configuration[NVIDIA Request Extensions (nvext)](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/nvidia-request-extensions-nvext)— custom request fields[Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning)— router behavior and tuning guidance[Metrics](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics)— available Prometheus metrics[Fault Tolerance](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance)— request migration and rejection