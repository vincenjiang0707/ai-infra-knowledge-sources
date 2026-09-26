source: https://docs.vllm.ai/en/latest/training/rlhf/
lastmod: 2026-09-24

# Reinforcement Learning from Human Feedback[¶](https://docs.vllm.ai#reinforcement-learning-from-human-feedback)

Reinforcement Learning from Human Feedback (RLHF) is a technique that fine-tunes language models using human-generated preference data to align model outputs with desired behaviors. vLLM can be used to generate the completions for RLHF.

The following open-source RL libraries use vLLM for fast rollouts (sorted alphabetically and non-exhaustive):

For weight synchronization between training and inference, see the [Weight Transfer](https://docs.vllm.ai/weight_transfer/) documentation, which covers the pluggable backend system with [NCCL](https://docs.vllm.ai/weight_transfer/nccl/) (multi-GPU) and [IPC](https://docs.vllm.ai/weight_transfer/ipc/) (same-GPU) engines.

For pipelining generation and training to improve GPU utilization and throughput, see the [Async Reinforcement Learning](https://docs.vllm.ai/async_rl/) guide, which covers the pause/resume API for safely updating weights mid-flight.

See the following notebooks showing how to use vLLM for GRPO: