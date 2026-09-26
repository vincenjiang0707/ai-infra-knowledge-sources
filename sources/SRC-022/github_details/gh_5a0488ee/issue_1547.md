# [Issue #1547] source file name is a bit confusing

source: https://github.com/ROCm/rccl/issues/1547
state: closed | updated: 2025-07-02T14:28:17Z
labels: Under Investigation

## 正文

The rccl file for rocm 6.2.4 is called rocm-6.2.4.tar.gz (https://github.com/ROCm/rccl/archive/refs/tags/rocm-6.2.4.tar.gz) which is a bit confusing, and it gets extracted to rccl-rocm-6.2.4. It would have been better to call the tar ball file something resembling rccl not just rocm.

## 评论 (2)

### harkgill-amd · 2025-06-25

Hi @hpourreza, the auto-generated release tarballs for rccl and all the other ROCm components share the same name as the tag they originate from. I believe this is just how GitHub handles the mapping between tag and tarball name in it's backend. The tarball post download then becomes `<repo>-<tag>.tar.gz`. For example, 

Tag: https://github.com/ROCm/rccl/releases/tag/rocm-6.4.1
Tarball: https://github.com/ROCm/rccl/archive/refs/tags/rocm-6.4.1.tar.gz
Downloaded: rccl-rocm-6.4.1.tar.gz

Other open source projects such as [vLLM](https://github.com/vllm-project/vllm/tags) and [SGLang ](https://github.com/sgl-project/sglang/tags) also follow this tagging workflow. 

### harkgill-amd · 2025-07-02

Will close this issue out for now but feel free to leave a comment if you have any other questions regarding the tagging workflows.
