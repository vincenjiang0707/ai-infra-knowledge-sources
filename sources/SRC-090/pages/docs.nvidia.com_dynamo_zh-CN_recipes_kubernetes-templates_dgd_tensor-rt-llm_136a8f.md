source: https://docs.nvidia.com/dynamo/zh-CN/recipes/kubernetes-templates/dgd/tensor-rt-llm
lastmod: 2026-09-24T19:58:16.636Z

TensorRT-LLM Deployment Templates


TensorRT-LLM Deployment Templates

Ready-to-apply DynamoGraphDeployment manifests for serving TensorRT-LLM with Dynamo on Kubernetes.

Copy-paste `DynamoGraphDeployment`

(`nvidia.com/v1beta1`

) manifests for the TensorRT-LLM backend,
grouped by topology. Each manifest is embedded from
[ examples/backends/trtllm/deploy/](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/trtllm/deploy)
— open an entry, use the copy button, then set your image tag and

`hf-token-secret`

before applying.Apply any template with:

kubectl apply -f agg.yaml

Some templates bundle a `ConfigMap`

(engine configuration) or a `PersistentVolumeClaim`

alongside the
deployment. Apply the whole file — every document in it is part of the example.

## Aggregated

###### agg.yaml · Baseline aggregated serving


agg.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-aggspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/tensorrtllm-runtime:my-tagname: mainreplicas: 1type: frontend- name: TRTLLMWorkerpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/agg.yamlcommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"requests:# Increase this value for larger models.ephemeral-storage: 2GiworkingDir: /workspace/replicas: 1type: worker

###### agg_router.yaml · Aggregated with KV-aware routing


agg_router.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-agg-routerspec:components:- name: FrontendpodTemplate:spec:containers:- env:- name: DYN_ROUTER_MODEvalue: kvimage: my-registry/tensorrtllm-runtime:my-tagname: mainreplicas: 1type: frontend- name: TRTLLMWorkerpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/agg.yaml- --publish-kv-eventscommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"requests:# Increase this value for larger models.ephemeral-storage: 2GiworkingDir: /workspace/replicas: 2type: worker

###### agg-with-config.yaml · Aggregated with an external engine ConfigMap (bundles a ConfigMap)


agg-with-config.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0# configmap that contains the custom trtllm configurationapiVersion: v1kind: ConfigMapmetadata:name: nvidia-configdata:agg.yaml: |tensor_parallel_size: 1moe_expert_parallel_size: 1enable_attention_dp: falsemax_num_tokens: 8192max_batch_size: 16trust_remote_code: truebackend: pytorchenable_chunked_prefill: truedisable_overlap_scheduler: truekv_cache_config:free_gpu_memory_fraction: 0.95cuda_graph_config:max_batch_size: 16---apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-aggspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/tensorrtllm-runtime:my-tagname: mainreplicas: 1type: frontend- name: TRTLLMWorkerpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- /workspace/examples/backends/trtllm/engine_configs/qwen3/agg.yamlcommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"# Mount the ConfigMap key as the engine args file without masking /workspace.volumeMounts:- mountPath: /workspace/examples/backends/trtllm/engine_configs/qwen3/agg.yamlname: nvidia-configreadOnly: truesubPath: agg.yamlworkingDir: /workspace/examples/backends/trtllm# Declare the ConfigMap as a pod volume.volumes:- configMap:name: nvidia-configname: nvidia-configreplicas: 1type: worker

## Disaggregated

###### disagg.yaml · Baseline disaggregated prefill/decode


disagg.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-disaggspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/tensorrtllm-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/decode.yaml- --disaggregation-mode- decodecommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/replicas: 1type: decode- name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/prefill.yaml- --disaggregation-mode- prefillcommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/replicas: 1type: prefill

###### disagg_router.yaml · Disaggregated with KV-aware routing


disagg_router.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-v1-disagg-routerspec:components:- name: FrontendpodTemplate:spec:containers:- env:- name: DYN_ROUTER_MODEvalue: kvimage: my-registry/tensorrtllm-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/decode.yaml- --disaggregation-mode- decodecommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/replicas: 2type: decode- name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/prefill.yaml- --disaggregation-mode- prefill- --publish-kv-eventscommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/replicas: 2type: prefill

###### disagg_planner.yaml · Disaggregated with Dynamo Planner autoscaling


disagg_planner.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-disagg-plannerspec:components:- name: FrontendpodTemplate:spec:containers:- args:- -m- dynamo.frontend- --http-port- "8000"- --kv-cache-block-size- "128"- --router-mode- kv- --router-kv-overlap-score-credit- "0.0"- --router-temperature- "0.0"- --no-kv-eventscommand:- python3image: my-registry/tensorrtllm-runtime:my-tagname: mainworkingDir: /workspace/examples/backends/trtllmreplicas: 1type: frontend- name: PlannerpodTemplate:spec:containers:- args:- -m- dynamo.planner- --config- '{"environment": "kubernetes", "backend": "trtllm", "optimization_target": "sla","enable_throughput_scaling": true, "enable_load_scaling": true, "pre_deployment_sweeping_mode":"none", "throughput_adjustment_interval_seconds": 60, "load_adjustment_interval_seconds": 5}'command:- python3envFrom:- secretRef:name: hf-token-secret# Planner image selection:# Dynamo >= 1.1.0: use the dedicated planner image# <registry>/dynamo-planner:<version># (backend runtime images no longer ship planner runtime deps# such as kubernetes_asyncio, pmdarima, prophet, aiconfigurator).# Dynamo < 1.1.0: use the backend runtime image# <registry>/tensorrtllm-runtime:<version>.image: my-registry/dynamo-planner:my-tagname: mainports:- containerPort: 9085name: metricsreplicas: 1type: planner- name: decodepodTemplate:spec:containers:- args:- -m- dynamo.trtllm- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/decode.yaml- --disaggregation-mode- decodecommand:- python3envFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-taglivenessProbe:failureThreshold: 1httpGet:path: /liveport: 9090periodSeconds: 5timeoutSeconds: 30name: mainreadinessProbe:failureThreshold: 60httpGet:path: /healthport: 9090periodSeconds: 10timeoutSeconds: 30resources:limits:nvidia.com/gpu: "1"workingDir: /workspace/terminationGracePeriodSeconds: 600replicas: 1type: decode- name: prefillpodTemplate:spec:containers:- args:- -m- dynamo.trtllm- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- ./examples/backends/trtllm/engine_configs/qwen3/prefill.yaml- --disaggregation-mode- prefillcommand:- python3envFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/terminationGracePeriodSeconds: 600replicas: 1type: prefill

###### disagg-multinode.yaml · Disaggregated across multiple nodes (bundles a ConfigMap and PersistentVolumeClaim)


disagg-multinode.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: v1kind: ConfigMapmetadata:name: nvidia-configdata:prefill.yaml: |# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0## Licensed under the Apache License, Version 2.0 (the "License");# you may not use this file except in compliance with the License.# You may obtain a copy of the License at## http://www.apache.org/licenses/LICENSE-2.0## Unless required by applicable law or agreed to in writing, software# distributed under the License is distributed on an "AS IS" BASIS,# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.# See the License for the specific language governing permissions and# limitations under the License.tensor_parallel_size: 8moe_expert_parallel_size: 1enable_attention_dp: falsemax_num_tokens: 8192trust_remote_code: truebackend: pytorchenable_chunked_prefill: true# Overlap scheduler not currently supported in prefill only workers.disable_overlap_scheduler: truekv_cache_config:free_gpu_memory_fraction: 0.80cache_transceiver_config:backend: DEFAULTdecode.yaml: |# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0## Licensed under the Apache License, Version 2.0 (the "License");# you may not use this file except in compliance with the License.# You may obtain a copy of the License at## http://www.apache.org/licenses/LICENSE-2.0## Unless required by applicable law or agreed to in writing, software# distributed under the License is distributed on an "AS IS" BASIS,# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.# See the License for the specific language governing permissions and# limitations under the License.tensor_parallel_size: 8moe_expert_parallel_size: 1enable_attention_dp: falsemax_num_tokens: 8192trust_remote_code: truebackend: pytorchenable_chunked_prefill: truedisable_overlap_scheduler: falsekv_cache_config:free_gpu_memory_fraction: 0.80cache_transceiver_config:backend: DEFAULT---apiVersion: v1kind: PersistentVolumeClaimmetadata:name: modelsspec:accessModes:- ReadWriteManyresources:requests:storage: 100Gi---apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: trtllm-disagg-tp8spec:backendFramework: trtllmcomponents:- name: FrontendpodTemplate:spec:containers:- args:- --http-port- "8000"command:- python3- -m- dynamo.frontendimage: my-registry/tensorrtllm-runtime:my-tagname: mainvolumeMounts:- mountPath: /modelsname: modelsworkingDir: /workspace/examples/backends/trtllmvolumes:- name: modelspersistentVolumeClaim:claimName: modelsreplicas: 1type: frontend- multinode:nodeCount: 2name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- /workspace/engine_configs/decode.yaml- --disaggregation-mode- decodecommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "4"volumeMounts:- mountPath: /modelsname: models- mountPath: /workspace/engine_configsname: nvidia-configreadOnly: trueworkingDir: /workspace/volumes:- name: modelspersistentVolumeClaim:claimName: models- configMap:name: nvidia-configname: nvidia-configreplicas: 1type: decode- multinode:nodeCount: 2name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --extra-engine-args- /workspace/engine_configs/prefill.yaml- --disaggregation-mode- prefillcommand:- python3- -m- dynamo.trtllmenvFrom:- secretRef:name: hf-token-secretimage: my-registry/tensorrtllm-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "4"volumeMounts:- mountPath: /modelsname: models- mountPath: /workspace/engine_configsname: nvidia-configreadOnly: trueworkingDir: /workspace/volumes:- name: modelspersistentVolumeClaim:claimName: models- configMap:name: nvidia-configname: nvidia-configreplicas: 1type: prefillenv:- name: OMPI_ALLOW_RUN_AS_ROOTvalue: "1"- name: OMPI_ALLOW_RUN_AS_ROOT_CONFIRMvalue: "1"- name: HF_HOMEvalue: /models

## Source

All templates live in
[ examples/backends/trtllm/deploy/](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/trtllm/deploy).
For local launch commands, see

[TensorRT-LLM Local Deployment Examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/tensor-rt-llm).