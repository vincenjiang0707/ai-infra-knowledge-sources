source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/diffusion
lastmod: 2026-09-23T23:30:39.914Z

# Diffusion

Deploy diffusion models for text-to-image, text-to-video, and more in Dynamo

## Overview

Dynamo supports serving diffusion models across multiple backends, enabling generation of images and video from text prompts. Backends expose diffusion capabilities through the same Dynamo pipeline infrastructure used for LLM inference, including frontend routing, scaling, and observability.

## Support Matrix

**Status:** ✅ Supported | ❌ Not supported

TRT-LLM video output currently supports MP4 only and requires an NVENC-capable GPU. GPUs without NVENC are not supported for TRT-LLM video output.

## Backend Documentation

For deployment guides, configuration, and examples for each backend: