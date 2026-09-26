# [Issue #2220] Quantized model behave differently on multi GPU with device_map="auto" compared to single  GPU

source: https://github.com/ModelCloud/GPTQModel/issues/2220
state: closed | updated: 2025-12-21T11:38:44Z
labels: 

## 正文

I quantized llma2-70b into Int8 format using [vllm expample](https://docs.vllm.com.cn/en/latest/features/quantization/gptqmodel.html).

But I found that if I load the model with `device_map="auto"` on 2 GPUs, the output attention hidden states of second half layers (on cuda:1) is different compared to 1 GPU case. here is my script, modified from [spec-bench](https://github.com/hemingkx/Spec-Bench/blob/main/evaluation/inference_sps.py)

```python
from typing import Optional, Callable
import torch
import argparse
from evaluation.eval import run_eval, reorg_answer_file
import pdb
from fastchat.utils import str_to_torch_dtype
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationMixin
from evaluation.decoding_tp import _assisted_decoding
from gptqmodel import GPTQModel, QuantizeConfig


def sps_forward(inputs, model, tokenizer, max_new_tokens, do_sample=False, temperature=0.0, drafter=None):
    input_ids = inputs.input_ids
    model.generation_config.max_new_tokens = max_new_tokens
    model.generation_config.output_hidden_states = True
    output_ids, idx, accept_length_list = model.generate(
        **inputs,
        generation_config=model.generation_config,
        assistant_model=drafter,
        do_sample=do_sample,
        temperature=temperature,
        return_dict_in_generate=True,
        output_hidden_states=True,
    )
    new_token = len(output_ids[0][len(input_ids[0]):])
    return output_ids, new_token, idx + 1, accept_length_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model-path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--drafter-path",
        type=str,
        required=True,
    )
    parser.add_argument("--model-id", type=str, required=True)
    parser.add_argument(
        "--bench-name",
        type=str,
        default="mt_bench",
        help="The name of the benchmark question set.",
    )
    parser.add_argument(
        "--question-begin",
        type=int,
        help="A debug option. The begin index of questions.",
    )
    parser.add_argument(
        "--question-end",
        type=int,
        help="A debug option. The end index of questions."
    )
    parser.add_argument("--answer-file", type=str, help="The output answer file.")
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=1024,
        help="The maximum number of new generated tokens.",
    )
    parser.add_argument(
        "--num-choices",
        type=int,
        default=1,
        help="How many completion choices to generate.",
    )
    parser.add_argument(
        "--num-gpus-per-model",
        type=int,
        default=1,
        help="The number of GPUs per model.",
    )
    parser.add_argument(
        "--num-gpus-total", type=int, default=1, help="The total number of GPUs."
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="The temperature for medusa sampling.",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="float16",
        choices=["float32", "float64", "float16", "bfloat16"],
        help="Override the default dtype. If not set, it will use float16 on GPU.",
    )
    parser.add_argument(
        "--drafter-dtype",
        type=str,
        default="float16",
        choices=["float32", "float64", "float16", "bfloat16"],
        help="Override the default dtype. If not set, it will use float16 on GPU.",
    )
    args = parser.parse_args()
    
    #_set_backend_determinism()
    
    GenerationMixin._assisted_decoding = _assisted_decoding
    print("[INFO] Patched GenerationMixin._assisted_decoding -> evaluation.decoding_tp._assisted_decoding")

    question_file = f"data/{args.bench_name}/question.jsonl"
    if args.answer_file:
        answer_file = args.answer_file
    else:
        answer_file = f"data/{args.bench_name}/model_answer/{args.model_id}.jsonl"

    print(f"Output to {answer_file}")
 
    model = GPTQModel.load(
        model_id_or_path=args.model_path,
        quantize_config=QuantizeConfig(bits=8, ),
        device_map="auto",
        low_cpu_mem_usage=True,
        trust_remote_code=True,
    )
    drafter = AutoModelForCausalLM.from_pretrained(
        args.drafter_path,
        torch_dtype=str_to_torch_dtype(args.drafter_dtype),
        low_cpu_mem_usage=True,
        device_map="auto",
    )
    
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    model.eval()
    drafter.eval()

    do_sample = args.temperature > 0.0
        
    run_eval(
        model=model,
        tokenizer=tokenizer,
        forward_func=sps_forward,
        model_id=args.model_id,
        question_file=question_file,
        question_begin=args.question_begin,
        question_end=args.question_end,
        answer_file=answer_file,
        max_new_tokens=args.max_new_tokens,
        num_choices=args.num_choices,
        num_gpus_per_model=args.num_gpus_per_model,
        num_gpus_total=args.num_gpus_total,
        drafter=drafter,
        temperature=args.temperature,
        do_sample=do_sample,
    )

    reorg_answer_file(answer_file)
```
I modified `_assistant_decoding` function to save one step infomation

```python
SAVE_DEBUG_FILE = os.environ.get("SAVE_SPECULATIVE_DEBUG", None)
# after 2.3. 
if SAVE_DEBUG_FILE :
            saved_hidden_states = [
                        hs[:, -candidate_length - 1 :].cpu().clone() for hs in outputs.hidden_states
                    ]
            step_data = {
                "step": step,
                "cur_len": cur_len,
                "candidate_length": candidate_length,
                "input_ids": input_ids.cpu().clone(),
                "candidate_input_ids": candidate_input_ids.cpu().clone(),
                "candidate_logits": candidate_logits.cpu().clone() if candidate_logits is not None else None,
                "target_logits": new_logits.cpu().clone(),
                "attention_mask": model_inputs.get("attention_mask").cpu().clone() if "attention_mask" in model_inputs else None,
                "position_ids": model_inputs.get("position_ids").cpu().clone() if "position_ids" in model_inputs else None,
                "drafter_device": str(drafter_device),
                "target_device": str(self.device),
                "hidden_states": saved_hidden_states,
            }
            debug_data["steps"].append(step_data)
            debug_data["final_output_ids"] = None  
            debug_data["accept_length_list"] = accept_length_list

            Path(SAVE_DEBUG_FILE).parent.mkdir(parents=True, exist_ok=True)
            with open(SAVE_DEBUG_FILE, "wb") as f:
                pickle.dump(debug_data, f)
            print(f"    drafter token: {candidate_input_ids[0, cur_len:].tolist()[:candidate_length]}")
            print(f"    target  argmax    : {new_logits[0, :-1].argmax(-1).tolist()}")
            import sys; sys.exit(0)  
```

and compared results between single GPU and multi GPUs using following code
```python
# compare_spec_debug.py
# compare_final_all.py
import pickle
import torch
import torch.nn.functional as F
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--single", type=str, required=True)
parser.add_argument("--multi",  type=str, required=True)
args = parser.parse_args()

def load_first_step(p):
    with open(p, "rb") as f:
        data = pickle.load(f)
    return [s for s in data["steps"] if s["step"] == 1][0]

single = load_first_step(args.single)
multi  = load_first_step(args.multi)

# 提取验证部分（去掉最后一个用于采样的位置）
s_tgt = single["target_logits"][:, :-1].squeeze(0)      # [L, V]
m_tgt = multi["target_logits"][:, :-1].squeeze(0)

s_cand = single["candidate_logits"].squeeze(0) if single["candidate_logits"] is not None else None
m_cand = multi["candidate_logits"].squeeze(0)  if multi["candidate_logits"]  is not None else None

drafter_tokens = single["candidate_input_ids"][0, single["cur_len"]: single["cur_len"]+single["candidate_length"]]

print("=" * 80)
print("完整第一步对比报告".center(80))
print("=" * 80)

print(f"candidate_length : {single['candidate_length']}")
print(f"drafter 猜测 token : {drafter_tokens.tolist()}")
print(f"input_ids 一致    : {torch.equal(single['input_ids'], multi['input_ids'])}")
print(f"candidate_input_ids 一致 : {torch.equal(single['candidate_input_ids'], multi['candidate_input_ids'])}")
print()

# 1. target_logits 单卡 vs 多卡
print("1. target_logits 单卡 ↔ 多卡 差异".center(70))
diff_tgt = torch.abs(s_tgt - m_tgt)
print(f"   最大绝对误差 : {diff_tgt.max().item():12.6f}")
print(f"   平均绝对误差 : {diff_tgt.mean().item():12.6f}")
print()

# 2. candidate_logits 单卡 vs 多卡（你特别要的）
print("2. candidate_logits 单卡 ↔ 多卡 差异".center(70))
if s_cand is not None and m_cand is not None:
    diff_cand = torch.abs(s_cand - m_cand)
    print(f"   最大绝对误差 : {diff_cand.max().item():12.6f}")
    print(f"   平均绝对误差 : {diff_cand.mean().item():12.6f}")
    print(f"   标准差       : {diff_cand.std().item():12.6f}")
print()

# 3. （candidate_logits → target_logits）
print("3. drafter 质量（candidate_logits → target_logits）".center(70))
print(f"{'':20} {'最大误差':>12} {'平均误差':>12} {'接受数':>8}")
if s_cand is not None:
    err_s = torch.abs(s_cand - s_tgt)
    accept_s = (s_tgt.argmax(-1) == drafter_tokens).sum().item()
    print(f"{'单卡':20} {err_s.max().item():12.6f} {err_s.mean().item():12.6f} {accept_s:5}/{len(drafter_tokens)}")
else:
    accept_s = (s_tgt.argmax(-1) == drafter_tokens).sum().item()
    print(f"{'单卡':20} {'(无cand)':>12} {'(无cand)':>12} {accept_s:5}/{len(drafter_tokens)}")

if m_cand is not None:
    err_m = torch.abs(m_cand - m_tgt)
    accept_m = (m_tgt.argmax(-1) == drafter_tokens).sum().item()
    print(f"{'多卡':20} {err_m.max().item():12.6f} {err_m.mean().item():12.6f} {accept_m:5}/{len(drafter_tokens)}")
else:
    accept_m = (m_tgt.argmax(-1) == drafter_tokens).sum().item()
    print(f"{'多卡':20} {'(无cand)':>12} {'(无cand)':>12} {accept_m:5}/{len(drafter_tokens)}")
print()

# 4. argmax 
print("位置级 argmax 对比".center(70))
s_top1 = s_tgt.argmax(-1)
m_top1 = m_tgt.argmax(-1)
for i, token in enumerate(drafter_tokens.tolist()):
    print(f"Pos {i}: drafter {token:5d} | single {s_top1[i].item():5d} {'✓' if s_top1[i].item() == token else '✗'} | "
          f"multi  {m_top1[i].item():5d} {'✓' if m_top1[i].item() == token else '✗'}")

print("5. hidden_states 分层差异".center(70))
s_hs = single.get("hidden_states", None)
m_hs = multi.get("hidden_states", None)

if s_hs is None or m_hs is None:
    print("   单卡或多卡缺少 hidden_states 字段，跳过。")
else:
    if len(s_hs) != len(m_hs):
        print(f"   层数不一致: single={len(s_hs)}, multi={len(m_hs)}")
    else:
        print(f"{'层':>4} {'shape一致':>10} {'max_abs':>12} {'mean_abs':>12}")
        first_diff_layer = None
        for li, (sh, mh) in enumerate(zip(s_hs, m_hs)):
            same_shape = tuple(sh.shape) == tuple(mh.shape)
            if not same_shape:
                print(f"{li:4d} {'False':>10} {'-':>12} {'-':>12}")
                continue
            diff = (sh - mh).abs()
            max_abs = diff.max().item()
            mean_abs = diff.mean().item()
            # first different layer
            if first_diff_layer is None and (max_abs > 0.0 or mean_abs > 0.0):
                first_diff_layer = li
            print(f"{li:4d} {str(same_shape):>10} {max_abs:12.6f} {mean_abs:12.6f}")


```

and the result shows that the llam2-7b drafter logits is same in 2 cases but quantized llama2-70b target's hidden states is dramatically different on the second GPU
```
candidate_length : 1
drafter 猜测 token : [26901]
input_ids 一致    : True
candidate_input_ids 一致 : True

                     1. target_logits 单卡 ↔ 多卡 差异                      
   最大绝对误差 :    18.126953
   平均绝对误差 :     2.402046

                    2. candidate_logits 单卡 ↔ 多卡 差异                    
   最大绝对误差 :     0.000000
   平均绝对误差 :     0.000000
   标准差       :     0.000000

           3. drafter 质量（candidate_logits → target_logits）            
                             最大误差         平均误差      接受数
单卡                       9.171875     1.171219     0/1
多卡                      17.580078     2.810862     0/1

                            位置级 argmax 对比                             
Pos 0: drafter 26901 | single 18585 ✗ | multi  19259 ✗
                        5. hidden_states 分层差异                         
   层    shape一致      max_abs     mean_abs
   0       True     0.000000     0.000000
   1       True     0.000000     0.000000
   2       True     0.000000     0.000000
   3       True     0.000000     0.000000
   4       True     0.000000     0.000000
   5       True     0.000000     0.000000
   6       True     0.000000     0.000000
   7       True     0.000000     0.000000
   8       True     0.000000     0.000000
   9       True     0.000000     0.000000
  10       True     0.000000     0.000000
  11       True     0.000000     0.000000
  12       True     0.000000     0.000000
  13       True     0.000000     0.000000
  14       True     0.000000     0.000000
  15       True     0.000000     0.000000
  16       True     0.000000     0.000000
  17       True     0.000000     0.000000
  18       True     0.000000     0.000000
  19       True     0.000000     0.000000
  20       True     0.000000     0.000000
  21       True     0.000000     0.000000
  22       True     0.000000     0.000000
  23       True     0.000000     0.000000
  24       True     0.000000     0.000000
  25       True     0.000000     0.000000
  26       True     0.000000     0.000000
  27       True     0.000000     0.000000
  28       True     0.000000     0.000000
  29       True     0.000000     0.000000
  30       True     0.000000     0.000000
  31       True     0.000000     0.000000
  32       True     0.000000     0.000000
  33       True     0.000000     0.000000
  34       True     0.000000     0.000000
  35       True     0.000000     0.000000
  36       True     0.000000     0.000000
  37       True     0.000000     0.000000
  38       True     0.000000     0.000000
  39       True     0.000000     0.000000
  40       True     0.000000     0.000000
  41       True     1.765625     0.326904
  42       True     2.902344     0.520020
  43       True     5.023438     0.672363
  44       True     7.066406     0.794434
  45       True     5.703125     0.947754
  46       True     8.804688     1.071289
  47       True    11.265625     1.173828
  48       True    15.304688     1.296875
  49       True    16.218750     1.413086
  50       True    20.765625     1.499023
  51       True    25.500000     1.581055
  52       True    28.000000     1.673828
  53       True    33.781250     1.760742
  54       True    38.500000     1.835938
  55       True    40.375000     1.911133
  56       True    43.531250     1.989258
  57       True    54.968750     2.070312
  58       True    55.031250     2.150391
  59       True    60.500000     2.222656
  60       True    65.062500     2.294922
  61       True    67.750000     2.388672
  62       True    69.562500     2.455078
  63       True    75.125000     2.533203
  64       True    78.750000     2.607422
  65       True    84.062500     2.699219
  66       True    85.375000     2.775391
  67       True    90.625000     2.857422
  68       True    96.937500     2.931641
  69       True   102.562500     3.019531
  70       True   101.187500     3.117188
  71       True   107.500000     3.218750
  72       True   105.187500     3.328125
  73       True   109.562500     3.462891
  74       True   112.937500     3.609375
  75       True   118.437500     3.736328
  76       True   109.250000     3.857422
  77       True   123.187500     4.031250
  78       True   141.875000     4.218750
  79       True   133.000000     4.457031
  80       True    39.062500     1.160156
```

What cause the situation and how can I solve it, please!!!

## 评论 (17)

### Qubitium · 2025-11-27

@DarkenStar 

1. Disable draft model
2. Remove low_cpu_memoory option


```py
model = GPTQModel.load(
        model_id_or_path=args.model_path,
        quantize_config=QuantizeConfig(bits=8, ),
        device_map="auto",
        low_cpu_mem_usage=True, <-- remove this
        trust_remote_code=True,
    )
    drafter = AutoModelForCausalLM.from_pretrained( <---- remove this....to isolate your problem
        args.drafter_path,
        torch_dtype=str_to_torch_dtype(args.drafter_dtype),
        low_cpu_mem_usage=True,
        device_map="auto",
    )
    
```

### DarkenStar · 2025-11-27

OK，thank you very much!!!
Let me write a test case

### DarkenStar · 2025-11-27

@Qubitium 
Hello, I write a new script with only using quantized model forward to get hidden states and logits
```python
import argparse
import pickle
from pathlib import Path

import torch
from transformers import AutoTokenizer
from gptqmodel import GPTQModel, QuantizeConfig


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model-path",
        type=str,
        default="/home/aocheng/QuantSpec/Llama-2-70b-hf-gptqmodel-8bit",
        help="Path to the GPTQ model (including tokenizer).",
    )
    parser.add_argument(
        "--save-path",
        type=str,
        required=True,
        help="Path to save the debug pickle file, e.g. /tmp/gptq_hidden_debug.pkl",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="Hello, this is a test input for multi-GPU GPTQ inference.",
        help="Prompt text for the test run.",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="float16",
        choices=["float16", "bfloat16", "float32", "bfloat16"],
        help="Torch dtype for inference.",
    )
    args = parser.parse_args()

    torch_dtype = {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }[args.dtype]

    print(f"[INFO] Loading GPTQModel from {args.model_path}")
    model = GPTQModel.load(
        model_id_or_path=args.model_path,
        quantize_config=QuantizeConfig(bits=8),
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch_dtype,
    )
    print("[INFO] Model loaded")

    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    print("[INFO] Tokenizer loaded")
    model.eval()

    print(f"[INFO] Prompt: {args.prompt!r}")
    inputs = tokenizer(
        args.prompt,
        return_tensors="pt",
        add_special_tokens=True,
    )
    print("[INFO] Tokenized prompt")

    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    print("[INFO] Inputs moved to device(s)")

    with torch.no_grad():
        print("[INFO] Starting forward pass...")
        outputs = model(
            **inputs,
            output_hidden_states=True,
            return_dict=True,
        )
    print("[INFO] Forward pass finished")

    # outputs.logits: [bs, seq_len, vocab]
    # outputs.hidden_states: tuple(num_layers+1) of [bs, seq_len, hidden]
    if outputs.hidden_states is None:
        raise RuntimeError(
            "Model did not return hidden_states. "
            "Please make sure the model supports output_hidden_states=True."
        )

    hidden_states = [h.cpu().clone() for h in outputs.hidden_states]
    logits = outputs.logits.cpu().clone()

    debug_obj = {
        "prompt": args.prompt,
        "input_ids": inputs["input_ids"].cpu().clone(),
        "logits": logits,
        "hidden_states": hidden_states,  # list[num_layers+1], each [1, seq_len, hidden]
        "model_dtype": str(torch_dtype),
        "model_device": str(model.device),
    }

    save_path = Path(args.save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "wb") as f:
        pickle.dump(debug_obj, f)

    print(f"[INFO] Forward pass finished. Debug data saved to: {save_path}")


if __name__ == "__main__":
    main()
```

and use following script to compare the result. Unfortunately, the result also shows different hidden states value of the second device, and the console output is below.

```python
import argparse
import pickle

import torch

parser = argparse.ArgumentParser(description="Compare single-GPU and multi-GPU hidden/debug dumps.")
parser.add_argument("--single", type=str, required=True, help="Path to single-GPU debug pickle.")
parser.add_argument("--multi",  type=str, required=True, help="Path to multi-GPU debug pickle.")
args = parser.parse_args()


def load_debug(p):
    with open(p, "rb") as f:
        data = pickle.load(f)
    return data


single = load_debug(args.single)
multi  = load_debug(args.multi)

print("=" * 80)
print("First-pass debug comparison (single-GPU vs multi-GPU)".center(80))
print("=" * 80)
print()

# 0. Basic metadata comparison
print("0. Basic metadata".center(70))
prompt_equal = (single.get("prompt", None) == multi.get("prompt", None))
print(f"prompt equal        : {prompt_equal}")
print(f"single prompt       : {repr(single.get('prompt', None))}")
print(f"multi  prompt       : {repr(multi.get('prompt', None))}")

single_dtype = single.get("model_dtype", "N/A")
multi_dtype  = multi.get("model_dtype", "N/A")
print(f"model_dtype single  : {single_dtype}")
print(f"model_dtype multi   : {multi_dtype}")

single_device = single.get("model_device", "N/A")
multi_device  = multi.get("model_device", "N/A")
print(f"model_device single : {single_device}")
print(f"model_device multi  : {multi_device}")
print()

# 1. input_ids comparison
print("1. input_ids comparison".center(70))
s_ids = single["input_ids"]
m_ids = multi["input_ids"]
print(f"shape single        : {tuple(s_ids.shape)}")
print(f"shape multi         : {tuple(m_ids.shape)}")
same_shape_ids = tuple(s_ids.shape) == tuple(m_ids.shape)
print(f"same shape          : {same_shape_ids}")
same_ids = torch.equal(s_ids, m_ids) if same_shape_ids else False
print(f"exactly equal       : {same_ids}")
if same_shape_ids and not same_ids:
    diff_positions = (s_ids != m_ids).nonzero(as_tuple=False)
    print(f"num differing tokens: {diff_positions.shape[0]}")
print()

# 2. logits comparison
print("2. logits comparison".center(70))
s_logits = single["logits"]          # [1, L, V]
m_logits = multi["logits"]
print(f"shape single        : {tuple(s_logits.shape)}")
print(f"shape multi         : {tuple(m_logits.shape)}")

same_shape_logits = tuple(s_logits.shape) == tuple(m_logits.shape)
print(f"same shape          : {same_shape_logits}")

if same_shape_logits:
    diff_logits = (s_logits - m_logits).abs()
    max_abs = diff_logits.max().item()
    mean_abs = diff_logits.mean().item()
    print(f"max absolute error  : {max_abs:12.6f}")
    print(f"mean absolute error : {mean_abs:12.6f}")
    # argmax token comparison along vocab dimension
    s_top1 = s_logits.argmax(-1)  # [1, L]
    m_top1 = m_logits.argmax(-1)
    same_top1 = torch.equal(s_top1, m_top1)
    print(f"top-1 token equal   : {same_top1}")
    if not same_top1:
        diff_pos = (s_top1 != m_top1).nonzero(as_tuple=False)
        print(f"num differing positions in top-1: {diff_pos.shape[0]}")
else:
    print("logits shapes mismatch, skip numeric comparison.")
print()

# 3. hidden_states comparison (per-layer)
print("3. hidden_states (per-layer) comparison".center(70))
s_hs = single.get("hidden_states", None)
m_hs = multi.get("hidden_states", None)

if s_hs is None or m_hs is None:
    print("Either single or multi does not contain 'hidden_states'; skipping.")
else:
    # ensure list/tuple of tensors
    if not isinstance(s_hs, (list, tuple)) or not isinstance(m_hs, (list, tuple)):
        print("hidden_states is not a list/tuple of tensors; skipping detailed comparison.")
    else:
        print(f"num layers (including embedding output): single={len(s_hs)}, multi={len(m_hs)}")
        if len(s_hs) != len(m_hs):
            print("layer counts differ, cannot do full one-to-one comparison.")
        print(f"{'layer':>6} {'same_shape':>12} {'max_abs':>12} {'mean_abs':>12}")
        first_diff_layer = None
        for li, (sh, mh) in enumerate(zip(s_hs, m_hs)):
            if not (isinstance(sh, torch.Tensor) and isinstance(mh, torch.Tensor)):
                print(f"{li:6d} {'False':>12} {'-':>12} {'-':>12}")
                continue
            same_shape = tuple(sh.shape) == tuple(mh.shape)
            if not same_shape:
                print(f"{li:6d} {'False':>12} {'-':>12} {'-':>12}")
                continue

            diff = (sh - mh).abs()
            max_abs = diff.max().item()
            mean_abs = diff.mean().item()
            if first_diff_layer is None and (max_abs > 0.0 or mean_abs > 0.0):
                first_diff_layer = li
            print(f"{li:6d} {str(same_shape):>12} {max_abs:12.6f} {mean_abs:12.6f}")

        print()
        if first_diff_layer is None:
            print("All compared layers are numerically identical (zero difference).")
        else:
            print(f"First layer with non-zero difference: {first_diff_layer}")
print()

print("=" * 80)
print("End of comparison report".center(80))
print("=" * 80)
```

output

```
================================================================================
             First-pass debug comparison (single-GPU vs multi-GPU)              
================================================================================

                          0. Basic metadata                           
prompt equal        : True
single prompt       : 'Hello, this is a test input for multi-GPU GPTQ inference.'
multi  prompt       : 'Hello, this is a test input for multi-GPU GPTQ inference.'
model_dtype single  : torch.float16
model_dtype multi   : torch.float16
model_device single : cuda:0
model_device multi  : cuda:0

                       1. input_ids comparison                        
shape single        : (1, 18)
shape multi         : (1, 18)
same shape          : True
exactly equal       : True

                         2. logits comparison                         
shape single        : (1, 18, 32000)
shape multi         : (1, 18, 32000)
same shape          : True
max absolute error  :    23.187500
mean absolute error :     4.042969
top-1 token equal   : False
num differing positions in top-1: 18

               3. hidden_states (per-layer) comparison                
num layers (including embedding output): single=81, multi=81
 layer   same_shape      max_abs     mean_abs
     0         True     0.000000     0.000000
     1         True     0.000000     0.000000
     2         True     0.000000     0.000000
     3         True     0.000000     0.000000
     4         True     0.000000     0.000000
     5         True     0.000000     0.000000
     6         True     0.000000     0.000000
     7         True     0.000000     0.000000
     8         True     0.000000     0.000000
     9         True     0.000000     0.000000
    10         True     0.000000     0.000000
    11         True     0.000000     0.000000
    12         True     0.000000     0.000000
    13         True     0.000000     0.000000
    14         True     0.000000     0.000000
    15         True     0.000000     0.000000
    16         True     0.000000     0.000000
    17         True     0.000000     0.000000
    18         True     0.000000     0.000000
    19         True     0.000000     0.000000
    20         True     0.000000     0.000000
    21         True     0.000000     0.000000
    22         True     0.000000     0.000000
    23         True     0.000000     0.000000
    24         True     0.000000     0.000000
    25         True     0.000000     0.000000
    26         True     0.000000     0.000000
    27         True     0.000000     0.000000
    28         True     0.000000     0.000000
    29         True     0.000000     0.000000
    30         True     0.000000     0.000000
    31         True     0.000000     0.000000
    32         True     0.000000     0.000000
    33         True     0.000000     0.000000
    34         True     0.000000     0.000000
    35         True     0.000000     0.000000
    36         True     0.000000     0.000000
    37         True     0.000000     0.000000
    38         True     0.000000     0.000000
    39         True     0.000000     0.000000
    40         True     0.000000     0.000000
    41         True     9.984375     1.247070
    42         True    10.906250     1.321289
    43         True    15.312500     1.399414
    44         True    22.937500     1.476562
    45         True    30.062500     1.576172
    46         True    38.406250     1.667969
    47         True    44.531250     1.754883
    48         True    70.437500     1.845703
    49         True    84.000000     1.910156
    50         True    97.000000     1.981445
    51         True   100.937500     2.048828
    52         True   109.000000     2.128906
    53         True   127.750000     2.205078
    54         True   137.625000     2.275391
    55         True   143.750000     2.345703
    56         True   154.500000     2.414062
    57         True   169.750000     2.468750
    58         True   178.375000     2.525391
    59         True   183.125000     2.589844
    60         True   191.625000     2.648438
    61         True   198.625000     2.712891
    62         True   201.750000     2.761719
    63         True   205.750000     2.816406
    64         True   206.250000     2.873047
    65         True   209.625000     2.929688
    66         True   210.750000     2.984375
    67         True   212.500000     3.058594
    68         True   215.500000     3.123047
    69         True   221.750000     3.189453
    70         True   226.625000     3.267578
    71         True   230.625000     3.363281
    72         True   233.250000     3.457031
    73         True   243.875000     3.554688
    74         True   237.250000     3.658203
    75         True   240.375000     3.769531
    76         True   236.000000     3.908203
    77         True   934.000000     4.074219
    78         True  1385.000000     4.312500
    79         True  1688.000000     4.644531
    80         True    95.312500     1.112305

First layer with non-zero difference: 41

================================================================================
                            End of comparison report                            
================================================================================
```

Could you please tell me how to fix the problem ? Please !!!

### Qubitium · 2025-11-27

Did you set do_sampling to false and temperature to 1.0?

Makes sure sampling is disabled so we get deterministic output to compare between  the two.

Do you have two of the same model GPU? 

### DarkenStar · 2025-11-28

@Qubitium 
I collected the hidden states and logits using a small debug script:
```python
CUDA_VISIBLE_DEVICES=6 python -m evaluation.inference_gptq_hidden_debug \
  --save-path ./gptq_single_hidden_debug.pkl \
  --dtype float16

CUDA_VISIBLE_DEVICES=6,7 python -m evaluation.inference_gptq_hidden_debug \
  --save-path ./gptq_multi_hidden_debug.pkl \
  --dtype float16
```

The script only runs a single forward pass with torch.no_grad() and does not use sampling at all (above script): 
```python
with torch.no_grad():
        print("[INFO] Starting forward pass...")
        outputs = model(
            **inputs,
            output_hidden_states=True,
            return_dict=True,
        )
```
So there is no do_sampling / temperature involved here – it's a plain deterministic forward pass on the same input ids.
And I run the scripy on same model GPU
```bash
Fri Nov 28 01:29:31 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.144.03             Driver Version: 550.144.03     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H20-3e                  On  |   00000000:65:02.0 Off |                    0 |
| N/A   36C    P0            119W /  500W |   14575MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA H20-3e                  On  |   00000000:65:03.0 Off |                    0 |
| N/A   41C    P0            124W /  500W |    2270MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA H20-3e                  On  |   00000000:67:02.0 Off |                    0 |
| N/A   53C    P0            269W /  500W |   38355MiB / 143771MiB |     99%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA H20-3e                  On  |   00000000:67:03.0 Off |                    0 |
| N/A   44C    P0            200W /  500W |   38099MiB / 143771MiB |      2%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA H20-3e                  On  |   00000000:69:02.0 Off |                    0 |
| N/A   37C    P0            121W /  500W |    2649MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA H20-3e                  On  |   00000000:69:03.0 Off |                    0 |
| N/A   41C    P0            127W /  500W |    2272MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA H20-3e                  On  |   00000000:6B:02.0 Off |                    0 |
| N/A   40C    P0            123W /  500W |    2134MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA H20-3e                  On  |   00000000:6B:03.0 Off |                    0 |
| N/A   35C    P0            124W /  500W |     330MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
```



### DarkenStar · 2025-12-01

@Qubitium Hello, could you please help me to fix or explan this error ? I think I have minimized the problem.

### Qubitium · 2025-12-10

@ZX-ModelCloud  Has been assigned to check this bug. Most likely this is a bug within transformers. 



### DarkenStar · 2025-12-12

> [@ZX-ModelCloud](https://github.com/ZX-ModelCloud) Has been assigned to check this bug. Most likely this is a bug within transformers.

Thanks a lot! Could you please inform me when this bug is fixed？I aslo make effort to find out the bug.

### ZX-ModelCloud · 2025-12-15

> > [@ZX-ModelCloud](https://github.com/ZX-ModelCloud) Has been assigned to check this bug. Most likely this is a bug within transformers.
> 
> Thanks a lot! Could you please inform me when this bug is fixed？I aslo make effort to find out the bug.

```
CUDA_VISIBLE_DEVICES=6 python -m evaluation.inference_gptq_hidden_debug \
  --save-path ./gptq_single_hidden_debug.pkl \
  --dtype float16

CUDA_VISIBLE_DEVICES=6,7 python -m evaluation.inference_gptq_hidden_debug \
  --save-path ./gptq_multi_hidden_debug.pkl \
  --dtype float16
```

Could you provide the inference log from when you ran these two commands?

---

```
from datasets import load_dataset
from gptqmodel import GPTQModel, QuantizeConfig

model_id = "meta-llama/Llama-2-70b-hf"
quant_path = "Llama-2-70b-hf-gptqmodel-8bit"

calibration_dataset = load_dataset(
    "allenai/c4",
    data_files="en/c4-train.00001-of-01024.json.gz",
    split="train"
).select(range(1024))["text"]

quant_config = QuantizeConfig(bits=8, group_size=128)

model = GPTQModel.load(model_id, quant_config)

# increase `batch_size` to match gpu/vram specs to speed up quantization
model.quantize(calibration_dataset, batch_size=2)

model.save(quant_path)
```
I quantized the llama-2-70b model locally and then ran the Python code you provided (the inference log show that both single and multi-GPU configurations used the Marlin kernel), and the hidden_states showed no difference between single and multi-GPU.

---

However, when I specified the backend as BACKEND.TRITON, a difference appeared.
```
================================================================================
             First-pass debug comparison (single-GPU vs multi-GPU)              
================================================================================

                          0. Basic metadata                           
prompt equal        : True
single prompt       : 'Hello, this is a test input for multi-GPU GPTQ inference.'
multi  prompt       : 'Hello, this is a test input for multi-GPU GPTQ inference.'
model_dtype single  : torch.float16
model_dtype multi   : torch.float16
model_device single : cuda:0
model_device multi  : cuda:0

                       1. input_ids comparison                        
shape single        : (1, 18)
shape multi         : (1, 18)
same shape          : True
exactly equal       : True

                         2. logits comparison                         
shape single        : (1, 18, 32000)
shape multi         : (1, 18, 32000)
same shape          : True
max absolute error  :    16.828125
mean absolute error :     3.529297
top-1 token equal   : False
num differing positions in top-1: 18

               3. hidden_states (per-layer) comparison                
num layers (including embedding output): single=81, multi=81
 layer   same_shape      max_abs     mean_abs
     0         True     0.000000     0.000000
     1         True     0.000000     0.000000
     2         True    12.523438     0.953613
     3         True   599.000000     0.961914
     4         True   599.000000     0.967773
     5         True   599.500000     0.969238
     6         True   599.500000     0.990234
     7         True   599.000000     0.993652
     8         True   601.500000     1.018555
     9         True  1668.000000     1.046875
    10         True  1673.000000     1.074219
    11         True  1677.000000     1.083984
    12         True  1680.000000     1.111328
    13         True  1680.000000     1.120117
    14         True  1680.000000     1.147461
    15         True  1680.000000     1.163086
    16         True  1682.000000     1.195312
    17         True  1681.000000     1.229492
    18         True  1682.000000     1.263672
    19         True  1688.000000     1.287109
    20         True  1689.000000     1.320312
    21         True  1689.000000     1.331055
    22         True  1689.000000     1.364258
    23         True  1689.000000     1.379883
    24         True  1689.000000     1.417969
    25         True  1689.000000     1.423828
    26         True  1688.000000     1.451172
    27         True  1689.000000     1.455078
    28         True  1688.000000     1.491211
    29         True  1689.000000     1.507812
    30         True  1688.000000     1.556641
    31         True  1688.000000     1.580078
    32         True  1688.000000     1.619141
    33         True  1688.000000     1.634766
    34         True  1688.000000     1.684570
    35         True  1689.000000     1.686523
    36         True  1689.000000     1.724609
    37         True  1690.000000     1.730469
    38         True  1690.000000     1.778320
    39         True  1689.000000     1.774414
    40         True  1688.000000     1.849609
    41         True  1688.000000     1.891602
    42         True  1688.000000     1.966797
    43         True  1688.000000     2.029297
    44         True  1688.000000     2.107422
    45         True  1689.000000     2.203125
    46         True  1689.000000     2.304688
    47         True  1689.000000     2.337891
    48         True  1689.000000     2.445312
    49         True  1690.000000     2.503906
    50         True  1689.000000     2.576172
    51         True  1689.000000     2.630859
    52         True  1689.000000     2.701172
    53         True  1690.000000     2.761719
    54         True  1690.000000     2.835938
    55         True  1689.000000     2.894531
    56         True  1690.000000     2.970703
    57         True  1690.000000     3.027344
    58         True  1690.000000     3.099609
    59         True  1692.000000     3.158203
    60         True  1692.000000     3.230469
    61         True  1691.000000     3.255859
    62         True  1691.000000     3.316406
    63         True  1690.000000     3.347656
    64         True  1690.000000     3.408203
    65         True  1689.000000     3.472656
    66         True  1689.000000     3.531250
    67         True  1689.000000     3.556641
    68         True  1689.000000     3.613281
    69         True  1688.000000     3.673828
    70         True  1690.000000     3.757812
    71         True  1689.000000     3.826172
    72         True  1690.000000     3.927734
    73         True  1690.000000     3.982422
    74         True  1689.000000     4.085938
    75         True  1687.000000     4.187500
    76         True  1542.000000     4.324219
    77         True   753.500000     4.492188
    78         True   304.750000     4.707031
    79         True   243.250000     4.980469
    80         True    98.125000     1.178711

First layer with non-zero difference: 2

================================================================================
                            End of comparison report                            
================================================================================
```

---

I tested with BACKEND.MARLIN and BACKEND.TORCH, and there was no difference in hidden_states between single and multi-GPU.

### DarkenStar · 2025-12-15

@ZX-ModelCloud It automatically selects `TritonV2QuantLinear` kernel for me.
```bash
from_quantized: adapter: None
INFO  Estimated Quantization BPW (bits per weight): 8.31875 bpw, based on [bits: 8, group_size: 128]
`torch_dtype` is deprecated! Use `dtype` instead!
INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
INFO   Kernel: Auto-selection: adding candidate `TorchQuantLinear`
INFO  Kernel: candidates -> `[TritonV2QuantLinear, TorchQuantLinear]`
INFO  Kernel: selected -> `TritonV2QuantLinear`.
INFO  Format: Converting `checkpoint_format` from `FORMAT.GPTQ` to internal `FORMAT.GPTQ_V2`.
INFO  Format: Converting GPTQ v1 to v2
INFO  Format: Conversion complete: 0.01373600959777832s
INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
INFO  Optimize: `TritonV2QuantLinear` compilation triggered.
INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=128009 (token='<|eot_id|>')
```

### Qubitium · 2025-12-15

> [@ZX-ModelCloud](https://github.com/ZX-ModelCloud) It automatically selects `TritonV2QuantLinear` kernel for me.
> 
> from_quantized: adapter: None
> INFO  Estimated Quantization BPW (bits per weight): 8.31875 bpw, based on [bits: 8, group_size: 128]
> `torch_dtype` is deprecated! Use `dtype` instead!
> INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
> INFO   Kernel: Auto-selection: adding candidate `TorchQuantLinear`
> INFO  Kernel: candidates -> `[TritonV2QuantLinear, TorchQuantLinear]`
> INFO  Kernel: selected -> `TritonV2QuantLinear`.
> INFO  Format: Converting `checkpoint_format` from `FORMAT.GPTQ` to internal `FORMAT.GPTQ_V2`.
> INFO  Format: Converting GPTQ v1 to v2
> INFO  Format: Conversion complete: 0.01373600959777832s
> INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
> INFO  Optimize: `TritonV2QuantLinear` compilation triggered.
> INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=128009 (token='<|eot_id|>')

The bug is in TritonV2 kernel with multi-gpu and we are checking why this is the case. Another issue for your env is why `Marlin` was not selected. Did you install gptqmodel correctly via `pip install -v gptqmodel --no-build-isolation`. If you don't pass `--no-build-isolation`, Marlin kernels will not be build for your system. H20 should be compatbile with Marlin. 

### DarkenStar · 2025-12-15

> > [@ZX-ModelCloud](https://github.com/ZX-ModelCloud) It automatically selects `TritonV2QuantLinear` kernel for me.
> > from_quantized: adapter: None
> > INFO  Estimated Quantization BPW (bits per weight): 8.31875 bpw, based on [bits: 8, group_size: 128]
> > `torch_dtype` is deprecated! Use `dtype` instead!
> > INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
> > INFO   Kernel: Auto-selection: adding candidate `TorchQuantLinear`
> > INFO  Kernel: candidates -> `[TritonV2QuantLinear, TorchQuantLinear]`
> > INFO  Kernel: selected -> `TritonV2QuantLinear`.
> > INFO  Format: Converting `checkpoint_format` from `FORMAT.GPTQ` to internal `FORMAT.GPTQ_V2`.
> > INFO  Format: Converting GPTQ v1 to v2
> > INFO  Format: Conversion complete: 0.01373600959777832s
> > INFO   Kernel: Auto-selection: adding candidate `TritonV2QuantLinear`
> > INFO  Optimize: `TritonV2QuantLinear` compilation triggered.
> > INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=128009 (token='<|eot_id|>')
> 
> The bug is in TritonV2 kernel with multi-gpu and we are checking why this is the case. Another issue for your env is why `Marlin` was not selected. Did you install gptqmodel correctly via `pip install -v gptqmodel --no-build-isolation`. If you don't pass `--no-build-isolation`, Marlin kernels will not be build for your system. H20 should be compatbile with Marlin.

Dose the version matters ?
```
Name: transformers
Version: 4.57.1
Name: gptqmodel
Version: 4.2.5
```

### Qubitium · 2025-12-15

>Dose the version matters ?

Version: 4.2.5 for gptqmodel is pretty old. Too old for us to provide support to be honest. 

### DarkenStar · 2025-12-15

> > Dose the version matters ?
> 
> Version: 4.2.5 for gptqmodel is pretty old. Too old for us to provide support to be honest.

Thanks for explain, I'll try to install new version package. By the way, does the kernel influence the inference speed very much?

### Qubitium · 2025-12-15

> > > Dose the version matters ?
> > 
> > 
> > Version: 4.2.5 for gptqmodel is pretty old. Too old for us to provide support to be honest.
> 
> Thanks for explain, I'll try to install new version package. By the way, does the kernel influence the inference speed very much?

Every kernel has different speed and quality profile. Torch reference kernel is the slowest but he most accurate. The faster the kernel, the lower the relative accuracy. 

### Qubitium · 2025-12-15

@DarkenStar  Pull `main`. Tritonv2 multip-gpu bug has been fixed. https://github.com/ModelCloud/GPTQModel/issues/2220

### DarkenStar · 2025-12-15

> [@DarkenStar](https://github.com/DarkenStar) Pull `main`. Tritonv2 multip-gpu bug has been fixed. [#2220](https://github.com/ModelCloud/GPTQModel/issues/2220)

Thanks!!!
