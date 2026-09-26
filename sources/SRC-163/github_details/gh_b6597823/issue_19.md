# [Issue #19] codellama34b ttft延迟问题

source: https://github.com/LLMServe/DistServe/issues/19
state: open | updated: 2024-07-17T03:36:35Z
labels: question

## 正文

你好，在最近的测试中，我在A100上测试Llama-13b、7b等模型，对比vllm和distserve, 在满足slo的情况下， distserve性能要优于vllm，但是在测试codellama-34b过程中，当我的输入长度为8192，发现TTFT要高出vllm约3倍左右，请问这个情况是正常的吗？vllm使用tp2, distserve使用prefill tp2, decode tp2。

## 评论 (7)

### PKUFlyingPig · 2024-07-02

不太正常，您测试的机器有 NVLINK 吗？

### sitabulaixizawaluduo · 2024-07-03

> 不太正常，您测试的机器有 NVLINK 吗？

有的，目前除了这个模型之外，测试的其他尺寸包括（1b、7b、13b）的TTFT都是要优于vllm的，这个是否与codellama-34b使用了GQA有关

### PKUFlyingPig · 2024-07-03

GQA应该不会影响 TTFT 的时间，可能是新版本的 vllm 针对长 conext 的 prefill kernel 有了新的优化，你可以做一下单 request 的 profiling 看看。

### sitabulaixizawaluduo · 2024-07-03

> GQA应该不会影响 TTFT 的时间，可能是新版本的 vllm 针对长 conext 的 prefill kernel 有了新的优化，你可以做一下单 request 的 profiling 看看。
这个是我部署时使用的参数
--context-pipeline-parallel-size 2 
--decoding-tensor-parallel-size 2 
--max-num-blocks-per-req 1024 
--context-max-tokens-per-batch 16384(8192也试过)
34B在distserve上输入为4096时时间TTFT感觉依旧不太正常，需要13s

### PKUFlyingPig · 2024-07-03

能提供下你测试用的 vllm 版本号吗

### sitabulaixizawaluduo · 2024-07-03

> 能提供下你测试用的 vllm 版本号吗

0.5.0post1, 可以直接从docker hub上拉最新的镜像

### lcvcl · 2024-07-17

我这边测试llama3 70b，速度也是没vllm快的，不管是ttft还是throughput，应该是vllm自己做了一波优化
