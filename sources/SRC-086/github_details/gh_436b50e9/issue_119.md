# [Issue #119] [Retraining] Use Liger Kernel to avoid multi-head logits materialization and scale the context length by N times

source: https://github.com/FasterDecoding/Medusa/issues/119
state: open | updated: 2024-08-26T05:23:37Z
labels: 

## 正文

https://github.com/linkedin/Liger-Kernel/tree/main/examples/medusa

With the implementation of FusedLinearCrossEntropy and other kernels in Liger-Kernel, we are able to effectively reduce the memory while increase the throughput. We are happy to collaborate and integrate with our kernels! 

![image](https://github.com/user-attachments/assets/da70dff7-e0b7-4be1-8b8c-a83a4ab82f8f)
![image](https://github.com/user-attachments/assets/3719d649-1210-43e3-919a-cd1f3850ea25)


## 评论 (1)

### ByronHsu · 2024-08-26

cc @ctlllll @leeyeehoo @zhyncs 
