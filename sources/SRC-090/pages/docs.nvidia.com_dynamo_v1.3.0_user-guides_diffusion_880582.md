source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/diffusion
lastmod: 2026-09-24T19:58:16.636Z

# Diffusion

Deploy diffusion models for text-to-image, text-to-video, and more in Dynamo

## Overview

Dynamo supports serving diffusion models across multiple backends, enabling generation of images and video from text prompts. Backends expose diffusion capabilities through the same Dynamo pipeline infrastructure used for LLM inference, including frontend routing, scaling, and observability.

## Support Matrix

**Status:** ✅ Supported | ❌ Not supported

TRT-LLM video output currently supports MP4 only and requires an NVENC-capable GPU. GPUs without NVENC are not supported for TRT-LLM video output.

## Backend Documentation

For deployment guides, configuration, and examples for each backend: