source: https://docs.vllm.ai/projects/recipes/en/stable/Tencent-Hunyuan/Hunyuan-Instruct.html
lastmod: 2026-04-27

# Hunyuan-A13B Instruct Usage Guide[¶](https://docs.vllm.ai#hunyuan-a13b-instruct-usage-guide)

This guide provides instructions to install and run Hunyuan-A13B-Instruct on AMD GPUs.

## Install vLLM[¶](https://docs.vllm.ai#install-vllm)

Note: The vLLM wheel for ROCm requires Python 3.12 and glibc >= 2.35. If your environment does not meet these requirements, please use the Docker-based setup as described in the

[documentation]. Supported GPUs: MI300X, MI325X, MI355X

uv venv
source .venv/bin/activate
uv pip install vllm --extra-index-url https://wheels.vllm.ai/rocm/


## Deploying Hunyuan-A13B Instruct[¶](https://docs.vllm.ai#deploying-hunyuan-a13b-instruct)

export VLLM_ROCM_USE_AITER=1
vllm serve tencent/Hunyuan-A13B-Instruct --tensor-parallel-size 2 --trust-remote-code