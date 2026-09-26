# [Issue #1653] Pytorch BERT failed to load state_dict

source: https://github.com/mlcommons/inference/issues/1653
state: closed | updated: 2026-05-06T00:40:58Z
labels: Stale

## 正文

Issue Description: 
I manually download the model.pytorch and vocab.txt to the designated folder and run `/home/user/cm/bin/python3 run.py --backend=pytorch --scenario=Offline   --max_examples 10 --mlperf_conf '/home/user/CM/repos/local/cache/b737554800c84148/inference/mlperf.conf' --user_conf '/home/user/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/c8eb2a31fd70402a93daee688bf391fa.conf' --accuracy 2>&1 | tee /home/user/CM/repos/local/cache/454869b45fbf4f67/test_results/default-reference-gpu-pytorch-v2.2.1-default_config/bert-99/offline/accuracy/console.out` command triggering the BERT benchmarking. 

**Error Message:**
```
Loading BERT configs...
Loading PyTorch model...
Traceback (most recent call last):
  File "/home/user/CM/repos/local/cache/b737554800c84148/inference/language/bert/run.py", line 150, in <module>
    main()
  File "/home/user/CM/repos/local/cache/b737554800c84148/inference/language/bert/run.py", line 75, in main
    sut = get_pytorch_sut(args)
  File "/home/user/CM/repos/local/cache/b737554800c84148/inference/language/bert/pytorch_SUT.py", line 111, in get_pytorch_sut
    return BERT_PyTorch_SUT(args)
  File "/home/user/CM/repos/local/cache/b737554800c84148/inference/language/bert/pytorch_SUT.py", line 60, in __init__
    self.model.load_state_dict(torch.load(model_file))
 

>  File "/home/user/cm/lib/python3.10/site-packages/torch/nn/modules/module.py", line 2153, in load_state_dict
>     raise RuntimeError('Error(s) in loading state_dict for {}:\n\t{}'.format(
> RuntimeError: Error(s) in loading state_dict for BertForQuestionAnswering:
>         Unexpected key(s) in state_dict: "bert.pooler.dense.weight", "bert.pooler.dense.bias"

```

## 评论 (1)

### github-actions[bot] · 2026-05-06

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
