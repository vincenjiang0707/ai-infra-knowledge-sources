# [Issue #120] CUDA error when trying to use llama3.1 8B 4bit quantized model sample

source: https://github.com/dropbox/hqq/issues/120
state: closed | updated: 2024-11-01T18:46:03Z
labels: 

## 正文

Get model from https://huggingface.co/mobiuslabsgmbh/Llama-3.1-8b-instruct_4bitgs64_hqq_calib
HQQ installed according to instructions and tried running the sample given on HF site.

After downloading the model, the execution fails on a CUDA error.

```Traceback (most recent call last):
  File "E:\Projekt\Python\aistuffidk\llama3_1_4b.py", line 25, in <module>
    prepare_for_inference(model, backend="torchao_int4")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\utils\patching.py", line 116, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4, verbose=verbose)
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\utils\patching.py", line 25, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\models\base.py", line 154, in patch_linearlayers
    patch_fct(tmp_mapping[name], patch_param),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\backends\torchao.py", line 324, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\backends\torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "C:\Program Files\Python312\Lib\site-packages\torch\utils\_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\backends\torchao.py", line 196, in process_hqq_quants
    self.scales_and_zeros = self.pack_scales_and_zeros(scales_torch, zeros_torch)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Demon\AppData\Roaming\Python\Python312\site-packages\hqq\backends\torchao.py", line 248, in pack_scales_and_zeros
    torch.cat(
RuntimeError: CUDA error: named symbol not found
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.```

Windows 10 64bit
Nvidia RTX 2070 w 8G VRAM
CUDA 12.4 & torch compiled with it

## 评论 (8)

### mobicham · 2024-09-18

Hi, I don't know if 12.4 is supported for the nightly torch. 
Can you try: 
- CUDA 12.1
- pip install torch==2.5.0.dev20240905+cu121 --index-url https://download.pytorch.org/whl/nightly/cu121; 
- pip install hqq (install hqq after installing pytorch)

### larin92 · 2024-09-23

same issue, cuda 12.4, originally used torch==2.4, tried these (didn't help):
```
pip install torch==2.6.0.dev20240922+cu124 --index-url https://download.pytorch.org/whl/nightly/cu124;
```
```
pip install torch==2.5.0.dev20240905+cu121 --index-url https://download.pytorch.org/whl/nightly/cu121;
```
```
pip install torch==2.6.0.dev20240923+cu121 --index-url https://download.pytorch.org/whl/nightly/cu121;
```

### mobicham · 2024-09-23

@larin92 did you set your environment to use cuda 12.1 ? Make sure you are using the right version:
```Python
export CUDA_HOME=/usr/local/cuda-12.1 # or the path where you have cuda-12.1
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
export PATH=${CUDA_HOME}/bin:${PATH}
```

### larin92 · 2024-09-23

for anyone bumping into this issue in future:
@mobicham explained in discord, for `torchao` to work you need at least Ampere GPU, same for `torch.compile`'ing the whole model

### mobicham · 2024-09-23

Thanks @larin92 ! Willl close the issue, unless you face issues with Ampere gpus and above

### NEWbie0709 · 2024-10-24

Hi, I am also facing this issue when running the code. This is the error and the code I used.
```
(hqq) user@i9-4090:/mnt/c/Users/i9-4090/Documents/tianyi$ python testing.py
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 115/115 [00:00<00:00, 6243.54it/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 197/197 [00:00<00:00, 12991.79it/s]
Model was already quantized
Starting from v4.46, the `logits` model output will have the same type as the model (except at train time, where it will always be FP32)
  0%|                                                                                                                                                                             | 0/999 [00:00<?, ?it/s]/home/user/miniconda3/envs/hqq/lib/python3.9/contextlib.py:87: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
  0%|▏                                                                                                                                                                  | 1/999 [00:07<2:08:50,  7.75s/it]/home/user/miniconda3/envs/hqq/lib/python3.9/contextlib.py:87: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
  0%|▎                                                                                                                                                                  | 2/999 [00:14<2:02:25,  7.37s/it]/home/user/miniconda3/envs/hqq/lib/python3.9/contextlib.py:87: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
  0%|▍                                                                                                                                                                  | 3/999 [00:14<1:07:26,  4.06s/it]/home/user/miniconda3/envs/hqq/lib/python3.9/contextlib.py:87: FutureWarning: `torch.backends.cuda.sdp_kernel()` is deprecated. In the future, this context manager will be removed. Please see `torch.nn.attention.sdpa_kernel()` for the new context manager, with updated signature.
  self.gen = func(*args, **kwds)
 99%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████  | 987/999 [00:22<00:00, 131.15it/s]unknown:0: unknown: block: [0,0,0], thread: [32,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [33,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [34,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [35,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [36,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [37,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [38,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [39,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [40,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [41,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [42,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [43,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [44,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [45,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [46,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [47,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [48,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [49,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [50,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [51,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [52,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [53,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [54,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [55,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [56,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [57,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [58,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [59,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [60,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [61,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [62,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [63,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [96,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [97,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [98,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [99,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [100,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [101,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [102,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [103,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [104,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [105,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [106,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [107,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [108,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [109,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [110,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [111,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [112,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [113,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [114,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [115,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [116,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [117,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [118,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [119,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [120,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [121,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [122,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [123,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [124,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [125,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [126,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [127,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [64,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [65,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [66,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [67,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [68,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [69,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [70,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [71,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [72,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [73,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [74,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [75,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [76,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [77,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [78,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [79,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [80,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [81,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [82,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [83,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [84,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [85,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [86,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [87,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [88,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [89,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [90,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [91,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [92,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [93,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [94,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [95,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [0,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [1,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [2,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [3,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [4,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [5,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [6,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [7,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [8,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [9,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [10,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [11,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [12,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [13,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [14,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [15,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [16,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [17,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [18,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [19,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [20,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [21,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [22,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [23,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [24,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [25,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [26,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [27,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [28,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [29,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [30,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
unknown:0: unknown: block: [0,0,0], thread: [31,0,0] Assertion `index out of bounds: 0 <= tmp42 < 1024` failed.
 99%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎ | 989/999 [00:22<00:00, 43.93it/s]
Traceback (most recent call last):
  File "/mnt/c/Users/i9-4090/Documents/tianyi/testing.py", line 167, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while
  File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 205, in warmup
    self.generate(prompt, print_tokens=False)
  File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 387, in generate
    return self.next_token_iterator(
  File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 352, in next_token_iterator
    next_token = self.gen_next_token(next_token)
  File "/home/user/miniconda3/envs/hqq/lib/python3.9/site-packages/hqq/utils/generation_hf.py", line 334, in gen_next_token
    self.cache_position += 1
RuntimeError: CUDA error: device-side assert triggered
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```


```
import torch
from transformers import AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.utils.patching import *
from hqq.core.quantize import *
from hqq.utils.generation_hf import HFGenerator


import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

model_id  = "VPTQ-community/Qwen2.5-7B-Instruct-v8-k256-256-woft"

compute_dtype = torch.bfloat16
device     = "cuda"
cache_path = "."

from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
#from hqq.models.hf.llama import LlamaHQQ as AutoHQQHFModel #OR for llama models
from hqq.core.quantize import *

model = AutoHQQHFModel.from_quantized("output/Qwen2.5-32B-Instruct-v8-k65536-256-woft_HQQ_4bit",cache_dir=cache_path, compute_dtype=torch.bfloat16, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_id,cache_dir=cache_path) 

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

prepare_for_inference(model,backend="torchao_int4")
#prepare_for_inference(model, backend="bitblas") #takes a while to init...

#Generate
###################################################
#For longer context, make sure to allocate enough cache via the cache_size= parameter
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() #Warm-up takes a while

import time
t1 = time.time()
gen.generate("Write an essay about large language models", print_tokens=True)
t2 = time.time()
print('Took', t2-t1, 'secs')
```

RTX 4090
13th Gen Intel(R) Core(TM) i9-13900KF 

### mobicham · 2024-10-24

Hey, sorry for the delay, I am traveling this week, will try to debug it when I get back home:

If you are using a language (only) model:
* If you are getting `CUDA error: device-side assert triggered` with `HFGenerator`, use the default HF transformers generator: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py#L39-L47
* Just follow this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py

If you are using a vision-language model: 
* You should only quantize the language model: `AutoHQQHFModel.quantize_model(model.language_model, ...)`
* Make sure the rest of the towers are moved to the right device, something like this (change it with respect to your model): https://github.com/mobiusml/hqq/blob/master/examples/hf/llava-v1.6-34b_24GB.py#L36-L40
* You can't use `HFGenerator` with vision-language model, so just use HF transformers generator.



### mobicham · 2024-10-25

I tried with Qwen, it's working fine like this, had to change a bit the chat template since Qwen has that system prompt:

```Python
#pip install torch==2.4.1 hqq; #2.4.1+cu124 
#OMP_NUM_THREADS=16 CUDA_VISIBLE_DEVICES=0 ipython3 ......
########################################################################
import torch, os
device        = 'cuda:0'
backend       = 'torchao_int4' 
compute_dtype = torch.bfloat16 if backend=="torchao_int4" else torch.float16
cache_dir     = '.' 
model_id      = "Qwen/Qwen2.5-7B-Instruct"

torch._dynamo.config.inline_inbuilt_nn_modules = False
########################################################################
from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *

#Load
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

#Quantize
nbits, group_size = 4, 128 
cached_model = model_id.split('/')[-1] + '_' + str(nbits) + '_' + str(group_size)
if(os.path.exists(cached_model)):
	model = AutoHQQHFModel.from_quantized(cached_model, compute_dtype=compute_dtype, device=device)
else:
	model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_dir, torch_dtype=compute_dtype, attn_implementation="sdpa")
	quant_config  = BaseQuantizeConfig(nbits=nbits, group_size=group_size, axis=1)
	AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
	AutoHQQHFModel.save_quantized(model, cached_model)

from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend=backend, verbose=False)

#Inference
########################################################################
# from hqq.utils.generation_hf import HFGenerator
# gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() 
# out = gen.generate("Write an essay about large language models.", print_tokens=False)

######################################################################
#Using HF model.generate()
from hqq.utils.generation_hf import patch_model_for_compiled_runtime

patch_model_for_compiled_runtime(model, tokenizer, warmup=True)

prompt = "Write an essay about large language models."

messages = [
    {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
inputs = tokenizer([tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)], return_tensors="pt").to(model.device)

import time
t1 = time.time()
outputs = model.generate(**inputs, max_new_tokens=1000, cache_implementation="static", pad_token_id=tokenizer.pad_token_id) 
t2 = time.time()
print('End-2-end speed:', str(int((inputs['input_ids'].numel() + outputs[0].numel()) / (t2-t1))) + ' tokens/sec') #165 tokens/sec | 4090 RTX
#print(tokenizer.decode(outputs[0]))
```
