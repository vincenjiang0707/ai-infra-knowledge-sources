# [Issue #89] 8-bit optimizers dont work with FSDP

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/89
state: closed | updated: 2026-04-27T14:13:07Z
labels: Duplicate, Contributions Welcome, FSDP, To Discuss Internally, Optimizers

## 正文

When I use an 8-bit ADAM with FSDP, I get an error as follows:

`RuntimeError: output tensor must have the same type as input tensor`

If my understanding is correct, there seems to be a casting issue. Is there any workaround this?

TIA.

## 评论 (30)

### TimDettmers · 2023-01-03

I looked at the deepspeed implementation before, which had a similar issue with shared weights. The problem was that the algorithm splits all tensors found in the optimizer state, which includes the quantization statistics. But this can lead to incorrect behavior. The workaround in deepspeed is to hide the quantization statistics by obscuring their type (putting the tensor into a list/tuple).

I am not sure if the error message that you provided is related to that or not.

It would be nice if we could get 8-bit Adam working for FSDP. Would you be able to provide a simple example for debugging and replication purposes? Since I will be pretty busy the next month, I would also be very happy to guide you on how to fix this if you create a PR and provide me with error messages / stack traces. I think it would be pretty useful since more and more people are using FSDP.

### philschmid · 2023-03-24

Hey @TimDettmers, 

I created a gist with an example. The gist includes a `process_dataset.py` to prepare a dataset and a `run_clm_bnb8.py` script, which uses the `adamw_bnb_8bit` optimizer and `FSDP`. 

https://gist.github.com/philschmid/99410e8bf66d34e52bb0cd5270b07989

I hope that's enough for you to test it. 


### philschmid · 2023-03-28

I tested the example i shared with the `adamw_bnb_8bit` and `adafactor` it seems that its not working if the training runs. 

AdamWInt8
```bash
{'loss': 2.6643, 'learning_rate': 4.847094801223242e-05, 'epoch': 0.09}
{'loss': 2.752, 'learning_rate': 4.694189602446483e-05, 'epoch': 0.18}
{'loss': 3.1493, 'learning_rate': 4.541284403669725e-05, 'epoch': 0.28}
{'loss': 3.412, 'learning_rate': 4.3883792048929664e-05, 'epoch': 0.37}
{'loss': 3.6722, 'learning_rate': 4.0825688073394495e-05, 'epoch': 0.55}
```

Adafactor
```bash
{'loss': 2.8385, 'learning_rate': 4.847094801223242e-05, 'epoch': 0.09}   
{'loss': 2.6384, 'learning_rate': 4.694189602446483e-05, 'epoch': 0.18}                   
{'loss': 2.5725, 'learning_rate': 4.541284403669725e-05, 'epoch': 0.28}
{'loss': 2.5757, 'learning_rate': 4.3883792048929664e-05, 'epoch': 0.37}
{'loss': 2.5297, 'learning_rate': 4.0825688073394495e-05, 'epoch': 0.55}                     
```

### prajdabre · 2023-04-03

Hi @TimDettmers in my latest test, it turns out that saving the model is the source of this issue.

Specifically the error pops up when I run this: optim_state = FSDP.full_optim_state_dict(model, optimizer)

What this is supposed to do is assemble the entire optimizer based on the model params. Now what I think is the problem is that the optimizer is in 8-bit but the model is not in 8-bit. The reason for my assumption is the error is thrown by 

File "/share03/draj/environments/.conda/envs/yanmtt/lib/python3.9/site-packages/torch/distributed/distributed_c10d.py", line 2136, in _all_gather_base
    work = group._allgather_base(output_tensor, input_tensor)

Indeed if you look here: https://github.com/pytorch/pytorch/blob/55daa835e97a6e742cba1f0e9d2a5c78b1615e99/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp#L2779

Then there is a constraint that the dtypes of tensors should be the same and we are not able to guarantee this for a sharded 8-bit optimizer.

If we can find some way to bypass this requirement, then we are good to go.

How do we overcome this issue?



### Kyeongpil · 2023-04-19

I have the same issue. #323
Is there any solution to solve this problem? @TimDettmers @prajdabre 

### Kyeongpil · 2023-04-20

There is another issue.
When I applied FSDP cpu offload with Adam8bit, I got the following error:

```
Expected a cuda device, but got: cpu
Traceback (most recent call last):
File "scripts/sft/run_train.py", line 509, in <module>
  main()
File "scripts/sft/run_train.py", line 503, in main
  run(artifact_config, train_config, experiment_config, execution_config)
File "scripts/sft/run_train.py", line 378, in run
  optimizer.step()
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/optim/lr_scheduler.py", line 68, in wrapper
  return wrapped(*args, **kwargs)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/accelerate/optimizer.py", line 140, in step
  self.optimizer.step(closure)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/optim/optimizer.py", line 140, in wrapper
  out = func(*args, **kwargs)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/autograd/grad_mode.py", line 27, in decorate_context
  return func(*args, **kwargs)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/bitsandbytes/optim/optimizer.py", line 263, in step
  self.update_step(group, p, gindex, pindex)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/autograd/grad_mode.py", line 27, in decorate_context
  return func(*args, **kwargs)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/bitsandbytes/optim/optimizer.py", line 504, in update_step
  F.optimizer_update_8bit_blockwise(
File "/home/kyeongpil/venv/lib/python3.8/site-packages/bitsandbytes/functional.py", line 972, in optimizer_update_8bit_blockwise
  prev_device = pre_call(g.device)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/bitsandbytes/functional.py", line 318, in pre_call
  torch.cuda.set_device(device)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/cuda/__init__.py", line 324, in set_device
  device = _get_device_index(device)
File "/home/kyeongpil/venv/lib/python3.8/site-packages/torch/cuda/_utils.py", line 30, in _get_device_index
  raise ValueError('Expected a cuda device, but got: {}'.format(device))
ValueError: Expected a cuda device, but got: cpuRank(3)
```

### prajdabre · 2023-04-28

Im not a 100% sure but this might be taken care of in pytorch 2.0.

### dotsnangles · 2023-05-07

I encountered a similar issue using PEFT LoRA, load_in_8bit, and DeepSpeed 3 (optimizer and params offload) with huggingface accelerator. on a single gpu, training was fine as expected.

If anyone found a workaround to enable parallel training with PEFT LoRA and load_in_8bit, please let me know.

### hscspring · 2023-05-16

it seems that pytorch 2 doesnot support 8bit

### 152334H · 2023-07-09

anyone still working on this....?

on the error @prajdabre was mentioning, I find that the problem does not come from a dtype mismatch, but rather a size mismatch. With printf debugging, I noticed that this seemed to first error on the absmax1 value, with
```python
output_tensor.shape == Size([361496576]), output_tensor.dtype == float32
input_tensor.shape == Size([22064]), input_tensor.dtype == float32
```



### HamidShojanazeri · 2023-07-18

cc @awgu

### github-actions[bot] · 2023-12-20

This issue has been automatically marked as stale because it has not had recent activity. If you think this still needs to be addressed please comment on this thread.



### 152334H · 2023-12-22

Noting that this issue, although stale, remains an issue. Although optimization can run, a functional state dict cannot be saved with 8bitadam.

I notice that there is a PR for FSDP functionality in https://github.com/TimDettmers/bitsandbytes/pull/840. It generally does not address the state dict issue in its tests.

### fabianlim · 2024-01-10

@Titus-von-Koeller @TimDettmers sorry to hijack this issue. Doing something related but not exactly the same. 

im trying to use FSDP with `bitsandbytes==0.42.0` to finetune `EleutherAI/pythia-1b` that has 8bit weights

- `AutoModelForCausalLM.from_pretrained("EleutherAI/pythia-1b", load_in_8bit=True)`
- added lora adapters, and i have different FSDP wrappers for anything that is not `bnb.Linear8bitLt`
    ```python
     GPTNeoXLayer(
        (input_layernorm): FullyShardedDataParallel(
          (_fsdp_wrapped_module): LayerNorm((2048,), eps=1e-05, elementwise_affine=True)
        )
        (post_attention_layernorm): FullyShardedDataParallel(
          (_fsdp_wrapped_module): LayerNorm((2048,), eps=1e-05, elementwise_affine=True)
        )
        (post_attention_dropout): Dropout(p=0.0, inplace=False)
        (post_mlp_dropout): Dropout(p=0.0, inplace=False)                                                                                                                                                                                                (attention): GPTNeoXAttention(
          (rotary_emb): FullyShardedDataParallel(
            (_fsdp_wrapped_module): GPTNeoXRotaryEmbedding()
          )
          (query_key_value): lora.Linear8bitLt(
            (base_layer): Linear8bitLt(in_features=2048, out_features=6144, bias=True)
            (lora_dropout): ModuleDict(
              (default): Dropout(p=0.1, inplace=False)
            )
            (lora_A): ModuleDict(
              (default): FullyShardedDataParallel(
                (_fsdp_wrapped_module): Linear(in_features=2048, out_features=8, bias=False)
              )
            )
            (lora_B): ModuleDict(
              (default): FullyShardedDataParallel(
                (_fsdp_wrapped_module): Linear(in_features=8, out_features=6144, bias=False)
              )
            )
            (lora_embedding_A): ParameterDict()
            (lora_embedding_B): ParameterDict()
          )
          (dense): Linear8bitLt(in_features=2048, out_features=2048, bias=True)
          (attention_dropout): Dropout(p=0.0, inplace=False)
        )
        (mlp): GPTNeoXMLP(
          (dense_h_to_4h): Linear8bitLt(in_features=2048, out_features=8192, bias=True)
          (dense_4h_to_h): Linear8bitLt(in_features=8192, out_features=2048, bias=True)
          (act): GELUActivation()
        )
      )
      ```

The FSDP wrapping will fail at [`_validate_tensors_to_flatten`](https://github.com/pytorch/pytorch/blob/v2.1.2/torch/distributed/fsdp/flat_param.py#L719) when it tries to flatten `Linear8bitLt` for sharding. This is because `Linear8bitLt.dtype` is `torch.int8`, and `_validate_tensors_to_flatten` requires that it be a floating point type. 

### fabianlim · 2024-01-10

> Noting that this issue, although stale, remains an issue. Although optimization can run, a functional state dict cannot be saved with 8bitadam.

@152334H when you were trying this, did you load the model in 4/8b precision? or the model is in 32b precision, but you want to activate `adamw_bnb_8bit`


### 152334H · 2024-01-10

? I do not test via huggingface.

I was in fact trying to only use an 8bit optimiser with 32bit weights, though, so I do not experience the int8 flatparameter issue you do. 

### Titus-von-Koeller · 2024-03-19

Hey @152334H @fabianlim @HamidShojanazeri @prajdabre @Kyeongpil @hscspring @dotsnangles @philschmid,

Could some of you please retest this and let us know if the particular problems that you were observing persist in the same for or if different, please put forward detailed logs + description?

We just released official FSDP support in the latest BNB version. However, this release was not focused on 8-bit optimizer support, yet.

Be sure to install with 
```
pip install bitsandbytes>=0.43.0
```

### fabianlim · 2024-03-20

@Titus-von-Koeller @TimDettmers I think the problem still remains even with BNB 0.43. The reason is because BNB performs optimizer steps with CUDA. 
1. when using CPU offload, the gradients are put onto the CPU
2. However before the BNB 8bit optimizer step,  there is a [`pre_call`](https://github.com/TimDettmers/bitsandbytes/blob/054837684e8c4e3ad3ef74919a71b906cde77700/bitsandbytes/functional.py#L1769) to put all of the tensors onto the same GPU
  ```python
   prev_device = pre_call(g.device)
   ```
4. However since the gradient `g` is on `cpu`, it is obvious why `pre_call` will fail, since now `device="cpu"` below:
  ```python
   def pre_call(device):
      prev_device = torch.cuda.current_device()
      torch.cuda.set_device(device)
      return prev_device
  ```
5. And finally, all of the optimizer quantities in the `is_on_gpu` call are on the `cpu`
  ```python
   is_on_gpu([g, p, state1, state2, qmap1, qmap2, absmax1, absmax2])
   ```

Thus while one can move all of the above quanities to gpu -> compute -> cpu. Im not sure if this is the most optimal way to do things as it will involve a lot of IO overhead.

### Titus-von-Koeller · 2024-03-20

@fabianlim Yes, you're right! Thanks for the detailed analysis, this really helps make things actionable.

I'll put it on my list of things to look into, but can't promise a timeline. We have a lot on our plate in the immediate future, as there are a lot of necessary changes that need to be prioritize to make BNB more maintainable and easier to contribute to.

In case you're interested to work with us on finding a solution, we would be super happy to collaborate and support you in any way!

### fabianlim · 2024-03-21

@Titus-von-Koeller On one hand, we can workaround this by loading all the quantities onto GPU, but this will be very inefficient. On the other hand, I feel the better approach would be to run the optimizer step alongside the FSDP sharding. 

As we see here, the [optimizer step can be run after the FSDP post grad hook](https://github.com/pytorch/pytorch/blob/cbbed4637737c7125bd7a3f8a81f23de1a46a9c9/torch/distributed/fsdp/_runtime_utils.py#L994-L999). There is a comment there to say that for CPU offload the parameters and gradients are run on CPU, but this should not be the case. If during offload, we can run the optimizer step in GPU before it gets offloaded, then this solves our problem and we do not need to shuffle params around

I have [posted a comment on pytorch](https://github.com/pytorch/pytorch/pull/120600#issuecomment-2009207827) asking when FSDP will start to support running `optim.step` on the GPU. I will keep you updated when I get a response.

### isaacbmiller · 2024-05-05

I have a repro using PL DDP:

Here is a semi-minimal repro (smallest I could get it). Breaking on 2xA100.

Repro gist: [https://gist.github.com/isaacbmiller/fc871d732d4d6a6b7ede3190a6979f40](https://gist.github.com/isaacbmiller/fc871d732d4d6a6b7ede3190a6979f40)

nvidia-smi
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A100-SXM...  On   | 00000000:4B:00.0 Off |                    0 |
| N/A   46C    P0    63W / 500W |      0MiB / 81920MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA A100-SXM...  On   | 00000000:E3:00.0 Off |                    0 |
| N/A   48C    P0    65W / 500W |      0MiB / 81920MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
```
deps
```
accelerate                0.28.0                   pypi_0    pypi
aiohttp                   3.9.3                    pypi_0    pypi
aiosignal                 1.3.1                    pypi_0    pypi
annotated-types           0.6.0                    pypi_0    pypi
antlr4-python3-runtime    4.9.3                    pypi_0    pypi
anyio                     4.3.0                    pypi_0    pypi
appdirs                   1.4.4                    pypi_0    pypi
argon2-cffi               23.1.0                   pypi_0    pypi
argon2-cffi-bindings      21.2.0                   pypi_0    pypi
arrow                     1.3.0                    pypi_0    pypi
asttokens                 2.4.1                    pypi_0    pypi
async-lru                 2.0.4                    pypi_0    pypi
attrs                     23.2.0                   pypi_0    pypi
babel                     2.14.0                   pypi_0    pypi
beautifulsoup4            4.12.3                   pypi_0    pypi
bitsandbytes              0.42.0                   pypi_0    pypi
blas                      1.0                         mkl  
bleach                    6.1.0                    pypi_0    pypi
blis                      0.7.11                   pypi_0    pypi
bzip2                     1.0.8                h5eee18b_5  
ca-certificates           2024.3.11            h06a4308_0  
catalogue                 2.0.10                   pypi_0    pypi
certifi                   2024.2.2                 pypi_0    pypi
cffi                      1.16.0                   pypi_0    pypi
charset-normalizer        3.3.2                    pypi_0    pypi
click                     8.1.7                    pypi_0    pypi
cloudpathlib              0.16.0                   pypi_0    pypi
comm                      0.2.2                    pypi_0    pypi
confection                0.1.4                    pypi_0    pypi
contourpy                 1.2.0                    pypi_0    pypi
cuda-cudart               12.1.105                      0    nvidia
cuda-cupti                12.1.105                      0    nvidia
cuda-libraries            12.1.0                        0    nvidia
cuda-nvrtc                12.1.105                      0    nvidia
cuda-nvtx                 12.1.105                      0    nvidia
cuda-opencl               12.4.127                      0    nvidia
cuda-runtime              12.1.0                        0    nvidia
cycler                    0.12.1                   pypi_0    pypi
cymem                     2.0.8                    pypi_0    pypi
datasets                  2.14.7                   pypi_0    pypi
debugpy                   1.8.1                    pypi_0    pypi
decorator                 5.1.1                    pypi_0    pypi
deepspeed                 0.14.0                   pypi_0    pypi
defusedxml                0.7.1                    pypi_0    pypi
dill                      0.3.7                    pypi_0    pypi
docker-pycreds            0.4.0                    pypi_0    pypi
editdistance              0.6.2                    pypi_0    pypi
einops                    0.8.0                    pypi_0    pypi
executing                 2.0.1                    pypi_0    pypi
fastjsonschema            2.19.1                   pypi_0    pypi
filelock                  3.13.1          py311h06a4308_0  
fonttools                 4.50.0                   pypi_0    pypi
fqdn                      1.5.1                    pypi_0    pypi
frozenlist                1.4.1                    pypi_0    pypi
fsspec                    2023.10.0                pypi_0    pypi
gcc                       5.4.0                         0    https://anaconda.org/brown-data-science/gcc/5.4.0/download
gitdb                     4.0.11                   pypi_0    pypi
gitpython                 3.1.42                   pypi_0    pypi
gmp                       6.2.1                h295c915_3  
gmpy2                     2.1.2           py311hc9b5ff0_0  
h11                       0.14.0                   pypi_0    pypi
hjson                     3.1.0                    pypi_0    pypi
httpcore                  1.0.5                    pypi_0    pypi
httpx                     0.27.0                   pypi_0    pypi
huggingface-hub           0.21.4                   pypi_0    pypi
hydra-core                1.3.2                    pypi_0    pypi
idna                      3.6                      pypi_0    pypi
iniconfig                 2.0.0                    pypi_0    pypi
intel-openmp              2023.1.0         hdb19cb5_46306  
ipykernel                 6.25.2                   pypi_0    pypi
ipython                   8.22.2                   pypi_0    pypi
ipywidgets                8.1.2                    pypi_0    pypi
isoduration               20.11.0                  pypi_0    pypi
jedi                      0.19.1                   pypi_0    pypi
jinja2                    3.1.3           py311h06a4308_0  
joblib                    1.3.2                    pypi_0    pypi
json5                     0.9.24                   pypi_0    pypi
jsonpointer               2.4                      pypi_0    pypi
jsonschema                4.21.1                   pypi_0    pypi
jsonschema-specifications 2023.12.1                pypi_0    pypi
jupyter                   1.0.0                    pypi_0    pypi
jupyter-client            8.6.1                    pypi_0    pypi
jupyter-console           6.6.3                    pypi_0    pypi
jupyter-core              5.7.2                    pypi_0    pypi
jupyter-events            0.10.0                   pypi_0    pypi
jupyter-lsp               2.2.4                    pypi_0    pypi
jupyter-server            2.13.0                   pypi_0    pypi
jupyter-server-terminals  0.5.3                    pypi_0    pypi
jupyterlab                4.1.5                    pypi_0    pypi
jupyterlab-pygments       0.3.0                    pypi_0    pypi
jupyterlab-server         2.25.4                   pypi_0    pypi
jupyterlab-widgets        3.0.10                   pypi_0    pypi
kiwisolver                1.4.5                    pypi_0    pypi
langcodes                 3.3.0                    pypi_0    pypi
ld_impl_linux-64          2.38                 h1181459_1  
libcublas                 12.1.0.26                     0    nvidia
libcufft                  11.0.2.4                      0    nvidia
libcufile                 1.9.1.3                       0    nvidia
libcurand                 10.3.5.147                    0    nvidia
libcusolver               11.4.4.55                     0    nvidia
libcusparse               12.0.2.55                     0    nvidia
libffi                    3.4.4                h6a678d5_0  
libgcc-ng                 11.2.0               h1234567_1  
libgomp                   11.2.0               h1234567_1  
libnpp                    12.0.2.50                     0    nvidia
libnvjitlink              12.1.105                      0    nvidia
libnvjpeg                 12.1.1.14                     0    nvidia
libstdcxx-ng              11.2.0               h1234567_1  
libuuid                   1.41.5               h5eee18b_0  
lightning                 2.2.1                    pypi_0    pypi
lightning-utilities       0.11.2                   pypi_0    pypi
lion-pytorch              0.1.4                    pypi_0    pypi
llvm-openmp               14.0.6               h9e868ea_0  
loralib                   0.1.2                    pypi_0    pypi
markdown-it-py            3.0.0                    pypi_0    pypi
markupsafe                2.1.5                    pypi_0    pypi
matplotlib                3.8.4                    pypi_0    pypi
matplotlib-inline         0.1.6                    pypi_0    pypi
mdurl                     0.1.2                    pypi_0    pypi
mistune                   3.0.2                    pypi_0    pypi
mkl                       2023.1.0         h213fc3f_46344  
mpc                       1.1.0                h10f8cd9_1  
mpfr                      4.0.2                hb69a4c5_1  
mpmath                    1.3.0           py311h06a4308_0  
multidict                 6.0.5                    pypi_0    pypi
multiprocess              0.70.15                  pypi_0    pypi
murmurhash                1.0.10                   pypi_0    pypi
nbclient                  0.10.0                   pypi_0    pypi
nbconvert                 7.16.3                   pypi_0    pypi
nbformat                  5.10.3                   pypi_0    pypi
ncurses                   6.4                  h6a678d5_0  
nest-asyncio              1.6.0                    pypi_0    pypi
networkx                  3.2.1                    pypi_0    pypi
ninja                     1.11.1.1                 pypi_0    pypi
nltk                      3.8.1                    pypi_0    pypi
notebook                  7.1.2                    pypi_0    pypi
notebook-shim             0.2.4                    pypi_0    pypi
numpy                     1.26.0                   pypi_0    pypi
nvidia-cublas-cu12        12.1.3.1                 pypi_0    pypi
nvidia-cuda-cupti-cu12    12.1.105                 pypi_0    pypi
nvidia-cuda-nvrtc-cu12    12.1.105                 pypi_0    pypi
nvidia-cuda-runtime-cu12  12.1.105                 pypi_0    pypi
nvidia-cudnn-cu12         8.9.2.26                 pypi_0    pypi
nvidia-cufft-cu12         11.0.2.54                pypi_0    pypi
nvidia-curand-cu12        10.3.2.106               pypi_0    pypi
nvidia-cusolver-cu12      11.4.5.107               pypi_0    pypi
nvidia-cusparse-cu12      12.1.0.106               pypi_0    pypi
nvidia-nccl-cu12          2.18.1                   pypi_0    pypi
nvidia-nvjitlink-cu12     12.4.99                  pypi_0    pypi
nvidia-nvtx-cu12          12.1.105                 pypi_0    pypi
omegaconf                 2.3.0                    pypi_0    pypi
openssl                   3.0.13               h7f8727e_0  
overrides                 7.7.0                    pypi_0    pypi
packaging                 24.0                     pypi_0    pypi
pandas                    2.2.2                    pypi_0    pypi
pandocfilters             1.5.1                    pypi_0    pypi
parso                     0.8.3                    pypi_0    pypi
pathtools                 0.1.2                    pypi_0    pypi
peft                      0.5.0                    pypi_0    pypi
pexpect                   4.9.0                    pypi_0    pypi
pillow                    10.3.0                   pypi_0    pypi
pip                       24.0                     pypi_0    pypi
platformdirs              4.2.0                    pypi_0    pypi
pluggy                    1.5.0                    pypi_0    pypi
preshed                   3.0.9                    pypi_0    pypi
prometheus-client         0.20.0                   pypi_0    pypi
prompt-toolkit            3.0.43                   pypi_0    pypi
protobuf                  4.25.3                   pypi_0    pypi
psutil                    5.9.8                    pypi_0    pypi
ptyprocess                0.7.0                    pypi_0    pypi
pure-eval                 0.2.2                    pypi_0    pypi
py-cpuinfo                9.0.0                    pypi_0    pypi
pyarrow                   15.0.2                   pypi_0    pypi
pyarrow-hotfix            0.6                      pypi_0    pypi
pycparser                 2.22                     pypi_0    pypi
pydantic                  2.6.4                    pypi_0    pypi
pydantic-core             2.16.3                   pypi_0    pypi
pygments                  2.17.2                   pypi_0    pypi
pynvml                    11.5.0                   pypi_0    pypi
pyparsing                 3.1.2                    pypi_0    pypi
pytest                    8.2.0                    pypi_0    pypi
python                    3.11.8               h955ad1f_0  
python-dateutil           2.9.0.post0              pypi_0    pypi
python-json-logger        2.0.7                    pypi_0    pypi
pytorch                   2.2.2           py3.11_cuda12.1_cudnn8.9.2_0    pytorch
pytorch-cuda              12.1                 ha16c6d3_5    pytorch
pytorch-lightning         2.2.1                    pypi_0    pypi
pytorch-mutex             1.0                        cuda    pytorch
pytz                      2024.1                   pypi_0    pypi
pyyaml                    6.0.1           py311h5eee18b_0  
pyzmq                     25.1.2                   pypi_0    pypi
qtconsole                 5.5.1                    pypi_0    pypi
qtpy                      2.4.1                    pypi_0    pypi
readline                  8.2                  h5eee18b_0  
referencing               0.34.0                   pypi_0    pypi
regex                     2023.12.25               pypi_0    pypi
requests                  2.31.0                   pypi_0    pypi
rfc3339-validator         0.1.4                    pypi_0    pypi
rfc3986-validator         0.1.1                    pypi_0    pypi
rich                      13.6.0                   pypi_0    pypi
rpds-py                   0.18.0                   pypi_0    pypi
safetensors               0.4.2                    pypi_0    pypi
scikit-learn              1.4.1.post1              pypi_0    pypi
scipy                     1.13.0                   pypi_0    pypi
seaborn                   0.13.2                   pypi_0    pypi
send2trash                1.8.2                    pypi_0    pypi
sentence-transformers     2.6.1                    pypi_0    pypi
sentry-sdk                1.43.0                   pypi_0    pypi
setproctitle              1.3.3                    pypi_0    pypi
setuptools                68.2.2          py311h06a4308_0  
six                       1.16.0                   pypi_0    pypi
smart-open                6.4.0                    pypi_0    pypi
smmap                     5.0.1                    pypi_0    pypi
sniffio                   1.3.1                    pypi_0    pypi
soupsieve                 2.5                      pypi_0    pypi
spacy                     3.7.4                    pypi_0    pypi
spacy-legacy              3.0.12                   pypi_0    pypi
spacy-loggers             1.0.5                    pypi_0    pypi
sqlite                    3.41.2               h5eee18b_0  
srsly                     2.4.8                    pypi_0    pypi
stack-data                0.6.3                    pypi_0    pypi
sympy                     1.12            py311h06a4308_0  
tbb                       2021.8.0             hdb19cb5_0  
terminado                 0.18.1                   pypi_0    pypi
thinc                     8.2.3                    pypi_0    pypi
threadpoolctl             3.4.0                    pypi_0    pypi
tinycss2                  1.2.1                    pypi_0    pypi
tk                        8.6.12               h1ccaba5_0  
tokenizers                0.15.2                   pypi_0    pypi
torch                     2.1.0                    pypi_0    pypi
torchdata                 0.7.1                    pypi_0    pypi
torchmetrics              1.3.2                    pypi_0    pypi
torchtriton               2.2.0                     py311    pytorch
tornado                   6.4                      pypi_0    pypi
tqdm                      4.66.1                   pypi_0    pypi
traitlets                 5.14.2                   pypi_0    pypi
transformers              4.40.0.dev0              pypi_0    pypi
triton                    2.0.0.dev20221202          pypi_0    pypi
trl                       0.7.1                    pypi_0    pypi
typer                     0.9.4                    pypi_0    pypi
types-python-dateutil     2.9.0.20240316           pypi_0    pypi
typing-extensions         4.10.0                   pypi_0    pypi
typing_extensions         4.9.0           py311h06a4308_1  
tzdata                    2024.1                   pypi_0    pypi
uri-template              1.3.0                    pypi_0    pypi
urllib3                   2.2.1                    pypi_0    pypi
wandb                     0.15.12                  pypi_0    pypi
wasabi                    1.1.2                    pypi_0    pypi
wcwidth                   0.2.13                   pypi_0    pypi
weasel                    0.3.4                    pypi_0    pypi
webcolors                 1.13                     pypi_0    pypi
webencodings              0.5.1                    pypi_0    pypi
websocket-client          1.7.0                    pypi_0    pypi
wheel                     0.43.0                   pypi_0    pypi
widgetsnbextension        4.0.10                   pypi_0    pypi
xxhash                    3.4.1                    pypi_0    pypi
xz                        5.4.6                h5eee18b_0  
yaml                      0.2.5                h7b6447c_0  
yarl                      1.9.4                    pypi_0    pypi
zlib                      1.2.13               h5eee18b_0
```


### Titus-von-Koeller · 2024-05-13

I don't have time to work on this in the next weeks due to needing to prioritize the `multi-backend-refactor` for which we're focusing our energies right now.

I see the big benefit of enabling this use-case and will prioritize it relatively high in the next months.

I'll use this thread to keep you posted. Thanks for the minimal repro, really appreciated @isaacbmiller (those are always really useful!). ❤️ 





### BramVanroy · 2024-07-23

EDIT: ignore the below, it does not seem to work as expected after all. Interesting behavior: initially it seems to work, but after saving and reloading the checkpoint, I get an error of mismatching types.

---

Just noting here that 8 bit adamw seems to work for me on FSDP with the following accelerate config:

```
compute_environment: LOCAL_MACHINE
debug: false
distributed_type: FSDP
downcast_bf16: 'no'
fsdp_config:
  fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
  fsdp_backward_prefetch: BACKWARD_PRE
  fsdp_cpu_ram_efficient_loading: true
  fsdp_forward_prefetch: false
  fsdp_offload_params: false
  fsdp_sharding_strategy: FULL_SHARD
  fsdp_state_dict_type: SHARDED_STATE_DICT
  fsdp_sync_module_states: true
  fsdp_use_orig_params: true
machine_rank: 0
main_process_ip: ''
main_process_port: 8000
main_training_function: main
mixed_precision: bf16
num_machines: 4
num_processes: 4
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```

### musabgultekin · 2024-07-24

Anyone knows alternative to bitsandbytes that we can use as a drop-in replacement until this gets fixed?

### nighting0le01 · 2024-10-28

@musabgultekin  did you find any replacement?? bnb 8 bit optims don't work with FSDP1 and FSDP2

### musabgultekin · 2024-10-28

No unfortunately.
I was able to use FSDP2 with only data parallel, rather than sharding. But didnt give much benefit due to not Sharding.
Sharding with FSDP2 + bitsandbytes doesnt work still. 

### musabgultekin · 2024-10-28

Use torchtune with torch2.5 for lower memory requirements, if you're fine-tuning LLMs

### nighting0le01 · 2024-10-28

@musabgultekin did you explore torchao low-bit optims? to work with FSDP2?

### musab-mk · 2025-01-17

@nighting0le01 I have not received notification for this comment, sorry for late response.

I can confirm `torchao.prototype.low_bit_optim.AdamW8bit` is working with FSDP2!

### lakshya-skyfall · 2026-04-27

This issue is still not fixed. I am not able to save the 8 bit AdamW optimizer with bnb while training a fp32 model. 
