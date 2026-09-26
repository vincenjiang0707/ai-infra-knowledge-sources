# [Issue #77] RuntimeError：RunOpsApiV2:build/CMakeFiles/torch_npu_dir/compile_depend.ts:243 NPU function error:c10_npu::acl::AclrtSynchronizeStreamWithTimeOut(stream),error code is 107027

source: https://github.com/Ascend/pytorch/issues/77
state: open | updated: 2025-10-14T07:03:00Z
labels: 

## 正文

I have meet this problem when use two piece 910B, start options is
 `export  ASCEND_LAUNCH_BLOCKING=1
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
vllm serve /data/qwen3-32B  --port 8080 --max-model-len 80000 -tp 2 --enable-prefix-caching --enable-chunked-prefill  --max-num-batched-tokens 4096 --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":80000}'`
after safetensors checkpoint load completed, when waitting for pendding NCCL work to finish before starting graph capture. It occured EE9999 Inner Error  and descripe like the title.   How can I solve  this problem?

## 评论 (1)

### yunyiyun · 2025-10-14

https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/maintenref/troubleshooting/troubleshooting_0001.html

Check the logs to see the specific error
