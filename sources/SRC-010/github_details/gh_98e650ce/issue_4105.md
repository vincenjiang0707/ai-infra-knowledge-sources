# [Issue #4105] [Bug] OpenGVLab/InternVL3-14B 使用lora适配器参数起服务后会报错TypeError: load_lora_weights() missing 1 required positional argument: 'adapter_id'

source: https://github.com/InternLM/lmdeploy/issues/4105
state: closed | updated: 2026-06-26T11:32:04Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

一开始我使用以下这个指令运行模型
```
lmdeploy serve api_server OpenGVLab/InternVL3-14B --adapters mylora=HsinHui04/internvl3-14b-lora-mdc-advice
```

虽然没有报错，但至 http://127.0.0.1:23333/v1/models 看我的模型并未load到我的lora，结果如下
```
{
  "object": "list",
  "data": [
    {
      "id": "OpenGVLab/InternVL3-14B",
      "object": "model",
      "created": 1762411649,
      "owned_by": "lmdeploy",
      "root": "OpenGVLab/InternVL3-14B",
      "parent": null,
      "permission": [
        {
          "id": "modelperm-UEgHEbY28jJhDch6Kkswwc",
          "object": "model_permission",
          "created": 1762411649,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": true,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ]
    }
  ]
}
```

 
参考#3594后，我尝试在指令加上`--backend pytorch`，lora有从huggingface载进去，指令如下
```
lmdeploy serve api_server OpenGVLab/InternVL3-14B \
	--adapters mylora=HsinHui04/internvl3-14b-lora-mdc-advice \
	--backend pytorch
```
但会报TypeError: load_lora_weights() missing 1 required positional argument: 'adapter_id'

所以想询问这是因为 LMDeploy 暂不支持 InternVL3-14B使用lora吗?

### Reproduction

lmdeploy serve api_server OpenGVLab/InternVL3-14B \
	--adapters mylora=HsinHui04/internvl3-14b-lora-mdc-advice \
	--backend pytorch

### Environment

```Shell
lmdeploy check_env
/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you.
  import pynvml  # type: ignore[import]
sys.platform: linux
Python: 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0: NVIDIA H100 80GB HBM3
CUDA_HOME: /usr/local/cuda-12.4
NVCC: Cuda compilation tools, release 12.4, V12.4.99
GCC: x86_64-linux-gnu-gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
PyTorch: 2.8.0+cu128
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 201703
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.7.1 (Git Hash 8d263e693366ef8db40acc569cc7d8edf644556d)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX512
  - CUDA Runtime 12.8
  - NVCC architecture flags: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 91.0.2  (built against CUDA 12.9)
    - Built with CuDNN 90.8
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=a1cb3cc05d46d198467bebbb6e8fba50a325d4e7, CUDA_VERSION=12.8, CUDNN_VERSION=9.8.0, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.8.0, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.23.0+cu128
LMDeploy: 0.10.2+
transformers: 4.57.1
fastapi: 0.121.0
pydantic: 2.11.10
triton: 3.4.0
NVIDIA Topology: 
	GPU0	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	0-25	0		N/A

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks
```

### Error traceback

```Shell
Traceback (most recent call last):
  File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 92, in _mp_proc
    engine = Engine.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 456, in from_pretrained
    return cls(model_path=pretrained_model_name_or_path,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 383, in __init__
    self.executor.init()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/base.py", line 189, in init
    self.build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/uni_executor.py", line 53, in build_model
    self.model_agent.build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 950, in build_model
    self._build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 943, in _build_model
    add_adapters(patched_model, adapters, dtype=self.model_config.dtype, device=device)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/models/patch.py", line 330, in add_adapters
    model.load_lora_weights(state_dict.items(), adapter_id=adapter_id)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/models/internvl.py", line 934, in load_lora_weights
    return load_lora_weights(weights, adapter_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: load_lora_weights() missing 1 required positional argument: 'adapter_id'
```

## 评论 (10)

### windreamer · 2025-11-06

@HsinHui-Tseng could you please try #4106 to test if this can fix the issue? Thanks.

### HsinHui-Tseng · 2025-11-07

Thank you for your reply.
I tried modifying lmdeploy/pytorch/models/internvl.py and lmdeploy/pytorch/models/internvl3_hf.py based on #4106, but it resulted in the following error:


### Error traceback
```
Traceback (most recent call last):
  File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/mp_engine/zmq_engine.py", line 92, in _mp_proc
    engine = Engine.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 456, in from_pretrained
    return cls(model_path=pretrained_model_name_or_path,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/engine.py", line 383, in __init__
    self.executor.init()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/base.py", line 189, in init
    self.build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/executor/uni_executor.py", line 53, in build_model
    self.model_agent.build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 950, in build_model
    self._build_model()
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/engine/model_agent.py", line 943, in _build_model
    add_adapters(patched_model, adapters, dtype=self.model_config.dtype, device=device)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/models/patch.py", line 330, in add_adapters
    model.load_lora_weights(state_dict.items(), adapter_id=adapter_id)
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/models/internvl.py", line 934, in load_lora_weights
    return load_lora_weights(self.language_model, weights, adapter_id)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/heimer_lan/lmdeploy_0.10.2-ms-swift/lib/python3.12/site-packages/lmdeploy/pytorch/adapter/adapter.py", line 107, in load_lora_weights
    param = params_dict[param_name]
            ~~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'language_model.model.layers.0.mlp.down_proj.lora_adapters.down_proj.lora_A'
```


### windreamer · 2025-11-07

It seems we didn't find corresponding lora parameters in your lora model. Could you please share your lora model or list your lora parameters so that we can reproduce this issue.

### HsinHui-Tseng · 2025-11-07

Thank you for your quick reply!
My LoRA has been uploaded to Hugging Face, and you can access it here:
 https://huggingface.co/HsinHui04/internvl3-14b-lora-mdc-advice

Here are the training parameters I used with ms-swift:
```
# Use `--template default`
nproc_per_node=1

```bash
CUDA_VISIBLE_DEVICES=0 \
MASTER_PORT=29501 \
NPROC_PER_NODE=$nproc_per_node \
swift sft \
    --model /home/heimer_lan/InternVL/pretrained/InternVL3-14B \
    --train_type lora \
    --dataset /path/train.json \
    --val_dataset /path/val.json \
    --torch_dtype bfloat16 \
    --template default \
    --num_train_epochs 10 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --lora_rank 8 \
    --lora_alpha 16 \
    --target_modules all-linear \
    --gradient_accumulation_steps $(expr 16 / $nproc_per_node) \
    --eval_steps 50 \
    --save_steps 50 \
    --save_total_limit 2 \
    --logging_steps 5 \
    --max_length 2048 \
    --output_dir /home/heimer_lan/ms-swift/output/MDC_advice_info_removeEmpty_lmdeploy_0.10.2/ \
    --system '請用繁體中文回答用戶的問題。' \
    --warmup_ratio 0.05 \
    --dataloader_num_workers 4 \
    --model_author swift \
    --model_name swift-robot \
    --deepspeed zero2
```
```

Thanks again for taking the time to check this issue and for your help!

### windreamer · 2025-11-07

May I know how do you train your lora model? It seems the parameter name is not what LMDeploy expected.

For lora models of internvl, the parameters should be named such as `language_model.model.layers.0.mlp.down_proj.lora_adapters.down_proj.lora_A`, while in your model, the parameter name is `base_model.model.language_model.model.layers.0.mlp.down_proj.lora_A.weight`

So I suspected you need to tweek your model to map the original name to the right name, as I think you just need a lora  fine-tuned language_model.

### HsinHui-Tseng · 2025-11-07

Thank you for your reply!

As mentioned in my previous comment, I trained my LoRA using ms-swift, with a training command slightly modified from the official example script here:
https://github.com/modelscope/ms-swift/blob/main/examples/train/base_to_chat/lora.sh

May I ask which training method or framework you would recommend for LoRA fine-tuning on InternVL3 models, so that the resulting parameter names can be fully compatible with LMDeploy?

Thanks again for your time and guidance!

### windreamer · 2025-11-07

Actrually I am not quite falimlar with this topic. You can check if the following link helps: https://internvl.readthedocs.io/en/latest/tutorials/coco_caption_finetune.html

### HsinHui-Tseng · 2025-11-20

Thank you for the suggestion!

I tried following the OpenGVLab / InternVL training tutorial and referenced the official scripts for InternVL3-14B here:
https://github.com/OpenGVLab/InternVL/tree/main/internvl_chat/shell/internvl3.0/2nd_finetune

However, all the provided scripts are for full fine-tuning, not LoRA.

So I attempted to adapt the previous-version script for LoRA fine-tuning, specifically this one from InternVL 2.5:
https://github.com/OpenGVLab/InternVL/blob/main/internvl_chat/shell/internvl2.5/2nd_finetune/internvl2_5_2b_dynamic_res_2nd_finetune_lora_coco.sh


Below is the LoRA training script I created based on `internvl3_14b_dynamic_res_2nd_finetune_full.sh` and adjusted according to the `internvl2_5_2b_dynamic_res_2nd_finetune_lora_coco.sh`:
```
set -x

```bash
GPUS=${GPUS:-1}
BATCH_SIZE=${BATCH_SIZE:-4}
PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-1}
GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / GPUS))


export PYTHONPATH="${PYTHONPATH}:$(pwd)"
export MASTER_PORT=34229
export TF_CPP_MIN_LOG_LEVEL=3
export LAUNCHER=pytorch
```

OUTPUT_DIR='work_dirs/internvl_chat_v3/internvl3_14b_dynamic_res_2nd_finetune_lora/test'

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
fi

# number of gpus: 1
# batch size per gpu: 4
# gradient accumulation steps: 4
# total batch size: 128
# epoch: 1
torchrun \
  --nnodes=1 \
  --node_rank=0 \
  --master_addr=127.0.0.1 \
  --nproc_per_node=${GPUS} \
  --master_port=${MASTER_PORT} \
  internvl/train/internvl_chat_finetune.py \
  --model_name_or_path "OpenGVLab/InternVL3-14B" \
  --conv_style "internvl2_5" \
  --use_fast_tokenizer False \
  --output_dir ${OUTPUT_DIR} \
  --meta_path "./shell/data/custom_dataset_hht.json" \
  --overwrite_output_dir True \
  --force_image_size 448 \
  --max_dynamic_patch 12 \
  --down_sample_ratio 0.5 \
  --drop_path_rate 0.1 \
  --freeze_llm True \
  --freeze_mlp True \
  --use_llm_lora 8 \
  --freeze_backbone True \
  --vision_select_layer -1 \
  --dataloader_num_workers 4 \
  --bf16 True \
  --num_train_epochs 1 \
  --per_device_train_batch_size ${PER_DEVICE_BATCH_SIZE} \
  --gradient_accumulation_steps ${GRADIENT_ACC} \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --save_steps 50 \
  --save_total_limit 1 \
  --learning_rate 2e-5 \
  --weight_decay 0.05 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --max_seq_length 16384 \
  --do_train True \
  --grad_checkpoint True \
  --group_by_length True \
  --dynamic_image_size True \
  --use_thumbnail True \
  --ps_version 'v2' \
  --deepspeed "zero_stage1_config.json" \
  --report_to "tensorboard" \
  2>&1 | tee -a "${OUTPUT_DIR}/training_log.txt"
```

But the output ended up being the final output is still the full model checkpoint, and  I don’t get any LoRA adapter files such as adapter_model.safetensors or adapter_config.json.

I would really appreciate any guidance on how to correctly perform LoRA fine-tuning for InternVL3-14B. 
Thank you again for your help! 

### windreamer · 2025-11-20

You may try [Xtuner]() for LoRA finetuning of InternVL3:

Here is an example script for internlm2-chat-7b: https://github.com/InternLM/xtuner/blob/main/xtuner/configs/custom_dataset/sft/internlm/internlm2_chat_7b_qlora_custom_sft_e1.py

And you can also read this Chinese doc for more details: https://github.com/InternLM/xtuner/blob/main/docs/zh_cn/legacy/training/custom_sft_dataset.rst

Hope these can help you.

### HsinHui-Tseng · 2025-11-28

Thank you for the detailed explanation and the reference!

I checked the Xtuner training example you provided, but it appears to come from older documentation. Most of the resources available online also reference the previous Xtuner workflow.

I’ve tried using the latest Xtuner 0.2.0 following the official documentation here:
https://xtuner.readthedocs.io/zh-cn/main/pretrain_sft/tutorial/mllm_trainer.html

Even in the newest version, there are no InternVL3 example scripts or configuration files, so I'm not sure how to correctly adapt the new configuration format to perform LoRA fine-tuning on InternVL3-14B.

If you could provide any guidance or point to a recommended configuration setup for Xtuner 0.2.0 (or any officially supported workflow), it would be extremely helpful.

Thank you again for your support!
