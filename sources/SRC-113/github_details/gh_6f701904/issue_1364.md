# [Issue #1364] torch.cuda.OutOfMemoryError: CUDA out of memory. 

source: https://github.com/mlcommons/inference/issues/1364
state: closed | updated: 2026-06-20T00:49:28Z
labels: Stale

## 正文

when I excude this command:
./run_local.sh pytorch dlrm terabyte gpu --scenario Server  --max-ind-range=40000000 --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt 

then:
Using 8 GPU(s)...
Reading pre-processed data=/home/user01/file/node05/joyecai/nfs_share/dlrm_raw_dataset/terabyte_processed.npz
Sparse features= 26, Dense features= 13
Using variable query size: custom distribution (file ./tools/dist_quantile.txt)
Traceback (most recent call last):
  File "/home/user01/file/node05/joyecai/code/mlcommons/inference/recommendation/dlrm/pytorch/python/main.py", line 619, in <module>    main()
  File "/home/user01/file/node05/joyecai/code/mlcommons/inference/recommendation/dlrm/pytorch/python/main.py", line 503, in main
    model = backend.load(args.model_path, inputs=args.inputs, outputs=args.outputs)
  File "/home/user01/file/node05/joyecai/code/mlcommons/inference/recommendation/dlrm/pytorch/python/backend_pytorch_native.py", line 61, in load
    dlrm = dlrm.to(self.device)  # .cuda()
  File "/home/user01/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1145, in to
    return self._apply(convert)
  File "/home/user01/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 797, in _apply
    module._apply(fn)
  File "/home/user01/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 797, in _apply
    module._apply(fn)
  File "/home/user01/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 820, in _apply    param_applied = fn(param)  File "/home/user01/miniconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1143, in convert    return t.to(device, dtype if t.is_floating_point() or t.is_complex() else None, non_blocking)
torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 18.91 GiB (GPU 0; 79.18 GiB total capacity; 70.34 GiB already allocated; 8.00 GiB free; 70.35 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

## 评论 (4)

### pgmpablo157321 · 2023-05-10

@ColaDrill What were the RAM and GPUs of the machine you tried to run the benchmark on?

### ColaDrill · 2023-05-11

> 1008GB RAM and 80GB x 8 GPU (NVIDIA A800)



### kkkparty · 2024-06-19

> > 1008GB RAM and 80GB x 8 GPU (NVIDIA A800)

did you fix oom issues?

### github-actions[bot] · 2026-06-20

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
