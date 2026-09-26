# [Issue #1622] omni_doc_bench_v1_6，文件名太长报错

source: https://github.com/modelscope/evalscope/issues/1622
state: closed | updated: 2026-08-25T03:05:05Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

```python
from evalscope import run_task
from evalscope.config import TaskConfig

task_cfg = TaskConfig(
    model='OvisOCR2',
    api_url='http://10.24.0.4:7092/v1',
    api_key='EMPTY_TOKEN',
    datasets=['omni_doc_bench_v1_6'],
    sandbox={'enabled': True},
    seed=42,
    eval_batch_size=8,
    repeats=1,
    timeout=600,
    generation_config={"do_sample":True, "max_tokens": 32768, "temperature":0.7, "top_p": 0.80, "presence_penalty": 1.5, "repetition_penalty": 1.0, "extra_body": {"chat_template_kwargs":{"enable_thinking": False}}},
    # limit=10,  # 正式评估时请删除此行
)

run_task(task_cfg=task_cfg)
```
- 文件名太长报错

```
}
2026-08-24 10:06:56 - evalscope - INFO: Start loading benchmark dataset: omni_doc_bench_v1_6                                                                                                                                                     
Processing records:  89%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▏                  | 1477/1651 [00:05<00:00, 278.90it/s]
2026-08-24 10:07:03 - evalscope - INFO: Running[eval]   0%| 0/1 [Elapsed: 00:06 < Remaining: ?, ?benchmark/s]                                                                                                                                    
Running[eval]:   0%|                                                                                                                                                                                                | 0/1 [00:06<?, ?benchmark/s]
Traceback (most recent call last):
  File "/cx8k/fs101/wzp/code/0929/vaeval/eval/ocr/scripts/omn.py", line 18, in <module>
    run_task(task_cfg=task_cfg)
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/run.py", line 26, in run_task
    return run_single_task(task_cfg)
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/run.py", line 41, in run_single_task
    result = evaluate_model(task_cfg, outputs)
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/run.py", line 182, in evaluate_model
    res_dict = evaluator.eval()
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/evaluator/evaluator.py", line 168, in eval
    dataset_dict = {k: v for k, v in self.benchmark.load_dataset().items() if len(v) > 0}
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/benchmark/adapters/default_data_adapter.py", line 63, in load_dataset
    self.test_dataset, self.fewshot_dataset = self.load()
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/benchmark/adapters/default_data_adapter.py", line 82, in load
    return self.load_from_remote()
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/benchmark/adapters/default_data_adapter.py", line 90, in load_from_remote
    test_dataset = self.load_subsets(test_load_func)
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/benchmark/adapters/default_data_adapter.py", line 228, in load_subsets
    subset_data = load_func(subset)
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/benchmarks/omnidoc_bench/v1_6/omnidoc_bench_v1_6_adapter.py", line 113, in load_subset
    ).load()
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/dataset/loader.py", line 305, in load
    memory_dataset = MemoryDataset(samples=data_to_samples(data=dataset, data_to_sample=data_to_sample), )
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/dataset/utils.py", line 53, in data_to_samples
    record_samples = as_sample_list(data_to_sample(record=record))
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/benchmarks/omnidoc_bench/v1_6/omnidoc_bench_v1_6_adapter.py", line 118, in record_to_sample
    download_dataset_file(
  File "/cx8k/fs101/wzp/code/0929/evalscope/evalscope/api/dataset/hub.py", line 221, in download_dataset_file
    return dataset_file_download(data_id_or_path, file_path, **download_kwargs)
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/modelscope/hub/file_download.py", line 115, in dataset_file_download
    return _compat_dataset_file_download(
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/modelscope_hub/compat/file_download.py", line 122, in dataset_file_download
    result = api.download_file(
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/modelscope_hub/api.py", line 1375, in download_file
    return self.downloader.download_file(
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/modelscope_hub/_download.py", line 587, in download_file
    with _optional_file_lock(lock_path, enabled=use_lock):
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/contextlib.py", line 135, in __enter__
    return next(self.gen)
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/modelscope_hub/_download.py", line 139, in _optional_file_lock
    lock.acquire(timeout=default_interval)
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/filelock/_api.py", line 332, in acquire
    self._acquire()
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/site-packages/filelock/_unix.py", line 42, in _acquire
    if not Path(self.lock_file).exists():
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/pathlib.py", line 1290, in exists
    self.stat()
  File "/cx8k/fs101/wzp/miniforge3/envs/evalscope/lib/python3.10/pathlib.py", line 1097, in stat
    return self._accessor.stat(self, follow_symlinks=follow_symlinks)
OSError: [Errno 36] File name too long: '/home/wzp/.cache/modelscope/hub/datasets/.lock/dataset_OpenDataLab___OmniDocBench_images___color_textbook_zhonggaokao_小学_KET听说读写逐项突破_KET听说读写逐项突破之轻松搞定KET写作25分 【10讲 褚连一】_第05讲第五课写作Part7详解_第五课写作Part7详解_page_001_png.lock'
(evalscope) wzp@bms-b7bb00cb28e64685:/cx8k/fs101/wzp/code/0929/vaeval$ rm -rf /home/wzp/.cache/modelscope/hub/datasets/.lock/dataset_OpenDataLab___OmniDocBench_images___color_textbook_zhonggaokao_小学_KET听说读写逐项突破_KET听说读写逐项突破 
之轻松搞定KET写作25分 【10讲 褚连一】_第05讲第五课写作Part7详解_第五课写作Part7详解_page_001_png.lock
```

## EvalScope 版本（必填）
Commit: bbd8d0359cd2cbdcb1657f195d12a27a93abb9d4

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式



## 评论 (2)

### Moenupa · 2026-08-24

I think this is a more modelscope-related issue.

A workaround is to set `--dataset-dir` to a shorter path (in combination with symlink if you want to keep the original folder).

### Yunnglin · 2026-08-25

Try using the latest version v1.11.0 again. The download method for this bench has been modified. The fundamental solution is to wait for the modelscope-hub to release a new version. This issue has been reported and resolved.
