# [Issue #1679] Provide support to install nvmitten from github

source: https://github.com/mlcommons/inference/issues/1679
state: closed | updated: 2026-05-05T00:38:28Z
labels: Stale

## 正文

I'm trying to run some benchmarks on a shared grace-hopper system with ARM architecture. I cannot use `docker` without `sudo` access. so I'm using singularity with the nvidia pytorch container. It seems that `nvmitten` wheels in `pip` is only supported for `x86`, so pip install fails.

Here are the commands I run:
```sh
$ apptainer run --nv pytorch-24.03-py3.sif
Apptainer> pip install cmind --user
Apptainer> export PATH=$PATH:$PYTHONUSERBASE/bin
Apptainer> cm pull repo mlcommon@ck
Apptainer> pip install transformers onnxruntime --user

Apptainer> cmr "run-mlperf inference _find-performance" --scenario=Offline --model=bert-99 --implementation=nvidia-original --device=cuda --backend=tensorrt --category=edge --division=open --quiet
```

And the output (I've replaced the actual path with myPath for privacy):

<details><summary>Click to expand</summary>

```sh
Checking compiler version ...

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Tue_Feb_27_16:20:28_PST_2024
Cuda compilation tools, release 12.4, V12.4.99
Build cuda_12.4.r12.4/compiler.33961263_0

Compiling program ...


Running program ...

/myPath/myProjects/gracehopper_eval/test_bert-99

/usr/bin/python3 -m pip install "/opt/nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl" --break-system-packages
Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com

* cm run script "run-mlperf inference _find-performance"

  * cm run script "detect os"
         ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
         ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "detect cpu"

    * cm run script "detect os"
           ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
           ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
         ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
         ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

  * cm run script "get python3"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/953112086af047b0/cm-cached-state.json

  * cm run script "get mlcommons inference src"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference

  * cm run script "get sut description"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4eb1e378486848b2/cm-cached-state.json

  * cm run script "install pip-package for-cmind-python _package.tabulate"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/68530b531ada4e67/cm-cached-state.json

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py
Using MLCommons Inference source from /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference

Running loadgen scenario: Offline and mode: performance

* cm run script "app mlperf inference generic _nvidia-original _bert-99 _tensorrt _cuda _test _offline"

  * cm run script "detect os"
         ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
         ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

  * cm run script "get sys-utils-cm"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/ceaa6a880d174aef/cm-cached-state.json

  * cm run script "get python"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/953112086af047b0/cm-cached-state.json

  * cm run script "get mlcommons inference src _deeplearningexamples"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference

  * cm run script "get mlperf inference utils"

    * cm run script "get mlperf inference src _deeplearningexamples"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-mlperf-inference-utils/customize.py

  * cm run script "get cuda-devices"

    * cm run script "get cuda _toolkit"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/fd3145f7d34d47a5/cm-cached-state.json
         ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
         ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/run.sh from tmp-run.sh
         ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-cuda-devices/customize.py
GPU Device ID: 0
GPU Name: NVIDIA GH200 480GB MIG 2g.24gb
GPU compute capability: 9.0
CUDA driver version: 12.4
CUDA runtime version: 12.4
Global memory: 24696061952
Max clock rate: 1980.000000 MHz
Total amount of shared memory per block: 49152
Total number of registers available per block: 65536
Warp size: 32
Maximum number of threads per multiprocessor:  2048
Maximum number of threads per block: 1024
Max dimension size of a thread block X: 1024
Max dimension size of a thread block Y: 1024
Max dimension size of a thread block Z: 64
Max dimension size of a grid size X: 2147483647
Max dimension size of a grid size Y: 65535
Max dimension size of a grid size Z: 65535



  * cm run script "get dataset squad language-processing"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/828df9f23e454669/cm-cached-state.json

  * cm run script "get dataset-aux squad-vocab"
       ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/864cf309fc784629/cm-cached-state.json

  * cm run script "reproduce mlperf nvidia inference _run_harness _bert-99 _offline _tensorrt _cuda _gpu_memory.24"

    * cm run script "detect os"
           ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
           ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
           ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

    * cm run script "detect cpu"

      * cm run script "detect os"
             ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
             ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
           ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
           ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
           ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

    * cm run script "get sys-utils-cm"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/ceaa6a880d174aef/cm-cached-state.json

    * cm run script "get mlperf inference nvidia scratch space"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8345dc5ed628489c/cm-cached-state.json

    * cm run script "get generic-python-lib _mlperf_logging"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/68c33cfd92fa45cd/cm-cached-state.json

    * cm run script "get ml-model bert _onnx _fp32"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/2eb45862c1af421d/cm-cached-state.json

Path to the ML model: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/c38c8b9d32834984/model.onnx

    * cm run script "get ml-model bert _onnx _int8"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b51f6bf2be145a2/cm-cached-state.json

Path to the ML model: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/e2e8968b2c694e78/bert_large_v1_1_fake_quant.onnx

    * cm run script "get squad-vocab"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/864cf309fc784629/cm-cached-state.json

    * cm run script "get mlcommons inference src _deeplearningexamples"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference

    * cm run script "get nvidia mlperf inference common-code"
         ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/e19ee3c61b6848eb/cm-cached-state.json

    * cm run script "generate user-conf mlperf inference"

      * cm run script "detect os"
             ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
             ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
               ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /myPath/myProjects/gracehopper_eval/test_bert-99
             ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python"
           ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/953112086af047b0/cm-cached-state.json

      * cm run script "get mlcommons inference src _deeplearningexamples"
           ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/10a0714d776b46d0/cm-cached-state.json

Path to the MLPerf inference benchmark configuration file: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference/mlperf.conf
Path to MLPerf inference benchmark sources: /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference

      * cm run script "get sut configs"
           ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/ed5215bc82df458c/cm-cached-state.json
Using MLCommons Inference source from '/myPath/myProjects/gracehopper_eval/CM/repos/local/cache/8b5a28e2854140cb/inference'
Original configuration value 1.0 target_qps
Adjusted configuration value 1.01 target_qps
Output Dir: '/myPath/myProjects/gracehopper_eval/test_bert-99/test_results/default-nvidia_original-gpu-tensorrt-vdefault-default_config/bert-99/offline/performance/run_1'
bert.Offline.target_qps = 1
bert.Offline.max_query_count = 10
bert.Offline.min_query_count = 10
bert.Offline.min_duration = 0

           ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/customize.py

    * cm run script "get generic-python-lib _package.nvmitten _path./opt/nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl"

      * cm run script "detect os"
             ! cd /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4b90e938757d4bc1
             ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
             ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py

      * cm run script "detect cpu"

        * cm run script "detect os"
               ! cd /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4b90e938757d4bc1
               ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/run.sh from tmp-run.sh
               ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-os/customize.py
             ! cd /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4b90e938757d4bc1
             ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/run.sh from tmp-run.sh
             ! call "postprocess" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/detect-cpu/customize.py

      * cm run script "get python3"
           ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/953112086af047b0/cm-cached-state.json

      * cm run script "get generic-python-lib _pip"
           ! load /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/ec8e4743d6a54f6e/cm-cached-state.json
               ! cd /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4b90e938757d4bc1
               ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
               ! call "detect_version" from /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/customize.py

          Extra PIP CMD:   --break-system-packages 

           ! cd /myPath/myProjects/gracehopper_eval/CM/repos/local/cache/4b90e938757d4bc1
           ! call /myPath/myProjects/gracehopper_eval/CM/repos/mlcommons@ck/cm-mlops/script/get-generic-python-lib/install.sh from tmp-run.sh

/usr/bin/python3 -m pip install "/opt/nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl" --break-system-packages
WARNING: Requirement '/opt/nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl' looks like a filename, but the file does not exist
Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com
ERROR: nvmitten-0.1.3-cp38-cp38-linux_x86_64.whl is not a supported wheel on this platform.

CM error: Portable CM script failed (name = get-generic-python-lib, return code = 256)


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note that it may be a portability issue of a third-party tool or a native script
wrapped and unified by this automation recipe (CM script). In such case,
please report this issue with a full log at "https://github.com/mlcommons/ck".
The CM concept is to collaboratively fix such issues inside portable CM scripts
to make existing tools and native scripts more portable, interoperable
and deterministic. Thank you!
```
</details>


Thanks for the help! @gfursin @arjunsuresh 

## 评论 (2)

### arjunsuresh · 2024-04-12

yes, the default nvmitten installation is supported only via the docker container. Since the nvmitten is now opensource we have added pip install support out of the container in [this PR](https://github.com/mlcommons/ck/pull/1198)

### github-actions[bot] · 2026-05-05

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
