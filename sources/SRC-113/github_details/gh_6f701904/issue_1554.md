# [Issue #1554] issue while inference/recommendation/dlrm/pytorch/ running with CPU docker.

source: https://github.com/mlcommons/inference/issues/1554
state: closed | updated: 2026-05-10T00:42:46Z
labels: Stale

## 正文

Hi,

I was running dlrm pytorch with CPU docker by using fake data. seeing below error.

/root/mlcommons/recommendation/dlrm/pytorch/python/dlrm_data_pytorch.py:328: UserWarning: Creating a tensor from a list of numpy.ndarrays is extremely slow. Please consider converting the list to a single numpy.ndarray with numpy.array() before converting to a tensor. (Triggered internally at /opt/conda/conda-bld/pytorch_1670525496686/work/torch/csrc/utils/tensor_new.cpp:230.)
  X_int = torch.log(torch.tensor(transposed_data[0], dtype=torch.float) + 1)
Traceback (most recent call last):
  File "python/main.py", line 619, in <module>
    main()
  File "python/main.py", line 535, in main
    _ = backend.predict(batch_dense_X, batch_lS_o, batch_lS_i)
  File "/root/mlcommons/recommendation/dlrm/pytorch/python/backend_pytorch_native.py", line 125, in predict
    output = self.model(dense_x=batch_dense_X, lS_o=batch_lS_o, lS_i=batch_lS_i)
  File "/opt/anaconda3/lib/python3.7/site-packages/torch/nn/modules/module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "/root/mlcommons/recommendation/dlrm/pytorch/python/dlrm_s_pytorch.py", line 528, in forward
    return self.sequential_forward(dense_x, lS_o, lS_i)
  File "/root/mlcommons/recommendation/dlrm/pytorch/python/dlrm_s_pytorch.py", line 600, in sequential_forward
    ly = self.apply_emb(lS_o, lS_i, self.emb_l, self.v_W_l)
  File "/root/mlcommons/recommendation/dlrm/pytorch/python/dlrm_s_pytorch.py", line 459, in apply_emb
    per_sample_weights=per_sample_weights,
  File "/opt/anaconda3/lib/python3.7/site-packages/torch/nn/modules/module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "/opt/anaconda3/lib/python3.7/site-packages/torch/nn/modules/sparse.py", line 391, in forward
    self.padding_idx)
  File "/opt/anaconda3/lib/python3.7/site-packages/torch/nn/functional.py", line 2393, in embedding_bag
    weight, input, offsets, scale_grad_by_freq, mode_enum, sparse, per_sample_weights, include_last_offset, padding_idx
**RuntimeError: Index 0 is out of bounds: 11395, range 0 to 11156**

Command i ran using CPU docker: ./run_local.sh terabyte cpu --max-ind-range=10000000

Machine used: x86_64 GNU/Linux

**Steps followed: **
cd $HOME/mlcommons/inference/recommendation/dlrm/pytorch/docker_cpu
./build_docker_cpu.sh
cd $HOME/mlcommons/inference/recommendation/dlrm/pytorch/docker_cpu
./run_docker_cpu.sh
cd mlcommons/recommendation/dlrm/pytorch
./run_local.sh terabyte cpu --max-ind-range=10000000

please provide the solution to this.

Thanks,
Siva

## 评论 (1)

### github-actions[bot] · 2026-05-10

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
