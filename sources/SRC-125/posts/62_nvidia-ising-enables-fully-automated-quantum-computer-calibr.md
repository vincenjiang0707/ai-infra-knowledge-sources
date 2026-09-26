# nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning

source: https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning/

[NVIDIA Ising Calibration](https://www.nvidia.com/en-us/solutions/quantum-computing/ising/) is an open source [vision language model (VLM)](https://www.nvidia.com/en-us/glossary/vision-language-models/) designed to interpret diagnostic outputs from quantum processors and determine how they should be tuned to continue operating.

This post introduces the latest model release, NVIDIA [Ising Calibration 1.5](https://huggingface.co/collections/nvidia/nvidia-ising), which advances AI-based QPU calibration by analyzing unfamiliar diagnostic results without prior training examples. Ising Calibration 1.5 also uses examples from related experiments when available and is 11.4% smaller at BF16 precision. This eases the deployment of agentic calibration workflows directly in local lab environments.

For the first time, the model is also available in an [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)-quantized version, enabling deployment on a single GPU or an NVIDIA DGX Spark—comparable with leading closed models such as Fable 5 and GPT 5.6 Sol.

## How is the Ising Calibration 1.5 model trained?

The Ising Calibration 1.5 model is trained on data generated from partner contributions across multiple qubit modalities, including superconducting qubits, quantum dots, ions, neutral atoms, electrons on Helium, and others specializing in calibration and control.

## How is Ising Calibration 1.5 performance evaluated?

Performance of Ising Calibration 1.5 is evaluated using the [QCalEval benchmark](https://github.com/nvidia/QCalEval), which measures a model’s ability to interpret experimental results, classify outcomes, evaluate significance, assess fit quality and key features, and recommend next steps. For additional details on the benchmark, model architecture, and evaluation results, see [QCalEval: Benchmarking Vision-Language Models for Quantum Calibration Plot Understanding](https://arxiv.org/abs/2604.25884).

The evaluation covers both zero-shot and in-context learning (ICL). Zero-shot reasoning analyzes results independently, while ICL evaluates results in the context of related samples. Both are important for building agents that can automate QPU bring-up and retune operations.

On the QCalEval benchmark, Ising Calibration 1.5 shows strong performance when analyzing diagnostic results without prior examples. It is now also 86.68% better than its predecessor when using examples from related experiments. It outperforms comparable open models and remains competitive with leading closed models.

Ising Calibration 1.5 advances AI and quantum computing calibration by outperforming all open models out of the box and on the QCalEval benchmark. It is competitive with state-of-the-art closed or 1T+ parameter models.

The 31-billion-parameter VLM is suited for data center GPUs such as NVIDIA Grace Blackwell and NVIDIA Vera Rubin. It also ships with a quantized version to NVFP4 where users can run this model on a consumer gaming card or [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) with only a small cost in accuracy.

The tokens per second (TPS) performance on DGX Spark has also been optimized, enabling good throughput locally for a fraction of the cost.

To learn more about deploying Ising Calibration 1.5 with an agent, check out the [NVIDIA/Quantum-Calibration-Agent-Blueprint](https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint/) GitHub repo.

## Get started with NVIDIA Ising open resources

The [NVIDIA Ising](https://www.nvidia.com/en-us/solutions/quantum-computing/ising/) model family is fully open. Weights, data, benchmarks, and recipes are provided so you can modify, deploy, and fine-tune your own models and variants for your specific QPUs.

### Model weights

Full-parameter checkpoints for Ising Calibration 1.5 are available on Hugging Face:

Ising Calibration 1.5 is also available as an [NVIDIA NIM](https://catalog.ngc.nvidia.com/orgs/nim/nvidia/containers/ising-calibration-1-5-31b/-?_lr=1) and hosted through [NVIDIA Build](https://build.nvidia.com/nvidia/ising-calibration-1.5-31b/playground). The [OpenMDW License](https://github.com/OpenMDW/OpenMDW/blob/main/1.1/LICENSE.OpenMDW-1.1) from Linux Foundation offers QPU builders and operators with the flexibility to maintain data control and deploy anywhere.

### Deployment recipes

A ready-to-use agent harness blueprint is available with support for this model and others, including large model cloud APIs.

[Quantum calibration agent blueprint](https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint/)is a script for deploying an agentic workflow using Ising Calibration 1.5 with the NVIDIA Nemo Agent Toolkit to quickly set up quantum calibration experiment automation.

### Open datasets and QCalEval benchmark

Ising Calibration 1.5 is built on real QPU data provided by partners and collaborators. A semantic quantum calibration benchmark has also been released to evaluate model effectiveness for this task.

- Check out the
[QCalEval dataset](https://huggingface.co/datasets/nvidia/QCalEval) - Run the
[QCalEval script](https://github.com/nvidia/QCalEval)

## Start the discussion at forums.developer.nvidia.com
