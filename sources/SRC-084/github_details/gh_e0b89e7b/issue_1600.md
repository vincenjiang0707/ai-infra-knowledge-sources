# [Issue #1600] Phi 4 Multimodal not working with BnB/4bit quantization

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1600
state: closed | updated: 2026-02-21T20:27:28Z
labels: Model Support

## 正文

### System Info

RTX 3090, Driver 561.09. 
Win 11
Python 3.12
Pytorch 2.6.0 +Cu124 (Cuda 12.4)
Transformers 4.51.1
BNB 0.45.5

### Reproduction

Running into some trouble with quantizing Phi 4 multimodal with BnB. The code to reproduce the error is: 

```
`model_path = <path_to_phi4_multimodal_from_HF_here>

nf4_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_use_double_quant=True,
   bnb_4bit_compute_dtype=torch.bfloat16
)

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    trust_remote_code=True,
    device_map='cuda',
    torch_dtype = torch.bfloat16,
    # if you do not use Ampere or later GPUs, change attention to "eager"
    _attn_implementation='flash_attention_2',
    quantization_config = nf4_config
)

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_message = <user_prompt_here>

generate_ids = model.generate(
            **inputs,
            max_new_tokens=2000,
            generation_config=generation_config,
            num_logits_to_keep=1,
            num_beams=1 )`
```

Gives the following error:

```
` File "cache\huggingface\modules\transformers_modules\Phi-4-multimodal-instruct\modeling_phi4mm.py", line 1987, in set_lora_adapter
    module.set_adapter(adapter_name)
  File "ache\huggingface\modules\transformers_modules\Phi-4-multimodal-instruct\modeling_phi4mm.py", line 2107, in forward
    self.set_lora_adapter('speech')
  File "phi4.py", line 91, in <module>
    **inputs,

            max_new_tokens=2000,

            generation_config=generation_config,

            num_logits_to_keep=1,

            num_beams=1 )

RuntimeError: only Tensors of floating point dtype can require gradients `
```

When `quantization_config` is removed from `from_pretrained`, the code works. The above code also works for the non multimodal variants of Phi-4. I wonder if the problem lies with how BnB interacts with the adapters that came with the multimodal model. 

Thanks in advance for any guidance. 

### Expected behavior

This to work like the non multimodal variants of Phi 4. 

## 评论 (1)

### TimDettmers · 2026-02-21

Closing this issue. The error (`RuntimeError: only Tensors of floating point dtype can require gradients`) originates in the Phi-4-multimodal model's custom `set_lora_adapter` code, which calls `module.set_adapter()` on quantized layers that don't support `requires_grad`. This is a model implementation issue in the Phi-4-multimodal HuggingFace code (loaded via `trust_remote_code=True`), not a bitsandbytes bug.

The model's built-in LoRA adapter switching mechanism assumes standard floating-point parameters and doesn't account for quantized layers. This would need to be fixed in the model's `modeling_phi4mm.py`. If you're still affected, consider filing an issue with the Phi-4 model maintainers.
