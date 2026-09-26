# [Issue #1062] 评测的参数从哪里看到？目前有些数据集复现不了结果

source: https://github.com/PaddlePaddle/ERNIE/issues/1062
state: closed | updated: 2025-07-29T01:51:54Z
labels: 

## 正文

比如：
C-Eval
结果：0.4591±0.0236 ，官方 C-Eval 报告 91.5
模型有一些冗余回答的现象，不会直接回答答案。可能某些参数没对齐？


vlmm 0.9.2
cuda: 12.9
python: 3.9
vlmm 启动命令： `"vllm serve \$模型保存地址    --host 33.236.231.151         --port 8081         --dtype bfloat16         --pipeline-parallel-size 1         --tensor-parallel-size 8       --trust-remote-code         --enable-chunked-prefill         --served-model-name  \$模型保存地址         --max-model-len 131072         --max-num-batched-tokens 2048         --max-num-seqs 256         --gpu-memory-utilization 0.9         --disable-custom-all-reduce --enable-chunked-prefill "`

temperature: 1
TopK: 1
TopP : 1









## 评论 (1)

### lianghao6 · 2025-07-29

前两天更新模型文件后 ceval能复现了
