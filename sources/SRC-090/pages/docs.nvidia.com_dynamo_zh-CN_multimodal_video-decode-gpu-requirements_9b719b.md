source: https://docs.nvidia.com/dynamo/zh-CN/multimodal/video-decode-gpu-requirements
lastmod: 2026-09-24T19:58:16.636Z

# Video Decode GPU Requirements

Dynamo decodes H.264 and H.265 (HEVC) video input on the GPU using NVDEC, NVIDIA’s
dedicated hardware video decoder, through
[PyNvVideoCodec](https://pypi.org/project/PyNvVideoCodec/).

Other formats — VP8, VP9 and AV1 — have **no video-input decoder** in the shipped images.
The in-tree VP8/VP9 FFmpeg serves the video *output* (generation) path; it is not wired to
video input, and the Rust `media-ffmpeg`

decoder is not built into these images. Video
input decodes through Python carriers (OpenCV, PyAV, decord) that the images deliberately
omit, so a VP8/VP9/AV1 clip fails with an unsupported-codec error unless one of those
packages is installed alongside.

This page covers which GPUs provide NVDEC, what the container must expose, and how Dynamo behaves when hardware decode is unavailable.

## GPU support

NVDEC is a fixed-function decode engine, separate from the SMs used for inference, so decoding adds negligible load to the GPU beyond a small YUV-to-RGB conversion.

A common misconception is that datacenter GPUs have no video engines. That applies to
**NVENC**, the hardware *encoder*, which NVIDIA omits from datacenter parts. The
*decoder* is present:

Every GPU above decodes both codecs Dynamo routes to hardware, so H.264 and H.265 video
input works across the datacenter lineup. Hopper’s NVDEC matches Turing’s feature set and
does **not** decode AV1; Blackwell adds AV1 decode. The Ada parts (L4, L40S, RTX 6000 Ada)
decode AV1 as well, and unlike the datacenter accelerators they also carry NVENC.

Because no datacenter GPU ships NVENC, Dynamo’s video *generation* path encodes with a
CPU VP9 encoder rather than a hardware H.264 encoder.

Under Multi-Instance GPU (MIG), NVDEC engines are divided across instances. A given MIG profile may expose fewer decoders than the full GPU, and some profiles expose none. Verify decode works in the exact profile you deploy.

## Container requirements

NVDEC links `libnvcuvid`

at runtime, which the NVIDIA container runtime only mounts when
the ** video driver capability** is requested. Without it,

`import PyNvVideoCodec`

fails
and Dynamo falls back to software decode.Dynamo’s runtime images already declare it:

With Docker that is usually enough, because the toolkit reads the capability from the image. To be explicit, or when overriding the variable for other reasons:

### Kubernetes

On Kubernetes the image’s `ENV`

is **not** reliably sufficient. Set the variable on the
container spec as well. Dynamo’s own GPU test runners shipped images carrying the `ENV`

and still had no hardware decode until the pod spec set it explicitly.

Add it to the container that runs the worker:

If it still does not take effect, the capability is being dropped below the pod. Check
`supported-driver-capabilities`

in `/etc/nvidia-container-runtime/config.toml`

on the
node, and — if the cluster runs in CDI mode — whether the generated device spec includes
the video libraries, since in that mode capabilities come from the spec rather than the
environment variable.

Missing the `video`

capability is the most common cause of hardware decode being
silently unavailable. The GPU itself is fine; the container simply cannot see the
decoder.

## Verifying hardware decode

`False`

means Dynamo will not use hardware decode in that container. Check, in order: the
`video`

driver capability, that `PyNvVideoCodec`

is installed, and that
`DYN_DISABLE_NVDEC`

is unset.

To distinguish “capability missing” from every other cause, look for the decode library itself. It is mounted by the container runtime, not installed by the image, so its absence points squarely at the capability:

Expect `libnvcuvid.so.1`

. Nothing means the `video`

capability did not reach this
container. If it is present on the node but not inside, the capability is being dropped
between the two.

## Behavior when NVDEC is unavailable

Hardware decode is additive and never blocks a request on its own: routing falls through to the software decode path where one exists.

In the shipped images there is no software decode path for video input, for any format.
The Python carriers that decode video input (OpenCV, PyAV, decord) are deliberately not
installed, and the in-tree VP8/VP9 FFmpeg serves the video *output* path rather than
input. So if NVDEC is unavailable, H.264 and H.265 fail with an unsupported-codec error
— and VP8, VP9 and AV1 fail the same way whether NVDEC is available or not, since NVDEC
does not decode them either.

Grant the container the `video`

driver capability so NVDEC can serve H.264 and H.265.
For the other formats, install a decode carrier alongside, or transcode the input to
H.264/H.265 before sending it.

### Installing a software decoder

To decode a format NVDEC does not cover — or H.264/H.265 on a host with no NVDEC — explicitly install the backend’s decode package at the validated version bounds:

Nothing installs automatically — this is a deliberate operator step. The images also ship
an installer with the same bounds plus idempotency and air-gap support
(`python -m dynamo.common.utils.install_media_decoders <backend>`

); see
[Additional Media Decoders](https://docs.nvidia.com/dynamo/multimodal/additional-media-decoders) for the full workflow,
including baking the install into an image layer for Kubernetes.

## Hardware encode (NVENC)

There is nothing to enable. Dynamo does not use NVENC on any path.

Video **output** — the generation path — encodes VP9 on the CPU with the in-tree FFmpeg.
That is deliberate and works everywhere: no datacenter GPU ships an encoder, so a
hardware encode path would be unavailable on exactly the parts most deployments run. On
workstation parts that do have NVENC (L4, L40S, RTX 6000 Ada) it simply stays unused.

The same `video`

driver capability governs both engines, so a container configured for
NVDEC as above needs no additional change. Encode performance does not depend on it.