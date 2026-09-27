# [Issue #184] No such file or directory: "VILA1.5-13b-AWQ/llm/model-00001-of-00006.safetensors"

source: https://github.com/mit-han-lab/llm-awq/issues/184
state: open | updated: 2024-07-02T09:50:25Z
labels: 

## 正文

I've done the following:

> Alternatively, one may also skip the quantization process and directy download the quantized VILA-1.5 checkpoints from [here](https://huggingface.co/Efficient-Large-Model). Take VILA-1.5-13B as an example, after running:

> cd tinychat
> git clone https://huggingface.co/Efficient-Large-Model/VILA1.5-13b-AWQ
> One may run:

```
python vlm_demo_new.py \
    --model-path VILA1.5-13b-AWQ \
    --quant-path VILA1.5-13b-AWQ/llm \ 
    --precision W4A16 \
    --image-file /PATH/TO/INPUT/IMAGE \
```

from the docs. Then for some reason the model_path looks for the non-quantized safetensors file:

```
(base) ~/llm-awq/tinychat$ CUDA_VISIBLE_DEVICES=0 python vlm_demo_new.py --model-path VILA1.5-13b-AWQ --quant-path VILA1.5-13b-AWQ/llm --precision W4A16 --image-file ../../docs-fuji-red.jpg
/home/ray/anaconda3/lib/python3.10/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
/home/ray/anaconda3/lib/python3.10/site-packages/transformers/utils/generic.py:309: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
/home/ray/anaconda3/lib/python3.10/site-packages/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: '/home/ray/anaconda3/lib/python3.10/site-packages/torchvision/image.so: undefined symbol: _ZN3c1017RegisterOperatorsD1Ev'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source?
  warn(
/home/ray/llm-awq/tinychat/models/vila_llama.py:31: UserWarning: model_dtype not found in config, defaulting to torch.float16.
  warnings.warn("model_dtype not found in config, defaulting to torch.float16.")
real weight quantization...(init only): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 40/40 [00:01<00:00, 26.14it/s]

[Warning] The awq quantized checkpoint seems to be in v1 format.
If the model cannot be loaded successfully, please use the latest awq library to re-quantized the model, or repack the current checkpoint with tinychat/offline-weight-repacker.py

Loading checkpoint:   0%|                                                                                                                                                                       | 0/1 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/home/ray/llm-awq/tinychat/vlm_demo_new.py", line 238, in <module>
    main(args)
  File "/home/ray/llm-awq/tinychat/vlm_demo_new.py", line 93, in main
    model.llm = load_awq_model(model.llm, args.quant_path, 4, 128, args.device)
  File "/home/ray/llm-awq/tinychat/utils/load_quant.py", line 82, in load_awq_model
    model = load_checkpoint_and_dispatch(
  File "/home/ray/anaconda3/lib/python3.10/site-packages/accelerate/big_modeling.py", line 579, in load_checkpoint_and_dispatch
    load_checkpoint_in_model(
  File "/home/ray/anaconda3/lib/python3.10/site-packages/accelerate/utils/modeling.py", line 1568, in load_checkpoint_in_model
    checkpoint = load_state_dict(checkpoint_file, device_map=device_map)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/accelerate/utils/modeling.py", line 1313, in load_state_dict
    with safe_open(checkpoint_file, framework="pt") as f:
FileNotFoundError: No such file or directory: "VILA1.5-13b-AWQ/llm/model-00001-of-00006.safetensors"
```

## 评论 (8)

### kousun12 · 2024-05-09

I got a little farther by specifying the actual `.pt` file:

```
(base) ray@6c663dea2a49:~/llm-awq/tinychat$ CUDA_VISIBLE_DEVICES=0 python vlm_demo_new.py --model-path VILA1.5-13b-AWQ/ --quant-path VILA1.5-13b-AWQ/llm/vila-1.5-13b-w4-g128-awq-v2.pt --image-file https://media.substrate.run/docs-fuji-red.jpg
/home/ray/anaconda3/lib/python3.10/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
/home/ray/anaconda3/lib/python3.10/site-packages/transformers/utils/generic.py:309: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
/home/ray/anaconda3/lib/python3.10/site-packages/torchvision/io/image.py:13: UserWarning: Failed to load image Python extension: '/home/ray/anaconda3/lib/python3.10/site-packages/torchvision/image.so: undefined symbol: _ZN3c1017RegisterOperatorsD1Ev'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source?
  warn(
/home/ray/llm-awq/tinychat/models/vila_llama.py:31: UserWarning: model_dtype not found in config, defaulting to torch.float16.
  warnings.warn("model_dtype not found in config, defaulting to torch.float16.")
real weight quantization...(init only): 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 40/40 [00:01<00:00, 27.16it/s]
Loading checkpoint: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:05<00:00,  5.93s/it]
==================================================
USER: what is this
--------------------------------------------------
ASSISTANT: Traceback (most recent call last):
  File "/home/ray/llm-awq/tinychat/vlm_demo_new.py", line 238, in <module>
    main(args)
  File "/home/ray/llm-awq/tinychat/vlm_demo_new.py", line 184, in main
    outputs = stream_output(output_stream, time_stats)
  File "/home/ray/llm-awq/tinychat/utils/conversation_utils.py", line 83, in stream_output
    for outputs in output_stream:
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 56, in generator_context
    response = gen.send(request)
  File "/home/ray/llm-awq/tinychat/stream_generators/llava_stream_gen.py", line 177, in LlavaStreamGenerator
    out = model(
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ray/llm-awq/tinychat/models/vila_llama.py", line 91, in forward
    outputs = self.llm.forward(
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ray/llm-awq/tinychat/models/llama.py", line 332, in forward
    h = self.model(tokens, start_pos, inputs_embeds)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ray/llm-awq/tinychat/models/llama.py", line 316, in forward
    h = layer(h, start_pos, freqs_cis, mask)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1532, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1541, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ray/llm-awq/tinychat/models/llama.py", line 263, in forward
    h = x + self.self_attn.forward(
RuntimeError: CUDA error: an illegal memory access was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

### hkunzhe · 2024-05-13

@kousun12, There may be issues with your environment. You can use the following dockerfile to setup an environment with llm-awq and VILA.
```
FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

RUN apt-get update && \
    apt-get install -y openssh-server python3-pip vim git tmux

# Install VILA firstly
RUN git clone https://github.com/Efficient-Large-Model/VILA.git /root/VILA
WORKDIR /root/VILA
RUN pip install --upgrade pip
RUN pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
RUN wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.4.2/flash_attn-2.4.2+cu118torch2.0cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
RUN pip install flash_attn-2.4.2+cu118torch2.0cxx11abiFALSE-cp310-cp310-linux_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu118

RUN pip install setuptools_scm --index-url=https://pypi.org/simple
RUN pip install -e . && pip install -e ".[train]"

RUN pip install git+https://github.com/huggingface/transformers@v4.36.2
RUN site_pkg_path=$(python3 -c 'import site; print(site.getsitepackages()[0])')
RUN cp -rv ./llava/train/transformers_replace/* $site_pkg_path/transformers/

# Then install llm-awq
RUN git clone https://github.com/mit-han-lab/llm-awq /root/llm-awq
WORKDIR /root/llm-awq
RUN pip install -e .
WORKDIR /root/llm-awq/awq/kernels
# https://github.com/pytorch/extension-cpp/issues/71#issuecomment-1183674660
# TORCH_CUDA_ARCH_LIST=$(python3 -c 'import torch; print(".".join(map(str, torch.cuda.get_device_capability(0))))')
# TORCH_CUDA_ARCH_LIST="8.0+PTX" for A100
RUN export TORCH_CUDA_ARCH_LIST="8.0+PTX"
RUN python3 setup.py install

RUN pip install opencv-python-headless

RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /root/.cache
```

### kousun12 · 2024-05-13

a dockerfile is very helpful - thanks for that. i will give this a try

### kousun12 · 2024-05-13

I'm also running on H100s and have seen issues in the log console around `TORCH_CUDA_ARCH_LIST` -- Should I be setting that to 9.0?

### hkunzhe · 2024-05-13

> I'm also running on H100s and have seen issues in the log console around `TORCH_CUDA_ARCH_LIST` -- Should I be setting that to 9.0?

I think so.

### NigelNelson · 2024-05-14

> I'm also running on H100s and have seen issues in the log console around `TORCH_CUDA_ARCH_LIST` -- Should I be setting that to 9.0?
Should be setting it as:
```bash
TORCH_CUDA_ARCH_LIST="9.0+PTX"
```


### cktlco · 2024-05-15

Based on the OP's suggestion, I was able to resolve exactly the same issue by specifying the `vila-1.5-13b-w4-g128-awq-v2.pt` file location (not just the `llm/` directory) directly in the `--quant-path` param. After this, the demo worked as expected.

```
python vlm_demo_new.py --model-path ../VILA1.5-13b-AWQ --quant-path ../VILA1.5-13b-AWQ/llm/vila-1.5-13b-w4-g128-awq-v2.pt --precision W4A16 --image-file ../VILA/demo_images/av.png
```

### rahulthakur319 · 2024-07-02

Thanks @cktlco . I also stumbled on the same issue. Using the exact file location path in `--quant-path`, I was able to get a bit further. However then this issue came up.

GPU: RTX A6000

```
python vlm_demo_new.py --model-path /root/llm-awq/tinychat/VILA1.5-13b-AWQ --quant-path /root/llm-awq/tinychat/VILA1.5-13b-AWQ/llm/vila-1.5-13b-w4-g128-awq-v2.pt --precision W4A16 --image-file /root/VILA/demo_images/av.png
```

Error

```
/root/llm-awq/tinychat/models/vila_llama.py:31: UserWarning: model_dtype not found in config, defaulting to torch.float16.
  warnings.warn("model_dtype not found in config, defaulting to torch.float16.")
real weight quantization...(init only): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 40/40 [00:03<00:00, 10.02it/s]
Loading checkpoint:   0%|                                                                                                                                         | 0/1 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "/root/llm-awq/tinychat/vlm_demo_new.py", line 238, in <module>
    main(args)
  File "/root/llm-awq/tinychat/vlm_demo_new.py", line 93, in main
    model.llm = load_awq_model(model.llm, args.quant_path, 4, 128, args.device)
  File "/root/llm-awq/tinychat/utils/load_quant.py", line 82, in load_awq_model
    model = load_checkpoint_and_dispatch(
  File "/usr/local/lib/python3.10/dist-packages/accelerate/big_modeling.py", line 579, in load_checkpoint_and_dispatch
    load_checkpoint_in_model(
  File "/usr/local/lib/python3.10/dist-packages/accelerate/utils/modeling.py", line 1568, in load_checkpoint_in_model
    checkpoint = load_state_dict(checkpoint_file, device_map=device_map)
  File "/usr/local/lib/python3.10/dist-packages/accelerate/utils/modeling.py", line 1391, in load_state_dict
    return torch.load(checkpoint_file, map_location=torch.device("cpu"))
  File "/usr/local/lib/python3.10/dist-packages/torch/serialization.py", line 797, in load
    with _open_zipfile_reader(opened_file) as opened_zipfile:
  File "/usr/local/lib/python3.10/dist-packages/torch/serialization.py", line 283, in __init__
    super().__init__(torch._C.PyTorchFileReader(name_or_buffer))
RuntimeError: PytorchStreamReader failed reading zip archive: failed finding central directory
```

