# [Issue #102] 对HSTU模型启用编译，编译 layer_norm 和 addmm_silu 算子报错 error: ub overflow

source: https://github.com/Ascend/pytorch/issues/102
state: open | updated: 2026-01-22T06:36:29Z
labels: 

## 正文

## 模型信息

HSTU，链接：https://gitcode.com/Ascend/RecSDK

## 环境信息
```bash
root@nb-a18190275368972288384443-a18190275368972288384443-0:/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu# pip list | grep torch
hybrid-torchrec         1.1.0
torch                   2.6.0+cpu
torch_npu               2.6.0
torchmetrics            1.0.3
torchrec                1.1.0+npu
torchx                  0.7.0
```

## 部署形态
```bash
#启用图编译
export USE_COMPILE=1
#开启ACLgraph
export USE_GRAPH=1
```

## 具体报错信息
```bash
root@nb-a18190275368972288384443-a18190275368972288384443-0:/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu# bash run_random_2k.sh
模型加载开始！
ERROR:torch_npu._inductor.config:Triton compilation failed: triton_unk_fused_native_layer_norm_0
def triton_unk_fused_native_layer_norm_0(in_ptr0, in_ptr1, in_ptr2, out_ptr1, x0_numel, r1_numel, X0BLOCK: tl.constexpr, X0BLOCK_SUB: tl.constexpr, R1BLOCK_SUB: tl.constexpr):
    x0_offset = tl.program_id(0) * X0BLOCK
    base_x0= tl.arange(0, X0BLOCK_SUB)
    loops_x0 = (X0BLOCK + X0BLOCK_SUB - 1) // X0BLOCK_SUB
    base_r1= tl.arange(0, R1BLOCK_SUB)
    loops_r1 = (r1_numel + R1BLOCK_SUB - 1) // R1BLOCK_SUB
    for loop_x0 in range(loops_x0):
        x0 = x0_offset + (loop_x0 * X0BLOCK_SUB) + base_x0[:,None]
        x0_mask = x0 < min(X0BLOCK+x0_offset, x0_numel)
        _tmp3 = tl.full([X0BLOCK_SUB, R1BLOCK_SUB], 0, tl.float32)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp0 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp1 = tmp0.to(tl.float32)
            tmp2 = tl.reshape(tmp1, [X0BLOCK_SUB, R1BLOCK_SUB])
            tmp4 = _tmp3 + tmp2
            _tmp3 = tl.where(r1_mask & x0_mask, tmp4, _tmp3)
        tmp3 = tl.sum(_tmp3, 1).reshape(X0BLOCK_SUB, 1)
        tmp5 = 4096.0
        tmp6 = tmp3 / tmp5
        _tmp12 = tl.full([X0BLOCK_SUB, R1BLOCK_SUB], 0, tl.float32)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp7 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp8 = tmp7.to(tl.float32)
            tmp9 = tmp8 - tmp6
            tmp10 = tmp9 * tmp9
            tmp11 = tl.reshape(tmp10, [X0BLOCK_SUB, R1BLOCK_SUB])
            tmp13 = _tmp12 + tmp11
            _tmp12 = tl.where(r1_mask & x0_mask, tmp13, _tmp12)
        tmp12 = tl.sum(_tmp12, 1).reshape(X0BLOCK_SUB, 1)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp14 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp23 = tl.load(in_ptr1 + (r1), r1_mask, other=0.0).to(tl.float32)
            tmp26 = tl.load(in_ptr2 + (r1), r1_mask, other=0.0).to(tl.float32)
            tmp15 = tmp14.to(tl.float32)
            tmp16 = tmp15 - tmp6
            tmp17 = 4096.0
            tmp18 = tmp12 / tmp17
            tmp19 = 1e-05
            tmp20 = tmp18 + tmp19
            tmp21 = tl.rsqrt(tmp20)
            tmp22 = tmp16 * tmp21
            tmp24 = tmp23.to(tl.float32)
            tmp25 = tmp22 * tmp24
            tmp27 = tmp26.to(tl.float32)
            tmp28 = tmp25 + tmp27
            tmp29 = tmp28.to(tl.float32)
            tl.store(out_ptr1 + (r1 + 4096*x0), tmp29, r1_mask & x0_mask)

metadata: {'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*bf16', 'in_ptr2': '*bf16', 'out_ptr1': '*bf16', 'x0_numel': 'i32', 'r1_numel': 'i32'}, 'device': 0, 'constants': {'X0BLOCK': 64, 'X0BLOCK_SUB': 4, 'R1BLOCK_SUB': 4096}, 'mix_mode': 'aiv', 'device_type': 'npu', 'num_warps': 1, 'num_stages': 1, 'debug': False, 'cc': 'Ascend910B3'}
Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 310, in compile
    next_module = compile_ir(module, metadata)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 526, in <lambda>
    lambda src, metadata: linalg_to_bin_enable_npu_compile(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 370, in linalg_to_bin_enable_npu_compile
    ret = subprocess.run(cmd_list, capture_output=True, check=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-compile', '/tmp/tmpqtxpq8xv/kernel.ttadapter.mlir', '--enable-auto-multi-buffer=True', '--enable-hfusion-compile=true', '--enable-hivm-compile=true', '--enable-triton-kernel-compile=true', '-o', '/tmp/tmpqtxpq8xv/kernel']' returned non-zero exit status 1.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/npu_triton_heuristics.py", line 257, in _precompile_config
    binary = triton.compile(*compile_args, **compile_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 319, in compile
    raise MLIRCompilationError(stage_name, error_detail)
triton.compiler.errors.MLIRCompilationError: 
///------------------[ERROR][Triton][BEG]------------------
[ConvertLinalgRToBinary] encounters error:
loc("/tmp/bishengir-compile-0cebf7/module.hivm.mlir":2:3): error: ub overflow, requires 3277568 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-0cebf7/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-0cebf7/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-975311/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-e53d5c/module.hivm.mlir":2:3): error: ub overflow, requires 3277568 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-e53d5c/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-e53d5c/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-fc8594/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-a07c6a/module.hivm.mlir":2:3): error: ub overflow, requires 3277568 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-a07c6a/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-a07c6a/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-566425/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-bbd0ee/module.hivm.mlir":2:3): error: ub overflow, requires 3277568 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-bbd0ee/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-bbd0ee/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-2c35a8/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-1959fe/module.hivm.mlir":2:3): error: ub overflow, requires 3277568 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-1959fe/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-1959fe/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-d9e455/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
[ERROR] Failed to run BiShengIR pipeline
///------------------[ERROR][Triton][END]------------------

ERROR:torch_npu._inductor.config:Triton compilation failed: triton_unk_fused_native_layer_norm_0
def triton_unk_fused_native_layer_norm_0(in_ptr0, in_ptr1, in_ptr2, out_ptr1, x0_numel, r1_numel, X0BLOCK: tl.constexpr, X0BLOCK_SUB: tl.constexpr, R1BLOCK_SUB: tl.constexpr):
    x0_offset = tl.program_id(0) * X0BLOCK
    base_x0= tl.arange(0, X0BLOCK_SUB)
    loops_x0 = (X0BLOCK + X0BLOCK_SUB - 1) // X0BLOCK_SUB
    base_r1= tl.arange(0, R1BLOCK_SUB)
    loops_r1 = (r1_numel + R1BLOCK_SUB - 1) // R1BLOCK_SUB
    for loop_x0 in range(loops_x0):
        x0 = x0_offset + (loop_x0 * X0BLOCK_SUB) + base_x0[:,None]
        x0_mask = x0 < min(X0BLOCK+x0_offset, x0_numel)
        _tmp3 = tl.full([X0BLOCK_SUB, R1BLOCK_SUB], 0, tl.float32)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp0 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp1 = tmp0.to(tl.float32)
            tmp2 = tl.reshape(tmp1, [X0BLOCK_SUB, R1BLOCK_SUB])
            tmp4 = _tmp3 + tmp2
            _tmp3 = tl.where(r1_mask & x0_mask, tmp4, _tmp3)
        tmp3 = tl.sum(_tmp3, 1).reshape(X0BLOCK_SUB, 1)
        tmp5 = 4096.0
        tmp6 = tmp3 / tmp5
        _tmp12 = tl.full([X0BLOCK_SUB, R1BLOCK_SUB], 0, tl.float32)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp7 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp8 = tmp7.to(tl.float32)
            tmp9 = tmp8 - tmp6
            tmp10 = tmp9 * tmp9
            tmp11 = tl.reshape(tmp10, [X0BLOCK_SUB, R1BLOCK_SUB])
            tmp13 = _tmp12 + tmp11
            _tmp12 = tl.where(r1_mask & x0_mask, tmp13, _tmp12)
        tmp12 = tl.sum(_tmp12, 1).reshape(X0BLOCK_SUB, 1)
        for loop_r1 in range(loops_r1):
            r1 = (loop_r1 * R1BLOCK_SUB) + base_r1[None,:]
            r1_mask = r1 < r1_numel
            tmp14 = tl.load(in_ptr0 + (r1 + 4096*x0), r1_mask & x0_mask, other=0.0).to(tl.float32)
            tmp23 = tl.load(in_ptr1 + (r1), r1_mask, other=0.0).to(tl.float32)
            tmp26 = tl.load(in_ptr2 + (r1), r1_mask, other=0.0).to(tl.float32)
            tmp15 = tmp14.to(tl.float32)
            tmp16 = tmp15 - tmp6
            tmp17 = 4096.0
            tmp18 = tmp12 / tmp17
            tmp19 = 1e-05
            tmp20 = tmp18 + tmp19
            tmp21 = tl.rsqrt(tmp20)
            tmp22 = tmp16 * tmp21
            tmp24 = tmp23.to(tl.float32)
            tmp25 = tmp22 * tmp24
            tmp27 = tmp26.to(tl.float32)
            tmp28 = tmp25 + tmp27
            tmp29 = tmp28.to(tl.float32)
            tl.store(out_ptr1 + (r1 + 4096*x0), tmp29, r1_mask & x0_mask)

metadata: {'signature': {'in_ptr0': '*bf16', 'in_ptr1': '*bf16', 'in_ptr2': '*bf16', 'out_ptr1': '*bf16', 'x0_numel': 'i32', 'r1_numel': 'i32'}, 'device': 0, 'constants': {'X0BLOCK': 64, 'X0BLOCK_SUB': 2, 'R1BLOCK_SUB': 4096}, 'mix_mode': 'aiv', 'device_type': 'npu', 'num_warps': 1, 'num_stages': 1, 'debug': False, 'cc': 'Ascend910B3'}
Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 310, in compile
    next_module = compile_ir(module, metadata)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 526, in <lambda>
    lambda src, metadata: linalg_to_bin_enable_npu_compile(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 370, in linalg_to_bin_enable_npu_compile
    ret = subprocess.run(cmd_list, capture_output=True, check=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-compile', '/tmp/tmpii8lo7s6/kernel.ttadapter.mlir', '--enable-auto-multi-buffer=True', '--enable-hfusion-compile=true', '--enable-hivm-compile=true', '--enable-triton-kernel-compile=true', '-o', '/tmp/tmpii8lo7s6/kernel']' returned non-zero exit status 1.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/npu_triton_heuristics.py", line 257, in _precompile_config
    binary = triton.compile(*compile_args, **compile_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 319, in compile
    raise MLIRCompilationError(stage_name, error_detail)
triton.compiler.errors.MLIRCompilationError: 
///------------------[ERROR][Triton][BEG]------------------
[ConvertLinalgRToBinary] encounters error:
loc("/tmp/bishengir-compile-176060/module.hivm.mlir":2:3): error: ub overflow, requires 1966848 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-176060/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-176060/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-e6506b/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-6ed3f1/module.hivm.mlir":2:3): error: ub overflow, requires 1966848 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-6ed3f1/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-6ed3f1/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-c34fff/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-322cef/module.hivm.mlir":2:3): error: ub overflow, requires 1966848 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-322cef/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-322cef/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-806e0d/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-fe34e9/module.hivm.mlir":2:3): error: ub overflow, requires 1966848 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-fe34e9/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-fe34e9/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-057d87/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-e4a349/module.hivm.mlir":2:3): error: ub overflow, requires 1966848 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-e4a349/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-e4a349/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-27b43a/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
[ERROR] Failed to run BiShengIR pipeline
///------------------[ERROR][Triton][END]------------------

ERROR:torch_npu._inductor.config:Triton compilation failed: triton_unk_fused_addmm_silu_1
def triton_unk_fused_addmm_silu_1(in_out_ptr0, in_ptr0, y0_numel, x1_numel, Y0BLOCK: tl.constexpr, Y0BLOCK_SUB: tl.constexpr, X1BLOCK_SUB: tl.constexpr):
    y0_offset = tl.program_id(0) * Y0BLOCK
    base_y0= tl.arange(0, Y0BLOCK_SUB)
    loops_y0 = (Y0BLOCK + Y0BLOCK_SUB - 1) // Y0BLOCK_SUB
    base_x1= tl.arange(0, X1BLOCK_SUB)
    loops_x1 = (x1_numel + X1BLOCK_SUB - 1) // X1BLOCK_SUB
    for loop_y0 in range(loops_y0):
        y0 = y0_offset + (loop_y0 * Y0BLOCK_SUB) + base_y0[:,None]
        y0_mask = y0 < min(Y0BLOCK+y0_offset, y0_numel)
        for loop_x1 in range(loops_x1):
            x1 = (loop_x1 * X1BLOCK_SUB) + base_x1[None,:]
            x1_mask = x1 < x1_numel
            tmp0 = tl.load(in_out_ptr0 + (x1 + 16384*y0), x1_mask & y0_mask).to(tl.float32)
            tmp1 = tl.load(in_ptr0 + (x1), x1_mask).to(tl.float32)
            tmp2 = tmp0 + tmp1
            tmp3 = tmp2.to(tl.float32)
            tmp4 = tl.sigmoid(tmp3)
            tmp5 = tmp3 * tmp4
            tmp6 = tmp5.to(tl.float32)
            tl.store(in_out_ptr0 + (x1 + 16384*y0), tmp6, x1_mask & y0_mask)

metadata: {'signature': {'in_out_ptr0': '*bf16', 'in_ptr0': '*bf16', 'y0_numel': 'i32', 'x1_numel': 'i32'}, 'device': 0, 'constants': {'Y0BLOCK': 64, 'Y0BLOCK_SUB': 2, 'X1BLOCK_SUB': 16384}, 'mix_mode': 'aiv', 'device_type': 'npu', 'num_warps': 1, 'num_stages': 1, 'debug': False, 'cc': 'Ascend910B3'}
Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 310, in compile
    next_module = compile_ir(module, metadata)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 526, in <lambda>
    lambda src, metadata: linalg_to_bin_enable_npu_compile(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 370, in linalg_to_bin_enable_npu_compile
    ret = subprocess.run(cmd_list, capture_output=True, check=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-compile', '/tmp/tmp0n2lgyvs/kernel.ttadapter.mlir', '--enable-auto-multi-buffer=True', '--enable-hfusion-compile=true', '--enable-hivm-compile=true', '--enable-triton-kernel-compile=true', '-o', '/tmp/tmp0n2lgyvs/kernel']' returned non-zero exit status 1.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/npu_triton_heuristics.py", line 257, in _precompile_config
    binary = triton.compile(*compile_args, **compile_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 319, in compile
    raise MLIRCompilationError(stage_name, error_detail)
triton.compiler.errors.MLIRCompilationError: 
///------------------[ERROR][Triton][BEG]------------------
[ConvertLinalgRToBinary] encounters error:
loc("/tmp/bishengir-compile-9a360a/module.hivm.mlir":2:3): error: ub overflow, requires 3145728 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-9a360a/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-9a360a/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-44e5d7/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-153e21/module.hivm.mlir":2:3): error: ub overflow, requires 3145728 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-153e21/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-153e21/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-2575cb/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-ee0228/module.hivm.mlir":2:3): error: ub overflow, requires 3145728 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-ee0228/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-ee0228/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-2b3623/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-067fb5/module.hivm.mlir":2:3): error: ub overflow, requires 3145728 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-067fb5/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-067fb5/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-6ca9ad/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-ad222f/module.hivm.mlir":2:3): error: ub overflow, requires 3145728 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-ad222f/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-ad222f/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-d0dd2f/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
[ERROR] Failed to run BiShengIR pipeline
///------------------[ERROR][Triton][END]------------------

ERROR:torch_npu._inductor.config:Triton compilation failed: triton_unk_fused_addmm_silu_1
def triton_unk_fused_addmm_silu_1(in_out_ptr0, in_ptr0, y0_numel, x1_numel, Y0BLOCK: tl.constexpr, Y0BLOCK_SUB: tl.constexpr, X1BLOCK_SUB: tl.constexpr):
    y0_offset = tl.program_id(0) * Y0BLOCK
    base_y0= tl.arange(0, Y0BLOCK_SUB)
    loops_y0 = (Y0BLOCK + Y0BLOCK_SUB - 1) // Y0BLOCK_SUB
    base_x1= tl.arange(0, X1BLOCK_SUB)
    loops_x1 = (x1_numel + X1BLOCK_SUB - 1) // X1BLOCK_SUB
    for loop_y0 in range(loops_y0):
        y0 = y0_offset + (loop_y0 * Y0BLOCK_SUB) + base_y0[:,None]
        y0_mask = y0 < min(Y0BLOCK+y0_offset, y0_numel)
        for loop_x1 in range(loops_x1):
            x1 = (loop_x1 * X1BLOCK_SUB) + base_x1[None,:]
            x1_mask = x1 < x1_numel
            tmp0 = tl.load(in_out_ptr0 + (x1 + 16384*y0), x1_mask & y0_mask).to(tl.float32)
            tmp1 = tl.load(in_ptr0 + (x1), x1_mask).to(tl.float32)
            tmp2 = tmp0 + tmp1
            tmp3 = tmp2.to(tl.float32)
            tmp4 = tl.sigmoid(tmp3)
            tmp5 = tmp3 * tmp4
            tmp6 = tmp5.to(tl.float32)
            tl.store(in_out_ptr0 + (x1 + 16384*y0), tmp6, x1_mask & y0_mask)

metadata: {'signature': {'in_out_ptr0': '*bf16', 'in_ptr0': '*bf16', 'y0_numel': 'i32', 'x1_numel': 'i32'}, 'device': 0, 'constants': {'Y0BLOCK': 64, 'Y0BLOCK_SUB': 1, 'X1BLOCK_SUB': 16384}, 'mix_mode': 'aiv', 'device_type': 'npu', 'num_warps': 1, 'num_stages': 1, 'debug': False, 'cc': 'Ascend910B3'}
Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 310, in compile
    next_module = compile_ir(module, metadata)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 526, in <lambda>
    lambda src, metadata: linalg_to_bin_enable_npu_compile(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 370, in linalg_to_bin_enable_npu_compile
    ret = subprocess.run(cmd_list, capture_output=True, check=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-compile', '/tmp/tmpqys2kh9n/kernel.ttadapter.mlir', '--enable-auto-multi-buffer=True', '--enable-hfusion-compile=true', '--enable-hivm-compile=true', '--enable-triton-kernel-compile=true', '-o', '/tmp/tmpqys2kh9n/kernel']' returned non-zero exit status 1.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/npu_triton_heuristics.py", line 257, in _precompile_config
    binary = triton.compile(*compile_args, **compile_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 319, in compile
    raise MLIRCompilationError(stage_name, error_detail)
triton.compiler.errors.MLIRCompilationError: 
///------------------[ERROR][Triton][BEG]------------------
[ConvertLinalgRToBinary] encounters error:
loc("/tmp/bishengir-compile-6a5baa/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-6a5baa/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-6a5baa/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-3a3687/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-5cc671/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-5cc671/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-5cc671/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-bd7d7b/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-97a88e/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-97a88e/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-97a88e/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-8f8ea3/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-8edb46/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-8edb46/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-8edb46/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-2a2e0a/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-0c779e/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-0c779e/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-0c779e/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-225cbe/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
[ERROR] Failed to run BiShengIR pipeline
///------------------[ERROR][Triton][END]------------------

ERROR:torch_npu._inductor.config:Triton compilation failed: triton_unk_fused_addmm_silu_1
def triton_unk_fused_addmm_silu_1(in_out_ptr0, in_ptr0, y0_numel, x1_numel, Y0BLOCK: tl.constexpr, Y0BLOCK_SUB: tl.constexpr, X1BLOCK_SUB: tl.constexpr):
    y0_offset = tl.program_id(0) * Y0BLOCK
    base_y0= tl.arange(0, Y0BLOCK_SUB)
    loops_y0 = (Y0BLOCK + Y0BLOCK_SUB - 1) // Y0BLOCK_SUB
    base_x1= tl.arange(0, X1BLOCK_SUB)
    loops_x1 = (x1_numel + X1BLOCK_SUB - 1) // X1BLOCK_SUB
    for loop_y0 in range(loops_y0):
        y0 = y0_offset + (loop_y0 * Y0BLOCK_SUB) + base_y0[:,None]
        y0_mask = y0 < min(Y0BLOCK+y0_offset, y0_numel)
        for loop_x1 in range(loops_x1):
            x1 = (loop_x1 * X1BLOCK_SUB) + base_x1[None,:]
            x1_mask = x1 < x1_numel
            tmp0 = tl.load(in_out_ptr0 + (x1 + 16384*y0), x1_mask & y0_mask).to(tl.float32)
            tmp1 = tl.load(in_ptr0 + (x1), x1_mask).to(tl.float32)
            tmp2 = tmp0 + tmp1
            tmp3 = tmp2.to(tl.float32)
            tmp4 = tl.sigmoid(tmp3)
            tmp5 = tmp3 * tmp4
            tmp6 = tmp5.to(tl.float32)
            tl.store(in_out_ptr0 + (x1 + 16384*y0), tmp6, x1_mask & y0_mask)

metadata: {'signature': {'in_out_ptr0': '*bf16', 'in_ptr0': '*bf16', 'y0_numel': 'i32', 'x1_numel': 'i32'}, 'device': 0, 'constants': {'Y0BLOCK': 48, 'Y0BLOCK_SUB': 1, 'X1BLOCK_SUB': 16384}, 'mix_mode': 'aiv', 'device_type': 'npu', 'num_warps': 1, 'num_stages': 1, 'debug': False, 'cc': 'Ascend910B3'}
Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 310, in compile
    next_module = compile_ir(module, metadata)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 526, in <lambda>
    lambda src, metadata: linalg_to_bin_enable_npu_compile(
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/backends/ascend/compiler.py", line 370, in linalg_to_bin_enable_npu_compile
    ret = subprocess.run(cmd_list, capture_output=True, check=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-compile', '/tmp/tmpjtjbq5my/kernel.ttadapter.mlir', '--enable-auto-multi-buffer=True', '--enable-hfusion-compile=true', '--enable-hivm-compile=true', '--enable-triton-kernel-compile=true', '-o', '/tmp/tmpjtjbq5my/kernel']' returned non-zero exit status 1.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/_inductor/npu_triton_heuristics.py", line 257, in _precompile_config
    binary = triton.compile(*compile_args, **compile_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/triton/compiler/compiler.py", line 319, in compile
    raise MLIRCompilationError(stage_name, error_detail)
triton.compiler.errors.MLIRCompilationError: 
///------------------[ERROR][Triton][BEG]------------------
[ConvertLinalgRToBinary] encounters error:
loc("/tmp/bishengir-compile-ddd823/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-ddd823/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-ddd823/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-95661c/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-b1a196/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-b1a196/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-b1a196/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-fdc22e/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-ed0a96/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-ed0a96/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-ed0a96/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-b648e6/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-c7b2dd/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-c7b2dd/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-c7b2dd/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-e9e9a7/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
loc("/tmp/bishengir-compile-f94cb6/module.hivm.mlir":2:3): error: ub overflow, requires 2097152 bits while 1572864 bits avaliable!
loc("/tmp/bishengir-compile-f94cb6/module.hivm.mlir":1:1): error: Failed to run BiShengHIR HIVM pipeline

Failed to run BiShengIR HIVM pipeline
[ERROR] Executing: /usr/local/Ascend/ascend-toolkit/latest/bin/bishengir-hivm-compile /tmp/bishengir-compile-f94cb6/module.hivm.mlir --limit-auto-multi-buffer-buffer=only-cube --enable-auto-bind-sub-block=true --enable-debug-info=false --limit-auto-multi-buffer-of-local-buffer=no-l0c --enable-hivm-auto-cv-balance=true --enable-static-bare-ptr=true --tile-mix-cube-loop=1 --enable-hivm-unit-flag-sync=false --enable-auto-blockify-loop=false --enable-code-motion=true --set-workspace-multibuffer=2 --allow-unregistered-dialects=false --tile-mix-vector-loop=1 --enable-hivm-global-workspace-reuse=false --enable-bin-relocation=true --limit-auto-multi-buffer-only-for-local-buffer=true --enable-hivm-inject-block-all-sync=false --enable-hivm-inject-barrier-all-sync=false --enable-hivm-nd2nz-on-vector=false --enable-hivm-auto-storage-align=true --enable-auto-multi-buffer=true --enable-sanitizer=false --enable-triton-kernel-compile=true -o /tmp/bishengir-compile-a94a3d/module.hivm.opt.mlir --enable-hivm-compile=true --convert-hir-to-lir=false
[ERROR] Failed to run BiShengIR pipeline
///------------------[ERROR][Triton][END]------------------

W1225 08:10:55.568000 40305 site-packages/torch/_inductor/debug.py:435] [0/0] model__0_inference_0 debug trace: /mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/torch_compile_debug/run_2025_12_25_08_10_48_803449-pid_40305/torchinductor/model__0_inference_0.0
Setting up cuda graphs ...
[DEBUG] start graph capture batchsize:1 num_tokens:2048
Traceback (most recent call last):
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 371, in <module>
    run_ranking_gr_inference()
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/benchmark/inference_benchmark_2b_random.py", line 197, in run_ranking_gr_inference
    model_predict = InferenceRankingGR(
                    ^^^^^^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/./model/inference_ranking_gr.py", line 169, in __init__
    self._hstu_block.set_cudagraph(
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 176, in set_cudagraph
    graph_max = capture_graph(
                ^^^^^^^^^^^^^^
  File "/mnt/workspace/workspace_ls/GR_benchmark/rec_model_zoo_pytorch/GR/NPU/GR_SparseMOE/recsys-examples/examples/hstu/modules/hstu_block_inference.py", line 316, in capture_graph
    static_uvqk = self._attention_layers[layer_idx].forward_input(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 574, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1380, in __call__
    return self._torchdynamo_orig_callable(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 1164, in __call__
    result = self._inner_convert(
             ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 547, in __call__
    return _compile(
           ^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 986, in _compile
    guarded_code = compile_inner(code, one_graph, hooks, transform)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 715, in compile_inner
    return _compile_inner(code, one_graph, hooks, transform)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_utils_internal.py", line 95, in wrapper_function
    return function(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 750, in _compile_inner
    out_code = transform_code_object(code, transform)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/bytecode_transformation.py", line 1361, in transform_code_object
    transformations(instructions, code_options)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 231, in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/convert_frame.py", line 662, in transform
    tracer.run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 2868, in run
    super().run()
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 1052, in run
    while self.step():
          ^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 962, in step
    self.dispatch_table[inst.opcode](self, inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3048, in RETURN_VALUE
    self._return(inst)
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3033, in _return
    self.output.compile_subgraph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1101, in compile_subgraph
    self.compile_and_call_fx_graph(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1382, in compile_and_call_fx_graph
    compiled_fn = self.call_user_compiler(gm)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1432, in call_user_compiler
    return self._call_user_compiler(gm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1483, in _call_user_compiler
    raise BackendCompilerFailed(self.compiler_fn, e).with_traceback(
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/output_graph.py", line 1462, in _call_user_compiler
    compiled_fn = compiler_fn(gm, self.example_inputs())
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/repro/after_dynamo.py", line 130, in __call__
    compiled_gm = compiler_fn(gm, example_inputs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch_npu/utils/_dynamo.py", line 161, in new_call
    return src_call(self, model_, inputs_)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/__init__.py", line 2340, in __call__
    return compile_fx(model_, inputs_, config_patches=self.config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 1863, in compile_fx
    return aot_autograd(
           ^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/backends/common.py", line 83, in __call__
    cg = aot_module_simplified(gm, example_inputs, **self.kwargs)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1155, in aot_module_simplified
    compiled_fn = dispatch_and_compile()
                  ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1131, in dispatch_and_compile
    compiled_fn, _ = create_aot_dispatcher_function(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 580, in create_aot_dispatcher_function
    return _create_aot_dispatcher_function(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 830, in _create_aot_dispatcher_function
    compiled_fn, fw_metadata = compiler_fn(
                               ^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/jit_compile_runtime_wrappers.py", line 203, in aot_dispatch_base
    compiled_fw = compiler(fw_module, updated_flat_args)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 489, in __call__
    return self.compiler_fn(gm, example_inputs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 1741, in fw_compiler_base
    return inner_compile(
           ^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 569, in compile_fx_inner
    return wrap_compiler_debug(_compile_fx_inner, compiler_name="inductor")(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_dynamo/repro/after_aot.py", line 102, in debug_wrapper
    inner_compiled_fn = compiler_fn(gm, example_inputs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 685, in _compile_fx_inner
    mb_compiled_graph = fx_codegen_and_compile(
                        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 1129, in fx_codegen_and_compile
    return scheme.codegen_and_compile(gm, example_inputs, inputs_to_check, graph_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 1046, in codegen_and_compile
    num_bytes, nodes_num_elem, node_runtimes = graph.count_bytes()
                                               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/graph.py", line 2008, in count_bytes
    num_bytes = node.get_read_write_buffers_sizes()
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 5, in get_read_write_buffers_sizes_cache_on_self
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/scheduler.py", line 659, in get_read_write_buffers_sizes
    node_bytes += get_buf_bytes(buf)
                  ^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.0/lib/python3.11/site-packages/torch/_inductor/scheduler.py", line 638, in get_buf_bytes
    assert isinstance(user.node, BaseSchedulerNode)
torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:
AssertionError: 

Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

[ERROR] 2025-12-25-08:10:56 (PID:40305, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

怀疑是复用了 GPU 算子的过大的 tile config，在 NPU 上导致 unified buffer overflow


## 评论 (1)

### fvfc-stpgh · 2026-01-22

感谢您的反馈，该现象为Triton算子编译报错，可能是因为block太大而造成的ub溢出，可以尝试通过设置sub block size切片解决，具体可以参考：https://gitcode.com/Ascend/triton-ascend/blob/master/docs/HighPerformanceGuide.md 。
如果您还有Triton算子编译相关的问题，可以前往Ascend/triton-ascend社区进行提问：https://gitcode.com/Ascend/triton-ascend/issues 。
