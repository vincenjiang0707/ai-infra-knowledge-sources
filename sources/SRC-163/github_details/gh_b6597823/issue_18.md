# [Issue #18] 一些关于TTFT的问题

source: https://github.com/LLMServe/DistServe/issues/18
state: closed | updated: 2024-06-25T06:07:29Z
labels: question

## 正文

请问，你们在做prefill的时候是否会只做prefill，还是会出现prefill和decode混合执行的情况

我对您的vllm的理解是这样的：优先TTFT，也就是说有了prefill的request会优先执行prefill，prefill和decode是不会混合执行的，每次生成一个token的时候进行一次调度，我执行的是您在readme中写的distserve-baseline-vllm分支

基于这样的理解，我没有想清楚，为什么TTFT会加快，对于distserve-prefill-66B而言，distserve-prefill采用tp4，vllm也采用tp4，vllm优先执行TTFT，那为什么distserve会提升TTFT呢

感谢您的回答

## 评论 (6)

### PKUFlyingPig · 2024-06-25

1. 只会做 prefill
2. 您的理解是对的，vllm本身也是这么实现的
3. 提升来自几个方面：（1）prefill 阶段的 kernel 算子性能；（2）rate 高了之后由于排队 vllm 无法及时处理 prefill 导致会将 queue 中的多个 prefill batch 在一起进行计算

### YLSnowy · 2024-06-25

（1）我看到您确实自己实现了算子，但我看到您在vllm中也调用了新的算子，我以为二者最终调用的kernel是一致的，如果不一致并且收益来源于kernel的变化，这样的比较是否不公平？
（2）rate高了之后，我发现在实验中您为了保证相对公平，distserve的rate始终为vllm的2倍（66B的背景下，4张卡 vs 8张卡），因此，rate提高之后，distserve的排队情况会更激烈，导致distserve会出现更多的prefill batch一起计算，但是prefill，vllm和distserve均为tp4，所以理论而言应该是distserve的TTFT latency高一些？
（3）所以我们复现的结果也的确是TTFT在不排队的时候性能和vllm一致，但是排队之后，distserve的TTFT latency明显高于vllm，导致性能下降

### PKUFlyingPig · 2024-06-25

(1) 在论文实验中我们为了公平比较所以让 vllm 也调用了新的算子，此前我理解成了你直接跑的官方的 vllm
(2) 是的，如果只看 prefill 的话，distserve 是在用相同的计算资源承受 2倍的 rate，理论上 TTFT latency 就是会更高
(3) goodput 的计算是要求同时满足 TTFT 和 TPOT 的 SLO，（2）中vllm为了更好的 TTFT 会损失大量的 TPOT 性能。distserve 可以在两个 SLO 之间 tradeoff，如果 TTFT 的要求很高，distserve 会增加 P：D 的比例，例如 7 张卡 prefill，1张卡 decode。通过调整最优配比来实现更好的 TTFT latency。

### YLSnowy · 2024-06-25

那我理解的就是distserve在和vllm的prefill使用相同的配置的情况下，即tp、pp、卡数一致的情况下，由于rate的不同，会导致distserve的TTFT latency高一点
所以您论文中的结果是怎么做到存在性能提升的呢？您论文中的配置我看到论文里面写清楚了，在66B的请款下，vllm是tp4，distserve是4-1-2-2，所以通过前面的结论看，TTFT latency应该不会有提升？

### PKUFlyingPig · 2024-06-25

论文中比较的 metric 是 goodput，即同时满足 TTFT 和 TPOT 的 SLO request 才能算作 effective throughput。

### YLSnowy · 2024-06-25

谢谢！非常感谢！
