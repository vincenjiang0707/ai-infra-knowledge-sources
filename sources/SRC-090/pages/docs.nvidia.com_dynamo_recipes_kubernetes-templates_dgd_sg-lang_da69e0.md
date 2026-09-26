source: https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgd/sg-lang
lastmod: 2026-09-24T19:58:16.636Z

# SGLang Deployment Templates

Ready-to-apply DynamoGraphDeployment manifests for serving SGLang with Dynamo on Kubernetes.

Copy-paste `DynamoGraphDeployment`

(`nvidia.com/v1beta1`

) manifests for the SGLang backend, grouped by
topology. Each manifest is embedded from
[ examples/backends/sglang/deploy/](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/sglang/deploy)
— open an entry, use the copy button, then set your image tag and

`hf-token-secret`

before applying.Apply any template with:

kubectl apply -f agg.yaml

## Aggregated

###### agg.yaml · Baseline aggregated serving


agg.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-aggspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-codecommand:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"requests:# Increase this value for larger models.ephemeral-storage: 2GiworkingDir: /workspace/examples/backends/sglangreplicas: 1type: worker

###### agg_router.yaml · Aggregated with KV-aware routing


agg_router.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-agg-routerspec:components:- name: FrontendpodTemplate:spec:containers:- env:- name: DYN_ROUTER_MODEvalue: kvimage: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --kv-events-config- '{"publisher":"zmq","topic":"kv-events","endpoint":"tcp://*:5557"}'command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"requests:# Increase this value for larger models.ephemeral-storage: 2GiworkingDir: /workspace/examples/backends/sglangreplicas: 1type: worker

###### agg_gms.yaml · Aggregated with GPU Memory Service sidecar


agg_gms.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0## GPU Memory Service (GMS) sidecar example.## The operator injects a GMS sidecar init container that provides shared GPU# memory access via DRA (Dynamic Resource Allocation). The sidecar runs two GMS# processes per GPU (weights + kv_cache) and communicates with the main container# over UDS sockets on a shared emptyDir volume.## Requires Kubernetes 1.34+ with DRA v1 enabled and the NVIDIA GPU DRA driver installed.apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-agg-gmsspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- experimental:gpuMemoryService: {}name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --load-format- gmscommand:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"requests:# Increase this value for larger models.ephemeral-storage: 2GiworkingDir: /workspace/examples/backends/sglangreplicas: 1type: worker

###### agg_logging.yaml · Aggregated with structured logging


agg_logging.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-agg-loggingspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-codecommand:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/examples/backends/sglangreplicas: 1type: workerenv:- name: DYN_LOGGING_JSONLvalue: "1"

## Disaggregated

###### disagg.yaml · Baseline disaggregated prefill/decode


disagg.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-disaggspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --disaggregation-mode- decode- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "12345"- --host- 0.0.0.0command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/examples/backends/sglangreplicas: 1type: decode- name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --disaggregation-mode- prefill- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "12345"- --host- 0.0.0.0command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/examples/backends/sglangreplicas: 1type: prefill

###### disagg_planner.yaml · Disaggregated with Dynamo Planner autoscaling


disagg_planner.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-disagg-plannerspec:components:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- name: PlannerpodTemplate:spec:containers:- args:- --config- '{"environment": "kubernetes", "backend": "sglang", "optimization_target": "sla","enable_throughput_scaling": true, "enable_load_scaling": true, "pre_deployment_sweeping_mode":"none", "throughput_adjustment_interval_seconds": 60, "load_adjustment_interval_seconds": 5}'command:- python3- -m- dynamo.plannerenvFrom:- secretRef:name: hf-token-secret# Planner image selection:# Dynamo >= 1.1.0: use the dedicated planner image# <registry>/dynamo-planner:<version># (backend runtime images no longer ship planner runtime deps# such as kubernetes_asyncio, pmdarima, prophet, aiconfigurator).# Dynamo < 1.1.0: use the backend runtime image# <registry>/sglang-runtime:<version>.image: my-registry/dynamo-planner:my-tagname: mainreplicas: 1type: planner- name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --disaggregation-mode- decode- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "12345"- --host- 0.0.0.0command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/examples/backends/sglangreplicas: 2type: decode- name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --page-size- "16"- --tp- "1"- --trust-remote-code- --disaggregation-mode- prefill- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "12345"- --host- 0.0.0.0command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "1"workingDir: /workspace/examples/backends/sglangreplicas: 2type: prefill

###### disagg-multinode.yaml · Disaggregated across multiple nodes


disagg-multinode.yaml

# SPDX-FileCopyrightText: Copyright (c) 2025-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.# SPDX-License-Identifier: Apache-2.0apiVersion: nvidia.com/v1beta1kind: DynamoGraphDeploymentmetadata:name: sglang-disagg-multinodespec:backendFramework: sglangcomponents:- name: FrontendpodTemplate:spec:containers:- image: my-registry/sglang-runtime:my-tagname: mainreplicas: 1type: frontend- multinode:nodeCount: 2name: decodepodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --tp-size- "8"- --trust-remote-code- --disaggregation-mode- decode- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "30001"- --host- 0.0.0.0- --mem-fraction-static- "0.82"command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "4"workingDir: /workspace/examples/backends/sglangreplicas: 1type: decode- multinode:nodeCount: 2name: prefillpodTemplate:spec:containers:- args:- --model-path- Qwen/Qwen3-0.6B- --served-model-name- Qwen/Qwen3-0.6B- --tp-size- "8"- --trust-remote-code- --disaggregation-mode- prefill- --disaggregation-transfer-backend- nixl- --disaggregation-bootstrap-port- "30001"- --mem-fraction-static- "0.82"- --host- 0.0.0.0command:- python3- -m- dynamo.sglangenvFrom:- secretRef:name: hf-token-secretimage: my-registry/sglang-runtime:my-tagname: mainresources:limits:nvidia.com/gpu: "4"workingDir: /workspace/examples/backends/sglangreplicas: 1type: prefillenv:- name: HF_TOKENvalueFrom:secretKeyRef:key: HF_TOKENname: hf-token-secret- name: GLOO_SOCKET_IFNAMEvalue: eth0

## Source

All templates live in
[ examples/backends/sglang/deploy/](https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/sglang/deploy).
For local launch commands, see

[SGLang Local Deployment Examples](https://docs.nvidia.com/dynamo/dev/recipes/cli-templates/sg-lang).