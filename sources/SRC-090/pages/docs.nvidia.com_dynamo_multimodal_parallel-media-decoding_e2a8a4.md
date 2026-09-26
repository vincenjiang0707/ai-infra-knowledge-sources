source: https://docs.nvidia.com/dynamo/multimodal/parallel-media-decoding
lastmod: 2026-09-24T19:58:16.636Z

# Parallel Media Decoding

Parallel media decoding moves image fetching, base64 decoding, and image decompression from the inference backend to the NVIDIA Dynamo Rust frontend. The frontend decodes images concurrently on a CPU worker pool and transfers the decoded pixel buffers to the backend through NIXL.

The backend still runs its model-specific multimodal processor and vision encoder. This feature changes where image input is decoded; it does not skip vision encoding.

## Support Matrix

`Agg`

refers to an aggregated worker. The entries in this matrix represent the
supported topologies for frontend decoding.

This matrix describes parallel media decoding, not the overall multimodal support of each backend. A backend can support video or audio by decoding it on the worker even when the frontend decoding path does not support that modality.

## When to Use

Use parallel media decoding when image preprocessing consumes a significant part of request latency or backend CPU time. It is most useful for workloads with:

- Concurrent requests containing HTTP, HTTPS, or base64-encoded images
- Multiple images in one request
- Backend workers whose request path is constrained by image fetching or decompression

Parallel media decoding can also be combined with the [embedding
cache](https://docs.nvidia.com/dynamo/multimodal/embedding-cache). Frontend decoding reduces image input processing
work, while the embedding cache can skip vision encoding for repeated images.

## How It Works

For each request, the frontend:

- Fetches the image URL or decodes the base64 data URL.
- Decodes images concurrently on a CPU worker pool.
- Registers the decoded pixel buffer with NIXL.
- Sends the buffer descriptor to the selected backend worker.

The backend reads the decoded pixels through NIXL, then continues with its normal multimodal processor and vision encoder.

## Enable Parallel Media Decoding

Add `--frontend-decoding`

to the backend worker command. Do not add the flag to
`dynamo.frontend`

; the backend advertises the decoder configuration when it
registers the model.

## Requirements and Limitations

- The published
`nvcr.io/nvidia/ai-dynamo/dynamo-frontend:1.4.2`

image installs NIXL wheels but does not expose the native NIXL and UCX libraries and plugins required by the Rust frontend. It cannot run parallel media decoding as shipped. Run the frontend in a backend runtime image or environment where NIXL and UCX are configured and available.