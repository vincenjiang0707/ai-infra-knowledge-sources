vllm serve model \
--tensor-parallel-size 4 \
--gpu-memory-utilization 0.9 \
--max-model-len 8192
See the docs for more details.
