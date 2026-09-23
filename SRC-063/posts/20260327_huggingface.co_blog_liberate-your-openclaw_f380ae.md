# Liberate your OpenClaw

source: https://huggingface.co/blog/liberate-your-openclaw
published: Fri, 27 Mar 2026 00:00:00 GMT

Image-Text-to-Text • 35B • Updated • 180k • 865

#
[
](https://huggingface.co#liberate-your-openclaw-🦀)
Liberate your OpenClaw 🦀

[Update on GitHub](https://github.com/huggingface/blog/blob/main/liberate-your-openclaw.md)

If you've been cut off and your OpenClaw, Pi, or Open Code agents need resuscitation, you can move them to open models in two ways:

- Use an open model served through Hugging Face Inference Providers.
- Run a fully local open model on your own hardware.

The hosted route is the fastest way back to a capable agent. The local route is the right fit if you want privacy, zero API costs, and full control.

To do so, just tell your claude code, your cursor or your favorite agent: *help me move my OpenClaw agents to Hugging Face models*, and link this page.

##
[
](https://huggingface.co#hugging-face-inference-providers)
Hugging Face Inference Providers

Hugging Face inference providers is an open platform that routes to providers of open source models. It’s the right choice if you want the best models or you don’t have the necessary hardware.

First, you’ll need to create a token [here](https://huggingface.co/settings/tokens). Then you can add that token to `openclaw`

like so:

```
openclaw onboard --auth-choice huggingface-api-key
```


Paste your Hugging Face token when prompted, and you’ll be asked to select a model.

We’d recommend [GLM-5](https://huggingface.co/zai-org/GLM-5) because of its excellent [Terminal Bench](https://huggingface.co/datasets/harborframework/terminal-bench-2.0) scores, but there are thousands to chose from [here](https://huggingface.co/inference/models).

You can update your Hugging Face model at any time entering its `repo_id`

in the OpenClaw config:

```
{
agents: {
defaults: {
model: {
primary: "huggingface/zai-org/GLM-5:fastest"
}
}
}
}
```


Note: HF PRO subscribers get $2 free credits each month which applies to Inference Providers usage, learn more [here](https://huggingface.co/pro).

##
[
](https://huggingface.co#local-setup)
Local Setup

Running models locally gives you full privacy, zero API costs, and the ability to experiment without rate limits.

Install Llama.cpp, a fully open source library for low resource inference.

```
# on mac or linux
brew install llama.cpp
# on windows
winget install llama.cpp
```


Start a local server with a built-in web UI:

```
llama-server -hf unsloth/Qwen3.5-35B-A3B-GGUF:UD-Q4_K_XL
```


Here, we’re using Qwen3.5-35B-A3B, which works great with 32GB of RAM. If you have different requirements, please check out the hardware compatibility [for the model you're interested in](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF). [There are thousands to choose from](https://huggingface.co/models?pipeline_tag=text-generation&library=gguf&sort=trending).

If you load the GGUF in llama.cpp, use an OpenClaw config like this:

```
openclaw onboard --non-interactive \
--auth-choice custom-api-key \
--custom-base-url "http://127.0.0.1:8080/v1" \
--custom-model-id "unsloth-qwen3.5-35b-a3b-gguf" \
--custom-api-key "llama.cpp" \
--secret-input-mode plaintext \
--custom-compatibility openai
```


Verify the server is running and the model is loaded:

```
curl http://127.0.0.1:8080/v1/models
```


##
[
](https://huggingface.co#which-path-should-you-choose)
Which path should you choose?

Use Hugging Face Inference Providers if you want the quickest path back to a capable OpenClaw agent. Use `llama.cpp`

if you want privacy, full local control, and no API bill.

Either way, you do not need a closed hosted model to get OpenClaw back on its feet!