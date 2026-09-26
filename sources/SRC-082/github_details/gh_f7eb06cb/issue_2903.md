# [Issue #2903] ParoQuant and GPTAQ Quantization Progress takes too long

source: https://github.com/ModelCloud/GPTQModel/issues/2903
state: closed | updated: 2026-06-21T07:27:50Z
labels: 

## 正文

> Hi， I successfully compiled it, but found the process is still taking very long.
> 
> How long does it typically take to quantize a ~30B model on a single H100 or similar GPU? Is my timing normal? Also, I noticed that as the quantization progresses, the VRAM usage is relatively low, but the time per step keeps getting longer?
> 
> <img width="640" height="82" alt="Image" src="https://github.com/user-attachments/assets/d567f79c-eeb2-4733-82ff-afca94e45653" />
> 
> <img width="1543" height="52" alt="Image" src="https://github.com/user-attachments/assets/c3996c64-16dd-4887-9501-6347da4b9d80" />
> 
> <img width="1539" height="60" alt="Image" src="https://github.com/user-attachments/assets/4f6145dc-0fc9-4594-b54c-ff6fd58b9eca" /> 

 _Originally posted by @Jealousc11gx in [#2898](https://github.com/ModelCloud/GPTQModel/issues/2898#issuecomment-4487770392)_

<img width="1554" height="69" alt="Image" src="https://github.com/user-attachments/assets/ab0af514-0b09-4eed-810f-0129ac6c4528" />

and there is another issue, when i quant the same model with gptaq, it stucked more than a day, and here is the log for the quantization of gptaq qwen3.5 27B, the loss is very high
`{
    "process": "gptaq",
    "layer": 0,
    "module": "linear_attn.in_proj_qkv",
    "feat: in, out": "5120, 10240",
    "dtype: size": "bf16: 103.1MB",
    "loss": "420.5862731934",
    "samples": "128",
    "damp": "0.01000",
    "time": "1.287",
    "fwd_time": "3.350",
    "(v)ram": "cuda 45.41G"
}
{
    "process": "gptaq",
    "layer": 0,
    "module": "linear_attn.in_proj_z",
    "feat: in, out": "5120, 6144",
    "dtype: size": "bf16: 61.9MB",
    "loss": "275.9195556641",
    "samples": "128",
    "damp": "0.01000",
    "time": "0.943",
    "fwd_time": "2.152",
    "(v)ram": "cuda 45.41G"
}
{
    "process": "gptaq",
    "layer": 0,
    "module": "linear_attn.out_proj",
    "feat: in, out": "6144, 5120",
    "dtype: size": "bf16: 61.9MB",
    "loss": "0.3225559294",
    "samples": "128",
    "damp": "0.01000",
    "time": "1.255",
    "fwd_time": "3.008",
    "(v)ram": "cuda 45.52G"
}
`

<img width="1546" height="244" alt="Image" src="https://github.com/user-attachments/assets/b7fc7add-82c1-41c0-83b7-ee2422414624" />

both quantization processes work in H100 single GPU 

and here is the gptaq main code:
`def main():
    args = parse_args()

    print("构建量化配置 ...", flush=True)

    qcfg = QuantizeConfig(
        bits=args.bits,
        group_size=args.group_size,
        sym=True,
        damp_percent=0.01,
        desc_act=False,
        offload_to_disk=False,
        act_group_aware=True,
        gptaq=GPTAQConfig(alpha=0.25, device="auto"),
        format=FORMAT.GPTQ,
    )

    model = GPTQModel.load(
        args.model_id,
        qcfg,
        trust_remote_code=True,
        dtype=torch.bfloat16,
    )

    conversations = load_conversations_from_jsonl(
        jsonl_path=args.jsonl_path,
        keep_system=args.keep_system,
        drop_assistant=args.drop_assistant,
        max_samples=args.max_samples,
        min_chars=args.min_chars,
        verbose=True,
    )

    if not conversations:
        raise RuntimeError("校准数据加载失败或清洗后为空，请检查 --jsonl-path 与 messages 格式。")

    calibration_dataset = conversations_to_calibration_texts(
        conversations=conversations,
        tokenizer=model.tokenizer,
        max_length=args.max_length,
        verbose=True,
    )

    if not calibration_dataset:
        raise RuntimeError("chat_template 后没有可用文本，请检查 tokenizer/chat template/messages 格式。")
    model.quantize(
        calibration_dataset,
        batch_size=args.batch_size,
    )

    os.makedirs(args.output_dir, exist_ok=True)
    model.save(args.output_dir)



if __name__ == "__main__":
    main()`

## 评论 (2)

### Qubitium · 2026-05-21

Expectations on time for quantization is 1) quant math 2) hw 3) vram 4) dtype. GPT-QModel tries to make them fast, but that's not the primary goal. The primary goal is quality first > quant time as quant time is a one time cost. 

We do welcome any contributions (prs) that make the process faster. 

### Qubitium · 2026-05-21

> Image
and there is another issue, when i quant the same model with gptaq, it stucked more than a day, and here is the log for the quantization of gptaq qwen3.5 27B, the loss is very high
{ "process": "gptaq", "layer": 0, "module": "linear_attn.in_proj_qkv", "feat: in, out": "5120, 10240", "dtype: size": "bf16: 103.1MB", "loss": "420.5862731934", "samples": "128", "damp": "0.01000", "time": "1.287", "fwd_time": "3.350", "(v)ram": "cuda 45.41G" } { "process": "gptaq", "layer": 0, "module": "linear_attn.in_proj_z", "feat: in, out": "5120, 6144", "dtype: size": "bf16: 61.9MB", "loss": "275.9195556641", "samples": "128", "damp": "0.01000", "time": "0.943", "fwd_time": "2.152", "(v)ram": "cuda 45.41G" } { "process": "gptaq", "layer": 0, "module": "linear_attn.out_proj", "feat: in, out": "6144, 5120", "dtype: size": "bf16: 61.9MB", "loss": "0.3225559294", "samples": "128", "damp": "0.01000", "time": "1.255", "fwd_time": "3.008", "(v)ram": "cuda 45.52G" } 

This may be a bug. 

Please reproduce this bug on a small model befor eyou move to larger models. 
