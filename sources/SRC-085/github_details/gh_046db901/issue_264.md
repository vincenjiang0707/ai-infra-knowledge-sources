# [Issue #264] Can EAGLE3 overfit one sample to see performance?

source: https://github.com/SafeAILab/EAGLE/issues/264
state: closed | updated: 2025-08-21T15:51:20Z
labels: 

## 正文

As the title describes, we want to overfit one sample using EAGLE3 for 1000 iters, we saw Acc is 0.89 and pLoss is 0.12 on each 7 slot, but still the vllm or the sglang accept rate is around 1.50, which is not even fast than no spec decode. So, the question is, can we overfit one sample or this is not work at all? thanks again for your reply

## 评论 (5)

### hongyanz · 2025-07-27

Not sure I understand the question. Can you clarify it again?

### ChiikawaSama · 2025-07-29

> Not sure I understand the question. Can you clarify it again?

sorry, my english is not good, let me explain in chinese, 我们仅使用了一条数据，想要去overfit一个EAGLE3的模型来看下具体的效果，训练代码中一样开的是7，且overfit的过程中（训练集/测试集用的都是这一条输入）position0～6的acc均可以达到0.89，ploss均可以达到0.12，这理论上来说是个非常好的结果了，但是实际用vllm / sglang进行infer的时候，接受率仍仅为1.5-，请问我们有什么比较好的办法来快速的在我们自己的模型和训练数据上验证EAGLE3的效果吗？还是说overfit是不太可行的方法

thanks for your reply again

### hongyanz · 2025-07-29

你有不在vllm和sgl上跑过吗？

### ChiikawaSama · 2025-07-29

> 你有不在vllm和sgl上跑过吗？

正在进行尝试中，不过我本身就使用vllm/sglang重刷了一遍输出，等我有进展了再给您回复 谢谢

### fan-niu · 2025-08-21

@ChiikawaSama Hi 请问有进展了吗？谢谢
