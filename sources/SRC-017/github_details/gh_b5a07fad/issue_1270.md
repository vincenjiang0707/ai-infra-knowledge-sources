# [Issue #1270] Provenance of NVTX headers in NCCL

source: https://github.com/NVIDIA/nccl/issues/1270
state: open | updated: 2026-09-18T12:20:26Z
labels: 

## 正文

NCCL appears to carry some sort of fork of `nvtx3` headers that match neither the headers in https://github.com/NVIDIA/nvtx nor the nvtx3 headers distributed with CUDA-12.x. Unfortunately, NCCL commit history does not mention the provenance of these headers, so it's not clear if they are a snapshot of some WIP branch in NVIDIA's internal repo, or if it's something developed by/for NCCL.

My issue is that when I build an application with CUDA-12, I generally need to compile everything with *one* set of those headers. Debugging ODR violations caused by different parts of the build including different variants of the headers is not fun.

Would it be possible to switch NCCL to use pristine upstream NVTX headers, and either keep NCCL-specific extensions only, or upstream the changes if they are not NCCL-specific?

@jrhemstad, @sjeaugey



## 评论 (14)

### kiskra-nvidia · 2024-04-29

We are using a snapshot of the headers from an internal repo. Funny you should ask though -- I've been pushing on the parties involved to get them in shape for the last few weeks, as they've been causing compilation warnings, especially with clang. Let me ping them again...

So I'm hoping that the next NCCL release will have an updated version, but it won't be the same as what's in the current CUDA release.

### Artem-B · 2024-04-29

I can help with clang-related issues. If the warnings are related to C++, clang is usually more strict than nvcc, and usually has a good reason to complain. 

> So I'm hoping that the next NCCL release will have an updated version, but it won't be the same as what's in the current CUDA release.

It does not have to be the same, as long as they can be used *instead* of the headers in CUDA-12. It would work for us short-term, as long as we have a variant that works for everyone.

Long term I would expect to see problems if/when NCCL's copy and NVTX repo and/or the version shipped with CUDA start to diverge. Shipping a fork as part of another library is a potential timebomb.




### kiskra-nvidia · 2024-04-30

Fixing the clang-related issues is not a problem; it's just that we didn't want to diverge from the upstream, which is what prompted us to attempt to resync with them.

### kiskra-nvidia · 2024-05-01

FYI, in the next NCCL version we will be using the NVTX headers based on https://github.com/NVIDIA/NVTX/tree/dev.

### BwL1289 · 2025-05-29

@kiskra-nvidia is there an update on this? This is a big problem especially when using system versions of nvtx3 and nccl with torch.

### Artem-B · 2025-05-29

I believe the latest NVTX release on https://github.com/NVIDIA/NVTX now has all the headers NCCL needs. The copy in NCCL can be replaced with a submodule pointing there.

### BwL1289 · 2025-05-29

@Artem-B agreed. We are now maintaining a fork of nccl with cmake support and support for device and host compilation with clang.

We were forced to patch numerous things in nvtx headers to make it compile with our system nvtx, and then reverted to using the bundled nvtx headers because the delta was so large. 

### kiskra-nvidia · 2025-06-02

@BwL1289 I know that we updated the NVTX headers in NCCL 2.22. Have they fallen behind again?

### BwL1289 · 2025-06-02

@kiskra-nvidia yes, there were a lot of differences between newer NVTX headers and the vendored version in NCCL.

I would recommend doing what @Artem-B proposed.

### BwL1289 · 2025-06-05

@kiskra-nvidia because I had this open from the other day, here's an example diff:

<img width="1351" alt="Image" src="https://github.com/user-attachments/assets/2d4499f7-b454-43b5-8469-dc6d50f9f2d2" />

### tilsche · 2025-06-25

@BwL1289, @Artem-B I understand the goal is to have a well-defined public NVTX version used in the distributed NCCL. To make sure this fixes your actual issues, can you please give some specific errors you are running into? Is this because you are trying to compile NCCL itself with _a different_ version of NVTX? Or do you somehow have _multiple_ versions of the NCCL headers during the compilation of NCCL? Or are you running into link-time ODR violation issues from different NCCL versions?

### BwL1289 · 2025-06-30

@tilsche I don't have the build log any longer to show specific errors. 

The compilation errors discussed [here](https://github.com/NVIDIA/nccl/issues/1270#issuecomment-2920340072) originate from the fact that the nvtx headers NCCL vendors, and the most recent upstream nvtx headers, are different.

What @Artem-B is saying is that, in general, it's dangerous to have more than one set of (different) headers on a system for the same package as this can lead to ODR violations. 



### tilsche · 2025-06-30

I think some things are getting mixed up here: Updating the NVTX headers in NCCL to the latest public version cannot guarantee that version is the one and only version on a system. Nor can it guarantee that the different versions are compatible in each and every way. But, we are trying to make sure that different versions of the NVTX headers are compatible to some extent:

- Backwards compatibility for compilation, but that is primarily relevant for header-only libraries using NVTX. NCCL can just use the included NVTX headers.
- For runtime/linkage, there could be problematic constellations with different NVTX versions in the same program with silent ODR (as in "same sequence of tokens") violations.

I'm trying to figure out if that has been broken in any way. If you run into traceable issues with that regard please feel free to open another issue for NVTX.

### 0z5a · 2026-09-18

I'd like to investigate whether this still affects current NCCL. I'll compare the bundled NVTX headers with upstream, check mixed-header builds for concrete compatibility issues, and validate annotation behavior on multi-GPU L20. 

I'll keep any proposed change minimal rather than replacing the headers wholesale. Is anyone already working on this, or is there a preferred direction?
