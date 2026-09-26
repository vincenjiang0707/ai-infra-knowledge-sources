# [Issue #1649] BERT Benchmark unable to execute successfully.

source: https://github.com/mlcommons/inference/issues/1649
state: closed | updated: 2026-05-06T00:41:02Z
labels: Stale

## 正文

**Command:** cmr "run mlperf inference generate-run-cmds _submission" --quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference --backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 --category=edge --division=open --env.CM_VERIFY_SSL=false 
**OS Version:** Ubuntu 22.04 with kernel 6.5.0
**CUDA Version:** 12.0
**Pytorch version:** 2.2.1

**Error Message:** 
Loading BERT configs...
Loading PyTorch model...
Traceback (most recent call last):
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/run.py", line 150, in <module>
    main()
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/run.py", line 75, in main
    sut = get_pytorch_sut(args)
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/pytorch_SUT.py", line 111, in get_pytorch_sut
    return BERT_PyTorch_SUT(args)
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/pytorch_SUT.py", line 60, in __init__
    self.model.load_state_dict(torch.load(model_file), strict=False)
  File "/home/user/cm/lib/python3.10/site-packages/torch/serialization.py", line 1040, in load
    return _legacy_load(opened_file, map_location, pickle_module, **pickle_load_args)
  File "/home/user/cm/lib/python3.10/site-packages/torch/serialization.py", line 1258, in _legacy_load
    magic_number = pickle_module.load(f, **pickle_load_args)
_pickle.UnpicklingError: invalid load key, '\x0a'.
Finished destroying SUT.

Traceback (most recent call last):
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/accuracy-squad.py", line 449, in <module>
    main()
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/accuracy-squad.py", line 433, in main
    results = load_loadgen_log(
  File "/home/user/CM/repos/local/cache/55013b57c45543c7/inference/language/bert/accuracy-squad.py", line 346, in load_loadgen_log
    with open(log_path) as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/user/CM/repos/local/cache/06800ef908814fab/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/mlperf_log_accuracy.json'

CM error: Portable CM script failed (name = process-mlperf-accuracy, return code = 256)


## 评论 (28)

### gfursin · 2024-02-27

Thank you for reporting @willamloo3192 ! 
Inference reference implementations are usually not checked for the latest PyTorch and CUDA versions. 
The [MLCommons CM automation project](https://github.com/mlcommons/ck) is intended to solve it and we will try to fix the implementation within the inference WG and add a related CM test to this repository ... 
CC @arjunsuresh - Arjun let's discuss it at our Discord server and if we can't fix the implementation, we can raise the issue at the inference WG ...




### gfursin · 2024-02-27

By the way @arjunsuresh - do you know who is the official maintainer of the reference BERT CUDA implementation?

### arjunsuresh · 2024-02-27

@gfursin Currently the inference WG is the maintainer. @pgmpablo157321 can you please help?

### arjunsuresh · 2024-02-29

Looks like the issue is with 'incomplete model download'. @willamloo3192 can you please do `cm rm cache --tags=get,ml-model,bert-large,_pytorch` and rerun the command? We have added checksum check to this model download now to avoid this issue in future.

### willamloo3192 · 2024-02-29

Hi @arjunsuresh , I tested out and with the command `cm rm cache --tags=get,ml-model,bert-large,_pytorch` and ```
cmr "run mlperf inference generate-run-cmds _submission" \
--quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference \
--backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 \
--category=edge --division=open --env.CM_VERIFY_SSL=false
```, but I faced the new error on following lines.

CM error: can't load Python module code (path=/home/user/CM/repos/mlcommons@ck/cm-mlops/script/run-mlperf-inference-app, name=customize, err=No module named 'tabulate')!

### arjunsuresh · 2024-02-29

oh. Can you try `pip install tabulate` and try? `tabulate` should have been automatically installed by cm - will see what happened here. 

### willamloo3192 · 2024-02-29

Okay.. tabulate issue resolved but the main problem still persists. 
Loading BERT configs...
Loading PyTorch model...
Traceback (most recent call last):
  File "/home/user/CM/repos/local/cache/5949d58265094a6e/inference/language/bert/run.py", line 150, in <module>
    main()
  File "/home/user/CM/repos/local/cache/5949d58265094a6e/inference/language/bert/run.py", line 75, in main
    sut = get_pytorch_sut(args)
  File "/home/user/CM/repos/local/cache/5949d58265094a6e/inference/language/bert/pytorch_SUT.py", line 111, in get_pytorch_sut
    return BERT_PyTorch_SUT(args)
  File "/home/user/CM/repos/local/cache/5949d58265094a6e/inference/language/bert/pytorch_SUT.py", line 60, in __init__
    self.model.load_state_dict(torch.load(model_file), strict=False)
  File "/home/user/inference/language/bert/cm/lib/python3.10/site-packages/torch/serialization.py", line 1040, in load
    return _legacy_load(opened_file, map_location, pickle_module, **pickle_load_args)
  File "/home/user/inference/language/bert/cm/lib/python3.10/site-packages/torch/serialization.py", line 1258, in _legacy_load
    magic_number = pickle_module.load(f, **pickle_load_args)
_pickle.UnpicklingError: invalid load key, '\x0a'.
Finished destroying SUT.


### arjunsuresh · 2024-02-29

Is it possible to do
```
cm run script --tags=get,ml-model,bert-large,_pytorch -j
```
This should show a line `"CM_ML_MODEL_BERT_LARGE_FP32_PATH": "/home/arjun/CM/repos/local/cache/81f24499ec4b4d4d/model.pytorch",`

And `md5sum` should give as follows 
```
md5sum /home/arjun/CM/repos/local/cache/81f24499ec4b4d4d/model.pytorch
00fbcbfaebfa20d87ac9885120a6e9b4  /home/arjun/CM/repos/local/cache/81f24499ec4b4d4d/model.pytorch
```

Most likely the model download is not happening.

### willamloo3192 · 2024-02-29

md5sum /home/user/CM/repos/local/cache/259a1a94cf834658/model.pytorch
15468abaab0f99c7d1a423cf8e60349a  /home/user/CM/repos/local/cache/259a1a94cf834658/model.pytorch
I have the same feeling too that download is not happening. 


### arjunsuresh · 2024-02-29

yes, the download is not working. Can you please try this to download from an alternate source?
```
cm rm cache --tags=get,ml-model,bert-large,_pytorch
cm run script --tags=get,ml-model,bert-large,_pytorch,_zenodo -j
```

### willamloo3192 · 2024-02-29

Same still


### arjunsuresh · 2024-02-29

Did the above commands do any download? 

### gfursin · 2024-02-29

Discussing with @willamloo3192 on Discord, it looks like his internet connection is via proxy. It's orthogonal to CM but we should be able to add support for Proxy-based network connection in CM. @willamloo3192 - let's check how we can do it via Discord - it can be useful for the community to have this support in CM. Thanks!

### willamloo3192 · 2024-03-04

Latest updates: 

With the latest CM fix, I'm able to execute the test with the command below

```
cmr "run mlperf inference generate-run-cmds _submission" \
--quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference \
--backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 \
--category=edge --division=open --env.CM_VERIFY_SSL=false 
```

Reaching to the stage where target_qps error pops up
```
  * cm run script "get generic-python-lib _package.dmiparser"
       ! load /home/user/CM/repos/local/cache/ac8ae65ef39d4850/cm-cached-state.json
Generating SUT description file for default-pytorch-2.2.1
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py

Traceback (most recent call last):
  File "/home/user/.local/bin/cmr", line 8, in <module>
    sys.exit(run_script())
  File "/home/user/.local/lib/python3.10/site-packages/cmind/cli.py", line 76, in run_script
    return run(['run', 'script'] + argv)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/cli.py", line 35, in run
    r = cm.access(argv, out='con')
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 587, in access
    r = action_addr(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 192, in run
    r = self._run(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 1360, in _run
    r = customize_code.preprocess(ii)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/script/run-mlperf-inference-app/customize.py", line 181, in preprocess
    r = cm.access(ii)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 743, in access
    return cm.access(i)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 587, in access
    r = action_addr(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 192, in run
    r = self._run(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 1438, in _run
    r = prepare_and_run_script_with_postprocessing(run_script_input)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 4270, in prepare_and_run_script_with_postprocessing
    rr = run_postprocess(customize_code, customize_common_input, recursion_spaces, env, state, const,
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 4322, in run_postprocess
    r = customize_code.postprocess(ii)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/customize.py", line 142, in postprocess
    return {'return': 1, 'error': f'No {metric} found in performance summary. Pattern checked "{pattern[metric]}"'}
KeyError: 'target_qps'

```

### arjunsuresh · 2024-03-05

@willamloo3192 The error means that the run somehow failed. Can you please add `--rerun` flag and share the full output?

### willamloo3192 · 2024-03-05

@arjunsuresh I tried with the `--rerun` flag and this is the error output.
```
user@user:~$ cmr "run mlperf inference generate-run-cmds _submission" \
--quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference \
--backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 \
--category=edge --division=open --env.CM_VERIFY_SSL=false --rerun

* cm run script "run mlperf inference generate-run-cmds _submission"

  * cm run script "detect os"
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

  * cm run script "get mlcommons inference src"
       ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf

  * cm run script "get sut description"

    * cm run script "detect os"
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get python3"
         ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

    * cm run script "get compiler gcc"
         ! load /home/user/CM/repos/local/cache/eb35dbdd076f4add/cm-cached-state.json

    * cm run script "get cuda-devices"

      * cm run script "get cuda _toolkit"
           ! load /home/user/CM/repos/local/cache/ffa46d47191b481a/cm-cached-state.json
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
rm: cannot remove 'a.out': No such file or directory

Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

Compiling program ...


Running program ...

/home/user
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA T1000 8GB
GPU compute capability: 7.5
CUDA driver version: 12.0
CUDA runtime version: 11.5
Global memory: 8362786816
Max clock rate: 1395.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  1024
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



    * cm run script "get generic-python-lib _package.dmiparser"
         ! load /home/user/CM/repos/local/cache/00ee5663ee0248da/cm-cached-state.json
Generating SUT description file for default-pytorch
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py

  * cm run script "get mlperf inference results dir"
       ! load /home/user/CM/repos/local/cache/872b94088ed443db/cm-cached-state.json

  * cm run script "install pip-package for-cmind-python _package.tabulate"
       ! load /home/user/CM/repos/local/cache/2cab78e2c97a4b38/cm-cached-state.json

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src"
         ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py
Using MLCommons Inference source from /home/user/CM/repos/local/cache/8eaf05e52449419b/inference

Running loadgen scenario: Offline and mode: performance

* cm run script "app mlperf inference generic _reference _bert-99 _pytorch _cuda _test _r4.0_default _offline"

  * cm run script "detect os"
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get sys-utils-cm"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get python"
       ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

  * cm run script "get mlcommons inference src _deeplearningexamples"
       ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py

  * cm run script "get dataset squad language-processing"
       ! load /home/user/CM/repos/local/cache/c80d923f53394101/cm-cached-state.json

  * cm run script "get dataset-aux squad-vocab"
       ! load /home/user/CM/repos/local/cache/87c4639b21fa462f/cm-cached-state.json

  * cm run script "app mlperf reference inference _cuda _offline _pytorch _bert-99 _fp32"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get sys-utils-cm"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "get python"
         ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

    * cm run script "get generic-python-lib _torch"
         ! load /home/user/CM/repos/local/cache/39b4a4c506724432/cm-cached-state.json

    * cm run script "get generic-python-lib _torch_cuda"
         ! load /home/user/CM/repos/local/cache/550a6c23204440d8/cm-cached-state.json

    * cm run script "get generic-python-lib _torchvision_cuda"
         ! load /home/user/CM/repos/local/cache/cf4490f2e79d466e/cm-cached-state.json

    * cm run script "get generic-python-lib _transformers"
         ! load /home/user/CM/repos/local/cache/5c7c6fb028fb431b/cm-cached-state.json

    * cm run script "get ml-model language-processing bert-large raw _pytorch _fp32"
         ! load /home/user/CM/repos/local/cache/ef502ac0e20c485a/cm-cached-state.json

Path to the ML model: /home/user/CM/repos/local/cache/8a8e22560d594def/model.pytorch

    * cm run script "get dataset squad original"
         ! load /home/user/CM/repos/local/cache/c80d923f53394101/cm-cached-state.json

    * cm run script "get dataset-aux squad-vocab"
         ! load /home/user/CM/repos/local/cache/87c4639b21fa462f/cm-cached-state.json

    * cm run script "generate user-conf mlperf inference"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python"
           ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

      * cm run script "get mlcommons inference src _deeplearningexamples"
           ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf

      * cm run script "get sut configs"
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/8eaf05e52449419b/inference'
Output Dir: '/home/user/CM/repos/local/cache/872b94088ed443db/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1'
bert.Offline.target_qps = 1
bert.Offline.max_query_count = 10
bert.Offline.min_query_count = 10
bert.Offline.min_duration = 0

           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py

    * cm run script "get loadgen"
         ! load /home/user/CM/repos/local/cache/06c74678b4bb4edb/cm-cached-state.json

    * cm run script "get mlcommons inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf

    * cm run script "get mlcommons inference src"
         ! load /home/user/CM/repos/local/cache/1c6b2de26cfc46b1/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf

    * cm run script "get generic-python-lib _package.psutil"
         ! load /home/user/CM/repos/local/cache/78464279b61b4ab7/cm-cached-state.json

    * cm run script "get generic-python-lib _package.pydantic"
         ! load /home/user/CM/repos/local/cache/7d380516ca464769/cm-cached-state.json

    * cm run script "get generic-python-lib _tokenization"
         ! load /home/user/CM/repos/local/cache/52c6b84e225b4bfb/cm-cached-state.json

    * cm run script "get generic-python-lib _six"
         ! load /home/user/CM/repos/local/cache/f2899a12f02b4908/cm-cached-state.json

    * cm run script "get generic-python-lib _package.absl-py"
         ! load /home/user/CM/repos/local/cache/af93969373564f64/cm-cached-state.json

    * cm run script "get generic-python-lib _boto3"
         ! load /home/user/CM/repos/local/cache/060f36e81c3e4beb/cm-cached-state.json
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/8eaf05e52449419b/inference'
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference-reference/customize.py

  * cm run script "benchmark-mlperf"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program-mlperf/customize.py

  * cm run script "benchmark-program program"

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py
***************************************************************************
CM script::benchmark-program/run.sh

Run Directory: /home/user/CM/repos/local/cache/8eaf05e52449419b/inference/language/bert

CMD: /usr/bin/python3 run.py --backend=pytorch --scenario=Offline   --mlperf_conf '/home/user/CM/repos/local/cache/8eaf05e52449419b/inference/mlperf.conf' --user_conf '/home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/d07f85c5066441ddb160471b3dada912.conf' 2>&1 | tee /home/user/CM/repos/local/cache/872b94088ed443db/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1/console.out

         ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/run-ubuntu.sh from tmp-run.sh
/home/user/.local/lib/python3.10/site-packages/transformers/utils/generic.py:311: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  torch.utils._pytree._register_pytree_node(
2024-03-05 23:28:59.478318: I tensorflow/core/util/port.cc:113] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2024-03-05 23:28:59.501371: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:9261] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-03-05 23:28:59.501399: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:607] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-03-05 23:28:59.502116: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1515] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2024-03-05 23:28:59.505850: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2024-03-05 23:28:59.963257: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
/home/user/.local/lib/python3.10/site-packages/transformers/utils/generic.py:311: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  torch.utils._pytree._register_pytree_node(
Loading BERT configs...
Loading PyTorch model...
Constructing SUT...
Finished constructing SUT.
Constructing QSL...
Loading cached features from 'eval_features.pickle'...
Finished constructing QSL.
Running LoadGen test...
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/customize.py

  * cm run script "save mlperf inference state"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/save-mlperf-inference-implementation-state/customize.py
       ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/customize.py

* cm run script "get mlperf sut description"

  * cm run script "detect os"
         ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/e1d33efda0a04a22/cm-cached-state.json

  * cm run script "get compiler gcc"
       ! load /home/user/CM/repos/local/cache/eb35dbdd076f4add/cm-cached-state.json

  * cm run script "get cuda-devices"

    * cm run script "get cuda _toolkit"
         ! load /home/user/CM/repos/local/cache/ffa46d47191b481a/cm-cached-state.json
         ! cd /home/user/CM/repos/local/cache/12da629f8acc488f
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
rm: cannot remove 'a.out': No such file or directory

Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

Compiling program ...


Running program ...

/home/user/CM/repos/local/cache/12da629f8acc488f
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA T1000 8GB
GPU compute capability: 7.5
CUDA driver version: 12.0
CUDA runtime version: 11.5
Global memory: 8362786816
Max clock rate: 1395.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  1024
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



  * cm run script "get generic-python-lib _package.dmiparser"
       ! load /home/user/CM/repos/local/cache/00ee5663ee0248da/cm-cached-state.json
Generating SUT description file for default-pytorch-2.2.1
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py


Traceback (most recent call last):
  File "/home/user/.local/bin/cmr", line 8, in <module>
    sys.exit(run_script())
  File "/home/user/.local/lib/python3.10/site-packages/cmind/cli.py", line 76, in run_script
    return run(['run', 'script'] + argv)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/cli.py", line 35, in run
    r = cm.access(argv, out='con')
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 587, in access
    r = action_addr(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 192, in run
    r = self._run(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 1370, in _run
    r = customize_code.preprocess(ii)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/script/run-mlperf-inference-app/customize.py", line 181, in preprocess
    r = cm.access(ii)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 743, in access
    return cm.access(i)
  File "/home/user/.local/lib/python3.10/site-packages/cmind/core.py", line 587, in access
    r = action_addr(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 192, in run
    r = self._run(i)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 1448, in _run
    r = prepare_and_run_script_with_postprocessing(run_script_input)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 4271, in prepare_and_run_script_with_postprocessing
    rr = run_postprocess(customize_code, customize_common_input, recursion_spaces, env, state, const,
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/automation/script/module.py", line 4323, in run_postprocess
    r = customize_code.postprocess(ii)
  File "/home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/customize.py", line 142, in postprocess
    return {'return': 1, 'error': f'No {metric} found in performance summary. Pattern checked "{pattern[metric]}"'}
KeyError: 'target_qps'
```


### arjunsuresh · 2024-03-05

@willamloo3192 Thank you. Is there any difference if `--device=cpu` is used? I'm not sure how compatible pytorch 2.2 and CUDA runtime 11.5 are.

### willamloo3192 · 2024-03-05

@arjunsuresh I havent tried on `--device=cpu` yet. Just that right now I rerun again with the cuda by remove all cm folders.. Right now it still downloading the model.pytorch,

### willamloo3192 · 2024-03-05

@arjunsuresh by removing all cm folders and rerun all from the beginning, I can run without any issue. 
```
user@user-Alder-Lake-Client-Platform:~$ cmr "run mlperf inference generate-run-cmds _submission" --quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference --backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 --category=edge --division=open --env.CM_VERIFY_SSL=false --rerun

* cm run script "run mlperf inference generate-run-cmds _submission"

  * cm run script "detect os"
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get mlcommons inference src"
       ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

  * cm run script "get sut description"

    * cm run script "detect os"
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get python3"
         ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

    * cm run script "get compiler gcc"
         ! load /home/user/CM/repos/local/cache/e550cb6f36d84ee2/cm-cached-state.json

    * cm run script "get cuda-devices"

      * cm run script "get cuda _toolkit"
           ! load /home/user/CM/repos/local/cache/5605f72ded514343/cm-cached-state.json
           ! cd /home/user
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
rm: cannot remove 'a.out': No such file or directory

Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

Compiling program ...


Running program ...

/home/user
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA T1000 8GB
GPU compute capability: 7.5
CUDA driver version: 12.0
CUDA runtime version: 11.5
Global memory: 8362786816
Max clock rate: 1395.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  1024
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



    * cm run script "get generic-python-lib _package.dmiparser"
         ! load /home/user/CM/repos/local/cache/73ef6cd3248942ec/cm-cached-state.json
Generating SUT description file for default-pytorch
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py

  * cm run script "get mlperf inference results dir"
       ! load /home/user/CM/repos/local/cache/288644a6351e42fc/cm-cached-state.json

  * cm run script "install pip-package for-cmind-python _package.tabulate"
       ! load /home/user/CM/repos/local/cache/dac3649fc0a44dfb/cm-cached-state.json

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py
Using MLCommons Inference source from /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference

Running loadgen scenario: Offline and mode: performance

* cm run script "app mlperf inference generic _reference _bert-99 _pytorch _cuda _test _r4.0_default _offline"

  * cm run script "detect os"
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get sys-utils-cm"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get python"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get mlcommons inference src _deeplearningexamples"
       ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py

  * cm run script "get dataset squad language-processing"
       ! load /home/user/CM/repos/local/cache/bc2c4a6c1c3948ba/cm-cached-state.json

  * cm run script "get dataset-aux squad-vocab"
       ! load /home/user/CM/repos/local/cache/23408b29649e42aa/cm-cached-state.json

  * cm run script "app mlperf reference inference _pytorch _bert-99 _offline _cuda _fp32"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get sys-utils-cm"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "get python"
         ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

    * cm run script "get generic-python-lib _torch"
         ! load /home/user/CM/repos/local/cache/d8afa8b746f6418d/cm-cached-state.json

    * cm run script "get generic-python-lib _torch_cuda"
         ! load /home/user/CM/repos/local/cache/85cc6b3adc6a4b81/cm-cached-state.json

    * cm run script "get generic-python-lib _torchvision_cuda"
         ! load /home/user/CM/repos/local/cache/f098ab9cb16943ab/cm-cached-state.json

    * cm run script "get generic-python-lib _transformers"
         ! load /home/user/CM/repos/local/cache/20cf8d8cd7bd45f0/cm-cached-state.json

    * cm run script "get ml-model language-processing bert-large raw _pytorch _fp32"

      * cm run script "download-and-extract _url.https://armi.in/files/fp32/model.pytorch"

        * cm run script "download file _cmutil _url.https://armi.in/files/fp32/model.pytorch"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/794d3001557f4944
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

Downloading from https://armi.in/files/fp32/model.pytorch

Downloading to /home/user/CM/repos/local/cache/794d3001557f4944/model.pytorch

/usr/lib/python3/dist-packages/urllib3/connectionpool.py:1020: InsecureRequestWarning: Unverified HTTPS request is being made to host 'proxy-dmz.intel.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  warnings.warn(
Downloaded: 100%
               ! cd /home/user/CM/repos/local/cache/794d3001557f4944
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/download-file/run.sh from tmp-run.sh

echo 00fbcbfaebfa20d87ac9885120a6e9b4 model.pytorch | md5sum -c
model.pytorch: OK
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/download-file/customize.py
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/download-and-extract/customize.py
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-ml-model-bert-large-squad/customize.py

    * cm run script "get dataset-aux squad-vocab"
         ! load /home/user/CM/repos/local/cache/23408b29649e42aa/cm-cached-state.json

Path to the ML model: /home/user/CM/repos/local/cache/794d3001557f4944/model.pytorch

    * cm run script "get dataset squad original"
         ! load /home/user/CM/repos/local/cache/bc2c4a6c1c3948ba/cm-cached-state.json

    * cm run script "get dataset-aux squad-vocab"
         ! load /home/user/CM/repos/local/cache/23408b29649e42aa/cm-cached-state.json

    * cm run script "generate user-conf mlperf inference"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get mlcommons inference src _deeplearningexamples"
           ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

      * cm run script "get sut configs"
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py
Config file missing for given hw_name: 'default', implementation: 'reference', device: 'gpu,  backend: 'pytorch', copying from default
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference'
Output Dir: '/home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1'
bert.Offline.target_qps = 1
bert.Offline.max_query_count = 10
bert.Offline.min_query_count = 10
bert.Offline.min_duration = 0

           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py

    * cm run script "get loadgen"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get mlcommons inference src"
           ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

      * cm run script "get compiler gcc"
           ! load /home/user/CM/repos/local/cache/e550cb6f36d84ee2/cm-cached-state.json

      * cm run script "get cmake"

        * cm run script "detect cpu"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/bb8a07727e404f5b
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
               ! cd /home/user/CM/repos/local/cache/bb8a07727e404f5b
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py
        - Searching for versions:  >= 3.12

        * cm run script "install cmake prebuilt"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/42a311d612d3402a
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
            # Requested version: 3.28.3
            # Prepared package URL: https://github.com/Kitware/CMake/releases/download/v3.28.3/cmake-3.28.3-linux-x86_64.tar.gz

Downloading from https://github.com/Kitware/CMake/releases/download/v3.28.3/cmake-3.28.3-linux-x86_64.tar.gz ...
Downloading to /home/user/CM/repos/local/cache/42a311d612d3402a/cmake-3.28.3-linux-x86_64.tar.gz

Downloaded: 100%
               ! cd /home/user/CM/repos/local/cache/42a311d612d3402a
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/install-cmake-prebuilt/run.sh from tmp-run.sh

Unarchiving cmake-3.28.3-linux-x86_64.tar.gz ...
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/install-cmake-prebuilt/customize.py
             ! cd /home/user/CM/repos/local/cache/bb8a07727e404f5b
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cmake/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cmake/customize.py
          Detected version: 3.28.3

Path to the tool: /home/user/CM/repos/local/cache/42a311d612d3402a/bin/cmake

      * cm run script "get generic-python-lib _package.wheel"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

        * cm run script "detect cpu"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
               ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

        * cm run script "get python3"
             ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

        * cm run script "get generic-python-lib _pip"
             ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
                 ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
                 ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
             ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "wheel"
Collecting wheel
  Using cached wheel-0.42.0-py3-none-any.whl (65 kB)
Installing collected packages: wheel
Successfully installed wheel-0.42.0
             ! cd /home/user/CM/repos/local/cache/11a84021eaf24982
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
            Detected version: 0.42.0

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json

      * cm run script "get generic-python-lib _package.pybind11"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

        * cm run script "detect cpu"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
               ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

        * cm run script "get python3"
             ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

        * cm run script "get generic-python-lib _pip"
             ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
                 ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
                 ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
             ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "pybind11"
Collecting pybind11
  Using cached pybind11-2.11.1-py3-none-any.whl (227 kB)
Installing collected packages: pybind11
Successfully installed pybind11-2.11.1
             ! cd /home/user/CM/repos/local/cache/24a2b596445b480d
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
            Detected version: 2.11.1

      * cm run script "get generic-python-lib _package.setuptools"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/a577d15d71004958
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

        * cm run script "detect cpu"

          * cm run script "detect os"
                 ! cd /home/user/CM/repos/local/cache/a577d15d71004958
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
                 ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
               ! cd /home/user/CM/repos/local/cache/a577d15d71004958
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

        * cm run script "get python3"
             ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

        * cm run script "get generic-python-lib _pip"
             ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
                 ! cd /home/user/CM/repos/local/cache/a577d15d71004958
                 ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
                 ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
            Detected version: 59.6.0
             ! cd /home/user/CM/repos/local/cache/a577d15d71004958
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-loadgen/run.sh from tmp-run.sh
******************************************************
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
mlperf_loadgen v4.0
-- Using C++ compiler flags: -O2 -O3 -W -Wall
-- Using C++ standard: 14
-- Using static linker flags:
-- Using shared linker flags: -O2
-- Using output path: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/build
CMake Warning (dev) at CMakeLists.txt:31 (find_package):
  Policy CMP0148 is not set: The FindPythonInterp and FindPythonLibs modules
  are removed.  Run "cmake --help-policy CMP0148" for policy details.  Use
  the cmake_policy command to set the policy and suppress this warning.

This warning is for project developers.  Use -Wno-dev to suppress it.

-- Found PythonInterp: /home/user/cm/bin/python3 (found version "3.10.12")
-- Using Python interpreter: /home/user/cm/bin/python3
-- Configuring done (9.2s)
-- Generating done (0.0s)
-- Build files have been written to: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/build
******************************************************
[  7%] Building CXX object CMakeFiles/mlperf_loadgen.dir/bindings/c_api.cc.o
[ 15%] Building CXX object CMakeFiles/mlperf_loadgen.dir/early_stopping.cc.o
[ 23%] Building CXX object CMakeFiles/mlperf_loadgen.dir/issue_query_controller.cc.o
[ 30%] Building CXX object CMakeFiles/mlperf_loadgen.dir/loadgen.cc.o
[ 38%] Building CXX object CMakeFiles/mlperf_loadgen.dir/logging.cc.o
[ 46%] Building CXX object CMakeFiles/mlperf_loadgen.dir/test_settings_internal.cc.o
[ 53%] Building CXX object CMakeFiles/mlperf_loadgen.dir/utils.cc.o
[ 61%] Building CXX object CMakeFiles/mlperf_loadgen.dir/results.cc.o
[ 69%] Building CXX object CMakeFiles/mlperf_loadgen.dir/version.cc.o
[ 76%] Building CXX object CMakeFiles/mlperf_loadgen.dir/version_generated.cc.o
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc: In member function ‘void mlperf::logging::AsyncLog::RecordTokenCompletion(uint64_t, std::chrono::_V2::system_clock::time_point, mlperf::QuerySampleLatency)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc:483:61: warning: unused parameter ‘completion_time’ [-Wunused-parameter]
  483 |                                       PerfClock::time_point completion_time,
      |                                       ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc: In member function ‘std::vector<long int> mlperf::logging::AsyncLog::GetTokenLatencies(size_t)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc:601:68: warning: unused parameter ‘expected_count’ [-Wunused-parameter]
  601 | std::vector<QuerySampleLatency> AsyncLog::GetTokenLatencies(size_t expected_count) {
      |                                                             ~~~~~~~^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc: In member function ‘std::vector<long int> mlperf::logging::AsyncLog::GetTimePerOutputToken(size_t)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc:607:72: warning: unused parameter ‘expected_count’ [-Wunused-parameter]
  607 | std::vector<QuerySampleLatency> AsyncLog::GetTimePerOutputToken(size_t expected_count){
      |                                                                 ~~~~~~~^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc: In member function ‘std::vector<long int> mlperf::logging::AsyncLog::GetTokensPerSample(size_t)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/logging.cc:613:58: warning: unused parameter ‘expected_count’ [-Wunused-parameter]
  613 | std::vector<int64_t> AsyncLog::GetTokensPerSample(size_t expected_count) {
      |                                                   ~~~~~~~^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::RunPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1138:58:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  918 |   PerformanceSummary perf_summary{sut->Name(), settings, std::move(pr)};
      |                      ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1138:58:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  988 |   PerformanceSummary base_perf_summary{sut->Name(), base_settings,
      |                      ^~~~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
 1010 |     PerformanceSummary perf_summary{sut->Name(), base_settings,
      |                        ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::RunPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1140:57:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  918 |   PerformanceSummary perf_summary{sut->Name(), settings, std::move(pr)};
      |                      ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1140:57:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  988 |   PerformanceSummary base_perf_summary{sut->Name(), base_settings,
      |                      ^~~~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
 1010 |     PerformanceSummary perf_summary{sut->Name(), base_settings,
      |                        ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::RunPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1142:52:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  918 |   PerformanceSummary perf_summary{sut->Name(), settings, std::move(pr)};
      |                      ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1142:52:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  988 |   PerformanceSummary base_perf_summary{sut->Name(), base_settings,
      |                      ^~~~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
 1010 |     PerformanceSummary perf_summary{sut->Name(), base_settings,
      |                        ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::RunPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1144:53:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  918 |   PerformanceSummary perf_summary{sut->Name(), settings, std::move(pr)};
      |                      ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:918:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1144:53:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  988 |   PerformanceSummary base_perf_summary{sut->Name(), base_settings,
      |                      ^~~~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:988:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
 1010 |     PerformanceSummary perf_summary{sut->Name(), base_settings,
      |                        ^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1010:24: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘std::pair<mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary> mlperf::loadgen::FindBoundaries(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1031:31:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1138:58:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  768 |   PerformanceSummary u_perf_summary{sut->Name(), u_settings, std::move(u_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘mlperf::loadgen::PerformanceSummary mlperf::loadgen::FindPeakPerformanceBinarySearch(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, const mlperf::loadgen::LoadableSampleSet&, mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1057:78:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::SingleStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1138:58:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  820 |   PerformanceSummary m_perf_summary{sut->Name(), m_settings, std::move(m_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘std::pair<mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary> mlperf::loadgen::FindBoundaries(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1031:31:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1140:57:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  768 |   PerformanceSummary u_perf_summary{sut->Name(), u_settings, std::move(u_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘mlperf::loadgen::PerformanceSummary mlperf::loadgen::FindPeakPerformanceBinarySearch(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, const mlperf::loadgen::LoadableSampleSet&, mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1057:78:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::MultiStream]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1140:57:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  820 |   PerformanceSummary m_perf_summary{sut->Name(), m_settings, std::move(m_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘std::pair<mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary> mlperf::loadgen::FindBoundaries(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1031:31:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1142:52:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  768 |   PerformanceSummary u_perf_summary{sut->Name(), u_settings, std::move(u_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘mlperf::loadgen::PerformanceSummary mlperf::loadgen::FindPeakPerformanceBinarySearch(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, const mlperf::loadgen::LoadableSampleSet&, mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1057:78:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Server]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1142:52:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  820 |   PerformanceSummary m_perf_summary{sut->Name(), m_settings, std::move(m_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘std::pair<mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary> mlperf::loadgen::FindBoundaries(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1031:31:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1144:53:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  768 |   PerformanceSummary u_perf_summary{sut->Name(), u_settings, std::move(u_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:768:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘mlperf::loadgen::PerformanceSummary mlperf::loadgen::FindPeakPerformanceBinarySearch(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, mlperf::loadgen::SequenceGen*, const mlperf::loadgen::LoadableSampleSet&, mlperf::loadgen::PerformanceSummary, mlperf::loadgen::PerformanceSummary) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1057:78:   required from ‘void mlperf::loadgen::FindPeakPerformanceMode(mlperf::SystemUnderTest*, mlperf::QuerySampleLibrary*, const mlperf::loadgen::TestSettingsInternal&, mlperf::loadgen::SequenceGen*) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1132:61:   required from ‘static mlperf::loadgen::RunFunctions mlperf::loadgen::RunFunctions::GetCompileTime() [with mlperf::TestScenario compile_time_scenario = mlperf::TestScenario::Offline]’
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:1144:53:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
  820 |   PerformanceSummary m_perf_summary{sut->Name(), m_settings, std::move(m_pr)};
      |                      ^~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::first_token_latency_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_min’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_max’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:820:22: warning: missing initializer for member ‘mlperf::loadgen::PerformanceSummary::time_per_output_token_mean’ [-Wmissing-field-initializers]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline; mlperf::TestMode mode = mlperf::TestMode::PerformanceOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
  137 |                       const ResponseCallback& response_cb) override {
      |                       ~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::Offline; mlperf::TestMode mode = mlperf::TestMode::AccuracyOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server; mlperf::TestMode mode = mlperf::TestMode::PerformanceOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::Server; mlperf::TestMode mode = mlperf::TestMode::AccuracyOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream; mlperf::TestMode mode = mlperf::TestMode::PerformanceOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::MultiStream; mlperf::TestMode mode = mlperf::TestMode::AccuracyOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream; mlperf::TestMode mode = mlperf::TestMode::PerformanceOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc: In instantiation of ‘void mlperf::loadgen::ResponseDelegateDetailed<scenario, mode>::TokenComplete(mlperf::loadgen::SampleMetadata*, mlperf::QuerySampleResponse*, std::chrono::_V2::system_clock::time_point, const ResponseCallback&) [with mlperf::TestScenario scenario = mlperf::TestScenario::SingleStream; mlperf::TestMode mode = mlperf::TestMode::AccuracyOnly; std::chrono::_V2::system_clock::time_point = std::chrono::time_point<std::chrono::_V2::system_clock, std::chrono::duration<long int, std::ratio<1, 1000000000> > >; mlperf::ResponseCallback = std::function<void(mlperf::QuerySampleResponse*)>]’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:135:10:   required from here
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/loadgen.cc:137:47: warning: unused parameter ‘response_cb’ [-Wunused-parameter]
[ 84%] Linking CXX static library libmlperf_loadgen.a
[ 84%] Built target mlperf_loadgen
[ 92%] Building CXX object CMakeFiles/benchmark.dir/benchmark/repro.cpp.o
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp: In member function ‘virtual void QSL::LoadSamplesToRam(const std::vector<long unsigned int>&)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp:37:52: warning: unused parameter ‘samples’ [-Wunused-parameter]
   37 |       const std::vector<mlperf::QuerySampleIndex>& samples) override {}
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp: In member function ‘virtual void QSL::UnloadSamplesFromRam(const std::vector<long unsigned int>&)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp:39:52: warning: unused parameter ‘samples’ [-Wunused-parameter]
   39 |       const std::vector<mlperf::QuerySampleIndex>& samples) override {}
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp: In member function ‘virtual void BasicSUT::IssueQuery(const std::vector<mlperf::QuerySample>&)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp:55:11: warning: comparison of integer expressions of different signedness: ‘int’ and ‘std::vector<mlperf::QuerySampleResponse>::size_type’ {aka ‘long unsigned int’} [-Wsign-compare]
   55 |     if (n > mResponses.size()) {
      |         ~~^~~~~~~~~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp: In member function ‘void QueueSUT::CompleteThread(int)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp:125:27: warning: comparison of integer expressions of different signedness: ‘int’ and ‘size_t’ {aka ‘long unsigned int’} [-Wsign-compare]
  125 |         for (int i = 0; i < actualSize; i++) {
      |                         ~~^~~~~~~~~~~~
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp: In member function ‘virtual void MultiBasicSUT::IssueQuery(const std::vector<mlperf::QuerySample>&)’:
/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/loadgen/benchmark/repro.cpp:171:11: warning: comparison of integer expressions of different signedness: ‘int’ and ‘std::vector<mlperf::QuerySampleResponse>::size_type’ {aka ‘long unsigned int’} [-Wsign-compare]
  171 |     if (n > reponses.size()) {
      |         ~~^~~~~~~~~~~~~~~~~
[100%] Linking CXX executable benchmark
[100%] Built target benchmark
Install the project...
-- Install configuration: ""
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/lib/libmlperf_loadgen.a
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/early_stopping.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/demos
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/demos/token_metrics
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/demos/lon
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/version.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/issue_query_controller.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/query_sample.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/docs
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/docs/src
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/logging.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/tests
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/tests/loadgen_test.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/benchmark
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/query_sample_library.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/system_under_test.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/tools
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/query_dispatch_library.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/bindings
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/bindings/c_api.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/test_settings_internal.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/loadgen.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/results.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/test_settings.h
-- Installing: /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install/include/utils.h
running bdist_wheel
running build
running build_ext
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/home/user/cm/include -I/usr/include/python3.10 -c flagcheck.cpp -o flagcheck.o -std=c++17
building 'mlperf_loadgen' extension
creating build
creating build/temp.linux-x86_64-3.10
creating build/temp.linux-x86_64-3.10/bindings
creating build/temp.linux-x86_64-3.10/generated
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c bindings/python_api.cc -o build/temp.linux-x86_64-3.10/bindings/python_api.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c early_stopping.cc -o build/temp.linux-x86_64-3.10/early_stopping.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c generated/version_generated.cc -o build/temp.linux-x86_64-3.10/generated/version_generated.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c issue_query_controller.cc -o build/temp.linux-x86_64-3.10/issue_query_controller.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c loadgen.cc -o build/temp.linux-x86_64-3.10/loadgen.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c logging.cc -o build/temp.linux-x86_64-3.10/logging.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c results.cc -o build/temp.linux-x86_64-3.10/results.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c test_settings_internal.cc -o build/temp.linux-x86_64-3.10/test_settings_internal.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c utils.cc -o build/temp.linux-x86_64-3.10/utils.o -std=c++17 -fvisibility=hidden -g0
x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DMAJOR_VERSION=4 -DMINOR_VERSION=0 -I. -I/home/user/cm/lib/python3.10/site-packages/pybind11/include -I/home/user/cm/include -I/usr/include/python3.10 -c version.cc -o build/temp.linux-x86_64-3.10/version.o -std=c++17 -fvisibility=hidden -g0
creating build/lib.linux-x86_64-3.10
x86_64-linux-gnu-g++ -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -g -fwrapv -O2 -O2 -std=c++14 -O3 -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.10/bindings/python_api.o build/temp.linux-x86_64-3.10/early_stopping.o build/temp.linux-x86_64-3.10/generated/version_generated.o build/temp.linux-x86_64-3.10/issue_query_controller.o build/temp.linux-x86_64-3.10/loadgen.o build/temp.linux-x86_64-3.10/logging.o build/temp.linux-x86_64-3.10/results.o build/temp.linux-x86_64-3.10/test_settings_internal.o build/temp.linux-x86_64-3.10/utils.o build/temp.linux-x86_64-3.10/version.o -o build/lib.linux-x86_64-3.10/mlperf_loadgen.cpython-310-x86_64-linux-gnu.so
/home/user/cm/lib/python3.10/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
copying build/lib.linux-x86_64-3.10/mlperf_loadgen.cpython-310-x86_64-linux-gnu.so -> build/bdist.linux-x86_64/wheel
running install_egg_info
running egg_info
creating mlperf_loadgen.egg-info
writing mlperf_loadgen.egg-info/PKG-INFO
writing dependency_links to mlperf_loadgen.egg-info/dependency_links.txt
writing top-level names to mlperf_loadgen.egg-info/top_level.txt
writing manifest file 'mlperf_loadgen.egg-info/SOURCES.txt'
reading manifest file 'mlperf_loadgen.egg-info/SOURCES.txt'
writing manifest file 'mlperf_loadgen.egg-info/SOURCES.txt'
Copying mlperf_loadgen.egg-info to build/bdist.linux-x86_64/wheel/mlperf_loadgen-4.0.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/mlperf_loadgen-4.0.dist-info/WHEEL
creating 'dist/mlperf_loadgen-4.0-cp310-cp310-linux_x86_64.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'mlperf_loadgen.cpython-310-x86_64-linux-gnu.so'
adding 'mlperf_loadgen-4.0.dist-info/METADATA'
adding 'mlperf_loadgen-4.0.dist-info/WHEEL'
adding 'mlperf_loadgen-4.0.dist-info/top_level.txt'
adding 'mlperf_loadgen-4.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
Processing ./dist/mlperf_loadgen-4.0-cp310-cp310-linux_x86_64.whl
Installing collected packages: mlperf-loadgen
Successfully installed mlperf-loadgen-4.0
******************************************************
Loadgen is built and installed to /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/install ...
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-loadgen/customize.py

    * cm run script "get mlcommons inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

    * cm run script "get mlcommons inference src"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

    * cm run script "get generic-python-lib _package.psutil"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
               ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "psutil"
Collecting psutil
  Using cached psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (288 kB)
Installing collected packages: psutil
Successfully installed psutil-5.9.8
           ! cd /home/user/CM/repos/local/cache/69cc7c700c404bb1
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 5.9.8

    * cm run script "get generic-python-lib _package.pydantic"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
      - Searching for versions:  <= 1.10.9
               ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "pydantic<=1.10.9"
Collecting pydantic<=1.10.9
  Using cached pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Requirement already satisfied: typing-extensions>=4.2.0 in /home/user/cm/lib/python3.10/site-packages (from pydantic<=1.10.9) (4.10.0)
Installing collected packages: pydantic
Successfully installed pydantic-1.10.9
           ! cd /home/user/CM/repos/local/cache/d0450bb9d029483c
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 1.10.9

    * cm run script "get generic-python-lib _tokenization"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
               ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "tokenization"
Collecting tokenization
  Using cached tokenization-1.0.7-py3-none-any.whl (10 kB)
Requirement already satisfied: regex in /home/user/cm/lib/python3.10/site-packages (from tokenization) (2023.12.25)
Installing collected packages: tokenization
Successfully installed tokenization-1.0.7
           ! cd /home/user/CM/repos/local/cache/e3ba52b3aab64fda
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 1.0.7

    * cm run script "get generic-python-lib _six"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
               ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "six"
Collecting six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six
Successfully installed six-1.16.0
           ! cd /home/user/CM/repos/local/cache/65373278f11e4f8b
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 1.16.0

    * cm run script "get generic-python-lib _package.absl-py"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
               ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "absl-py"
Collecting absl-py
  Using cached absl_py-2.1.0-py3-none-any.whl (133 kB)
Installing collected packages: absl-py
Successfully installed absl-py-2.1.0
           ! cd /home/user/CM/repos/local/cache/dd079bf5797a485f
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 2.1.0

    * cm run script "get generic-python-lib _boto3"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
               ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
           ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh
/home/user/cm/bin/python3 -m pip install "boto3"
Collecting boto3
  Using cached boto3-1.34.55-py3-none-any.whl (139 kB)
Collecting botocore<1.35.0,>=1.34.55
  Using cached botocore-1.34.55-py3-none-any.whl (12.0 MB)
Collecting jmespath<2.0.0,>=0.7.1
  Using cached jmespath-1.0.1-py3-none-any.whl (20 kB)
Collecting s3transfer<0.11.0,>=0.10.0
  Using cached s3transfer-0.10.0-py3-none-any.whl (82 kB)
Collecting urllib3<2.1,>=1.25.4
  Using cached urllib3-2.0.7-py3-none-any.whl (124 kB)
Collecting python-dateutil<3.0.0,>=2.1
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Requirement already satisfied: six>=1.5 in /home/user/cm/lib/python3.10/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.35.0,>=1.34.55->boto3) (1.16.0)
Installing collected packages: urllib3, python-dateutil, jmespath, botocore, s3transfer, boto3
  Attempting uninstall: urllib3
    Found existing installation: urllib3 2.2.1
    Uninstalling urllib3-2.2.1:
      Successfully uninstalled urllib3-2.2.1
Successfully installed boto3-1.34.55 botocore-1.34.55 jmespath-1.0.1 python-dateutil-2.9.0.post0 s3transfer-0.10.0 urllib3-2.0.7
           ! cd /home/user/CM/repos/local/cache/827165fbd6d248db
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
          Detected version: 1.34.55
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference'
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference-reference/customize.py

  * cm run script "benchmark-mlperf"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program-mlperf/customize.py

  * cm run script "benchmark-program program"

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py
***************************************************************************
CM script::benchmark-program/run.sh

Run Directory: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/language/bert

CMD: /home/user/cm/bin/python3 run.py --backend=pytorch --scenario=Offline   --mlperf_conf '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf' --user_conf '/home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/1eeee988a63342cead7818a2b8dae9a3.conf' 2>&1 | tee /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1/console.out

         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/run-ubuntu.sh from tmp-run.sh
================================================
MLPerf Results Summary
================================================
SUT name : PySUT
Scenario : Offline
Mode     : PerformanceOnly
Samples per second: 3.7052
Result is : VALID
  Min duration satisfied : Yes
  Min queries satisfied : Yes
  Early stopping satisfied: Yes

================================================
Additional Stats
================================================
Min latency (ns)                : 1243699357
Max latency (ns)                : 2698910555
Mean latency (ns)               : 1970115780
50.00 percentile latency (ns)   : 2051145745
90.00 percentile latency (ns)   : 2698910555
95.00 percentile latency (ns)   : 2698910555
97.00 percentile latency (ns)   : 2698910555
99.00 percentile latency (ns)   : 2698910555
99.90 percentile latency (ns)   : 2698910555

================================================
Test Parameters Used
================================================
samples_per_query : 10
target_qps : 1
target_latency (ns): 0
max_async_queries : 1
min_duration (ms): 0
max_duration (ms): 0
min_query_count : 1
max_query_count : 10
qsl_rng_seed : 13281865557512327830
sample_index_rng_seed : 198141574272810017
schedule_rng_seed : 7575108116881280410
accuracy_log_rng_seed : 0
accuracy_log_probability : 0
accuracy_log_sampling_target : 0
print_timestamps : 0
performance_issue_unique : 0
performance_issue_same : 0
performance_issue_same_index : 0
performance_sample_count : 10833

No warnings encountered during test.

No errors encountered during test.
Loading BERT configs...
Loading PyTorch model...
Constructing SUT...
Finished constructing SUT.
Constructing QSL...
No cached features at 'eval_features.pickle'... converting from examples...
Creating tokenizer...
Reading examples...
Converting examples to features...
Caching features at 'eval_features.pickle'...
Finished constructing QSL.
Running LoadGen test...
Done!
Destroying SUT...
Destroying QSL...
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/customize.py

  * cm run script "save mlperf inference state"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/save-mlperf-inference-implementation-state/customize.py
       ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/customize.py

* cm run script "get mlperf sut description"

  * cm run script "detect os"
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get compiler gcc"
       ! load /home/user/CM/repos/local/cache/e550cb6f36d84ee2/cm-cached-state.json

  * cm run script "get cuda-devices"

    * cm run script "get cuda _toolkit"
         ! load /home/user/CM/repos/local/cache/5605f72ded514343/cm-cached-state.json
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
rm: cannot remove 'a.out': No such file or directory

Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

Compiling program ...


Running program ...

/home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA T1000 8GB
GPU compute capability: 7.5
CUDA driver version: 12.0
CUDA runtime version: 11.5
Global memory: 8362786816
Max clock rate: 1395.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  1024
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



  * cm run script "get generic-python-lib _package.dmiparser"
       ! load /home/user/CM/repos/local/cache/73ef6cd3248942ec/cm-cached-state.json
Generating SUT description file for default-pytorch-2.2.1
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py


SUT: default-reference-gpu-pytorch-v2.2.1-default_config, model: bert-99, scenario: Offline, target_qps updated as 3.7052
New config stored in /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-configs/configs/default/reference-implementation/gpu-device/pytorch-framework/framework-version-v2.2.1/default_config-config.yaml
[2024-03-06 00:49:33,876 log_parser.py:50 INFO] Sucessfully loaded MLPerf log from /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1/mlperf_log_detail.txt.
[2024-03-06 00:49:33,876 log_parser.py:50 INFO] Sucessfully loaded MLPerf log from /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1/mlperf_log_detail.txt.

* cm run script "detect os"
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

* cm run script "detect cpu"

  * cm run script "detect os"
         ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

* cm run script "dump pip freeze"

  * cm run script "get python"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/performance/run_1
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/run.sh from tmp-run.sh
Running:
/home/user/cm/bin/python3 /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/dump.py

       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/customize.py

Running loadgen scenario: Offline and mode: accuracy

* cm run script "app mlperf inference generic _reference _bert-99 _pytorch _cuda _test _r4.0_default _offline"

  * cm run script "detect os"
         ! cd /home/user
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get sys-utils-cm"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get python"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get mlcommons inference src _deeplearningexamples"
       ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py

  * cm run script "get dataset squad language-processing"
       ! load /home/user/CM/repos/local/cache/bc2c4a6c1c3948ba/cm-cached-state.json

  * cm run script "get dataset-aux squad-vocab"
       ! load /home/user/CM/repos/local/cache/23408b29649e42aa/cm-cached-state.json

  * cm run script "app mlperf reference inference _pytorch _bert-99 _offline _cuda _fp32"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get sys-utils-cm"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "get python"
         ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

    * cm run script "get generic-python-lib _torch"
         ! load /home/user/CM/repos/local/cache/d8afa8b746f6418d/cm-cached-state.json

    * cm run script "get generic-python-lib _torch_cuda"
         ! load /home/user/CM/repos/local/cache/85cc6b3adc6a4b81/cm-cached-state.json

    * cm run script "get generic-python-lib _torchvision_cuda"
         ! load /home/user/CM/repos/local/cache/f098ab9cb16943ab/cm-cached-state.json

    * cm run script "get generic-python-lib _transformers"
         ! load /home/user/CM/repos/local/cache/20cf8d8cd7bd45f0/cm-cached-state.json

    * cm run script "get ml-model language-processing bert-large raw _pytorch _fp32"
         ! load /home/user/CM/repos/local/cache/b5d8c1ac353d4338/cm-cached-state.json

Path to the ML model: /home/user/CM/repos/local/cache/794d3001557f4944/model.pytorch

    * cm run script "get dataset squad original"
         ! load /home/user/CM/repos/local/cache/bc2c4a6c1c3948ba/cm-cached-state.json

    * cm run script "get dataset-aux squad-vocab"
         ! load /home/user/CM/repos/local/cache/23408b29649e42aa/cm-cached-state.json

    * cm run script "generate user-conf mlperf inference"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
               ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python"
           ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

      * cm run script "get mlcommons inference src _deeplearningexamples"
           ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

      * cm run script "get sut configs"
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-configs/customize.py
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference'
Output Dir: '/home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy'
bert.Offline.target_qps = 1
bert.Offline.max_query_count = 10
bert.Offline.min_query_count = 10
bert.Offline.min_duration = 0

           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py

    * cm run script "get loadgen"
         ! load /home/user/CM/repos/local/cache/1c510f3ae9cb4cf2/cm-cached-state.json

    * cm run script "get mlcommons inference src _deeplearningexamples"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

    * cm run script "get mlcommons inference src"
         ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

    * cm run script "get generic-python-lib _package.psutil"
         ! load /home/user/CM/repos/local/cache/69cc7c700c404bb1/cm-cached-state.json

    * cm run script "get generic-python-lib _package.pydantic"
         ! load /home/user/CM/repos/local/cache/d0450bb9d029483c/cm-cached-state.json

    * cm run script "get generic-python-lib _tokenization"
         ! load /home/user/CM/repos/local/cache/e3ba52b3aab64fda/cm-cached-state.json

    * cm run script "get generic-python-lib _six"
         ! load /home/user/CM/repos/local/cache/65373278f11e4f8b/cm-cached-state.json

    * cm run script "get generic-python-lib _package.absl-py"
         ! load /home/user/CM/repos/local/cache/dd079bf5797a485f/cm-cached-state.json

    * cm run script "get generic-python-lib _boto3"
         ! load /home/user/CM/repos/local/cache/827165fbd6d248db/cm-cached-state.json
Using MLCommons Inference source from '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference'
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference-reference/customize.py

  * cm run script "benchmark-mlperf"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program-mlperf/customize.py

  * cm run script "benchmark-program program"

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py
***************************************************************************
CM script::benchmark-program/run.sh

Run Directory: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/language/bert

CMD: /home/user/cm/bin/python3 run.py --backend=pytorch --scenario=Offline   --max_examples 10 --mlperf_conf '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf' --user_conf '/home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/43a8ad48974b4b2daf46c30504ab61fd.conf' --accuracy 2>&1 | tee /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/console.out

         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/run-ubuntu.sh from tmp-run.sh

No warnings encountered during test.

No errors encountered during test.
Loading BERT configs...
Loading PyTorch model...
Constructing SUT...
Finished constructing SUT.
Constructing QSL...
Loading cached features from 'eval_features.pickle'...
Finished constructing QSL.
Running LoadGen test...
Done!
Destroying SUT...
Destroying QSL...
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/benchmark-program/customize.py

  * cm run script "save mlperf inference state"
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/save-mlperf-inference-implementation-state/customize.py
       ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/app-mlperf-inference/customize.py

* cm run script "get mlperf sut description"

  * cm run script "detect os"
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get compiler gcc"
       ! load /home/user/CM/repos/local/cache/e550cb6f36d84ee2/cm-cached-state.json

  * cm run script "get cuda-devices"

    * cm run script "get cuda _toolkit"
         ! load /home/user/CM/repos/local/cache/5605f72ded514343/cm-cached-state.json
         ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
rm: cannot remove 'a.out': No such file or directory

Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0

Compiling program ...


Running program ...

/home/user/CM/repos/local/cache/0d16ec40ce1f4543
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA T1000 8GB
GPU compute capability: 7.5
CUDA driver version: 12.0
CUDA runtime version: 11.5
Global memory: 8362786816
Max clock rate: 1395.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  1024
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



  * cm run script "get generic-python-lib _package.dmiparser"
       ! load /home/user/CM/repos/local/cache/73ef6cd3248942ec/cm-cached-state.json
Generating SUT description file for default-pytorch-2.2.1
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-sut-description/customize.py

* cm run script "run accuracy mlperf _squad _float32"

  * cm run script "get python3"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

  * cm run script "get mlcommons inference src _deeplearningexamples"
       ! load /home/user/CM/repos/local/cache/670a612255374426/cm-cached-state.json

Path to MLPerf inference benchmark sources: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference
Path to the MLPerf inference benchmark configuration file: /home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/mlperf.conf

  * cm run script "get generic-python-lib _boto3"
       ! load /home/user/CM/repos/local/cache/827165fbd6d248db/cm-cached-state.json

  * cm run script "get generic-python-lib _package.transformers"

    * cm run script "detect os"
           ! cd /home/user/CM/repos/local/cache/90c7cb92062d4848
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /home/user/CM/repos/local/cache/90c7cb92062d4848
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /home/user/CM/repos/local/cache/90c7cb92062d4848
           ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get python3"
         ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json

    * cm run script "get generic-python-lib _pip"
         ! load /home/user/CM/repos/local/cache/ebeefcc94d6149e2/cm-cached-state.json
             ! cd /home/user/CM/repos/local/cache/90c7cb92062d4848
             ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
             ! call "detect_version" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py
        Detected version: 4.38.2
         ! cd /home/user/CM/repos/local/cache/90c7cb92062d4848
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py

  * cm run script "get dataset squad language-processing"
       ! load /home/user/CM/repos/local/cache/bc2c4a6c1c3948ba/cm-cached-state.json

  * cm run script "get generic-python-lib _torch"
       ! load /home/user/CM/repos/local/cache/d8afa8b746f6418d/cm-cached-state.json

  * cm run script "get generic-python-lib _tokenization"
       ! load /home/user/CM/repos/local/cache/e3ba52b3aab64fda/cm-cached-state.json
       ! cd /home/user/CM/repos/local/cache/0d16ec40ce1f4543
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/process-mlperf-accuracy/run.sh from tmp-run.sh
/home/user/cm/bin/python3 '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/language/bert/accuracy-squad.py' --val_data '/home/user/CM/repos/local/cache/0d16ec40ce1f4543/dev-v1.1.json' --log_file '/home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/mlperf_log_accuracy.json' --vocab_file '/home/user/CM/repos/local/cache/23408b29649e42aa/vocab.txt' --out_file '/home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/predictions.json' --features_cache_file '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/language/bert/eval_features.pickle' --output_dtype float32 --max_examples 10 > '/home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/accuracy.txt'
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/process-mlperf-accuracy/customize.py

Accuracy file: /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/accuracy.txt

{"exact_match": 0.0, "f1": 0.0}
Reading examples...
Loading cached features from '/home/user/CM/repos/local/cache/9d8b603a33934bb7/inference/language/bert/eval_features.pickle'...
Loading LoadGen logs...
Post-processing predictions...
Writing predictions to: /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/predictions.json
Evaluating predictions...



* cm run script "detect os"
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

* cm run script "detect cpu"

  * cm run script "detect os"
         ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy
         ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

* cm run script "dump pip freeze"

  * cm run script "get python"
       ! load /home/user/CM/repos/local/cache/f3407d0c7df14fdc/cm-cached-state.json
       ! cd /home/user/CM/repos/local/cache/288644a6351e42fc/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy
       ! call /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/run.sh from tmp-run.sh
Running:
/home/user/cm/bin/python3 /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/dump.py

       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/dump-pip-freeze/customize.py
default-reference-gpu-pytorch-v2.2.1-default_config
+---------+----------+----------+-------+-----------------+---------------------------------+
|  Model  | Scenario | Accuracy |  QPS  | Latency (in ms) | Power Efficiency (in samples/J) |
+---------+----------+----------+-------+-----------------+---------------------------------+
| bert-99 | Offline  |  X 0.0   | 3.705 |        -        |                                 |
+---------+----------+----------+-------+-----------------+---------------------------------+

The MLPerf inference results are stored at /home/user/CM/repos/local/cache/288644a6351e42fc/test_results

       ! call "postprocess" from /home/user/CM/repos/mlcommons@ck/cm-mlops/script/run-mlperf-inference-app/customize.py

```

### willamloo3192 · 2024-03-05

Before closing this ticket, I would like to ask how can we obtain the f1_score out of the command stated above? 


### arjunsuresh · 2024-03-05

Accuracy is the f1 score here. But there's some issue with the accuracy run as the expected f1 score for first 10 samples is 70%. 

Also, you can do `cm pull repo mlcommons@ck` and do a rerun as I believe the current run happened on CPU even though `--device=cuda` is given. 

### willamloo3192 · 2024-03-05

Via CPU, the QPS reading around 1.0
If the accuracy reading issue able to resolve on Nvidia, Intel and AMD GPUs, that would be perfect.
Besides that, do MLPerf supports Intel and AMD GPUs? Anything setup do we need to follow before we can perform those benchmarking?   

### arjunsuresh · 2024-03-05

I just tried this command on Nvidia 4090
```
 cmr "run mlperf inference generate-run-cmds _submission" --quiet --submitter="MLCommons" --hw_name=default --model=bert-99 --implementation=reference --backend=pytorch --device=cuda --scenario=Offline --adr.compiler.tags=gcc  --target_qps=1 --category=edge --division=open --env.CM_VERIFY_SSL=false --rerun  --test_query_count=200
 ```
This is the result
```
+---------+----------+----------+--------+-----------------+---------------------------------+
|  Model  | Scenario | Accuracy |  QPS   | Latency (in ms) | Power Efficiency (in samples/J) |
+---------+----------+----------+--------+-----------------+---------------------------------+
| bert-99 | Offline  |  X 70.0  | 76.819 |        -        |                                 |
+---------+----------+----------+--------+-----------------+---------------------------------+
```
MLPerf inference should run on AMD GPUs - you can just change `--device=rocm` in the command. But this was last tested on rocm 5.6 and due to the unavailability of the device we couldn't test any later versions. 

### willamloo3192 · 2024-03-06

Noted. I will try on that. The accuracy reading shows up due to the latest updates of the CM?

### willamloo3192 · 2024-03-06

I tested on Nvidia T1000 with the latest version of CM + the command you provided, unfortunately here is the outcome with the accuracy=0
```
+---------+----------+----------+-------+-----------------+---------------------------------+
|  Model  | Scenario | Accuracy |  QPS  | Latency (in ms) | Power Efficiency (in samples/J) |
+---------+----------+----------+-------+-----------------+---------------------------------+
| bert-99 | Offline  |  X 0.0   | 5.926 |        -        |                                 |
+---------+----------+----------+-------+-----------------+---------------------------------+
```


### willamloo3192 · 2024-03-06

After I remove and reclone CM, I managed to get the accuracy, just that the accuracy level is pretty low. 

```
+---------+----------+-----------+-------+-----------------+---------------------------------+
|  Model  | Scenario | Accuracy  |  QPS  | Latency (in ms) | Power Efficiency (in samples/J) |
+---------+----------+-----------+-------+-----------------+---------------------------------+
| bert-99 | Offline  | X 1.91154 | 5.946 |        -        |                                 |
+---------+----------+-----------+-------+-----------------+---------------------------------+
```


### msidd · 2024-03-27

i am getting very similar error when running following command . i am attaching the whole error log file 
[error.txt](https://github.com/mlcommons/inference/files/14781278/error.txt)


`cm run script --tags=run-mlperf,inference,_r3.1,_performance-only,_full  \
   --division=closed \
   --category=datacenter \
   --device=cpu \
   --model=bert-99 \
   --precision=float32 \
   --implementation=mlcommons-python \
   --backend=pytorch \
   --scenario=Server \
   --execution_mode=valid \
   --power=no \
   --adr.python.version_min=3.8 \
   --clean \
   --compliance=yes \
   --quiet \
   --time`

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
