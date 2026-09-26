source: https://docs.nvidia.com/dynamo/advanced-customizations/writing-custom-backends/runtime-containers
lastmod: 2026-09-24T19:58:16.636Z

# Runtime Containers

Build Dynamo runtime images for built-in or custom backends

Dynamo runtime images package the Dynamo runtime with an inference engine. The same container build flow can generate images for the built-in engines or a backend that you add on top of the Dynamo runtime.

Use [ container/render.py](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/container/render.py) to select the engine family and Docker target:

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

## Declare the Runtime Version for Kubernetes

When you deploy a custom image with a `DynamoGraphDeployment`

(DGD) or standalone
`DynamoComponentDeployment`

(DCD), admission determines the Dynamo runtime compatibility version
from the component’s main-container image tag. The tag itself must be a semantic version. Tags such
as `1.4.0`

, `v1.4.0`

, and `1.4.0-cuda13`

can provide the version. Set
`runtimeVersionOverride`

when the image is tagless, digest-only, uses a tag such as `latest`

,
`main`

, `sha-abc`

, or `cuda13-1.4.0`

, or when a semantic-version tag does not identify the Dynamo
runtime version packaged in the image.

Set the override to the canonical `MAJOR.MINOR.PATCH`

Dynamo runtime version without a `v`

prefix,
prerelease suffix, or build metadata. Each numeric segment may contain at most four digits.
Admission can verify that an image tag is parseable, but it cannot determine whether that tag
actually represents the Dynamo runtime version. Set the override when a valid semantic-version
tag describes another part of the image stack:

The override is optional in the CRD schema but conditionally required by admission:

The main image remains required when an override is set. Sidecar image tags are not used for runtime-version detection. The override declares the Dynamo runtime packaged in the image; it is not the CUDA, inference-engine, operator, Git, or image-build version. It does not rewrite the image or change the rendered Pod, and changing only this field does not trigger a worker rollout. For compatibility, an existing component created without its pod configuration or main image can still be updated while that field remains missing. New components must provide both, and adding, changing, or removing the image applies current admission validation.

## Run Locally

Use `container/run.sh`

to launch the image with the same GPU and mount defaults used by Dynamo development workflows:

For the full container build reference, target matrix, and troubleshooting notes, see the repository-level [Container Development Guide](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/container/README.md).