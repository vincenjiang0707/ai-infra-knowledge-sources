source: https://docs.vllm.ai/en/latest/deployment/k8s/
lastmod: 2026-09-23

# Using Kubernetes[¶](https://docs.vllm.ai#using-kubernetes)

Deploying vLLM on Kubernetes is a scalable and efficient way to serve machine learning models. This guide walks you through deploying vLLM using native Kubernetes.

Alternatively, you can deploy vLLM to Kubernetes using any of the following:

[Helm](https://docs.vllm.ai/frameworks/helm/)[NVIDIA Dynamo](https://docs.vllm.ai/integrations/dynamo/)[InftyAI/llmaz](https://docs.vllm.ai/integrations/llmaz/)[llm-d](https://docs.vllm.ai/integrations/llm-d/)[KAITO](https://docs.vllm.ai/integrations/kaito/)[KServe](https://docs.vllm.ai/integrations/kserve/)[Kthena](https://docs.vllm.ai/integrations/kthena/)[KubeRay](https://docs.vllm.ai/integrations/kuberay/)[kubernetes-sigs/lws](https://docs.vllm.ai/frameworks/lws/)[meta-llama/llama-stack](https://docs.vllm.ai/integrations/llamastack/)[substratusai/kubeai](https://docs.vllm.ai/integrations/kubeai/)[vllm-project/AIBrix](https://docs.vllm.ai/integrations/aibrix/)[vllm-project/production-stack](https://docs.vllm.ai/integrations/production-stack/)

## Deployment with CPUs[¶](https://docs.vllm.ai#deployment-with-cpus)

Note

The use of CPUs here is for demonstration and testing purposes only and its performance will not be on par with GPUs.

First, create a Kubernetes PVC and Secret for downloading and storing Hugging Face model:

## Config

cat <<EOF |kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: vllm-models
spec:
accessModes:
- ReadWriteOnce
volumeMode: Filesystem
resources:
requests:
storage: 50Gi
---
apiVersion: v1
kind: Secret
metadata:
name: hf-token-secret
type: Opaque
stringData:
token: "REPLACE_WITH_TOKEN"
EOF


Here, the `token`

field stores your **Hugging Face access token**. For details on how to generate a token, see the [Hugging Face documentation](https://huggingface.co/docs/hub/en/security-tokens).

Next, start the vLLM server as a Kubernetes Deployment and Service.

Note that you will want to configure your vLLM image based on your processor arch:

## Config

VLLM_IMAGE=public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:latest # use this for x86_64
VLLM_IMAGE=public.ecr.aws/q9t5s3a7/vllm-arm64-cpu-release-repo:latest # use this for arm64
cat <<EOF |kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
name: vllm-server
spec:
replicas: 1
selector:
matchLabels:
app.kubernetes.io/name: vllm
template:
metadata:
labels:
app.kubernetes.io/name: vllm
spec:
containers:
- name: vllm
image: $VLLM_IMAGE
command: ["/bin/sh", "-c"]
args: [
"vllm serve meta-llama/Llama-3.2-1B-Instruct"
]
env:
- name: HF_TOKEN
valueFrom:
secretKeyRef:
name: hf-token-secret
key: token
ports:
- containerPort: 8000
volumeMounts:
- name: llama-storage
mountPath: /root/.cache/huggingface
volumes:
- name: llama-storage
persistentVolumeClaim:
claimName: vllm-models
---
apiVersion: v1
kind: Service
metadata:
name: vllm-server
spec:
selector:
app.kubernetes.io/name: vllm
ports:
- protocol: TCP
port: 8000
targetPort: 8000
type: ClusterIP
EOF


We can verify that the vLLM server has started successfully via the logs (this might take a couple of minutes to download the model):

kubectl logs -l app.kubernetes.io/name=vllm
...
INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


## Deployment with GPUs[¶](https://docs.vllm.ai#deployment-with-gpus)

**Pre-requisite**: Ensure that you have a running [Kubernetes cluster with GPUs](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/).

-
Create a PVC, Secret and Deployment for vLLM

PVC is used to store the model cache and it is optional, you can use hostPath or other storage options

## Yaml

Secret is optional and only required for accessing gated models, you can skip this step if you are not using gated models

[apiVersion: v1](https://docs.vllm.ai#__codelineno-4-1)[kind: Secret](https://docs.vllm.ai#__codelineno-4-2)[metadata:](https://docs.vllm.ai#__codelineno-4-3)[name: hf-token-secret](https://docs.vllm.ai#__codelineno-4-4)[namespace: default](https://docs.vllm.ai#__codelineno-4-5)[type: Opaque](https://docs.vllm.ai#__codelineno-4-6)[stringData:](https://docs.vllm.ai#__codelineno-4-7)[token: "REPLACE_WITH_TOKEN"](https://docs.vllm.ai#__codelineno-4-8)Next to create the deployment file for vLLM to run the model server. The following example deploys the

`Mistral-7B-Instruct-v0.3`

model.Here are two examples for using NVIDIA GPU and AMD GPU.

NVIDIA GPU:

## Yaml

[apiVersion: apps/v1](https://docs.vllm.ai#__codelineno-5-1)[kind: Deployment](https://docs.vllm.ai#__codelineno-5-2)[metadata:](https://docs.vllm.ai#__codelineno-5-3)[name: mistral-7b](https://docs.vllm.ai#__codelineno-5-4)[namespace: default](https://docs.vllm.ai#__codelineno-5-5)[labels:](https://docs.vllm.ai#__codelineno-5-6)[app: mistral-7b](https://docs.vllm.ai#__codelineno-5-7)[spec:](https://docs.vllm.ai#__codelineno-5-8)[replicas: 1](https://docs.vllm.ai#__codelineno-5-9)[selector:](https://docs.vllm.ai#__codelineno-5-10)[matchLabels:](https://docs.vllm.ai#__codelineno-5-11)[app: mistral-7b](https://docs.vllm.ai#__codelineno-5-12)[template:](https://docs.vllm.ai#__codelineno-5-13)[metadata:](https://docs.vllm.ai#__codelineno-5-14)[labels:](https://docs.vllm.ai#__codelineno-5-15)[app: mistral-7b](https://docs.vllm.ai#__codelineno-5-16)[spec:](https://docs.vllm.ai#__codelineno-5-17)[volumes:](https://docs.vllm.ai#__codelineno-5-18)[- name: cache-volume](https://docs.vllm.ai#__codelineno-5-19)[persistentVolumeClaim:](https://docs.vllm.ai#__codelineno-5-20)[claimName: mistral-7b](https://docs.vllm.ai#__codelineno-5-21)[# vLLM needs to access the host's shared memory for tensor parallel inference.](https://docs.vllm.ai#__codelineno-5-22)[- name: shm](https://docs.vllm.ai#__codelineno-5-23)[emptyDir:](https://docs.vllm.ai#__codelineno-5-24)[medium: Memory](https://docs.vllm.ai#__codelineno-5-25)[sizeLimit: "2Gi"](https://docs.vllm.ai#__codelineno-5-26)[containers:](https://docs.vllm.ai#__codelineno-5-27)[- name: mistral-7b](https://docs.vllm.ai#__codelineno-5-28)[image: vllm/vllm-openai:latest](https://docs.vllm.ai#__codelineno-5-29)[command: ["/bin/sh", "-c"]](https://docs.vllm.ai#__codelineno-5-30)[args: [](https://docs.vllm.ai#__codelineno-5-31)["vllm serve mistralai/Mistral-7B-Instruct-v0.3 --trust-remote-code --enable-chunked-prefill --max-num-batched-tokens 1024"](https://docs.vllm.ai#__codelineno-5-32)[]](https://docs.vllm.ai#__codelineno-5-33)[env:](https://docs.vllm.ai#__codelineno-5-34)[- name: HF_TOKEN](https://docs.vllm.ai#__codelineno-5-35)[valueFrom:](https://docs.vllm.ai#__codelineno-5-36)[secretKeyRef:](https://docs.vllm.ai#__codelineno-5-37)[name: hf-token-secret](https://docs.vllm.ai#__codelineno-5-38)[key: token](https://docs.vllm.ai#__codelineno-5-39)[ports:](https://docs.vllm.ai#__codelineno-5-40)[- containerPort: 8000](https://docs.vllm.ai#__codelineno-5-41)[resources:](https://docs.vllm.ai#__codelineno-5-42)[limits:](https://docs.vllm.ai#__codelineno-5-43)[cpu: "10"](https://docs.vllm.ai#__codelineno-5-44)[memory: 20G](https://docs.vllm.ai#__codelineno-5-45)[nvidia.com/gpu: "1"](https://docs.vllm.ai#__codelineno-5-46)[requests:](https://docs.vllm.ai#__codelineno-5-47)[cpu: "2"](https://docs.vllm.ai#__codelineno-5-48)[memory: 6G](https://docs.vllm.ai#__codelineno-5-49)[nvidia.com/gpu: "1"](https://docs.vllm.ai#__codelineno-5-50)[volumeMounts:](https://docs.vllm.ai#__codelineno-5-51)[- mountPath: /root/.cache/huggingface](https://docs.vllm.ai#__codelineno-5-52)[name: cache-volume](https://docs.vllm.ai#__codelineno-5-53)[- name: shm](https://docs.vllm.ai#__codelineno-5-54)[mountPath: /dev/shm](https://docs.vllm.ai#__codelineno-5-55)[livenessProbe:](https://docs.vllm.ai#__codelineno-5-56)[httpGet:](https://docs.vllm.ai#__codelineno-5-57)[path: /health](https://docs.vllm.ai#__codelineno-5-58)[port: 8000](https://docs.vllm.ai#__codelineno-5-59)[initialDelaySeconds: 60](https://docs.vllm.ai#__codelineno-5-60)[periodSeconds: 10](https://docs.vllm.ai#__codelineno-5-61)[readinessProbe:](https://docs.vllm.ai#__codelineno-5-62)[httpGet:](https://docs.vllm.ai#__codelineno-5-63)[path: /health](https://docs.vllm.ai#__codelineno-5-64)[port: 8000](https://docs.vllm.ai#__codelineno-5-65)[initialDelaySeconds: 60](https://docs.vllm.ai#__codelineno-5-66)[periodSeconds: 5](https://docs.vllm.ai#__codelineno-5-67)AMD GPU:

You can refer to the

`deployment.yaml`

below if using AMD ROCm GPU like MI300X.## Yaml

[apiVersion: apps/v1](https://docs.vllm.ai#__codelineno-6-1)[kind: Deployment](https://docs.vllm.ai#__codelineno-6-2)[metadata:](https://docs.vllm.ai#__codelineno-6-3)[name: mistral-7b](https://docs.vllm.ai#__codelineno-6-4)[namespace: default](https://docs.vllm.ai#__codelineno-6-5)[labels:](https://docs.vllm.ai#__codelineno-6-6)[app: mistral-7b](https://docs.vllm.ai#__codelineno-6-7)[spec:](https://docs.vllm.ai#__codelineno-6-8)[replicas: 1](https://docs.vllm.ai#__codelineno-6-9)[selector:](https://docs.vllm.ai#__codelineno-6-10)[matchLabels:](https://docs.vllm.ai#__codelineno-6-11)[app: mistral-7b](https://docs.vllm.ai#__codelineno-6-12)[template:](https://docs.vllm.ai#__codelineno-6-13)[metadata:](https://docs.vllm.ai#__codelineno-6-14)[labels:](https://docs.vllm.ai#__codelineno-6-15)[app: mistral-7b](https://docs.vllm.ai#__codelineno-6-16)[spec:](https://docs.vllm.ai#__codelineno-6-17)[volumes:](https://docs.vllm.ai#__codelineno-6-18)[# PVC](https://docs.vllm.ai#__codelineno-6-19)[- name: cache-volume](https://docs.vllm.ai#__codelineno-6-20)[persistentVolumeClaim:](https://docs.vllm.ai#__codelineno-6-21)[claimName: mistral-7b](https://docs.vllm.ai#__codelineno-6-22)[# vLLM needs to access the host's shared memory for tensor parallel inference.](https://docs.vllm.ai#__codelineno-6-23)[- name: shm](https://docs.vllm.ai#__codelineno-6-24)[emptyDir:](https://docs.vllm.ai#__codelineno-6-25)[medium: Memory](https://docs.vllm.ai#__codelineno-6-26)[sizeLimit: "8Gi"](https://docs.vllm.ai#__codelineno-6-27)[hostNetwork: true](https://docs.vllm.ai#__codelineno-6-28)[hostIPC: true](https://docs.vllm.ai#__codelineno-6-29)[containers:](https://docs.vllm.ai#__codelineno-6-30)[- name: mistral-7b](https://docs.vllm.ai#__codelineno-6-31)[image: rocm/vllm:rocm6.2_mi300_ubuntu20.04_py3.9_vllm_0.6.4](https://docs.vllm.ai#__codelineno-6-32)[securityContext:](https://docs.vllm.ai#__codelineno-6-33)[seccompProfile:](https://docs.vllm.ai#__codelineno-6-34)[type: Unconfined](https://docs.vllm.ai#__codelineno-6-35)[runAsGroup: 44](https://docs.vllm.ai#__codelineno-6-36)[capabilities:](https://docs.vllm.ai#__codelineno-6-37)[add:](https://docs.vllm.ai#__codelineno-6-38)[- SYS_PTRACE](https://docs.vllm.ai#__codelineno-6-39)[command: ["/bin/sh", "-c"]](https://docs.vllm.ai#__codelineno-6-40)[args: [](https://docs.vllm.ai#__codelineno-6-41)["vllm serve mistralai/Mistral-7B-v0.3 --port 8000 --trust-remote-code --enable-chunked-prefill --max-num-batched-tokens 1024"](https://docs.vllm.ai#__codelineno-6-42)[]](https://docs.vllm.ai#__codelineno-6-43)[env:](https://docs.vllm.ai#__codelineno-6-44)[- name: HF_TOKEN](https://docs.vllm.ai#__codelineno-6-45)[valueFrom:](https://docs.vllm.ai#__codelineno-6-46)[secretKeyRef:](https://docs.vllm.ai#__codelineno-6-47)[name: hf-token-secret](https://docs.vllm.ai#__codelineno-6-48)[key: token](https://docs.vllm.ai#__codelineno-6-49)[ports:](https://docs.vllm.ai#__codelineno-6-50)[- containerPort: 8000](https://docs.vllm.ai#__codelineno-6-51)[resources:](https://docs.vllm.ai#__codelineno-6-52)[limits:](https://docs.vllm.ai#__codelineno-6-53)[cpu: "10"](https://docs.vllm.ai#__codelineno-6-54)[memory: 20G](https://docs.vllm.ai#__codelineno-6-55)[amd.com/gpu: "1"](https://docs.vllm.ai#__codelineno-6-56)[requests:](https://docs.vllm.ai#__codelineno-6-57)[cpu: "6"](https://docs.vllm.ai#__codelineno-6-58)[memory: 6G](https://docs.vllm.ai#__codelineno-6-59)[amd.com/gpu: "1"](https://docs.vllm.ai#__codelineno-6-60)[volumeMounts:](https://docs.vllm.ai#__codelineno-6-61)[- name: cache-volume](https://docs.vllm.ai#__codelineno-6-62)[mountPath: /root/.cache/huggingface](https://docs.vllm.ai#__codelineno-6-63)[- name: shm](https://docs.vllm.ai#__codelineno-6-64)[mountPath: /dev/shm](https://docs.vllm.ai#__codelineno-6-65)You can get the full example with steps and sample yaml files from

[https://github.com/ROCm/k8s-device-plugin/tree/master/example/vllm-serve](https://github.com/ROCm/k8s-device-plugin/tree/master/example/vllm-serve). -
Create a Kubernetes Service for vLLM

Next, create a Kubernetes Service file to expose the

`mistral-7b`

deployment:## Yaml

[apiVersion: v1](https://docs.vllm.ai#__codelineno-7-1)[kind: Service](https://docs.vllm.ai#__codelineno-7-2)[metadata:](https://docs.vllm.ai#__codelineno-7-3)[name: mistral-7b](https://docs.vllm.ai#__codelineno-7-4)[namespace: default](https://docs.vllm.ai#__codelineno-7-5)[spec:](https://docs.vllm.ai#__codelineno-7-6)[ports:](https://docs.vllm.ai#__codelineno-7-7)[- name: http-mistral-7b](https://docs.vllm.ai#__codelineno-7-8)[port: 80](https://docs.vllm.ai#__codelineno-7-9)[protocol: TCP](https://docs.vllm.ai#__codelineno-7-10)[targetPort: 8000](https://docs.vllm.ai#__codelineno-7-11)[# The label selector should match the deployment labels & it is useful for prefix caching feature](https://docs.vllm.ai#__codelineno-7-12)[selector:](https://docs.vllm.ai#__codelineno-7-13)[app: mistral-7b](https://docs.vllm.ai#__codelineno-7-14)[sessionAffinity: None](https://docs.vllm.ai#__codelineno-7-15)[type: ClusterIP](https://docs.vllm.ai#__codelineno-7-16) -
Deploy and Test

Apply the deployment and service configurations using

`kubectl apply -f <filename>`

:To test the deployment, run the following

`curl`

command:[curl http://mistral-7b.default.svc.cluster.local/v1/completions \](https://docs.vllm.ai#__codelineno-9-1)[-H "Content-Type: application/json" \](https://docs.vllm.ai#__codelineno-9-2)[-d '{](https://docs.vllm.ai#__codelineno-9-3)["model": "mistralai/Mistral-7B-Instruct-v0.3",](https://docs.vllm.ai#__codelineno-9-4)["prompt": "San Francisco is a",](https://docs.vllm.ai#__codelineno-9-5)["max_tokens": 7,](https://docs.vllm.ai#__codelineno-9-6)["temperature": 0](https://docs.vllm.ai#__codelineno-9-7)[}'](https://docs.vllm.ai#__codelineno-9-8)If the service is correctly deployed, you should receive a response from the vLLM model.


## Serving with gRPC[¶](https://docs.vllm.ai#serving-with-grpc)

vLLM can serve models over gRPC instead of HTTP by passing the `--grpc`

flag. This requires the optional gRPC dependencies:

When using `--grpc`

, the server exposes the standard [gRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) (`grpc.health.v1.Health`

), which integrates with Kubernetes [native gRPC probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-grpc-liveness-probe) (available since Kubernetes 1.24).

To deploy with gRPC, change the `vllm serve`

command to include `--grpc`

and replace `httpGet`

probes with `grpc`

probes:

containers:
- name: mistral-7b
image: vllm/vllm-openai:latest
command: ["/bin/sh", "-c"]
args: [
"pip install vllm[grpc] && vllm serve mistralai/Mistral-7B-Instruct-v0.3 --grpc --port 50051 --trust-remote-code"
]
ports:
- containerPort: 50051
livenessProbe:
grpc:
port: 50051
initialDelaySeconds: 120
periodSeconds: 10
readinessProbe:
grpc:
port: 50051
initialDelaySeconds: 120
periodSeconds: 5


Note

The gRPC health service checks the engine status on every probe. If the engine is unhealthy or the server is shutting down, the probe returns `NOT_SERVING`

.

You can also verify the health service manually with `grpcurl`

:

## Troubleshooting[¶](https://docs.vllm.ai#troubleshooting)

### Startup Probe or Readiness Probe Failure, container log contains "KeyboardInterrupt: terminated"[¶](https://docs.vllm.ai#startup-probe-or-readiness-probe-failure-container-log-contains-keyboardinterrupt-terminated)

If the startup or readiness probe failureThreshold is too low for the time needed to start up the server, Kubernetes scheduler will kill the container. A couple of indications that this has happened:

- container log contains "KeyboardInterrupt: terminated"
`kubectl get events`

shows message`Container $NAME failed startup probe, will be restarted`


To mitigate, increase the failureThreshold to allow more time for the model server to start serving. You can identify an ideal failureThreshold by removing the probes from the manifest and measuring how much time it takes for the model server to show it's ready to serve.

## Conclusion[¶](https://docs.vllm.ai#conclusion)

Deploying vLLM with Kubernetes allows for efficient scaling and management of ML models leveraging GPU resources. By following the steps outlined above, you should be able to set up and test a vLLM deployment within your Kubernetes cluster. If you encounter any issues or have suggestions, please feel free to contribute to the documentation.