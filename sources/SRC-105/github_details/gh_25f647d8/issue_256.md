# [Issue #256] Can dcgm-exporter collect the POD gpu usage metrics in K8S?

source: https://github.com/NVIDIA/DCGM/issues/256
state: open | updated: 2025-09-30T09:21:20Z
labels: 

## 正文

Hi 
   I didn't find the GPU usage mertics at POD level,it only collect the each gpu card usage metrics in total.

We want to monitor how many gpu resource is used for every k8s pod .

image: nvcr.io/nvidia/k8s/dcgm-exporter:4.2.3-4.1.3-ubuntu22.04 

## 评论 (1)

### geniuslc11 · 2025-09-30

Is there anyone working on this issue?

<img width="1905" height="462" alt="Image" src="https://github.com/user-attachments/assets/2c95201a-df2c-4931-b5df-eea417dca981" />

All the monitored metrics the namespace is the same "monitoring" ,the pod label is the same "dcgm-exporter-1749543171-tzq4s ",not the actual application pods name
