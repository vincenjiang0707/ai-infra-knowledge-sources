# [Issue #3251] [Bug] iOS SDK: current available model_libs in dist/lib/libmodel_iphone.a: []

source: https://github.com/mlc-ai/mlc-llm/issues/3251
state: closed | updated: 2026-03-02T14:51:10Z
labels: bug

## 正文

## 🐛 Bug

Met with the `current available model_libs in dist/lib/libmodel_iphone.a: []` validation error when following iOS App SDK instructions: https://llm.mlc.ai/docs/deploy/ios.html#build-ios-app-from-source

## To Reproduce

I am (religiously) following the above instruction.

- I am using the main branch, with commit id: 517d79be
- Before I ran $ mlc_llm package, I even simplified `MLCChat/mlc-package-config.json`:
```
{
   "device": "iphone",
   "model_list": [
      {
         "model": "HF://mlc-ai/gemma-2b-it-q4f16_1-MLC",
         "model_id": "gemma-2b-q4f16_1",
         "estimated_vram_bytes": 3000000000,
         "overrides": {
            "prefill_chunk_size": 128
         },
         "bundle_weight": true
      }
   ]
}
```

- The log message indicates that available model libs are empty. And thus, there is no way for me to move to the subsequent steps. 
```
[2025-06-14 15:03:12] INFO package.py:212: Validating the library dist/lib/libmodel_iphone.a
[2025-06-14 15:03:12] INFO package.py:213: List of available model libs packaged: [], if we have '-' in the model_lib string, it will be turned into '_'
```

- The validation error came out of package.py. In there, there is a pattern requirement of suffix = "___tvm_dev_mblob". This might be the issues, as none of the .o object filenames that are created during the process has this suffix. That explains why available model libs packaged: [] - just a thought.

## Environment

 - Platform: IOS
 - Operating system: MacOS
 - How you installed MLC-LLM: conda env
 - How you installed TVM-Unity: https://llm.mlc.ai/docs/install/tvm.html
 - Python version: 3.11
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`: GIT_COMMIT_HASH: 0b6c2618a3aba1ad77479fea7a2ccd0f65e7594e


## 评论 (4)

### pr0m1see · 2025-06-15

I have the same problem when I built for Android. 

The output said this:

```
This can happen when we manually specified model_lib_path_for_prepare_libs in mlc-package-config.json
        Consider remove model_lib_path_for_prepare_libs (so library can be jitted)or check the compile command
```
But there is no specified model_lib_path_for_prepare_libs in my json file.

### pr0m1see · 2025-06-16

I found a workaround: simply removing the sys.exit(255) line from mlc_llm's package.py.

### xintoteai · 2025-06-16

@pr0m1see Simply commenting out this line won't work, as `mlc_llm` lib is installed using out of the wheel file from https://mlc.ai/wheels. Are you suggesting that I must build my own mlc_llm lib from source? Or perhaps you can share your tricks.

### Uladzimir-Bulakhau · 2025-06-20

Same errors. INFO package.py:258: Validation failed
