source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/multimodal
lastmod: 2026-09-24T19:58:16.636Z

# Multimodal Model Serving

Dynamo supports multimodal inference across multiple LLM backends, enabling models to process images, video, and audio alongside text.

## Key Features

Dynamo provides support for improving latency and throughput for vision-and-language workloads through the following features, that can be used together or separately, depending on your workload characteristics:

## Support Matrix

**Status:** ✅ Supported | 🧪 Experimental | ❌ Not supported

## Security: URL Validation

All multimodal loaders route remote fetches through a shared URL policy
(`dynamo.common.multimodal.url_validator`

). Only
`https://`

and `data:`

URLs are allowed by default, private / internal IPs are blocked,
and local file access is disabled. Every HTTP redirect hop is re-validated
against the policy.

Two environment variables loosen the defaults for non-public deployments:

**Never set DYN_MM_ALLOW_INTERNAL=1 on public-facing deployments.** It opens SSRF paths to cloud metadata endpoints (AWS IMDS, GCE, Azure) and other internal services.

## Example Workflows

Reference implementations for deploying multimodal models:

## Backend Documentation

Detailed deployment guides, configuration, and examples for each backend: