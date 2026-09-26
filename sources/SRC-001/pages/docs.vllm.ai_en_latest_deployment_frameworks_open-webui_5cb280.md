source: https://docs.vllm.ai/en/latest/deployment/frameworks/open-webui/
lastmod: 2026-09-24

# Open WebUI[¶](https://docs.vllm.ai#open-webui)

[Open WebUI](https://github.com/open-webui/open-webui) is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs, with built-in RAG capabilities, making it a powerful AI deployment solution.

To get started with Open WebUI using vLLM, follow these steps:

-
Install the

[Docker](https://docs.docker.com/engine/install/). -
Start the vLLM server with a supported chat completion model:

-
Start the Open WebUI Docker container:

-
Open it in the browser:

[http://open-webui-host:3000/](http://open-webui-host:3000/)At the top of the page, you should see the model

`Qwen/Qwen3-0.6B-Chat`

.