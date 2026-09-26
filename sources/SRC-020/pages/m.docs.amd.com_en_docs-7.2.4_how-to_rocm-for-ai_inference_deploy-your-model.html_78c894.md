source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/inference/deploy-your-model.html

# Deploying your model[#](https://rocm.docs.amd.com#deploying-your-model)

2026-02-19

2 min read time

ROCm enables inference and deployment for various classes of models including CNN, RNN, LSTM, MLP, and transformers. This section focuses on deploying transformers-based LLM models.

ROCm supports vLLM and Hugging Face TGI as major LLM-serving frameworks.

## Serving using vLLM[#](https://rocm.docs.amd.com#serving-using-vllm)

vLLM is a fast and easy-to-use library for LLM inference and serving. AMD is actively working with the vLLM team to improve performance and support the latest ROCm versions.

See the [GitHub repository](https://github.com/vllm-project/vllm) and [official vLLM documentation](https://docs.vllm.ai/) for more information.

For guidance on using vLLM with ROCm, refer to [Installation with ROCm](https://docs.vllm.ai/en/stable/getting_started/installation/gpu.html#amd-rocm).

### vLLM installation[#](https://rocm.docs.amd.com#vllm-installation)

vLLM supports two ROCm-capable installation methods. Refer to the official documentation use the following links.

[Build from source with Docker](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html?device=rocm#build-image-from-source)(recommended)

### vLLM walkthrough[#](https://rocm.docs.amd.com#vllm-walkthrough)

Refer to this developer blog for guidance on serving with vLLM [Inferencing and serving with vLLM on AMD GPUs — ROCm
Blogs](https://rocm.blogs.amd.com/artificial-intelligence/vllm/README.html)

### Validating vLLM performance[#](https://rocm.docs.amd.com#validating-vllm-performance)

ROCm provides a prebuilt optimized Docker image for validating the performance of LLM inference with vLLM
on the MI300X GPU. The Docker image includes ROCm, vLLM, PyTorch, and tuning files in the CSV
format. For more information, see the guide to
[LLM inference performance testing with vLLM on the AMD Instinct™ MI300X GPU](https://github.com/ROCm/MAD/blob/develop/benchmark/vllm/README.md)
on the ROCm GitHub repository.

## Serving using Hugging Face TGI[#](https://rocm.docs.amd.com#serving-using-hugging-face-tgi)

The [Hugging Face Text Generation Inference](https://huggingface.co/docs/text-generation-inference/index)
(TGI) library is optimized for serving LLMs with low latency. Refer to the [Quick tour of TGI](https://huggingface.co/docs/text-generation-inference/quicktour) for more details.

### TGI installation[#](https://rocm.docs.amd.com#tgi-installation)

The easiest way to use Hugging Face TGI with ROCm on AMD Instinct GPUs is to use the official Docker image at
[huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference/pkgs/container/text-generation-inference).

### TGI walkthrough[#](https://rocm.docs.amd.com#tgi-walkthrough)

Set up the LLM server.

Deploy the Llama2 7B model with TGI using the official Docker image.

model=TheBloke/Llama-2-7B-fp16 volume=$PWD docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 1g -p 8080:80 -v $volume:/data --name tgi_amd ghcr.io/huggingface/text-generation-inference:1.2-rocm --model-id $model

Set up the client.

Open another shell session and run the following command to access the server with the client URL.


curl 127.0.0.1:8080/generate \\ -X POST \\ -d '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":20}}' \\ -H 'Content-Type: application/json'

Access the server with request endpoints.


pip install request PYTHONPATH=/usr/lib/python3/dist-packages python requests_model.py ``requests_model.py`` should look like: .. code-block:: python import requests headers = { "Content-Type": "application/json", } data = { 'inputs': 'What is Deep Learning?', 'parameters': { 'max_new_tokens': 20 }, } response = requests.post('http://127.0.0.1:8080/generate', headers=headers, json=data) print(response.json())


vLLM and Hugging Face TGI are robust solutions for anyone looking to deploy LLMs for applications that demand high performance, low latency, and scalability.

Visit the topics in [Using ROCm for AI](https://rocm.docs.amd.com/index.html) to learn about other ROCm-aware solutions for AI development.