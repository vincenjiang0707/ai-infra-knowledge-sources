# [Issue #3395] phi-3.5-vision strange output

source: https://github.com/mlc-ai/mlc-llm/issues/3395
state: open | updated: 2026-02-12T06:59:25Z
labels: question

## 正文

## ❓ General Questions

<!-- Describe your questions -->

<img width="1790" height="566" alt="Image" src="https://github.com/user-attachments/assets/88b392e0-e32e-47ec-90ed-590e7abeb7f8" />

When I used Phi-3.5 Vision, I ran the example code many times, but why is the output so strange? It seems like it didn't recognize the image at all, and it's just gibberish.
I tried custom compiling llava-1.5-7b and then interacting with the same input image, but the model's responses were completely off-topic? I hope to get some help.

`from mlc_llm import MLCEngine

# Create engine
model = "/root/autodl-tmp/phi-mlc"
engine = MLCEngine(model)

# Run chat completion in OpenAI API.
for response in engine.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": "https://www.ilankelman.org/stopsigns/australia.jpg",
                },
                {
                    "type": "text",
                    "text": "Describe this image please."
                },
            ],
        },
    ],
    model=model,
    stream=True,
):
    for choice in response.choices:
        print(choice.delta.content, end="", flush=True)
print("\n")

engine.terminate()
`
My MLC-LLM version was built from source code. TVM was installed using a pre-built package.
pip install --pre -U -f https://mlc.ai/wheels mlc-ai-nightly-cu124


## 评论 (5)

### Chunmian-art · 2025-12-28

I meet the same question!

Do you address this problem?

### gnguralnick · 2026-02-10

also experiencing this issue

### Chunmian-art · 2026-02-10

> also experiencing this issue

I recommend you to use the MNN codebase. The MLC framework is no longer actively maintained with infrequent updates. MNN supports the mainstream MLLM such as Qwen, LLaVA and GLM.

### gnguralnick · 2026-02-10

interesting, thank you for the suggestion. does MNN work with webgpu for use in the browser similar to webllm (which is built on top of mlc-llm)?

### Chunmian-art · 2026-02-12

> interesting, thank you for the suggestion. does MNN work with webgpu for use in the browser similar to webllm (which is built on top of mlc-llm)?

I have deployed the MNN-based VLM to the phone successfully. You can try to deploy it using the webgpu.
