source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/backends/custom-backend/runtime-containers
lastmod: 2026-09-23T23:30:39.914Z

# Runtime Containers

Build Dynamo runtime images for built-in or custom backends

Dynamo runtime images package the Dynamo runtime with an inference engine. The same container build flow can generate images for the built-in engines or a backend that you add on top of the Dynamo runtime.

Use [ container/render.py](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/container/render.py) to select the engine family and Docker target:

## Engine and Target Toggles

`--framework`

chooses the engine base. Use `vllm`

, `sglang`

, or `trtllm`

for built-in backends. Use `none`

when you want a Dynamo-only base image and plan to install your own backend package.

`--target`

chooses the image shape:

## Custom Backend Image

For a Python custom backend, start with a built-in engine image if you need that framework’s CUDA/Python stack, or use `--framework=none`

if your backend brings its own dependencies:

Then layer your backend package into a small Dockerfile:

For a Rust custom backend, build the backend binary in your own builder stage and copy it into the Dynamo runtime image:

## Run Locally

Use `container/run.sh`

to launch the image with the same GPU and mount defaults used by Dynamo development workflows:

For the full container build reference, target matrix, and troubleshooting notes, see the repository-level [Container Development Guide](https://docs.nvidia.com/dynamo/v1.2.1/container/README.md).