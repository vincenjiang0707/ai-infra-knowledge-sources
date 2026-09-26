source: https://docs.nvidia.com/dynamo/multimodal/overview
lastmod: 2026-09-24T19:58:16.636Z

# Multimodal Model Serving

Deploy multimodal models with image, video, and audio support in Dynamo

Dynamo supports multimodal inference across multiple LLM backends, enabling models to process images, video, and audio alongside text.

## Which Feature to Use

Dynamo provides support for improving latency and throughput for multimodal workloads, with image and video inputs, through the following features. Use them together or separately, depending on your workload characteristics:

These features currently support image and video inputs only. Support for audio modalities will be added in upcoming releases.

## Multimodal Performance Optimization Features

## Example Workflows

Reference implementations for deploying multimodal models for each backend:

To use an author-provided custom vision tower or projector, see [Custom Vision Encoders](https://docs.nvidia.com/dynamo/advanced-customizations/custom-vision-encoders).