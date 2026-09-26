# [Issue #1609] LIBFABRIC/EFA CUDA DMA-BUF registration fails with Bad address on GB200 arm64

source: https://github.com/ai-dynamo/nixl/issues/1609
state: closed | updated: 2026-05-04T18:41:04Z
labels: 

## 正文

## Summary

NIXL `LIBFABRIC` backend fails to register CUDA VRAM when libfabric/EFA is configured to use CUDA DMA-BUF on AWS GB200 (`p6e-gb200.36xlarge`, arm64). The same NIXL functional probe passes on H100 EFA images, including one image with the same EFA installer/libfabric version.

The failure happens during memory registration, before transfer submission:

```text
libfabric:...:core:cuda_hmem_detect_dmabuf_support():680<info> cuda dmabuf support status: 1
libfabric:...:core:fi_param_get_():399<info> read bool var hmem_cuda_use_dmabuf=1
libfabric:...:core:cuda_get_dmabuf_fd():753<info> Get dma buf handle with fd: 57, offset: 0, page aligned base address: 0xe15fbdc00000, page aligned size: 131072, cuda allocation address 0xe15fbdc00000, cuda allocation length: 131072
libfabric:...:core:ofi_register_provider():526<info> registering provider: ofi_hook_dmabuf_peer_mem (204.0)
Registering GPU 0: src=0xe15fbdc00000, dst=0xe15fbdd00000, bytes=1048576
libfabric:...:efa:mr:efa_mr_reg_impl():893<warn> Unable to register MR of 1048576 bytes: Bad address, flags 0, ibv pd: 0x375ad3f0, total mr reg size 52232192, mr reg count 2
libfabric:...:efa:mr:efa_mr_regattr():1060<warn> Unable to register MR: Bad address
E... libfabric_rail.cpp:1362] fi_mr_reg failed on rail 2: Bad address (buffer=0xe15fbdc00000, length=1048576, requested_key=0)
E... libfabric_rail_manager.cpp:776] Failed to register memory on rail 2
E... libfabric_backend.cpp:788] Rail Manager registerMemory failed
E... nixl_agent.cpp:506] registerMem: registration failed for the specified or all potential backends
nixl_cu12._bindings.nixlBackendError: NIXL_ERR_BACKEND
```

## Environment

Failing GB200 image:

- Platform: AWS GB200 / `p6e-gb200.36xlarge`
- Architecture: arm64
- GPU: NVIDIA GB200
- OS/kernel on node: Ubuntu 24.04.4, `6.14.0-1018-aws-64k`
- Image: `nvcr.io/nvidian/dynamo-dev/jihao-glm5:efa-1.1-arm64-v2`
- Image digest: `sha256:4f5e3b9d3ab6fb6e5369ff84d689ee547eab449da9ac63a4ae3ae93d6f615596`
- Python: 3.12
- Torch: `2.9.1+cu129`, CUDA `12.9`
- NIXL: `nixl 1.0.0`, `nixl-cu12 1.0.0`
- EFA installer: `1.47.0`
- libfabric: `2.4.0amzn1.0`

I also rebuilt the same image with NIXL `release/1.1.0` at commit `4b2e56190b8c5bb0fa6a690df732d8b7d21e2b60`:

- Image: `nvcr.io/nvidian/dynamo-dev/jihao-glm5:efa-1.1-arm64-v2-nixl-1.1.0`
- Image digest: `sha256:b4936d56cdc40df371af33e77b5a2f55d9ef401c85571d70e7df2e2e84a94429`
- NIXL packages: `nixl` meta package still reports `1.0.0`; `nixl-cu12` reports `1.1.0`
- Build options: `-Denable_plugins=LIBFABRIC,POSIX`, `-Dlibfabric_path=/opt/amazon/efa`, `-Dcudapath_inc=/usr/local/cuda/include`, `-Dcudapath_lib=/usr/local/cuda/targets/sbsa-linux/lib`

The failure is unchanged with `nixl-cu12 1.1.0`.

Passing comparison images:

1. H100 SGLang image
   - Image: `nvcr.io/nvidian/dynamo-dev/jihao-sglang:efa-1.0.1-amd64`
   - Digest: `sha256:28bbdd6bcb993216cce0fb9e1b56292d5751f41ecfbf9d7400ea4562f436473d`
   - Platform: H100 / amd64
   - Torch: `2.9.1+cu130`
   - NIXL: `nixl 0.10.1`, `nixl-cu13 0.10.1`
   - EFA installer: `1.45.1`
   - libfabric: `2.3.1amzn3.0`
   - Result: DMA-BUF registration and NIXL `WRITE` pass on all 8 H100s.

2. H100 vLLM image
   - Image: `nvcr.io/nvstaging/ai-dynamo/vllm-runtime:1.1.0rc6-efa-amd64`
   - Digest: `sha256:165cad7869ddc845f723db6a498d5257cbdd1aae89e5283d1dc85a3cd20880b0`
   - Platform: H100 / amd64
   - Torch: `2.10.0+cu129`
   - NIXL: `nixl 0.10.1`, `nixl-cu12 0.10.1`
   - EFA installer: `1.47.0`
   - libfabric: `2.4.0amzn1.0`
   - Result: DMA-BUF registration and NIXL `WRITE` pass on all 8 H100s.

## Reproduction

Run a single-process NIXL functional probe that:

1. Creates two NIXL agents in the same process using the `LIBFABRIC` backend.
2. Allocates CUDA tensors with PyTorch.
3. Calls `torch.cuda.set_device(0)` before registration.
4. Registers source and destination tensors with NIXL.
5. Exchanges metadata between the two agents.
6. Performs a NIXL `WRITE`.
7. Verifies destination data.

Environment:

```bash
FI_PROVIDER=efa
FI_LOG_LEVEL=info
FI_HMEM=cuda
FI_HMEM_CUDA_ENABLE_XFER=1
FI_HMEM_CUDA_USE_DMABUF=1
FI_EFA_USE_DEVICE_RDMA=1
FI_EFA_ENABLE_SHM_TRANSFER=0
NIXL_LOG_LEVEL=WARN
```

Command:

```bash
python3 nixl_libfabric_dmabuf_probe.py --bytes 1048576 --max-gpus 1 --timeout-s 60
```

The same probe succeeds if `FI_HMEM_CUDA_USE_DMABUF=0`, but libfabric warns that CUDA buffers are not registered with EFA and that synchronization/copy fallback may affect performance:

```text
Failed to register CUDA buffer with the EFA device, FI_HMEM transfers that require peer to peer support will fail.
cudaDeviceSynchronize() will be performed ... performance may be impacted.
```

## Expected Behavior

When `FI_HMEM_CUDA_USE_DMABUF=1`, NIXL `LIBFABRIC` backend should be able to register CUDA VRAM through libfabric/EFA and complete the transfer, as it does on the H100 EFA images.

## Actual Behavior

On GB200/arm64, libfabric detects DMA-BUF support and obtains a DMA-BUF fd, but EFA MR registration fails with `Bad address`; NIXL returns `NIXL_ERR_BACKEND` from `register_memory`.

## What We Tried

- Verified that the failing path is actually the DMA-BUF path using `FI_LOG_LEVEL=info`.
- Verified CUDA allocation succeeds; failure is not a CUDA OOM/allocation failure.
- Verified `FI_HMEM_CUDA_USE_DMABUF=0` avoids this specific failure, but falls back to a slower/synchronized path.
- Rebuilt the image with NIXL `release/1.1.0` (`nixl-cu12 1.1.0`) to include the recent LIBFABRIC multi-GPU registration fixes. The failure still reproduces on a single visible GB200 GPU.
- Compared with H100 images. The vLLM H100 image uses the same EFA installer/libfabric version (`1.47.0` / `2.4.0amzn1.0`) and passes, so libfabric version alone does not look sufficient to explain the failure.

## Question

Can NIXL help determine whether the `LIBFABRIC` backend is passing the expected registration attributes for CUDA DMA-BUF memory on GB200/arm64, or whether this looks like a lower-level CUDA driver/kernel/libfabric/EFA provider issue?

Any recommended additional logging, debug build flags, or standalone NIXL/libfabric repro that would make this easier to hand to the EFA/libfabric side would be useful.


## 评论 (1)

### jh-nv · 2026-05-04

This is actually due to the aws fork of libfabric https://github.com/ofiwg/libfabric/issues/12019. Closing the ticket. 
