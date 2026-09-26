source: https://docs.mlcommons.org/inference/benchmarks/medical_imaging/3d-unet/

# Medical Imaging using 3d-unet (KiTS 2019 kidney tumor segmentation task)[¶](https://docs.mlcommons.org#medical-imaging-using-3d-unet-kits-2019-kidney-tumor-segmentation-task)

## MLPerf Reference Implementation in Python[¶](https://docs.mlcommons.org#mlperf-reference-implementation-in-python)

Tip

- MLCommons reference implementations are only meant to provide a rules compliant reference implementation for the submitters and in most cases are not best performing. If you want to benchmark any system, it is advisable to use the vendor MLPerf implementation for that system like Nvidia, Intel etc.

3D-UNET-99

### Datacenter category[¶](https://docs.mlcommons.org#datacenter-category)

In the datacenter category, 3d-unet-99 has Offline, Server scenarios and all of the scenarios are mandatory for a closed division submission.

#### Pytorch framework[¶](https://docs.mlcommons.org#pytorch-framework)

##### CPU device[¶](https://docs.mlcommons.org#cpu-device)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

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

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--docker --quiet \
--test_query_count=10 --rerun
```


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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_1)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_1)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_1)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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
**Device Memory**: To be updated -
**Disk Space**: 60GB

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

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--docker --quiet \
--test_query_count=50 --rerun
```


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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_4)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_2)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_5)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_5)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_2)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_3)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_6)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_6)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_3)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_7)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_7)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_3)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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


**Disk Space**: 60GB

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=rocm \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_4)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_8)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_8)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_4)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_9)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_9)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_4)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

### Edge category[¶](https://docs.mlcommons.org#edge-category)

In the edge category, 3d-unet-99 has Offline, SingleStream scenarios and all of the scenarios are mandatory for a closed division submission.

#### Pytorch framework[¶](https://docs.mlcommons.org#pytorch-framework_1)

##### CPU device[¶](https://docs.mlcommons.org#cpu-device_1)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_2)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario_2)

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--docker --quiet \
--test_query_count=10 --rerun
```


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

###### Offline[¶](https://docs.mlcommons.org#offline_5)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_10)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_10)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_11)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_11)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_5)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_3)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python_3)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_3)

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_6)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_12)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_12)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_1)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_13)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_13)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_6)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


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

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_1)

## Please click here to see the minimum system requirements for running the benchmark


-
**Device Memory**: To be updated -
**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_3)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario_3)

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--docker --quiet \
--test_query_count=50 --rerun
```


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

###### Offline[¶](https://docs.mlcommons.org#offline_7)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_14)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_14)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_2)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_15)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_15)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_7)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_4)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

Tip

- It is advisable to use the commands in the Docker tab for CUDA. Run the below native command only if you are already on a CUDA setup with cuDNN and TensorRT installed.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python_4)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_4)

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_8)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_16)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_16)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_3)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_17)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_17)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_8)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


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

##### ROCm device[¶](https://docs.mlcommons.org#rocm-device_1)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_5)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Setup a virtual environment for Python[¶](https://docs.mlcommons.org#setup-a-virtual-environment-for-python_5)

```
mlcr install,python-venv --name=mlperf
export MLC_SCRIPT_EXTRA_CMD="--adr.python.name=mlperf"
```


###### # Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_5)

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
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=rocm \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_9)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_18)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_18)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_4)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_19)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_19)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_9)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=rocm \
--quiet
```


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

3D-UNET-99.9

### Datacenter category[¶](https://docs.mlcommons.org#datacenter-category_1)

In the datacenter category, 3d-unet-99.9 has Offline, Server scenarios and all of the scenarios are mandatory for a closed division submission.

#### Pytorch framework[¶](https://docs.mlcommons.org#pytorch-framework_2)

##### CPU device[¶](https://docs.mlcommons.org#cpu-device_2)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_4)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_6)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_10)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_20)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_20)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_5)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_21)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_21)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_10)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_6)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_7)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_11)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_22)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_22)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_6)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_23)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_23)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_11)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cpu \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_2)

## Please click here to see the minimum system requirements for running the benchmark


-
**Device Memory**: To be updated -
**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_5)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_8)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_12)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_24)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_24)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_7)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_25)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_25)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_12)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_7)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

Tip

- It is advisable to use the commands in the Docker tab for CUDA. Run the below native command only if you are already on a CUDA setup with cuDNN and TensorRT installed.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_9)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_13)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_26)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_26)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_8)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_27)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_27)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_13)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

##### ROCm device[¶](https://docs.mlcommons.org#rocm-device_2)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_8)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_10)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=rocm \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_14)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_28)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_28)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_9)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_29)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_29)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_14)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=rocm \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

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

### Edge category[¶](https://docs.mlcommons.org#edge-category_1)

In the edge category, 3d-unet-99.9 has Offline, SingleStream scenarios and all of the scenarios are mandatory for a closed division submission.

#### Pytorch framework[¶](https://docs.mlcommons.org#pytorch-framework_3)

##### CPU device[¶](https://docs.mlcommons.org#cpu-device_3)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_6)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_11)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_15)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_30)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_30)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_5)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_31)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_31)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_15)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_9)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_12)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cpu \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_16)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_32)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_32)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_6)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_33)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_33)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cpu \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_16)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cpu \
--quiet
```


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

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_3)

## Please click here to see the minimum system requirements for running the benchmark


-
**Device Memory**: To be updated -
**Disk Space**: 60GB

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_7)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_13)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_17)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_34)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_34)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_7)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_35)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_35)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_17)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


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

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_10)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

Tip

- It is advisable to use the commands in the Docker tab for CUDA. Run the below native command only if you are already on a CUDA setup with cuDNN and TensorRT installed.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_14)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_18)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_36)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_36)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_8)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_37)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_37)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_18)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


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

##### ROCm device[¶](https://docs.mlcommons.org#rocm-device_3)

## Please click here to see the minimum system requirements for running the benchmark


**Disk Space**: 60GB

###### Native Environment[¶](https://docs.mlcommons.org#native-environment_11)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_15)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=rocm \
--quiet \
--test_query_count=10 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_19)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_38)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_38)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_9)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_39)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_39)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=rocm \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_19)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=reference \
--framework=pytorch \
--category=edge \
--execution_mode=valid \
--device=rocm \
--quiet
```


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

- If you want to download the official MLPerf model and dataset for 3d-unet-99.9 you can follow
[this README](https://docs.mlcommons.org/get-3d-unet-data/).

## Nvidia MLPerf Implementation[¶](https://docs.mlcommons.org#nvidia-mlperf-implementation)

3D-UNET-99

### Datacenter category[¶](https://docs.mlcommons.org#datacenter-category_2)

In the datacenter category, 3d-unet-99 has Offline, Server scenarios and all of the scenarios are mandatory for a closed division submission.

#### TensorRT framework[¶](https://docs.mlcommons.org#tensorrt-framework)

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_4)

## Please click here to see the minimum system requirements for running the benchmark


**Device Memory**: To be updated

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_8)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario_4)

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

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. Example:`--batch_size.3d-unet:2`


Tip

-
Default batch size is assigned based on

[GPU memory](https://github.com/mlcommons/cm4mlops/blob/dd0c35856969c68945524d5c80414c615f5fe42c/script/app-mlperf-inference-nvidia/_cm.yaml#L1129)or the[specified GPU](https://github.com/mlcommons/cm4mlops/blob/dd0c35856969c68945524d5c80414c615f5fe42c/script/app-mlperf-inference-nvidia/_cm.yaml#L1370). Please click more option for*docker launch*or*run command*to see how to specify the GPU name. -
When run with

`--all_models=yes`

, all the benchmark models of NVIDIA implementation can be executed within the same container. -
If you encounter an error related to ulimit or max locked memory during the run_harness step, please refer to the

[this](https://github.com/mlcommons/mlperf-automations/issues/664)issue for details and resolution steps.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--docker --quiet \
--test_query_count=50 --rerun
```


## Please click here to see more options for the docker launch


-
`--docker_privileged`

: to launch the container in privileged mode -
`--docker_mlc_repo=<Custom MLC GitHub repo URL in username@repo format>`

: to use a custom fork of mlperf-automations repository inside the docker image -
`--docker_mlc_repo_branch=<Custom MLC GitHub repo Branch>`

: to checkout a custom branch of the cloned mlperf-automations repository inside the docker image -
`--docker_cache=no`

: to not use docker cache during the image build `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.

###### Offline[¶](https://docs.mlcommons.org#offline_20)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_40)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_40)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_10)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_41)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_41)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_20)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.

### Edge category[¶](https://docs.mlcommons.org#edge-category_2)

In the edge category, 3d-unet-99 has Offline, SingleStream scenarios and all of the scenarios are mandatory for a closed division submission.

#### TensorRT framework[¶](https://docs.mlcommons.org#tensorrt-framework_1)

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_5)

## Please click here to see the minimum system requirements for running the benchmark


**Device Memory**: To be updated

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_9)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

###### # Docker Container Build and Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#docker-container-build-and-performance-estimation-for-offline-scenario_5)

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

is the desired batch size. This option works only if the implementation in use is supporting the given batch size. Example:`--batch_size.3d-unet:2`


Tip

-
Default batch size is assigned based on

[GPU memory](https://github.com/mlcommons/cm4mlops/blob/dd0c35856969c68945524d5c80414c615f5fe42c/script/app-mlperf-inference-nvidia/_cm.yaml#L1129)or the[specified GPU](https://github.com/mlcommons/cm4mlops/blob/dd0c35856969c68945524d5c80414c615f5fe42c/script/app-mlperf-inference-nvidia/_cm.yaml#L1370). Please click more option for*docker launch*or*run command*to see how to specify the GPU name. -
When run with

`--all_models=yes`

, all the benchmark models of NVIDIA implementation can be executed within the same container. -
If you encounter an error related to ulimit or max locked memory during the run_harness step, please refer to the

[this](https://github.com/mlcommons/mlperf-automations/issues/664)issue for details and resolution steps.

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--docker --quiet \
--test_query_count=50 --rerun
```


## Please click here to see more options for the docker launch


-
`--docker_privileged`

: to launch the container in privileged mode -
`--docker_mlc_repo=<Custom MLC GitHub repo URL in username@repo format>`

: to use a custom fork of mlperf-automations repository inside the docker image -
`--docker_mlc_repo_branch=<Custom MLC GitHub repo Branch>`

: to checkout a custom branch of the cloned mlperf-automations repository inside the docker image -
`--docker_cache=no`

: to not use docker cache during the image build `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.

###### Offline[¶](https://docs.mlcommons.org#offline_21)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_42)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_42)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_10)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_43)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_43)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_21)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.

3D-UNET-99.9

### Datacenter category[¶](https://docs.mlcommons.org#datacenter-category_3)

In the datacenter category, 3d-unet-99.9 has Offline, Server scenarios and all of the scenarios are mandatory for a closed division submission.

#### TensorRT framework[¶](https://docs.mlcommons.org#tensorrt-framework_2)

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_6)

## Please click here to see the minimum system requirements for running the benchmark


**Device Memory**: To be updated

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_10)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_16)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_22)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_44)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_44)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### Server[¶](https://docs.mlcommons.org#server_11)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_45)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_45)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--scenario=Server\
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_22)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=datacenter \
--server_target_qps=<SERVER_TARGET_QPS> \
--execution_mode=valid \
--device=cuda \
--quiet
```


Tip

`<SERVER_TARGET_QPS>`

must be determined manually. It is usually around 80% of the Offline QPS, but on some systems, it can drop below 50%. If a higher value is specified, the latency constraint will not be met, and the run will be considered invalid.

## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.

### Edge category[¶](https://docs.mlcommons.org#edge-category_3)

In the edge category, 3d-unet-99.9 has Offline, SingleStream scenarios and all of the scenarios are mandatory for a closed division submission.

#### TensorRT framework[¶](https://docs.mlcommons.org#tensorrt-framework_3)

##### CUDA device[¶](https://docs.mlcommons.org#cuda-device_7)

## Please click here to see the minimum system requirements for running the benchmark


**Device Memory**: To be updated

###### Docker Environment[¶](https://docs.mlcommons.org#docker-environment_11)

Please refer to the [installation page](https://docs.mlcommons.org/inference/install/) to install MLCFlow for running the automated benchmark commands.

You can reuse the same environment as described for 3d-unet-99.

###### Performance Estimation for Offline Scenario[¶](https://docs.mlcommons.org#performance-estimation-for-offline-scenario_17)

```
mlcr run-mlperf,inference,_find-performance,_full,_r5.1-dev \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=test \
--device=cuda \
--quiet \
--test_query_count=50 --rerun
```


###### Offline[¶](https://docs.mlcommons.org#offline_23)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_46)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_46)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=Offline \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### SingleStream[¶](https://docs.mlcommons.org#singlestream_11)

###### performance-only[¶](https://docs.mlcommons.org#performance-only_47)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_performance-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### accuracy-only[¶](https://docs.mlcommons.org#accuracy-only_47)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_accuracy-only \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--scenario=SingleStream \
--execution_mode=valid \
--device=cuda \
--quiet
```


###### All Scenarios[¶](https://docs.mlcommons.org#all-scenarios_23)

```
mlcr run-mlperf,inference,_full,_r5.1-dev,_all-scenarios \
--model=3d-unet-99.9 \
--implementation=nvidia \
--framework=tensorrt \
--category=edge \
--execution_mode=valid \
--device=cuda \
--quiet
```


## Please click here to see more options for the RUN command


-
Use

`--division=closed`

to do a closed division submission which includes compliance runs -
Use

`--rerun`

to do a rerun even when a valid run exists - Use
`--compliance`

to do the compliance runs (only applicable for closed division) once the valid runs are successful `--gpu_name=<Name of the GPU>`

: The GPUs with supported configs in MLC are`orin`

,`rtx_4090`

,`rtx_a6000`

,`rtx_6000_ada`

,`l4`

,`t4`

and`a100`

. For other GPUs, default configuration as per the GPU memory will be used.