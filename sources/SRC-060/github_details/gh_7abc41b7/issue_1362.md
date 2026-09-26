# [Issue #1362] is this corect code for video inference using baidu/ERNIE-4.5-VL-28B-A3B-Thinking??? is there any official code example available?

source: https://github.com/PaddlePaddle/ERNIE/issues/1362
state: open | updated: 2026-01-07T12:08:02Z
labels: 

## 正文

```
import torch
from transformers import AutoProcessor, AutoTokenizer, AutoModelForCausalLM

model_path = 'baidu/ERNIE-4.5-VL-28B-A3B-Thinking'
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    dtype=torch.bfloat16,
    trust_remote_code=True
)

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
model.add_image_preprocess(processor)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What color clothes is the girl in the picture wearing?"
            },
            {
                "type": "video",
                "video_path": {
                    "path": "sample_video.mp4"
                }
            },
        ]
    },
]

text = processor.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
image_inputs, video_inputs = processor.process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)

device = next(model.parameters()).device
inputs = inputs.to(device)

generated_ids = model.generate(
    inputs=inputs['input_ids'].to(device),
    **inputs,
    max_new_tokens=1024,
    use_cache=False
    )
output_text = processor.decode(generated_ids[0][len(inputs['input_ids'][0]):])
print(output_text)

```

## 评论 (10)

### BossPi · 2025-11-17

Thank you for your question. I'm sorry for the late reply. If you want to input a video for inference, you can organize your messages in the following way:
```
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the video in two sentences in English."},
            {"type": "video_url", "video_url": {"url": "https://paddlenlp.bj.bcebos.com/datasets/paddlemix/demo_video/example_video.mp4"}},
        ]
    },
]
```
If you have any further questions, please feel free to let us know.

### Arslan-Mehmood1 · 2025-11-17

Thanks @BossPi , I'll test it and share the feedback.

### Arslan-Mehmood1 · 2025-11-17

@BossPi  and what if video is not a url, but a local .mp4 path? will same work?

### BossPi · 2025-11-17

Yes, it will same work if the video is a local .mp4 path.

### Arslan-Mehmood1 · 2025-11-21

@BossPi , thanks its working.
Its taking 249 sec for 19 sec video - A100-80GB GPU
Video - 720 × 1280 - 30FPS.

is the Ernie processing video at original resolution and fps?
and is there any way we can disable or lower thinking level?

### BossPi · 2025-11-21

Ernie processing video at fps:2 and max pixels:1196 * 28 * 28.
We don't recommend to disable thinking mode. If you do want to disable thinking mode, you can process your messages like this:
```
text = processor.tokenizer.apply_chat_template(
    messages, 
    tokenize=False, 
    add_generation_prompt=True, 
    chat_template_kwargs={"options": {"thinking_mode": "close"}},
)
```
In additionally, we recommend you using FastDeploy for more efficient infer performence: https://github.com/PaddlePaddle/FastDeploy

### Arslan-Mehmood1 · 2025-11-27

Thanks @BossPi 

### BossPi · 2025-11-27

I'm glad to be of help to you.

### manzar96 · 2026-01-02

@BossPi is there a way to specifically set the fps or the maximum number of frames sampled from the video?

Thanks in advance.


### BossPi · 2026-01-07

With Fastdeploy, you could set `--mm-processor-kwargs '{"video_max_frames": 30}'` to set max frames  sampled from the video. 
For more infomation, you can check out this link: https://github.com/PaddlePaddle/FastDeploy/blob/release/2.3/docs/get_started/ernie-4.5-vl.md?plain=1#L37-L38
