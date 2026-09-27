# [Issue #659] Can HybridEP NIXL path support EFA/libfabric, or is it UCX/GDA-specific?

source: https://github.com/deepseek-ai/DeepEP/issues/659
state: open | updated: 2026-06-09T02:26:13Z
labels: 

## 正文

Hi HybridEP team,

Thanks for the work on the hybrid-ep branch and the experimental NIXL path. I’m investigating whether HybridEP+NIXL can run on AWS GPU instances using EFA, rather than UCX over InfiniBand/RoCE.

From reading the current hybrid-ep branch, it looks like the NIXL path may currently be tightly coupled to the UCX GPU backend. In particular, csrc/hybrid_ep/buffer/nixl_connector.cu appears to explicitly initialize the NIXL backend with "UCX":
```
agent->getPluginParams("UCX", ...)
agent->createBackend("UCX", ...)
```

and the setup/build logic appears to include UCX-specific GPU headers and Mellanox verbs libraries, for example:
```
include/gpu/ucx
UCX_HOME/include
mlx5
ibverbs
```

The NIXL path also appears to rely on GPU-side/device APIs such as deferred GPU operations / nixlPut-style usage, which I understand may currently be specific to the UCX GPU backend.

My question is:

**Is the HybridEP NIXL path intended to support non-UCX NIXL backends such as LIBFABRIC, or is it currently expected to work only with UCX/GDA-style backends?**

Concretely, I’m trying to understand whether AWS EFA support would require only a small backend-selection change, e.g.:
```
auto backend = getenv("DEEPEP_NIXL_BACKEND") ?: "UCX";
agent->getPluginParams(backend, ...);
agent->createBackend(backend, ...);
```
or whether the current implementation depends on UCX GPU/device-channel APIs that do not have an equivalent in the NIXL LIBFABRIC backend.

For AWS EFA, standalone NIXL appears to support VRAM transfers through the LIBFABRIC backend, but my understanding is that this is host-posted NIXL transfer support rather than necessarily CUDA-device-side NIXL API support. If that understanding is wrong, I’d appreciate clarification.

A few specific questions:

1. Is LIBFABRIC backend support planned or expected for the HybridEP NIXL path?
2. Does the current HybridEP NIXL implementation require NIXL GPU-side/device APIs that are only available for UCX?
3. Would supporting EFA/libfabric likely require a host-posted transfer/proxy-thread design, or should the existing NIXL path be adaptable?
4. Are there recommended compile-time or runtime knobs for selecting a non-UCX NIXL backend?

Happy to help test on AWS EFA instances if useful.

Thanks!

## 评论 (2)

### irenedea · 2026-06-06

Hey @Autumn1998, I see you have worked on hybrid-ep recently, do you know? Thanks!

### Autumn1998 · 2026-06-09

cc @qiaok
