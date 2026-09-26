# Transformers backend integration in SGLang

source: https://huggingface.co/blog/transformers-backend-sglang
published: Mon, 23 Jun 2025 00:00:00 GMT

#
[
](https://huggingface.co#transformers-backend-integration-in-sglang)
Transformers backend integration in SGLang

[Update on GitHub](https://github.com/huggingface/blog/blob/main/transformers-backend-sglang.md)

But once you're ready to move from notebooks to production, inference performance becomes mission-critical. That’s where SGLang comes in.

Designed for high-throughput, low-latency inference, SGLang now offers seamless integration with transformers as a backend. This means you can pair the flexibility of transformers with the raw performance of SGLang.

Let’s dive into what this integration enables and how you can use it.

#
[
](https://huggingface.co#tldr)
TL;DR

SGLang now supports Hugging Face transformers as a backend, letting you run any transformers-compatible model with high-performance inference out of the box.

```
import sglang as sgl
llm = sgl.Engine("meta-llama/Llama-3.2-1B-Instruct", impl="transformers")
print(llm.generate(["The capital of France is"], {"max_new_tokens": 20})[0])
```


No native support needed — SGLang automatically falls back to Transformers when needed, or you can set `impl="transformers"`

explicitly.

#
[
](https://huggingface.co#transformers-and-sglang)
Transformers and SGLang

Let’s walk through a simple text generation example with `meta-llama/Llama-3.2-1B-Instruct`

to compare both approaches.

##
[
](https://huggingface.co#transformers)
Transformers

transformers library is great for experimentation, small-scale tasks and training, but it's not optimized for high-volume or low-latency scenarios.

```
from transformers import pipeline
pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B-Instruct")
generate_kwargs = {
"top_p": 0.95,
"top_k": 20,
"temperature": 0.8,
"max_new_tokens": 256
}
result = pipe("The future of AI is", **generate_kwargs)
print(result[0]["generated_text"])
```


##
[
](https://huggingface.co#sglang)
SGLang

SGLang takes a different track, prioritizing efficiency with features like RadixAttention (a memory-efficient attention mechanism). Inference with SGLang is noticeably faster and more resource-efficient, especially under load. Here’s the same task in SGlang using an offline engine:

```
import sglang as sgl
if __name__ == '__main__':
llm = sgl.Engine(model_path="meta-llama/Llama-3.2-1B-Instruct")
prompts = ["The future of AI is"]
sampling_params = {
"top_p": 0.95,
"top_k": 20,
"temperature": 0.8,
"max_new_tokens": 256
}
outputs = llm.generate(prompts, sampling_params)
print(outputs[0])
```


Or you can spin a server and send requests:

```
python3 -m sglang.launch_server \
--model-path meta-llama/Llama-3.2-1B-Instruct \
--host 0.0.0.0 \
--port 30000
```


```
response = requests.post(
"http://localhost:30000/generate",
json={
"text": "The future of AI is",
"sampling_params": {
"top_p": 0.95,
"top_k": 20,
"temperature": 0.8,
"max_new_tokens": 256
},
},
)
print(response.json())
```


Note that SGLang also offers an OpenAI-compatible API, making it a drop-in replacement for external services.

#
[
](https://huggingface.co#transformers-backend-in-sglang)
Transformers backend in SGLang

With the new transformers backend integration, SGLang can now automatically fall back to using transformers models it doesn’t natively support. This means in practice:

- Instant access to new models added to transformers
- Support for custom models from the Hugging Face Hub
- Less engineering overhead

This unlocks faster inference and optimized deployment (e.g enabling RadixAttention) without sacrificing the simplicity and versatility of transformers ecosystem.

##
[
](https://huggingface.co#usage)
Usage

```
llm = sgl.Engine(model_path="meta-llama/Llama-3.2-1B-Instruct", impl="transformers")
```


Note that specifying the impl parameter is optional. If the model is not natively supported by SGLang, it switches to transformers implementation on its own.

Any model on the Hugging Face Hub that works with `transformers`

using `trust_remote_code=True`

and properly implements attention is compatible with SGLang. You can find the exact requirements in the official [documentation](https://docs.sglang.ai/supported_models/transformers_fallback.html#remote-code). If your custom model meets these criteria, all you need to do is set trust_remote_code=True when loading it.

```
llm = sgl.Engine(model_path="new-custom-transformers-model", impl="transformers", trust_remote_code=True)
```


##
[
](https://huggingface.co#example)
Example

Kyutai Team’s Helium isn’t yet natively supported by SGLang. This is where transformers backend shines, enabling optimized inference without waiting for native support.

```
python3 -m sglang.launch_server \
--model-path kyutai/helium-1-preview-2b \
--impl transformers \
--host 0.0.0.0 \
--port 30000
```


```
response = requests.post(
"http://localhost:30000/generate",
json={
"text": "The capital of France is",
"sampling_params": {
"top_p": 0.95,
"top_k": 20,
"temperature": 0.8,
"max_new_tokens": 256
},
},
)
print(response.json())
```


#
[
](https://huggingface.co#next-steps)
Next steps

There are several key areas we are actively working on to enhance this integration:

Performance Improvements: transformer models currently lag behind the native integration in terms of performance.Our primary objective is to optimize and narrow this gap.

LoRA Support

VLM Integration: we are also working toward adding support for Vision-Language Models (VLM) to broaden the range of capabilities and use cases.