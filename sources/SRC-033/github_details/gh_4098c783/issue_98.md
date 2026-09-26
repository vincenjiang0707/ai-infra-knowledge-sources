# [Issue #98] 补图过多导致压测卡死

source: https://github.com/Ascend/pytorch/issues/98
state: open | updated: 2026-01-12T12:19:17Z
labels: 

## 正文

python -m sglang.launch_server --model-path $MODEL_PATH \
    --host 127.0.0.1 --port 7439 --trust-remote-code --nnodes 1 --node-rank 0  \
    --attention-backend ascend --device npu \
    --tp-size 1 --mem-fraction-static 0.8 --cuda-graph-max-bs 64  --dtype bfloat16

捕12张图，压测gsm8k精度时，数据集总量为1319条，在第1255条卡死；
只捕一张图bs=64，压测gsm8k精度通过

## 评论 (1)

### yunyiyun · 2026-01-12

图模式时stream资源有限制，请看下是否是资源耗尽
https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/aclcppdevg_03_1782.html
如果不是资源耗尽，可以在卡住时采集下c++/python堆栈看下卡住情况
同时可以在sglang社区提问咨询其适配使用情况
