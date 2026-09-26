source: https://docs.mlcommons.org/inference/benchmarks/text_to_image/sdxl/

# Text to Image using Stable Diffusion[¶](https://docs.mlcommons.org#text-to-image-using-stable-diffusion)

## MLPerf Reference Implementation in Python[¶](https://docs.mlcommons.org#mlperf-reference-implementation-in-python)

Tip

- MLCommons reference implementations are only meant to provide a rules compliant reference implementation for the submitters and in most cases are not best performing. If you want to benchmark any system, it is advisable to use the vendor MLPerf implementation for that system like Nvidia, Intel etc.


Note:SDXL reference implementation does not support multithreading.

SDXL

### Edge category[¶](https://docs.mlcommons.org#edge-category)

In the edge category, sdxl has Offline, SingleStream scenarios and all of the scenarios are mandatory for a closed division submission.

#### Pytorch framework[¶](https://docs.mlcommons.org#pytorch-framework)

##### CPU device[¶](https://docs.mlcommons.org#cpu-device)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 50GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario)

Tip

-
Compliance runs can be enabled by adding

`--compliance=yes`

. -
Number of threads could be adjusted using

`--threads=#`

, where`#`

is the desired number of threads. This option works only if the implementation in use supports threading. -
Batch size could be adjusted using

`--batch_size=#`

, where`#`

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. -
`_r5.1-dev`

could also be given instead of`_r6.0-dev`

if you want to run the benchmark with the MLPerf version being 4.1. -
Add

`--adr.mlperf-implementation.tags=_branch.master,_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the official MLPerf Inference implementation in a custom fork. -
Add

`--adr.inference-src.tags=_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the model config accuracy script in the submission checker within a custom fork. -
Add

`--adr.inference-src.version=custom`

if you are using the modified MLPerf Inference code or accuracy script on submission checker within a custom fork.

Tip

`--env.MLC_MLPERF_MODEL_SDXL_DOWNLOAD_TO_HOST=yes`

option can be used to download the model on the host so that it can be reused across different container lanuches.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--docker --quiet \
--test_query_count=10 --rerun
```


Tip

`--precision=bfloat16`

can give better performance

The above command should get you to an interactive shell inside the docker container and do a quick test run for the Offline scenario. Once inside the docker container please do the below commands to do the accuracy + performance runs for each scenario.

## Please click here to see more options for the docker launch


-
`--docker_privileged`

: to launch the container in privileged mode -
`--docker_mlc_repo=<Custom MLC GitHub repo URL in username@repo format>`

: to use a custom fork of mlperf-automations repository inside the docker image -
`--docker_mlc_repo_branch=<Custom MLC GitHub repo Branch>`

: to checkout a custom branch of the cloned mlperf-automations repository inside the docker image -
`--docker_cache=no`

: to not use docker cache during the image build `--docker_os=ubuntu`

: ubuntu and rhel are supported.`--docker_os_version=20.04`

: [20.04, 22.04] are supported for Ubuntu and [8, 9] for RHEL

###### Offline[¶](https://docs.mlcommons.org#offline)

###### performance-only[¶](https://docs.mlcommons.org#performance-only)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### SingleStream[¶](https://docs.mlcommons.org#singlestream)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful

###### Native Environment[¶](https://docs.mlcommons.org#native-environment)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario)

Tip

-
Compliance runs can be enabled by adding

`--compliance=yes`

. -
Number of threads could be adjusted using

`--threads=#`

, where`#`

is the desired number of threads. This option works only if the implementation in use supports threading. -
Batch size could be adjusted using

`--batch_size=#`

, where`#`

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. -
`_r5.1-dev`

could also be given instead of`_r6.0-dev`

if you want to run the benchmark with the MLPerf version being 4.1. -
Add

`--adr.mlperf-implementation.tags=_branch.master,_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the official MLPerf Inference implementation in a custom fork. -
Add

`--adr.inference-src.tags=_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the model config accuracy script in the submission checker within a custom fork. -
Add

`--adr.inference-src.version=custom`

if you are using the modified MLPerf Inference code or accuracy script on submission checker within a custom fork.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


Tip

`--precision=bfloat16`

can give better performance

The above command should do a test run of Offline scenario and record the estimated offline_target_qps.

###### Offline[¶](https://docs.mlcommons.org#offline_1)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### SingleStream[¶](https://docs.mlcommons.org#singlestream_1)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`--precision=bfloat16`

can give better performance

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device)

## Please click here to see the minimum system requirements for running the benchmark


-
**Device Memory**: 24GB(fp32), 16GB(fp16) -
**Disk Space**: 50GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_1)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario_1)

Tip

-
Compliance runs can be enabled by adding

`--compliance=yes`

. -
Number of threads could be adjusted using

`--threads=#`

, where`#`

is the desired number of threads. This option works only if the implementation in use supports threading. -
Batch size could be adjusted using

`--batch_size=#`

, where`#`

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. -
`_r5.1-dev`

could also be given instead of`_r6.0-dev`

if you want to run the benchmark with the MLPerf version being 4.1. -
Add

`--adr.mlperf-implementation.tags=_branch.master,_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the official MLPerf Inference implementation in a custom fork. -
Add

`--adr.inference-src.tags=_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the model config accuracy script in the submission checker within a custom fork. -
Add

`--adr.inference-src.version=custom`

if you are using the modified MLPerf Inference code or accuracy script on submission checker within a custom fork.

Tip

`--env.MLC_MLPERF_MODEL_SDXL_DOWNLOAD_TO_HOST=yes`

option can be used to download the model on the host so that it can be reused across different container lanuches.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--docker --quiet \
--test_query_count=50 --rerun
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

The above command should get you to an interactive shell inside the docker container and do a quick test run for the Offline scenario. Once inside the docker container please do the below commands to do the accuracy + performance runs for each scenario.

## Please click here to see more options for the docker launch


-
`--docker_privileged`

: to launch the container in privileged mode -
`--docker_mlc_repo=<Custom MLC GitHub repo URL in username@repo format>`

: to use a custom fork of mlperf-automations repository inside the docker image -
`--docker_mlc_repo_branch=<Custom MLC GitHub repo Branch>`

: to checkout a custom branch of the cloned mlperf-automations repository inside the docker image -
`--docker_cache=no`

: to not use docker cache during the image build

###### Offline[¶](https://docs.mlcommons.org#offline_2)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_4)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_4)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### SingleStream[¶](https://docs.mlcommons.org#singlestream_2)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_5)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_5)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_1)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

Tip

- It is advisable to use the commands in the Docker tab for CUDA. Run the below native command only if you are already on a CUDA setup with cuDNN and TensorRT installed.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python_1)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_1)

Tip

-
Compliance runs can be enabled by adding

`--compliance=yes`

. -
Number of threads could be adjusted using

`--threads=#`

, where`#`

is the desired number of threads. This option works only if the implementation in use supports threading. -
Batch size could be adjusted using

`--batch_size=#`

, where`#`

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. -
`_r5.1-dev`

could also be given instead of`_r6.0-dev`

if you want to run the benchmark with the MLPerf version being 4.1. -
Add

`--adr.mlperf-implementation.tags=_branch.master,_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the official MLPerf Inference implementation in a custom fork. -
Add

`--adr.inference-src.tags=_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the model config accuracy script in the submission checker within a custom fork. -
Add

`--adr.inference-src.version=custom`

if you are using the modified MLPerf Inference code or accuracy script on submission checker within a custom fork.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

The above command should do a test run of Offline scenario and record the estimated offline_target_qps.

###### Offline[¶](https://docs.mlcommons.org#offline_3)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_6)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_6)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### SingleStream[¶](https://docs.mlcommons.org#singlestream_3)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_7)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_7)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful

##### ROCm device[¶](https://docs.mlcommons.org#rocm-device)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 50GB

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_2)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python_2)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_2)

Tip

-
Compliance runs can be enabled by adding

`--compliance=yes`

. -
Number of threads could be adjusted using

`--threads=#`

, where`#`

is the desired number of threads. This option works only if the implementation in use supports threading. -
Batch size could be adjusted using

`--batch_size=#`

, where`#`

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. -
`_r5.1-dev`

could also be given instead of`_r6.0-dev`

if you want to run the benchmark with the MLPerf version being 4.1. -
Add

`--adr.mlperf-implementation.tags=_branch.master,_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the official MLPerf Inference implementation in a custom fork. -
Add

`--adr.inference-src.tags=_repo.<CUSTOM_INFERENCE_REPO_LINK>`

if you are modifying the model config accuracy script in the submission checker within a custom fork. -
Add

`--adr.inference-src.version=custom`

if you are using the modified MLPerf Inference code or accuracy script on submission checker within a custom fork.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=rocm \
--quiet \
--test_query_count=10 --rerun
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

The above command should do a test run of Offline scenario and record the estimated offline_target_qps.

###### Offline[¶](https://docs.mlcommons.org#offline_4)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_8)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_8)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### SingleStream[¶](https://docs.mlcommons.org#singlestream_4)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_9)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_9)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_4)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=sdxl \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`--precision=float16`

can help run on GPUs with less RAM / gives better performance

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful

- If you want to download the official MLPerf model and dataset for sdxl you can follow
[this README](https://docs.mlcommons.org/get-sdxl-data/).