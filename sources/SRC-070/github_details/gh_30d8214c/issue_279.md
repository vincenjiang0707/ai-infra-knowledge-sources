# [Issue #279] [v3.2]  deep_gemm::fp8_mqa_logits performs poorly on the H200

source: https://github.com/deepseek-ai/DeepGEMM/issues/279
state: open | updated: 2026-01-16T07:42:31Z
labels: 

## 正文

<img width="1538" height="824" alt="Image" src="https://github.com/user-attachments/assets/53731e4c-e26d-4a14-9ed0-640c19fbd75f" />

## 评论 (3)

### thqq479 · 2026-01-16

**env** : python3.10 cuda12.4 deep_gemm=2.1.1.post3

**server** : python -m sglang.launch_server --disable-overlap-schedule --model-path "$MODEL_PATH" --port "$PORT" --schedule-conservativeness 0.2 --tp 8 --chunked-prefill-size 8192 --mem-fraction-static 0 .83 --tool-call-parser deepseekv32 --reasoning-parser deepseek-v3 --decode-log-interval 1 --disable-radix-cache

**client** : python3 -m sglang.bench_serving --backend sglang --dataset-name random-ids --num-prompts 1 --random-input 64000 --random-output 100 --random-range-ratio 0.9 --model /DeepSeek-V3.2 --max-concurrency 1 --host 127.0.0.1 --port 30000 --request-rate 1 --profier

### thqq479 · 2026-01-16

The performance of sglang running v3.2 is significantly worse than v3.1. Profiler analysis shows that the fp8_mqa_logits() function accounts for half of the total attention time, which is not what we expected, right? @LyricZhao 

### thqq479 · 2026-01-16

<img width="1511" height="762" alt="Image" src="https://github.com/user-attachments/assets/072dbe14-eb96-408b-98f4-e7bcf788dfb6" />
