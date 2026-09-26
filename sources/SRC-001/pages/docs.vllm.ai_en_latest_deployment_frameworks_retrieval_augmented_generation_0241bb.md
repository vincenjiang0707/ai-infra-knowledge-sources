source: https://docs.vllm.ai/en/latest/deployment/frameworks/retrieval_augmented_generation/
lastmod: 2026-09-24

# Retrieval-Augmented Generation[¶](https://docs.vllm.ai#retrieval-augmented-generation)

[Retrieval-augmented generation (RAG)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) is a technique that enables generative artificial intelligence (Gen AI) models to retrieve and incorporate new information. It modifies interactions with a large language model (LLM) so that the model responds to user queries with reference to a specified set of documents, using this information to supplement information from its pre-existing training data. This allows LLMs to use domain-specific and/or updated information. Use cases include providing chatbot access to internal company data or generating responses based on authoritative sources.

Here are the integrations:

- vLLM +
[langchain](https://github.com/langchain-ai/langchain)+[milvus](https://github.com/milvus-io/milvus) - vLLM +
[llamaindex](https://github.com/run-llama/llama_index)+[milvus](https://github.com/milvus-io/milvus)

## vLLM + langchain[¶](https://docs.vllm.ai#vllm-langchain)

### Prerequisites[¶](https://docs.vllm.ai#prerequisites)

Set up the vLLM and langchain environment:

pip install -U vllm \
langchain_milvus langchain_openai \
langchain_community beautifulsoup4 \
langchain-text-splitters


### Deploy[¶](https://docs.vllm.ai#deploy)

-
Start the vLLM server with the supported embedding model, e.g.

-
Start the vLLM server with the supported chat completion model, e.g.

-
Use the script:

[examples/applications/rag/retrieval_augmented_generation_with_langchain.py](https://github.com/vllm-project/vllm/blob/main/examples/applications/rag/retrieval_augmented_generation_with_langchain.py) -
Run the script


## vLLM + llamaindex[¶](https://docs.vllm.ai#vllm-llamaindex)

### Prerequisites[¶](https://docs.vllm.ai#prerequisites_1)

Set up the vLLM and llamaindex environment:

pip install vllm \
```bash
llama-index llama-index-readers-web \
llama-index-llms-openai-like \
llama-index-embeddings-openai-like \
llama-index-vector-stores-milvus \
```


### Deploy[¶](https://docs.vllm.ai#deploy_1)

-
Start the vLLM server with the supported embedding model, e.g.

-
Start the vLLM server with the supported chat completion model, e.g.

-
Use the script:

[examples/applications/rag/retrieval_augmented_generation_with_llamaindex.py](https://github.com/vllm-project/vllm/blob/main/examples/applications/rag/retrieval_augmented_generation_with_llamaindex.py) -
Run the script: