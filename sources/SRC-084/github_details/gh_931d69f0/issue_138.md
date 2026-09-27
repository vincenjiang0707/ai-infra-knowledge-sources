# [Issue #138] Quantizing the model makes slower

source: https://github.com/dropbox/hqq/issues/138
state: closed | updated: 2025-01-09T23:42:29Z
labels: 

## 正文

Thanks for your great work. I'm getting a issue with quantizing the model.
I'm using 'MiniCPM-V-2_6' and having a issue that slows the model when quezting the model to 4-bit.

I found the issue that I should quantize only the language model part and did it. However it's still slower.

```
model_id = "openbmb/MiniCPM-V-2_6"

model = AutoModel.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16, attn_implementation='flash_attention_2') # use _attn_implementation='sdpa' to disable flash attention
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=1)
AutoHQQHFModel.quantize_model(model.llm, quant_config=quant_config, compute_dtype=torch.bfloat16, device="cuda")

# model.vpm = model.vpm.to(device="cuda")
# model.resampler = model.resampler.to(device="cuda")

model = model.eval().cuda()
# model.generation_config.cache_implementation = "static"
model.forward = torch.compile(model.forward, mode="reduce-overhead", fullgraph=True)

HQQLinear.set_backend(HQQBackend.PYTORCH)
prepare_for_inference(model, backend="torchao_int4", verbose=True)
```

When only using `prepare_for_inference(model, backend="torchao_int4", verbose=True)` its not too slow, however when using with the 4-bit quantization, it triples the generation time.

Can I get what I did wrong?

Also when using the `torchao_int4`, it dosen't make big difference in tps. I


## 评论 (26)

### mobicham · 2025-01-03

Hey! Please follow exactly this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py
Just replace the model name with yours and it should work.

Here are a couple of things in your sample code:
-You should not torch compile the model yourself, we have util functions to do that, because only the decoding part should be quantized.
-Compilation should be done after patching, not before.
-You should not call cuda(), `quantize_model` already takes care of it.


### 2U1 · 2025-01-03

@mobicham Thanks for your reply, I followed the code of llava in the repo(I found a issue of qwen2-vl that I should only quantize the llm part), becuase it's a vision-langugage model.
I only quantize the llm part and moving the other parts to the cuda.

quantizing the model slows downing the generation, and when using the `prepare_for_inference(model, backend="torchao_int4", verbose=True)`, it triples the time. When using the `ATEN` backend, it's slight faster than unquantized model.



### mobicham · 2025-01-03

Hm, when you use `torchao_int4`, it will not use the ATEN/PYTORCH backend, it will use the `torchao_int4` backend, so that's strange.

What do you get running an LLM like llama3 via this example: https://github.com/mobiusml/hqq/blob/master/examples/backends/hqq_lib_demo.py

The llava example is not using torch.compile though fyi, you could probably adapt the generate function from Aria: https://github.com/mobiusml/hqq/blob/master/hqq/utils/aria.py#L229 , but it's not gonna work out-of-the-box.

Also, what gpu do you have? 

### 2U1 · 2025-01-03

@mobicham I'm using 4090 
Also, I meant that using ATEN rather than using torchao_int4 gets faster. 
When using `prepare_for_inference(model, backend="torchao_int4"` it slower thant just using the original huggingface model. With unquatized one. I can't really get whats wrong.
I've saw the code that you made with, using static_cache and compiling the forward fuction. So, I've added the code, that you can see in the first post. 



I'll test it and let you know when using llama3.


### mobicham · 2025-01-03

Can you please run this example, without changing anything in the code: 
```Python
import torch
device        = 'cuda:0'
backend       = 'torchao_int4' #"torchao_int4" (4-bit only) or "bitblas" (4-bit + 2-bit)
compute_dtype = torch.bfloat16 if backend=="torchao_int4" else torch.float16
cache_dir     = '.' 
model_id      = 'meta-llama/Meta-Llama-3-8B-Instruct'

########################################################################
#Load model
from transformers import AutoModelForCausalLM, AutoTokenizer
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *

#Load
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
model     = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=cache_dir, torch_dtype=compute_dtype, attn_implementation="sdpa")

#Quantize
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=1)
AutoHQQHFModel.quantize_model(model, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
HQQLinear.set_backend(HQQBackend.PYTORCH)

#Optimize
from hqq.utils.patching import prepare_for_inference
prepare_for_inference(model, backend=backend, verbose=True)

#Inference
########################################################################
#Using a custom generator
from hqq.utils.generation_hf import HFGenerator
gen = HFGenerator(model, tokenizer, max_new_tokens=1000, do_sample=True, compile="partial").warmup() 
out = gen.generate("Write an essay about large language models.", print_tokens=True)
```
You should get ~150 tokens/sec, fp16 is ~40 tokens/sec.

### 2U1 · 2025-01-05

@mobicham Sorry for the late response.
Yes this code works totally fine.

I'm bit curious that what is the main issue causing my model won't boost the generation speed.

### mobicham · 2025-01-06

@2U1 because VLMs work a bit differently in the decoding phase. It needs some custom decoding call to support torch.compile. 

Have you tried VLLM? It supports HQQ but you need to use the transformers HqqConfig not hqq's lib: https://huggingface.co/docs/transformers/main/en/quantization/hqq
Then you need to save the model + pre-processor via `.save_pretrained` and load the saved quantized model into VLLM. I know it works for LLMs, haven't tried VLM though.

### 2U1 · 2025-01-06

I was gonna use a custom server for it. Thanks for help. I'll just gonna use the quantized without the compiled one. 

Thanks again for your great work.

### mobicham · 2025-01-06

Unfortunately it will not run fast without the compile. 

It's not too difficult though, you just need to adapt <a href="https://github.com/mobiusml/hqq/blob/master/hqq/utils/aria.py#L263C5-L263C37">this function</a>, and the inference code would look like <a href="https://github.com/mobiusml/hqq/blob/master/examples/hf/aria_multimodal.py">this</a>
-> The model needs to support static cache, otherwise this will not work.

### 2U1 · 2025-01-06

Thanks I'll try it.

Also can I ask you question? When using the code `model.language_model.generation_config.cache_implementation = "static"` does this work for `batch_size>1`?  

### mobicham · 2025-01-06

I think so: https://github.com/huggingface/transformers/issues/35444

### 2U1 · 2025-01-07

I was struggling with it. 
It keeps throwing me a dynamo error. 

```
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer, AutoProcessor
from hqq.utils.patching import prepare_for_inference
import torchao
import outlines
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *
import transformers
from torch.nn.attention import sdpa_kernel, SDPBackend

model_id = "openbmb/MiniCPM-V-2_6"

model = AutoModel.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16, attn_implementation='sdpa') # sdpa or flash_attention_2, no eager
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=1)
AutoHQQHFModel.quantize_model(model.llm, quant_config=quant_config, compute_dtype=torch.bfloat16, device="cuda")

model.vpm = model.vpm.to(device="cuda", dtype=torch.bfloat16)
model.resampler = model.resampler.to(device="cuda", dtype=torch.bfloat16)

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)
prepare_for_inference(model.llm, backend="torchao_int4", verbose=True)

model.llm.config.use_cache = True
model.llm.generation_config.cache_implementation = "static"
model.eval()

forward_compiled = torch.compile(model.llm.forward, mode="reduce-overhead", fullgraph=True)
forward_simple = model.llm.forward

from torch.nn.attention import sdpa_kernel, SDPBackend

def is_one_step_decoding(args, kwargs):
    if len(args) > 0 and isinstance(args[0], torch.Tensor) and args[0].shape[-1] == 1:
        return True
    if "input_ids" in kwargs and isinstance(kwargs["input_ids"], torch.Tensor):
        if kwargs["input_ids"].shape[-1] == 1:
            return True
    if "inputs_embeds" in kwargs and isinstance(kwargs["inputs_embeds"], torch.Tensor):
        if kwargs["inputs_embeds"].shape[1] == 1:
            return True
    return False

def custom_forward(*args, **kwargs):
    if is_one_step_decoding(args, kwargs):
        out_fct = forward_compiled

        with sdpa_kernel([SDPBackend.MATH]):
            out = out_fct(*args, **kwargs)
        return out

    # Prefill phase
    else:
        out_fct = forward_simple
        out = out_fct(*args, **kwargs)
        return out

model.llm.forward = custom_forward

image = Image.open("/home/workspace/VLM/sample/frame_0005.png")
groups.append(image)

user_text = "(<image>./</image>)\n" * len(groups) + "Tell me about this image."

messages = [
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": user_text,
    }
]

prompts_list = [processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)]
images_list = [groups]

inputs = processor(
    prompts_list,
    images_list,
    max_slice_num=9,
    use_image_id=True,
    return_tensors="pt",
    max_lengths=8192
).to(model.device)

generation_config = {
    "temperature": 0.05,
    "do_sample": True,
    "repetition_penalty": 1.05
}

inputs.pop('image_sizes', None)

with torch.inference_mode():
    generated_ids = model.generate(
        **inputs,
        tokenizer=tokenizer,
        max_new_tokens=10,
        vision_hidden_states=None,
        stream=False,
        decode_text=True,
        **generation_config
    )

print(generated_ids)
```
This is my whole code. Am I missing something?

EDIT.
Sorry, It was the problem of transformers version. Downgrading to 4.46.3 works fine. 

### mobicham · 2025-01-07

Did you check if `is_one_step_decoding` is actually returning True during the decoding phase ? If so, do you get a speed-up? 

### 2U1 · 2025-01-07

@mobicham Yes, that returns true. I've downgraded  `transformers==4.46.3` and it works well now.
Also, it's a bit odd that it takes more time than just using `ATEN` backend when using multi-image. Maybe it's caused by recompliation of static cache. 
I just changed my code to answer in one word like classification so, it's okay for now only using quantization.

It really helped me a lot for understanding how it works. Thanks for the help.

### mobicham · 2025-01-07

`ATEN` doesn't work with `axis=1`, only with `axis=0`. 

 `torchao_int4` should work well up to batch-size 8 for the *decoding* phase, the prefill will be slower, so I think what happens is that you measure the end-2-end processing time, and since the prefill phase is heavy in VLMs because of the image tokens, you don't get a large speed-up. 

You can use the <a href="https://github.com/mobiusml/gemlite/">gemlite</a> backend instead which should be much faster for the prefill and since you are using the 4090, that should be the best backend actually.

### 2U1 · 2025-01-07

Thanks for the comment.

Yes when I was using `ATEN` I was using `axis=0`. I've forgot to mention it. I was testing almost every combination at the readme.
I'll try the gemlite backend. Thank you so much.

### mobicham · 2025-01-07

`ATEN` will probably be faster with large context-size and a large decoding batch-size

### 2U1 · 2025-01-07

Also can I ask you one more question?
Does the `gemlite` works with A5000 or A40? I've saw the repo but I'm not sure with it. 

### mobicham · 2025-01-07

> Also can I ask you one more question? Does the `gemlite` works with A5000 or A40? I've saw the repo but I'm not sure with it.

Yeah it should, it even works on older gpus like 2080, 2080 Ti


### mobicham · 2025-01-07

@2U1 I gave Qwen-VL a try, but compile is crashing: https://github.com/mobiusml/hqq/commit/02bf69235253d6becf35b83cce75f5363af79dd7

I will see what I can do


### 2U1 · 2025-01-07

Yes I get somekind of error like `TypeError: GemLiteLinearTriton.__init__() got an unexpected keyword argument 'exhaustive'`. 
Also it look like gemlite need to use fp16. So when I've changed my code to fp16 and tested, it just outputs some random word.

### 2U1 · 2025-01-08

@mobicham Also I found out, in the latest transformers version 4.47.1 it auto compiles the model when using generate.
`output =model.generate(**input_ids, max_new_tokens=10, cache_implementation="static")`

### mobicham · 2025-01-08

> Yes I get somekind of error like `TypeError: GemLiteLinearTriton.__init__() got an unexpected keyword argument 'exhaustive'`. Also it look like gemlite need to use fp16. So when I've changed my code to fp16 and tested, it just outputs some random word.

Strange, I used it yesterday and it was working fine, can you try with the master branches:
```
pip install git+https://github.com/mobiusml/hqq/ --upgrade;
pip install git+https://github.com/mobiusml/gemlite/ --upgrade;
```
Can you share the code snippet ?
Yes only supports fp16, but that should not be an issue. 

> @mobicham Also I found out, in the latest transformers version 4.47.1 it auto compiles the model when using generate. `output =model.generate(**input_ids, max_new_tokens=10, cache_implementation="static")`

I downgraded to 4.46 and it was still breaking, only with Qwen-VL though, the other models work fine.


### 2U1 · 2025-01-08

I've installed from the source and fixed the error (Both the gemlite and hqq). 
However, in my case I've just made my code as video clip classification(output token is very short). When the batchsize or the input length changes, it compiles againg and takes quite more time that it dosen't fit in my scenario. So, just using flash-attention2 without using static cache and `torch.compile` is the fastest (Only quantizeing the model) for me right now.

I'll use the gemlite with another scenario. Thank you very much.

BTW the Qwen2-VL works with upgrading `transformers==4.47.1`. 

This is the whole code for Qwen2-VL I've used. It auto compiles in the `generate` so no need for compiling outside.
```
model_id = "Qwen/Qwen2-VL-7B-Instruct"

model = Qwen2VLForConditionalGeneration.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16, attn_implementation="sdpa") # use _attn_implementation='sdpa' to disable flash attention
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

quant_config = BaseQuantizeConfig(nbits=4, group_size=64, axis=1)
AutoHQQHFModel.quantize_model(model.model, quant_config=quant_config, compute_dtype=torch.bfloat16, device="cuda")

model.visual = model.visual.to(device="cuda", dtype=torch.bfloat16)
model.lm_head = model.lm_head.to(device="cuda", dtype=torch.bfloat16)

HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)
prepare_for_inference(model.model, backend="torchao_int4", verbose=True)

model.eval()

from decord import VideoReader, cpu

def encode_video_by_interval(video_path, interval_seconds=5, frames_per_second=1):
    """
    Encode video frames by extracting frames every 1 second within regular intervals.

    Args:
        video_path (str): Path to the video file.
        interval_seconds (int): Interval in seconds between frame groups.
        frames_per_second (int): Number of frames per second to sample within each second.

    Returns:
        list of lists: Each sublist contains base64 encoded frames for a specific interval.
    """
    vr = VideoReader(video_path, ctx=cpu(0), num_threads=1)
    avg_fps = vr.get_avg_fps()  # Average frames per second of the video
    total_frame_num = len(vr)
    total_seconds = total_frame_num / avg_fps

    # Create a list of frame indices for each interval
    all_intervals = []
    for start_time in range(0, int(total_seconds), interval_seconds):
        interval_frames = []
        for second_offset in range(interval_seconds):
            current_second = start_time + second_offset
            if current_second >= total_seconds:
                break  # Stop if we exceed the video duration
            for frame_offset in range(frames_per_second):
                target_frame = int(current_second * avg_fps) + int(frame_offset * (avg_fps / frames_per_second))
                if target_frame < total_frame_num:
                    interval_frames.append(target_frame)
        if interval_frames:  # Add the interval only if it has frames
            all_intervals.append(interval_frames)

    print(f"Frame indices per interval: {all_intervals}")

    # Extract and encode frames for each interval
    all_encoded_frames = []
    for interval in all_intervals:
        frames = vr.get_batch(interval).asnumpy()
        interval_encoded_frames = []
        for frame in frames:
            img = Image.fromarray(frame).convert("RGB")
            interval_encoded_frames.append(img)
        all_encoded_frames.append(interval_encoded_frames)

    return all_encoded_frames
    
encoded_frame_groups = encode_video_by_interval('sample.mp4', interval_seconds=5, frames_per_second=1)

for groups in encoded_frame_groups:

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "video",
                    "video": groups,
                    "resized_height": 280,
                    "resized_width": 280
                },
                {
                    "type": "text",
                    "content": "Describe the video."
                }
            ]
        }
    ]

    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text = [text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    ).to(model.device)

    generation_config = {
        "temperature": 0.05,
        "do_sample": True
    }

    generated_ids = model.generate(**inputs, max_new_tokens=10, **generation_config, cache_implementation="static")
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=True)

    print(output_text)
 ```

### mobicham · 2025-01-09

Yeah compile only makes sense when the input is static, that's why normally you wouldn't compile for the prefill phase!
Thanks, yeah skipping compile in Qwen-VL since it does compile automatically in the newer versions of transformers :+1: 

### 2U1 · 2025-01-09

@mobicham I think the previsous versions had some problem with Qwen2-VL's m-rope and it was fixed with the feature I mentioned above.
Thanks for the help!
