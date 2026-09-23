source: https://docs.vllm.ai/projects/recipes/en/stable/index.html
lastmod: 2026-04-27

[vLLM Recipes](https://docs.vllm.ai/projects/recipes)[¶](https://docs.vllm.ai#vllm-recipes)

This repo intends to host community maintained common recipes to run vLLM answering the question:
**How do I run model X on hardware Y for task Z?**

## Guides[¶](https://docs.vllm.ai#guides)

### Arcee AI [¶](https://docs.vllm.ai#arcee-ai)

### DeepSeek [¶](https://docs.vllm.ai#deepseek)

### Ernie [¶](https://docs.vllm.ai#ernie)

### GLM [¶](https://docs.vllm.ai#glm)

### Google [¶](https://docs.vllm.ai#google)

### inclusionAI [¶](https://docs.vllm.ai#inclusionai)

### InternVL [¶](https://docs.vllm.ai#internvl)

### InternLM [¶](https://docs.vllm.ai#internlm)

### Jina AI [¶](https://docs.vllm.ai#jina-ai)

### Llama[¶](https://docs.vllm.ai#llama)

### Microsoft [¶](https://docs.vllm.ai#microsoft)

### MiniMax [¶](https://docs.vllm.ai#minimax)

### Xiaomi MiMo [¶](https://docs.vllm.ai#xiaomi-mimo)

### Mistral AI [¶](https://docs.vllm.ai#mistral-ai)

### Moonshotai [¶](https://docs.vllm.ai#moonshotai)

### NVIDIA[¶](https://docs.vllm.ai#nvidia)

### OpenAI [¶](https://docs.vllm.ai#openai)

### PaddlePaddle [¶](https://docs.vllm.ai#paddlepaddle)

### Qwen [¶](https://docs.vllm.ai#qwen)

### Seed [¶](https://docs.vllm.ai#seed)

### StepFun [¶](https://docs.vllm.ai#stepfun)

### Tencent-Hunyuan [¶](https://docs.vllm.ai#tencent-hunyuan)

## Contributing[¶](https://docs.vllm.ai#contributing)

New recipes live as structured YAML at `models/<hf_org>/<hf_repo>.yaml`

and render on [recipes.vllm.ai](https://recipes.vllm.ai/). **See CONTRIBUTING.md for the full schema, VRAM formula, and validation steps.**

Quick loop:

pnpm install
pnpm dev # http://localhost:3000
node scripts/build-recipes-api.mjs # validates every YAML + rebuilds the JSON API


### Legacy MkDocs guides[¶](https://docs.vllm.ai#legacy-mkdocs-guides)

The top-level Markdown directories (`DeepSeek/`

, `Qwen/`

, etc.) are the historical MkDocs site, kept as a reference during the YAML migration. To preview them:

uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv run mkdocs serve --dev-addr 127.0.0.1:8001


## License[¶](https://docs.vllm.ai#license)

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/vllm-project/recipes/blob/main/LICENSE) file for details.