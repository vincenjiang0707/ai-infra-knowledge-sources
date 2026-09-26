source: https://docs.vllm.ai/en/latest/serving/integrations/langchain/
lastmod: 2026-09-24

To run inference on a single or multiple GPUs, use VLLM class from langchain.

Code

fromlangchain_community.llmsimportVLLMllm=VLLM(model="Qwen/Qwen3-4B",trust_remote_code=True,# mandatory for hf modelsmax_new_tokens=128,top_k=10,top_p=0.95,temperature=0.8,# for distributed inference# tensor_parallel_size=...,)print(llm("What is the capital of France ?"))