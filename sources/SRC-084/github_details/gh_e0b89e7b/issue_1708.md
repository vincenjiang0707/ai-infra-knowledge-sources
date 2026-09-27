# [Issue #1708] Error invalid argument at line 337 in file /src/csrc/pythonInterface.cpp

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1708
state: closed | updated: 2026-02-16T11:47:24Z
labels: Hugging Face Integration, Optimizers

## 正文

### System Info

I'm getting the error "Error invalid argument at line 337 in file /src/csrc/pythonInterface.cpp" when continuing to train from a previously saved SFT Trainer checkpoint when running in a multi-GPU environment.

Attached below is a repro - iTraining his works prior to resume on 8 GPUs, and prior and after resume on 1 GPU.  Is the configuration used to reload for 8 GPUs somehow getting messed up?  Am I initializing the model the wrong way?

Using CUDA 12.1 & PT 2.5.1
pip3 install torch torchvision torchaudio packaging --index-url https://download.pytorch.org/whl/cu121

root@cw-dfw-h100-004-320-012:/app# python3 -c "import torch; print(f'PyTorch version: {torch.version}')"
PyTorch version: 2.5.1+cu121


### Reproduction

Repro:
```
# export HF_TOKEN=YOUR_TOKEN_FOR_LLAMA3

<1 GPU, works>
python3 ./test.py  
python3 ./test.py --resume /root/lustre/outputs/doc_sft_training_artifacts/checkpoint-2/

<8 GPUs, fail on resume>
 torchrun          --nproc_per_node 8         --nnodes 1         --node_rank $SLURM_NODEID          --rdzv_id $SLURM_JOB_ID          --rdzv_backend c10d          --rdzv_endpoint $(hostname)  ./test.py 

 torchrun          --nproc_per_node 8         --nnodes 1         --node_rank $SLURM_NODEID          --rdzv_id $SLURM_JOB_ID          --rdzv_backend c10d          --rdzv_endpoint $(hostname)  ./test.py --resume /root/lustre/outputs/doc_sft_training_artifacts/checkpoint-2/      # *FAIL*
```

Here's the training portion to repro:
```
mgschwind@cw-dfw-cs-001-login-01:~/lustre/rl$ cat ~/test.py
# =================================================================================
# Fine-Tuning Script
# =================================================================================
import torch
import re
import argparse
import json
import os
import signal
import sys
import glob
from datetime import datetime
from tqdm import tqdm
from datasets import Dataset, IterableDataset
from trl import GRPOConfig, SFTConfig
from trl import GRPOTrainer, SFTTrainer
#from checkpointed_trainer import (
#    GRPOTrainerCheckpoint as GRPOTrainer,
#    SFTTrainerCheckpoint as SFTTrainer
#)
from transformers import TrainingArguments, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel, get_peft_model, LoraConfig, prepare_model_for_kbit_training
from typing import Callable, Optional, List, Dict, Iterator, Tuple, Iterable
from pathlib import Path
import re

SYSTEM_PROMPT = """
SYSTEM_PROMPT not initialized
"""

# --- Data Preparation ---
def get_documentation_dataset(corpus_path: str) -> Optional[Dataset]:
    """
    Scans a directory for .md and .txt files and loads them into a dataset.
    """
    all_texts = [
	     "bla bla bla bla bla" * 20
	     ] *100

    print(f"Total documents loaded for pre-training: {len(all_texts)}")
    if not all_texts:
        return None

    # The SFTTrainer can work with a simple "text" column
    dataset = Dataset.from_dict({"text": all_texts})
    return dataset

def main(args):
    # Each process gets a unique rank from 0 to 7.
    # This line ensures that each process will only use its assigned GPU.
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)

    # Print so we know what is going on.
    print(f"DEBUG: local rank = {local_rank}")

    # Define the target device for the current process
    device = torch.device(f"cuda:{local_rank}")

    model, tokenizer = None, None
    trainer = None

    # try:
    if True:
        # --- MODEL LOADING ---
        model_to_load = args.model_name

        quantization_config = BitsAndBytesConfig(
            load_in_4bit=args.load_in_4bit,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
        )


        # Ensure each process loads the model to its assigned GPU
        # without using FSDP.
        device_map = {"": torch.cuda.current_device()}

        model = AutoModelForCausalLM.from_pretrained(
            model_to_load,
            quantization_config=quantization_config,
            torch_dtype=torch.bfloat16, # <-- Load weights in low precision
            device_map=local_rank, # <-- Use the exlicit rank
            # device_map="auto", <-- appears to trigger FSDP DTensor
            token=args.hf_token,
            attn_implementation="flash_attention_2",
        )

        tokenizer = AutoTokenizer.from_pretrained(
            args.model_name,
            token=args.hf_token,
            # supposedly in lieu of SFT Trainer config
            model_max_length=args.max_seq_length,
        )

        model = prepare_model_for_kbit_training(model)

        # create
        peft_config = LoraConfig(
            r=args.lora_rank,
            lora_alpha=args.lora_alpha,
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=[
                "q_proj", "k_proj", "v_proj", "o_proj",
                "gate_proj", "up_proj", "down_proj",
                ],
            )
        model = get_peft_model(model, peft_config)
        # --- END VANILLA HUGGING FACE MODEL LOADING ---

        # --- Documentation SFT Phase ---
        artifacts_dir = f"{args.output_dir}/doc_sft_training_artifacts"
        if True:
            prior_phase_activated = True
            print("\n--- Starting Documentation SFT Phase ---")
            doc_dataset = get_documentation_dataset(args.doc_sft_path)

            if doc_dataset:
                is_resuming_doc_sft = (
                    args.resume_from_checkpoint and
                    os.path.realpath(args.resume_from_checkpoint).startswith(os.path.realpath(artifacts_dir))
                )
                resume_path_for_doc_sft = args.resume_from_checkpoint if is_resuming_doc_sft else None

                # MODIFIED: Use SFTConfig
                training_args = TrainingArguments(
                    output_dir=artifacts_dir,
                    # add torch.compile - doesn't help
                    # torch_compile=True,
                    # --- THIS IS THE DEFINITIVE FIX ---
                    gradient_checkpointing=True,
                    gradient_checkpointing_kwargs={"use_reentrant": False},
                    # --- Disable FSDP & enable DDP ---
                    fsdp="",  # An empty string explicitly disables FSDP
                    ddp_find_unused_parameters=False,
                    # other args
                    per_device_train_batch_size=24,
                    gradient_accumulation_steps=4,
                    warmup_steps=1,
                    max_steps=10,
                    save_steps=2,
                    learning_rate=2e-4,
                    bf16=True,
                    logging_steps=1,
                    optim="paged_adamw_8bit",
                    weight_decay=0.01,
                    lr_scheduler_type="linear",
                    seed=args.seed,
                    report_to="none",
                )

                trainer = SFTTrainer(
                    model=model,
                    train_dataset=doc_dataset,
                    args=training_args,
                )

                print("Starting SFT training.")
                trainer.train(resume_from_checkpoint=resume_path_for_doc_sft)
                print("Documentation SFT training complete.")
                doc_sft_save_path = f"{artifacts_dir}/doc_sft_checkpoint"
                print(f"Saving Documentation SFT LoRA adapters to {doc_sft_save_path}...")
                model.save_pretrained(doc_sft_save_path)
                tokenizer.save_pretrained(doc_sft_save_path)
                doc_dataset = None
        else:
            print("--- Skipping SFT Phase ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tune a model with SFT and GRPO.")
    parser.add_argument("--model_name", type=str, default="meta-llama/Meta-Llama-3.1-8B-Instruct")
    parser.add_argument("--max_seq_length", type=int, default=1024)
    parser.add_argument("--load_in_4bit", action="store_true", default=True)
    parser.add_argument("--lora_rank", type=int, default=32)
    parser.add_argument("--lora_alpha", type=int, default=32)
    parser.add_argument("--hf_token", type=str, default=None)
    parser.add_argument("--output_dir", type=str, default="/root/lustre/outputs")
    parser.add_argument("--learning_rate", type=float, default=5e-6)
    parser.add_argument("--per_device_train_batch_size", type=int, default=1)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=1)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--num_generations", type=int, default=24)
    parser.add_argument("--max_steps", type=int, default=250)
    parser.add_argument("--save_steps", type=int, default=250)
    parser.add_argument("--logging_steps", type=int, default=1)
    parser.add_argument("--max_grad_norm", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=3407)
    parser.add_argument("--max_prompt_length", type=int, default=512)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.7)
    parser.add_argument("--sft_max_steps", type=int, default=2000)
    parser.add_argument("--timeout", type=str, default="00:00", help='Set a training timeout in HH:MM format.')
    parser.add_argument("--no_sft", action="store_true", help="Skip SFT, only run GRPO training")
    parser.add_argument("--no_grpo", action="store_true", help="Skip GRPO, only run SFT training")
    parser.add_argument("--resume_from_checkpoint", type=str, default=None, help="Path to checkpoint.")
    parser.add_argument("--ci_jobs", action="store_true", help="Use CI jobs for training")
    parser.add_argument("--doc_sft_path", type=str, default=None, help="Path to documentation files for pre-training.")
    parser.add_argument("--doc_sft_max_steps", type=int, default=1000, help="Max steps for doc SFT phase.")

    args = parser.parse_args()
    main(args)
```

requirements.txt
```
cat requirements.txt
# It is recommended to install PyTorch first, following the official instructions
# for your specific CUDA version: https://pytorch.org/get-started/locally/
torch

# Core  training libraries
trl>=0.8.6
transformers>=4.41.0
datasets>=2.19.0
peft>=0.11.1
accelerate>=0.30.0
bitsandbytes>=0.43.0

# Use Flash Attention 2
flash-attn

# VLLM for fast inference (Optional, but used in the original notebook)
# Note: VLLM installation can be complex. Please refer to the official VLLM documentation
# for your specific OS and CUDA version if the following command fails.
# https://docs.vllm.ai/en/latest/getting_started/installation.html
vllm

# Other dependencies
sentencepiece
protobuf
huggingface_hub
hf_transfer
xformers

#progress bar
tqdm
```

Using CUDA 12.1 &  PT 2.5.1
pip3 install torch torchvision torchaudio packaging --index-url https://download.pytorch.org/whl/cu121

root@cw-dfw-h100-004-320-012:/app# python3 -c "import torch; print(f'PyTorch version: {torch.__version__}')"
PyTorch version: 2.5.1+cu121

*** RUN WITH HF on 2.5.1 ***
RUN sed -i -e 's/if not is_torch_greater_or_equal/if False: #/' \
    /usr/local/lib/python3.10/dist-packages/transformers/utils/import_utils.py

### Expected behavior

Train, Training resume from checkpoint, finish successfully.

## 评论 (2)

### matthewdouglas · 2025-07-16

Hi,
Resuming with paged optimizers might not work as expected. Can you try with AdamW8bit, or plain AdamW, to see if you have the same issue?

### TimDettmers · 2026-02-16

Closing this issue as stale. The maintainer asked in July 2025 whether the issue reproduces with AdamW8bit or plain AdamW instead of the paged optimizer, but there was no follow-up.

Checkpoint resumption with paged optimizers in multi-GPU setups is a known limitation area — see #782 for the broader tracking issue on checkpoint resumption problems.

If you're still experiencing this on the latest bitsandbytes, please reopen or file a new issue with the results of testing with a non-paged optimizer (AdamW8bit or plain AdamW) to help isolate the root cause.
