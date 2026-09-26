# [Issue #31] [Inference] IndexError: list index out of range

source: https://github.com/FasterDecoding/Medusa/issues/31
state: closed | updated: 2023-09-19T01:17:44Z
labels: 

## 正文

你好！我很顺利的完成了训练，但是在User输入后，模型推断时遇见了这个bug...
使用的infer命令：
`CUDA_VISIBLE_DEVICES=0 python -m medusa.inference.cli --model /data/lxy/models/test_medusa_mlp_lmsys_vicuna-7b-v1.5_medusa_3_lr_0.001_layers_1 --base-model /data/lxy/models/lmsys_vicuna-7b-v1.5`
报错信息：
```
USER: hi
ASSISTANT: Traceback (most recent call last):
  File "/home/lxy/miniconda3/envs/langchain/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/lxy/miniconda3/envs/langchain/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/lxy/Medusa/medusa/inference/cli.py", line 228, in <module>
    main(args)
  File "/home/lxy/Medusa/medusa/inference/cli.py", line 162, in main
    outputs = chatio.stream_output(
  File "/home/lxy/miniconda3/envs/langchain/lib/python3.10/site-packages/fastchat/serve/cli.py", line 59, in stream_output
    for outputs in output_stream:
  File "/home/lxy/Medusa/medusa/model/medusa_model.py", line 280, in medusa_generate
    candidates, tree_candidates = generate_candidates(
  File "/home/lxy/Medusa/medusa/model/utils.py", line 215, in generate_candidates
    candidate_i = torch.topk(medusa_logits[i, 0, -1], medusa_topk[i]).indices
IndexError: list index out of range
```
我在试图定位并解决这个问题，请问有什么修改建议嘛~十分感谢！

## 评论 (2)

### ctlllll · 2023-09-18

https://github.com/FasterDecoding/Medusa/issues/16#issuecomment-1721664531
Hi! 看起来和上面这个issue是同一个问题，可以试试这里的解决方案 :)

### helldog-star · 2023-09-19

> [#16 (comment)](https://github.com/FasterDecoding/Medusa/issues/16#issuecomment-1721664531) Hi! 看起来和上面这个issue是同一个问题，可以试试这里的解决方案 :)

收到，谢谢~
