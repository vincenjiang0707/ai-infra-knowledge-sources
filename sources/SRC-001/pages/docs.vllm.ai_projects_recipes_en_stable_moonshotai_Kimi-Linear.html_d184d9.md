source: https://docs.vllm.ai/projects/recipes/en/stable/moonshotai/Kimi-Linear.html
lastmod: 2026-04-27

# Kimi-Linear Usage Guide[¶](https://docs.vllm.ai#kimi-linear-usage-guide)

This guide describes how to run moonshotai/Kimi-Linear-48B-A3B-Instruct.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

uv venv
source .venv/bin/activate
# Install a stable version (avoid 0.12.0)
uv pip install vllm==0.11.2 --torch-backend auto


**Note**: Regarding Kimi-Linear, vLLM 0.12.0 has a known bug with

`MLAModules.__init__() missing 1 required positional argument: 'indexer_rotary_emb'`

. Please avoid this version.
## Running Kimi-Linear[¶](https://docs.vllm.ai#running-kimi-linear)

It's easy to run Kimi-Linear. The following snippets assume you have 4 or 8 GPUs on a single node.

### 4-GPU tensor parallel[¶](https://docs.vllm.ai#4-gpu-tensor-parallel)

```bash
vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct \
--port 8000 \
--tensor-parallel-size 4 \
--max-model-len 1048576 \
--trust-remote-code
```


### 8-GPU tensor parallel[¶](https://docs.vllm.ai#8-gpu-tensor-parallel)

```bash
vllm serve moonshotai/Kimi-Linear-48B-A3B-Instruct \
--port 8000 \
--tensor-parallel-size 8 \
--max-model-len 1048576 \
--trust-remote-code
```


If you see OOM, reduce

`--max-model-len`

(e.g. 65536) or increase`--gpu-memory-utilization`

(≤ 0.95).

Once the server is up, test it with: