# [Issue #34] DistServe是否支持异构推理？

source: https://github.com/LLMServe/DistServe/issues/34
state: closed | updated: 2024-08-06T02:26:36Z
labels: 

## 正文

我的机器有两张卡，分别是A40和A30，A40拥有48G显存，A30拥有24G显存，使用的模型是Llama-2-7b-chat-hf，精度为fp16。按计算来说两卡应该都能放下，但作为decode机器的A30会报OOM错误。

## 评论 (4)

### RobertLou · 2024-08-05

(ParaWorker pid=85294) Error: Peer-to-peer access is unsupported on this platform.
(ParaWorker pid=85294) In the current version of distserve, it is necessary to use a platform that supports GPU P2P access.
好吧，应该是连接的问题？这里的P2P访问是指NVlink吗,我使用nvidia-smi topo -m查询得知我的GPU之间需要通过PCIe进行传输数据。

### RobertLou · 2024-08-05

好吧，我查到SwiftTransformer中的报错了，看上去确实必须Nvlink？如果走PCIe就得先到CPU上数据转一圈？

### ddqspace-xyz · 2024-08-06

意思是运行DistServe环境，必须是支持NVlink的GPU才可以？

### RobertLou · 2024-08-06

> 意思是运行DistServe环境，必须是支持NVlink的GPU才可以？

是的吧，其他的互联方式Infiniband和高速网卡连接什么的我不了解，从代码上来看主要是cudaIpcOpenMemHandle和cudaMemcpy2DAsync这两个接口，我这边两卡没有直接互连就会报错。
