# [Issue #4436] [Bug] v0.12.2-cu12.8部署qwen3.5的时候请，求任何内容出现 illegal memory

source: https://github.com/InternLM/lmdeploy/issues/4436
state: open | updated: 2026-05-06T22:41:26Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

latest-cu128  在单卡2080TI（  22G显存 ） + 8卡成功部署了Qwen3.5-35B-A3B。但是用请求测试的时候出现illegal memory 错误

### Reproduction

docker run -d \
```bash
    --runtime nvidia \
    --gpus '"device=0,1,2,3,4,5,6,7"'\
    --name lmdeploy_ht \
    -v /data/model/hugginface:/models \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    -p 23333:23333 \
    --ipc=host \
    --shm-size=128g \
    docker.1ms.run/openmmlab/lmdeploy:v0.12.2-cu12.8 \
    tail -f /dev/null
```
docker exec -it lmdeploy_ht bash


lmdeploy serve api_server /models/Qwen/Qwen3.5-35B-A3B  \
```bash
    --tp 8  \
    --cache-max-entry-count 0.8 \
    --log-level INFO \
    --max-concurrent-requests 4 \
    --model-name pkumlm_txt \
    --backend turbomind\
    --max_batch_size 64 \
    --cache-block-seq-len 32
```

<img width="1399" height="898" alt="Image" src="https://github.com/user-attachments/assets/81fd5cf9-1eb3-431f-8b1d-fba5debc9c2b" />

<img width="1377" height="323" alt="Image" src="https://github.com/user-attachments/assets/78741b40-9cac-4951-821e-59aff5c4333d" />


### Environment

```Shell
v0.12.2-cu12.8
单卡2080TI（  22G显存 ） * 8卡
Qwen3.5-35B-A3B
```

### Error traceback

```Shell
curl  -H "Accept: application/json"  -H "Content-type: application/json"   -X POST  -d '{"model": "pkumlm_txt","messages":[{"role":"user","content":"你是谁"} ]}'   http://192.168.1.36:23333/v1/chat/completions

报错
2026-03-19 12:52:50,954 - lmdeploy - INFO - turbomind.py:687 - [async_stream_infer] session 1 start
[TM][INFO] [SeqMgr][Create] ID 1
[TM][WARNING] [ProcessInferRequests] [1] total sequence length (11 + 262133) exceeds `session_len` (258368), `max_new_tokens` is truncated to 258357
invalid argument
```

## 评论 (0)
