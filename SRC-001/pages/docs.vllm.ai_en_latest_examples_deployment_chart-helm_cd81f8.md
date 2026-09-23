source: https://docs.vllm.ai/en/latest/examples/deployment/chart-helm/
lastmod: 2026-09-23

# Helm Charts[¶](https://docs.vllm.ai#helm-charts)

Source [https://github.com/vllm-project/vllm/tree/main/examples/deployment/chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/deployment/chart-helm).

This directory contains a Helm chart for deploying the vllm application. The chart includes configurations for deployment, autoscaling, resource management, and more.

## Files[¶](https://docs.vllm.ai#files)

- Chart.yaml: Defines the chart metadata including name, version, and maintainers.
- ct.yaml: Configuration for chart testing.
- lintconf.yaml: Linting rules for YAML files.
- values.schema.json: JSON schema for validating values.yaml.
- values.yaml: Default values for the Helm chart.
- templates/_helpers.tpl: Helper templates for defining common configurations.
- templates/configmap.yaml: Template for creating ConfigMaps.
- templates/custom-objects.yaml: Template for custom Kubernetes objects.
- templates/deployment.yaml: Template for creating Deployments.
- templates/hpa.yaml: Template for Horizontal Pod Autoscaler.
- templates/job.yaml: Template for Kubernetes Jobs.
- templates/poddisruptionbudget.yaml: Template for Pod Disruption Budget.
- templates/pvc.yaml: Template for Persistent Volume Claims.
- templates/secrets.yaml: Template for Kubernetes Secrets.
- templates/service.yaml: Template for creating Services.

## Running Tests[¶](https://docs.vllm.ai#running-tests)

This chart includes unit tests using [helm-unittest](https://github.com/helm-unittest/helm-unittest). Install the plugin and run tests:

# Install plugin
helm plugin install https://github.com/helm-unittest/helm-unittest
# Run tests
helm unittest .


## Example materials[¶](https://docs.vllm.ai#example-materials)

## Chart.yaml

apiVersion: v2
name: chart-vllm
description: Chart vllm
# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and therefore cannot be deployed.
type: application
# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
# Versions are expected to follow Semantic Versioning (https://semver.org/)
version: 0.0.2
maintainers:
- name: mfournioux


## lintconf.yaml

---
rules:
braces:
min-spaces-inside: 0
max-spaces-inside: 0
min-spaces-inside-empty: -1
max-spaces-inside-empty: -1
brackets:
min-spaces-inside: 0
max-spaces-inside: 0
min-spaces-inside-empty: -1
max-spaces-inside-empty: -1
colons:
max-spaces-before: 0
max-spaces-after: 1
commas:
max-spaces-before: 0
min-spaces-after: 1
max-spaces-after: 1
comments:
require-starting-space: true
min-spaces-from-content: 2
document-end: disable
document-start: disable # No --- to start a file
empty-lines:
max: 2
max-start: 0
max-end: 0
hyphens:
max-spaces-after: 1
indentation:
spaces: consistent
indent-sequences: whatever # - list indentation will handle both indentation and without
check-multi-line-strings: false
key-duplicates: enable
line-length: disable # Lines can be any length
new-line-at-end-of-file: disable
new-lines:
type: unix
trailing-spaces: enable
truthy:
level: warning


## templates/_helpers.tpl

{{/*
Define ports for the pods
*/}}
{{- define "chart.container-port" -}}
{{- default "8000" .Values.containerPort }}
{{- end }}
{{/*
Define service name
*/}}
{{- define "chart.service-name" -}}
{{- if .Values.serviceName }}
{{- .Values.serviceName | lower | trim }}
{{- else }}
{{- printf "%s-service" .Release.Name }}
{{- end }}
{{- end }}
{{/*
Define deployment name
*/}}
{{- define "chart.deployment-name" -}}
{{- printf "%s-deployment-vllm" .Release.Name }}
{{- end }}
{{/*
Define service port
*/}}
{{- define "chart.service-port" -}}
{{- if .Values.servicePort }}
{{- .Values.servicePort }}
{{- else }}
{{- include "chart.container-port" . }}
{{- end }}
{{- end }}
{{/*
Define service port name
*/}}
{{- define "chart.service-port-name" -}}
"service-port"
{{- end }}
{{/*
Define container port name
*/}}
{{- define "chart.container-port-name" -}}
"container-port"
{{- end }}
{{/*
Define deployment strategy
*/}}
{{- define "chart.strategy" -}}
strategy:
{{- if not .Values.deploymentStrategy }}
rollingUpdate:
maxSurge: 100%
maxUnavailable: 0
{{- else }}
{{ toYaml .Values.deploymentStrategy | indent 2 }}
{{- end }}
{{- end }}
{{/*
Define additional ports
*/}}
{{- define "chart.extraPorts" }}
{{- with .Values.extraPorts }}
{{ toYaml . }}
{{- end }}
{{- end }}
{{/*
Define chart external ConfigMaps and Secrets
*/}}
{{- define "chart.externalConfigs" -}}
{{- with .Values.externalConfigs -}}
{{ toYaml . }}
{{- end }}
{{- end }}
{{/*
Define liveness et readiness probes
*/}}
{{- define "chart.probes" -}}
{{- if .Values.readinessProbe }}
readinessProbe:
{{- with .Values.readinessProbe }}
{{- toYaml . | nindent 2 }}
{{- end }}
{{- end }}
{{- if .Values.livenessProbe }}
livenessProbe:
{{- with .Values.livenessProbe }}
{{- toYaml . | nindent 2 }}
{{- end }}
{{- end }}
{{- end }}
{{/*
Define resources
*/}}
{{- define "chart.resources" -}}
requests:
memory: {{ required "Value 'resources.requests.memory' must be defined !" .Values.resources.requests.memory | quote }}
cpu: {{ required "Value 'resources.requests.cpu' must be defined !" .Values.resources.requests.cpu | quote }}
{{- if and (gt (int (index .Values.resources.requests "nvidia.com/gpu")) 0) (gt (int (index .Values.resources.limits "nvidia.com/gpu")) 0) }}
nvidia.com/gpu: {{ required "Value 'resources.requests.nvidia.com/gpu' must be defined !" (index .Values.resources.requests "nvidia.com/gpu") | quote }}
{{- end }}
limits:
memory: {{ required "Value 'resources.limits.memory' must be defined !" .Values.resources.limits.memory | quote }}
cpu: {{ required "Value 'resources.limits.cpu' must be defined !" .Values.resources.limits.cpu | quote }}
{{- if and (gt (int (index .Values.resources.requests "nvidia.com/gpu")) 0) (gt (int (index .Values.resources.limits "nvidia.com/gpu")) 0) }}
nvidia.com/gpu: {{ required "Value 'resources.limits.nvidia.com/gpu' must be defined !" (index .Values.resources.limits "nvidia.com/gpu") | quote }}
{{- end }}
{{- end }}
{{/*
Define User used for the main container
*/}}
{{- define "chart.user" }}
{{- if .Values.image.runAsUser }}
runAsUser:
{{- with .Values.runAsUser }}
{{- toYaml . | nindent 2 }}
{{- end }}
{{- end }}
{{- end }}
{{- define "chart.extraInitEnv" -}}
- name: S3_ENDPOINT_URL
valueFrom:
secretKeyRef:
name: {{ .Release.Name }}-secrets
key: s3endpoint
- name: S3_BUCKET_NAME
valueFrom:
secretKeyRef:
name: {{ .Release.Name }}-secrets
key: s3bucketname
- name: AWS_ACCESS_KEY_ID
valueFrom:
secretKeyRef:
name: {{ .Release.Name }}-secrets
key: s3accesskeyid
- name: AWS_SECRET_ACCESS_KEY
valueFrom:
secretKeyRef:
name: {{ .Release.Name }}-secrets
key: s3accesskey
{{- if .Values.extraInit.s3modelpath }}
- name: S3_PATH
value: "{{ .Values.extraInit.s3modelpath }}"
{{- end }}
{{- if hasKey .Values.extraInit "awsEc2MetadataDisabled" }}
- name: AWS_EC2_METADATA_DISABLED
value: "{{ .Values.extraInit.awsEc2MetadataDisabled }}"
{{- end }}
{{- end }}
{{/*
Define chart labels
*/}}
{{- define "chart.labels" -}}
{{- with .Values.labels -}}
{{ toYaml . }}
{{- end }}
{{- end }}


## templates/configmap.yaml

## templates/custom-objects.yaml

## templates/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
name: {{ include "chart.deployment-name" . | quote }}
namespace: {{ .Release.Namespace }}
labels:
{{- include "chart.labels" . | nindent 4 }}
spec:
replicas: {{ .Values.replicaCount }}
{{- include "chart.strategy" . | nindent 2 }}
selector:
matchLabels:
{{- include "chart.labels" . | nindent 6 }}
progressDeadlineSeconds: 1200
template:
metadata:
labels:
{{- include "chart.labels" . | nindent 8 }}
spec:
containers:
- name: "vllm"
image: "{{ required "Required value 'image.repository' must be defined !" .Values.image.repository }}:{{ required "Required value 'image.tag' must be defined !" .Values.image.tag }}"
{{- if .Values.image.command }}
command :
{{- with .Values.image.command }}
{{- toYaml . | nindent 10 }}
{{- end }}
{{- end }}
securityContext:
{{- if .Values.image.securityContext }}
{{- with .Values.image.securityContext }}
{{- toYaml . | nindent 12 }}
{{- end }}
{{- else }}
runAsNonRoot: false
{{- include "chart.user" . | indent 12 }}
{{- end }}
imagePullPolicy: IfNotPresent
{{- if .Values.image.env }}
env :
{{- with .Values.image.env }}
{{- toYaml . | nindent 10 }}
{{- end }}
{{- else }}
env: []
{{- end }}
{{- if or .Values.externalConfigs .Values.configs .Values.secrets }}
envFrom:
{{- if .Values.configs }}
- configMapRef:
name: "{{ .Release.Name }}-configs"
{{- end }}
{{- if .Values.secrets}}
- secretRef:
name: "{{ .Release.Name }}-secrets"
{{- end }}
{{- include "chart.externalConfigs" . | nindent 12 }}
{{- end }}
ports:
- name: {{ include "chart.container-port-name" . }}
containerPort: {{ include "chart.container-port" . }}
{{- include "chart.extraPorts" . | nindent 12 }}
{{- include "chart.probes" . | indent 10 }}
resources: {{- include "chart.resources" . | nindent 12 }}
volumeMounts:
- name: {{ .Release.Name }}-storage
mountPath: /data
{{- with .Values.extraContainers }}
{{ toYaml . | nindent 8 }}
{{- end }}
{{- if and .Values.extraInit (or .Values.extraInit.modelDownload.enabled .Values.extraInit.initContainers) }}
initContainers:
{{- if .Values.extraInit.modelDownload.enabled }}
- name: wait-download-model
image: {{ .Values.extraInit.modelDownload.image.repository }}:{{ .Values.extraInit.modelDownload.image.tag }}
imagePullPolicy: {{ .Values.extraInit.modelDownload.image.pullPolicy }}
command: {{ .Values.extraInit.modelDownload.waitContainer.command | toJson }}
args:
{{- toYaml .Values.extraInit.modelDownload.waitContainer.args | nindent 10 }}
env:
{{- if .Values.extraInit.modelDownload.waitContainer.env }}
{{- toYaml .Values.extraInit.modelDownload.waitContainer.env | nindent 10 }}
{{- else }}
{{- include "chart.extraInitEnv" . | nindent 10 }}
{{- end }}
resources:
requests:
cpu: 200m
memory: 1Gi
limits:
cpu: 500m
memory: 2Gi
volumeMounts:
- name: {{ .Release.Name }}-storage
mountPath: /data
{{- end }}
{{- with .Values.extraInit.initContainers }}
{{- toYaml . | nindent 6 }}
{{- end }}
{{- end }}
volumes:
- name: {{ .Release.Name }}-storage
persistentVolumeClaim:
claimName: {{ .Release.Name }}-storage-claim
{{- with .Values.nodeSelector }}
nodeSelector:
{{- toYaml . | nindent 8 }}
{{- end }}
{{- with .Values.tolerations }}
tolerations:
{{- toYaml . | nindent 8 }}
{{- end }}
{{- if and (gt (int (index .Values.resources.requests "nvidia.com/gpu")) 0) (gt (int (index .Values.resources.limits "nvidia.com/gpu")) 0) }}
runtimeClassName: nvidia
affinity:
nodeAffinity:
requiredDuringSchedulingIgnoredDuringExecution:
nodeSelectorTerms:
- matchExpressions:
- key: nvidia.com/gpu.product
operator: In
{{- with .Values.gpuModels }}
values:
{{- toYaml . | nindent 20 }}
{{- end }}
{{- end }}


## templates/hpa.yaml

{{- if .Values.autoscaling.enabled }}
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
name: "{{ .Release.Name }}-hpa"
namespace: {{ .Release.Namespace }}
spec:
scaleTargetRef:
apiVersion: apps/v1
kind: Deployment
name: {{ include "chart.deployment-name" . | quote }}
minReplicas: {{ .Values.autoscaling.minReplicas }}
maxReplicas: {{ .Values.autoscaling.maxReplicas }}
metrics:
{{- if .Values.autoscaling.targetCPUUtilizationPercentage }}
- type: Resource
resource:
name: cpu
target:
type: Utilization
averageUtilization: {{ .Values.autoscaling.targetCPUUtilizationPercentage }}
{{- end }}
{{- if .Values.autoscaling.targetMemoryUtilizationPercentage }}
- type: Resource
resource:
name: memory
target:
type: Utilization
averageUtilization: {{ .Values.autoscaling.targetMemoryUtilizationPercentage }}
{{- end }}
{{- end }}


## templates/job.yaml

{{- if and .Values.extraInit .Values.extraInit.modelDownload.enabled }}
apiVersion: batch/v1
kind: Job
metadata:
name: "{{ .Release.Name }}-init-vllm"
namespace: {{ .Release.Namespace }}
spec:
ttlSecondsAfterFinished: 100
template:
metadata:
name: init-vllm
spec:
containers:
- name: job-download-model
image: {{ .Values.extraInit.modelDownload.image.repository }}:{{ .Values.extraInit.modelDownload.image.tag }}
imagePullPolicy: {{ .Values.extraInit.modelDownload.image.pullPolicy }}
command: {{ .Values.extraInit.modelDownload.downloadJob.command | toJson }}
args:
{{- toYaml .Values.extraInit.modelDownload.downloadJob.args | nindent 8 }}
env:
{{- if .Values.extraInit.modelDownload.downloadJob.env }}
{{- toYaml .Values.extraInit.modelDownload.downloadJob.env | nindent 8 }}
{{- else }}
{{- include "chart.extraInitEnv" . | nindent 8 }}
{{- end }}
volumeMounts:
- name: {{ .Release.Name }}-storage
mountPath: /data
resources:
requests:
cpu: 200m
memory: 1Gi
limits:
cpu: 500m
memory: 2Gi
restartPolicy: OnFailure
volumes:
- name: {{ .Release.Name }}-storage
persistentVolumeClaim:
claimName: "{{ .Release.Name }}-storage-claim"
{{- end }}


## templates/poddisruptionbudget.yaml

## templates/pvc.yaml

## templates/secrets.yaml

## templates/service.yaml

apiVersion: v1
kind: Service
metadata:
name: {{ include "chart.service-name" . | quote }}
namespace: {{ .Release.Namespace }}
spec:
type: ClusterIP
ports:
- name: {{ include "chart.service-port-name" . }}
port: {{ include "chart.service-port" . }}
targetPort: {{ include "chart.container-port-name" . }}
protocol: TCP
selector:
{{- include "chart.labels" . | nindent 4 }}


## tests/deployment_test.yaml

suite: test deployment
templates:
- deployment.yaml
tests:
- it: should use configured labels for the deployment selector and pods
set:
labels:
environment: production
release: qwen-serving
asserts:
- equal:
path: spec.selector.matchLabels
value:
environment: production
release: qwen-serving
- equal:
path: spec.template.metadata.labels
value:
environment: production
release: qwen-serving
- it: should create wait-download-model init container when modelDownload is enabled
set:
extraInit:
modelDownload:
enabled: true
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: [ "/bin/bash" ]
args:
- "-eucx"
- "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
downloadJob:
command: [ "/bin/bash" ]
args:
- "-eucx"
- "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
initContainers: [ ]
pvcStorage: "1Gi"
s3modelpath: "relative_s3_model_path/opt-125m"
awsEc2MetadataDisabled: true
asserts:
- hasDocuments:
count: 1
- isKind:
of: Deployment
- isNotEmpty:
path: spec.template.spec.initContainers
- equal:
path: spec.template.spec.initContainers[0].name
value: wait-download-model
- equal:
path: spec.template.spec.initContainers[0].image
value: amazon/aws-cli:2.6.4
- equal:
path: spec.template.spec.initContainers[0].imagePullPolicy
value: IfNotPresent
- it: should only create custom init containers when modelDownload is disabled
set:
extraInit:
modelDownload:
enabled: false
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: [ "/bin/bash" ]
args: [ "-c", "echo test" ]
downloadJob:
command: [ "/bin/bash" ]
args: [ "-c", "echo test" ]
initContainers:
- name: llm-d-routing-proxy
image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
imagePullPolicy: IfNotPresent
ports:
- containerPort: 8080
name: proxy
pvcStorage: "10Gi"
asserts:
- hasDocuments:
count: 1
- isKind:
of: Deployment
- lengthEqual:
path: spec.template.spec.initContainers
count: 1
- equal:
path: spec.template.spec.initContainers[0].name
value: llm-d-routing-proxy
- equal:
path: spec.template.spec.initContainers[0].image
value: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
- equal:
path: spec.template.spec.initContainers[0].ports[0].containerPort
value: 8080
- it: should create both wait-download-model and custom init containers when both are enabled
set:
extraInit:
modelDownload:
enabled: true
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: [ "/bin/bash" ]
args:
- "-eucx"
- "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
downloadJob:
command: [ "/bin/bash" ]
args:
- "-eucx"
- "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
initContainers:
- name: llm-d-routing-proxy
image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
imagePullPolicy: IfNotPresent
ports:
- containerPort: 8080
name: proxy
pvcStorage: "10Gi"
asserts:
- hasDocuments:
count: 1
- isKind:
of: Deployment
- lengthEqual:
path: spec.template.spec.initContainers
count: 2
- equal:
path: spec.template.spec.initContainers[0].name
value: wait-download-model
- equal:
path: spec.template.spec.initContainers[0].image
value: amazon/aws-cli:2.6.4
- equal:
path: spec.template.spec.initContainers[1].name
value: llm-d-routing-proxy
- equal:
path: spec.template.spec.initContainers[1].image
value: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
- equal:
path: spec.template.spec.initContainers[1].ports[0].containerPort
value: 8080


## tests/hpa_test.yaml

suite: test horizontal pod autoscaler
templates:
- hpa.yaml
release:
name: demo
tests:
- it: should target the deployment created by this release
set:
autoscaling:
enabled: true
minReplicas: 1
maxReplicas: 3
targetCPUUtilizationPercentage: 80
asserts:
- equal:
path: spec.scaleTargetRef.name
value: demo-deployment-vllm


## tests/job_test.yaml

suite: test job
templates:
- job.yaml
tests:
- it: should create job when modelDownload is enabled
set:
extraInit:
modelDownload:
enabled: true
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: [ "/bin/bash" ]
args: [ "-c", "wait" ]
downloadJob:
command: [ "/bin/bash" ]
args:
- "-eucx"
- "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
pvcStorage: "1Gi"
s3modelpath: "relative_s3_model_path/opt-125m"
awsEc2MetadataDisabled: true
asserts:
- hasDocuments:
count: 1
- isKind:
of: Job
- equal:
path: spec.template.spec.containers[0].name
value: job-download-model
- equal:
path: spec.template.spec.containers[0].image
value: amazon/aws-cli:2.6.4
- equal:
path: spec.template.spec.restartPolicy
value: OnFailure
- it: should not create job when modelDownload is disabled
set:
extraInit:
modelDownload:
enabled: false
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: [ "/bin/bash" ]
args: [ "-c", "wait" ]
downloadJob:
command: [ "/bin/bash" ]
args: [ "-c", "download" ]
initContainers:
- name: llm-d-routing-proxy
image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
pvcStorage: "10Gi"
asserts:
- hasDocuments:
count: 0


## tests/pvc_test.yaml

suite: test pvc
templates:
- pvc.yaml
tests:
# Test Case: PVC Created When extraInit Defined
- it: should create pvc when extraInit is defined
set:
extraInit:
modelDownload:
enabled: true
image:
repository: "amazon/aws-cli"
tag: "2.6.4"
pullPolicy: "IfNotPresent"
waitContainer:
command: ["/bin/bash"]
args: ["-c", "wait"]
downloadJob:
command: ["/bin/bash"]
args: ["-c", "download"]
pvcStorage: "10Gi"
asserts:
- hasDocuments:
count: 1
- isKind:
of: PersistentVolumeClaim
- equal:
path: spec.accessModes[0]
value: ReadWriteOnce
- equal:
path: spec.resources.requests.storage
value: 10Gi


## tests/service_test.yaml

suite: test service
templates:
- service.yaml
release:
name: demo
tests:
- it: should honor the configured service name
set:
serviceName: vllm-api
asserts:
- equal:
path: metadata.name
value: vllm-api
- it: should select pods using the configured labels
set:
labels:
environment: production
release: qwen-serving
asserts:
- equal:
path: spec.selector
value:
environment: production
release: qwen-serving


## values.schema.json

{
"$schema": "http://json-schema.org/schema#",
"type": "object",
"properties": {
"image": {
"type": "object",
"properties": {
"repository": {
"type": "string"
},
"tag": {
"type": "string"
},
"command": {
"type": "array",
"items": {
"type": "string"
}
}
},
"required": [
"command",
"repository",
"tag"
]
},
"containerPort": {
"type": "integer"
},
"serviceName": {
"type": [
"null",
"string"
]
},
"servicePort": {
"type": "integer"
},
"extraPorts": {
"type": "array"
},
"replicaCount": {
"type": "integer"
},
"deploymentStrategy": {
"type": "object"
},
"resources": {
"type": "object",
"properties": {
"requests": {
"type": "object",
"properties": {
"cpu": {
"type": "integer"
},
"memory": {
"type": "string"
},
"nvidia.com/gpu": {
"type": "integer"
}
},
"required": [
"cpu",
"memory",
"nvidia.com/gpu"
]
},
"limits": {
"type": "object",
"properties": {
"cpu": {
"type": "integer"
},
"memory": {
"type": "string"
},
"nvidia.com/gpu": {
"type": "integer"
}
},
"required": [
"cpu",
"memory",
"nvidia.com/gpu"
]
}
},
"required": [
"limits",
"requests"
]
},
"gpuModels": {
"type": "array",
"items": {
"type": "string"
}
},
"autoscaling": {
"type": "object",
"properties": {
"enabled": {
"type": "boolean"
},
"minReplicas": {
"type": "integer"
},
"maxReplicas": {
"type": "integer"
},
"targetCPUUtilizationPercentage": {
"type": "integer"
}
},
"required": [
"enabled",
"maxReplicas",
"minReplicas",
"targetCPUUtilizationPercentage"
]
},
"configs": {
"type": "object"
},
"secrets": {
"type": "object"
},
"externalConfigs": {
"type": "array"
},
"customObjects": {
"type": "array"
},
"maxUnavailablePodDisruptionBudget": {
"type": "string"
},
"extraInit": {
"type": "object",
"properties": {
"modelDownload": {
"type": "object",
"properties": {
"enabled": {
"type": "boolean"
},
"image": {
"type": "object",
"properties": {
"repository": {
"type": "string"
},
"tag": {
"type": "string"
},
"pullPolicy": {
"type": "string"
}
},
"required": ["repository", "tag", "pullPolicy"]
},
"waitContainer": {
"type": "object",
"properties": {
"command": {
"type": "array",
"items": {"type": "string"}
},
"args": {
"type": "array",
"items": {"type": "string"}
},
"env": {
"type": "array",
"items": {"type": "object"}
}
},
"required": ["command", "args"]
},
"downloadJob": {
"type": "object",
"properties": {
"command": {
"type": "array",
"items": {"type": "string"}
},
"args": {
"type": "array",
"items": {"type": "string"}
},
"env": {
"type": "array",
"items": {"type": "object"}
}
},
"required": ["command", "args"]
}
},
"required": ["enabled", "image", "waitContainer", "downloadJob"]
},
"initContainers": {
"type": "array",
"items": {"type": "object"}
},
"s3modelpath": {
"type": "string"
},
"pvcStorage": {
"type": "string"
},
"awsEc2MetadataDisabled": {
"type": "boolean"
}
},
"required": [
"modelDownload",
"initContainers",
"pvcStorage"
]
},
"extraContainers": {
"type": "array"
},
"readinessProbe": {
"type": "object",
"properties": {
"initialDelaySeconds": {
"type": "integer"
},
"periodSeconds": {
"type": "integer"
},
"failureThreshold": {
"type": "integer"
},
"httpGet": {
"type": "object",
"properties": {
"path": {
"type": "string"
},
"port": {
"type": "integer"
}
},
"required": [
"path",
"port"
]
}
},
"required": [
"failureThreshold",
"httpGet",
"initialDelaySeconds",
"periodSeconds"
]
},
"livenessProbe": {
"type": "object",
"properties": {
"initialDelaySeconds": {
"type": "integer"
},
"failureThreshold": {
"type": "integer"
},
"periodSeconds": {
"type": "integer"
},
"httpGet": {
"type": "object",
"properties": {
"path": {
"type": "string"
},
"port": {
"type": "integer"
}
},
"required": [
"path",
"port"
]
}
},
"required": [
"failureThreshold",
"httpGet",
"initialDelaySeconds",
"periodSeconds"
]
},
"labels": {
"type": "object",
"properties": {
"environment": {
"type": "string"
},
"release": {
"type": "string"
}
},
"required": [
"environment",
"release"
]
}
},
"required": [
"autoscaling",
"configs",
"containerPort",
"customObjects",
"deploymentStrategy",
"externalConfigs",
"extraContainers",
"extraInit",
"extraPorts",
"gpuModels",
"image",
"labels",
"livenessProbe",
"maxUnavailablePodDisruptionBudget",
"readinessProbe",
"replicaCount",
"resources",
"secrets",
"servicePort"
]
}


## values.yaml

# -- Default values for chart vllm
# -- Declare variables to be passed into your templates.
# -- Image configuration
image:
# -- Image repository
repository: "vllm/vllm-openai"
# -- Image tag
tag: "latest"
# -- Container launch command
command: ["vllm", "serve", "/data/", "--served-model-name", "opt-125m", "--enforce-eager", "--dtype", "bfloat16", "--block-size", "16", "--host", "0.0.0.0", "--port", "8000"]
# -- Container port
containerPort: 8000
# -- Service name
serviceName:
# -- Service port
servicePort: 80
# -- Additional ports configuration
extraPorts: []
# -- Number of replicas
replicaCount: 1
# -- Deployment strategy configuration
deploymentStrategy: {}
# -- Resource configuration
resources:
requests:
# -- Number of CPUs
cpu: 4
# -- CPU memory configuration
memory: 16Gi
# -- Number of gpus used
nvidia.com/gpu: 1
limits:
# -- Number of CPUs
cpu: 4
# -- CPU memory configuration
memory: 16Gi
# -- Number of gpus used
nvidia.com/gpu: 1
# -- Type of gpu used
gpuModels:
- "TYPE_GPU_USED"
# -- Autoscaling configuration
autoscaling:
# -- Enable autoscaling
enabled: false
# -- Minimum replicas
minReplicas: 1
# -- Maximum replicas
maxReplicas: 100
# -- Target CPU utilization for autoscaling
targetCPUUtilizationPercentage: 80
# targetMemoryUtilizationPercentage: 80
# -- Configmap
configs: {}
# -- Secrets configuration
secrets: {}
# -- External configuration
externalConfigs: []
# -- Custom Objects configuration
customObjects: []
# -- Disruption Budget Configuration
maxUnavailablePodDisruptionBudget: ""
# -- Additional configuration for the init container
extraInit:
# -- Model download functionality (optional)
modelDownload:
# -- Enable model download job and wait container
enabled: true
# -- Image configuration for model download operations
image:
# -- Image repository
repository: "amazon/aws-cli"
# -- Image tag
tag: "2.6.4"
# -- Image pull policy
pullPolicy: "IfNotPresent"
# -- Wait container configuration (init container that waits for model to be ready)
waitContainer:
# -- Command to execute
command: ["/bin/bash"]
# -- Arguments for the wait container
args:
- "-eucx"
- "while aws --endpoint-url $S3_ENDPOINT_URL s3 sync --dryrun s3://$S3_BUCKET_NAME/$S3_PATH /data | grep -q download; do sleep 10; done"
# -- Environment variables (optional, overrides S3 defaults entirely if specified)
# env:
# - name: HUGGING_FACE_HUB_TOKEN
# value: "your-token"
# - name: MODEL_ID
# value: "meta-llama/Llama-2-7b"
# -- Download job configuration (job that actually downloads the model)
downloadJob:
# -- Command to execute
command: ["/bin/bash"]
# -- Arguments for the download job
args:
- "-eucx"
- "aws --endpoint-url $S3_ENDPOINT_URL s3 sync s3://$S3_BUCKET_NAME/$S3_PATH /data"
# -- Environment variables (optional, overrides S3 defaults entirely if specified)
# env:
# - name: HUGGING_FACE_HUB_TOKEN
# value: "your-token"
# - name: MODEL_ID
# value: "meta-llama/Llama-2-7b"
# -- Custom init containers (appended after wait-download-model if modelDownload is enabled)
initContainers: []
# Example for llm-d sidecar:
# initContainers:
# - name: llm-d-routing-proxy
# image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
# imagePullPolicy: IfNotPresent
# ports:
# - containerPort: 8080
# name: proxy
# securityContext:
# runAsUser: 1000
# -- Path of the model on the s3 which hosts model weights and config files
s3modelpath: "relative_s3_model_path/opt-125m"
# -- Storage size for the PVC
pvcStorage: "1Gi"
# -- Disable AWS EC2 metadata service
awsEc2MetadataDisabled: true
# -- Additional containers configuration
extraContainers: []
# -- Readiness probe configuration
readinessProbe:
# -- Number of seconds after the container has started before readiness probe is initiated
initialDelaySeconds: 5
# -- How often (in seconds) to perform the readiness probe
periodSeconds: 5
# -- Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not ready
failureThreshold: 3
# -- Configuration of the Kubelet http request on the server
httpGet:
# -- Path to access on the HTTP server
path: /health
# -- Name or number of the port to access on the container, on which the server is listening
port: 8000
# -- Liveness probe configuration
livenessProbe:
# -- Number of seconds after the container has started before liveness probe is initiated
initialDelaySeconds: 15
# -- Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not alive
failureThreshold: 3
# -- How often (in seconds) to perform the liveness probe
periodSeconds: 10
# -- Configuration of the Kubelet http request on the server
httpGet:
# -- Path to access on the HTTP server
path: /health
# -- Name or number of the port to access on the container, on which the server is listening
port: 8000
labels:
environment: "test"
release: "test"