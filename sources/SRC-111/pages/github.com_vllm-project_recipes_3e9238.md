source: https://github.com/vllm-project/recipes

This repo intends to host community maintained common recipes to run vLLM answering the question:
**How do I run model X on hardware Y for task Z?**

New recipes live as structured YAML at `models/<hf_org>/<hf_repo>.yaml`

and render on [recipes.vllm.ai](https://recipes.vllm.ai/). **See CONTRIBUTING.md for the full schema, VRAM formula, and validation steps.**

Quick loop:

```
pnpm install
pnpm dev # http://localhost:3000
node scripts/build-recipes-api.mjs # validates every YAML + rebuilds the JSON API
```

The top-level Markdown directories (`DeepSeek/`

, `Qwen/`

, etc.) are the historical MkDocs site, kept as a reference during the YAML migration. To preview them:

```
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv run mkdocs serve --dev-addr 127.0.0.1:8001
```

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/vllm-project/recipes/blob/main/LICENSE) file for details.