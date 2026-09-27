# [Issue #3487] [Bug] Tensor parallelism on Vulkan fails with SequentiallyConsistent SPIR-V barrier on Windows

source: https://github.com/mlc-ai/mlc-llm/issues/3487
state: open | updated: 2026-05-12T10:19:07Z
labels: bug

## 正文

Bug: Tensor parallelism on Vulkan fails with SequentiallyConsistent SPIR-V barrier on Windows

## Environment

| Component | Version |
|-----------|---------|
| MLC LLM   | 0.1.dev0 |
| TVM       | 0.20.dev990+gc2028da5a |
| Python    | 3.11.15 |
| OS        | Windows 10 (10.0.19045) |

**GPU 0**
```
deviceName        = AMD Radeon R9 200 Series
apiVersion        = 1.2.170 (4202666)
driverVersion     = 2.0.179 (8388787)
shaderFloat16                      = false
storageBuffer16BitAccess           = true
uniformAndStorageBuffer16BitAccess = true
```

**GPU 1**
```
deviceName        = AMD Radeon R9 290X
apiVersion        = 1.2.170 (4202666)
driverVersion     = 2.0.179 (8388787)
shaderFloat16                      = false
storageBuffer16BitAccess           = true
uniformAndStorageBuffer16BitAccess = true
```

---

## To Reproduce

Steps to reproduce the behavior:

```bash
python -m mlc_llm chat HF://mlc-ai/DeepSeek-R1-Distill-Qwen-7B-q4f16_1-MLC \
  --overrides "tensor_parallel_shards=2;context_window_size=4096" \
  --device "vulkan -from_device=0"
```

Also reproduced with `q4f32_1`:

```bash
python -m mlc_llm chat HF://mlc-ai/DeepSeek-R1-Distill-Qwen-7B-q4f32_1-MLC \
  --overrides "tensor_parallel_shards=2;context_window_size=4096" \
  --device "vulkan -from_device=0"
```

Setting `TVM_SPIRV_VALIDATE=0` does **not** suppress the validation in this build.

---

## Error

```
[2026-04-22 22:17:07] INFO pipeline.py:57: Compilation complete! Exporting to disk

File "D:\a\package\package\tvm\src\target\spirv\spirv_utils.cc", line 101,
in void __cdecl tvm::codegen::SPIRVTools::ValidateShader(
    const class std::vector<unsigned int, class std::allocator<unsigned int>> &)

tvm.error.InternalError: Check failed: res == SPV_SUCCESS (-14 vs. 0) :
  index=403 error:[VUID-StandaloneSpirv-MemorySemantics-10866]
  ControlBarrier: Memory Semantics with SequentiallyConsistent memory order
  must not be used in the Vulkan API
    OpControlBarrier %int_2 %int_2 %int_272
```

Followed by:

```
RuntimeError: Cannot find compilation output, compilation failed
```

---

## Expected Behavior

Compilation should complete successfully with `tensor_parallel_shards=2` on Vulkan.

TVM's SPIR-V codegen should emit `AcquireRelease` memory semantics instead of
`SequentiallyConsistent` for `ControlBarrier` instructions, as required by the
Vulkan specification:
https://registry.khronos.org/vulkan/specs/latest/html/vkspec.html#VUID-StandaloneSpirv-MemorySemantics-10866

---

## Additional Notes

- Both GPUs have identical Vulkan capabilities: `shaderFloat16 = false`, `storageBuffer16BitAccess = true`
- The error occurs regardless of quantization (`q4f16_1` or `q4f32_1`)
- The error is caught by TVM's own SPIR-V validator (`spirv_utils.cc`) **before** shaders are submitted to the driver â€” this is a codegen issue, not a driver/hardware limitation
- Setting `TVM_SPIRV_VALIDATE=0` does not bypass the validation in this build
- Single GPU (`tensor_parallel_shards=1`) has not been fully tested yet as a workaround due to memory constraints (4 GB per GPU)
- full stack dump:

[output.txt](https://github.com/user-attachments/files/26988751/output.txt)

## 评论 (1)

### truffle-dev · 2026-05-12

For cross-reference: this is the same SPIR-V codegen issue as apache/tvm#18915 (open, two other reporters, no PR yet). The layout-decoration follow-up from that same thread landed in apache/tvm#18914, but the `SequentiallyConsistent` → `AcquireRelease` change for `OpControlBarrier` is still pending upstream. The fix-shape lives in TVM's `codegen_spirv`, not mlc-llm — your validator stop in `spirv_utils.cc:101` is catching what TVM's emitter produced.

