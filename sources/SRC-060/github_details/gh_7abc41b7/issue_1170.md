# [Issue #1170] ernie多模态大模型怎么实现多个请求同时处理？

source: https://github.com/PaddlePaddle/ERNIE/issues/1170
state: closed | updated: 2025-11-24T12:00:55Z
labels: 

## 正文

python -m fastdeploy.entrypoints.openai.api_server \
       --model baidu/ERNIE-4.5-VL-28B-A3B-Paddle \
       --port 8180 \
       --metrics-port 8181 \
       --engine-worker-queue-port 8182 \
       --max-model-len 32768 \
       --enable-mm \
       --reasoning-parser ernie-45-vl \
       --max-num-seqs 32
设置了  --max-num-seqs 32， 多个大模型请求访问8180端口的时候大模型还是串行处理的，并没有实现并发处理。

## 评论 (2)

### Jiang-Jia-Jun · 2025-08-25

@shuzhikun Hi，你是怎么判断模型内部是串行处理的呢？ 

服务内部的处理逻辑如下
1. 所有并发的请求会首先进入到内存队列中
2. 对于多模态模型，每次从队列中取一个请求进行Prefill（在此步骤中，之前还在Decode阶段未完成的请求，会同时完成一步Decode生成）
3. Prefill完成的请求新插入到Decode的Batch中，继续进行Decode操作

其中上面说的Prefill阶段会完成第一个Token的生成，Decode阶段会循环不断生成新的Token直至结束。因此从这里可以看到服务的并行处理阶段是在Decode阶段，也就是设定的max-num-seqs的最大值即为它的并发上限。可以查看log/worker_process.log，看到num_running_requests，表示服务并行处理请求的数量。

此外，服务是否能并发处理，还取决于KVCache的大小，例如如果输入都很长，此时KVCache不足以支撑多条请求并发生成，那么可能会造成请求排队串行处理的现象。

### nepeplwu · 2025-11-24

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
