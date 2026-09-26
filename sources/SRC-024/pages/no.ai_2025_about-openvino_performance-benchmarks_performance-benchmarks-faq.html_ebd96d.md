source: https://docs.openvino.ai/2025/about-openvino/performance-benchmarks/performance-benchmarks-faq.html
lastmod: 

# Performance Information F.A.Q.[#](https://docs.openvino.ai#performance-information-f-a-q)

## How often do performance benchmarks get updated?

New performance benchmarks are typically published on every
`major.minor`

release of the Intel® Distribution of OpenVINO™ toolkit.

## Where can I find the models used in the performance benchmarks?

All models used are published on [Hugging Face](https://huggingface.co/OpenVINO).

## Will there be any new models added to the list used for benchmarking?

The models used in the performance benchmarks were chosen based on general adoption and usage in deployment scenarios. New models that support a diverse set of workloads and usage are added periodically.

## How can I run the benchmark results on my own?

All of the performance benchmarks on traditional network models are generated using the
open-source tool within the Intel® Distribution of OpenVINO™ toolkit
called [benchmark_app](https://docs.openvino.ai/get-started/learn-openvino/openvino-samples/benchmark-tool.html).

For diffusers (Stable-Diffusion) and foundational models (aka LLMs) please use the OpenVINO GenAI
opensource repo [OpenVINO GenAI tools/llm_bench](https://github.com/openvinotoolkit/openvino.genai/tree/master/tools/llm_bench)

For a simple instruction on testing performance, see the [Getting Performance Numbers Guide](https://docs.openvino.ai/getting-performance-numbers.html).

## Where can I find a more detailed description of the workloads used for benchmarking?

The image size used in inference depends on the benchmarked network. The table below presents the list of input sizes for each network model and a link to more information on that model:

Model |
Public Network |
Task |
Input Size |
|---|---|---|---|
DeepSeek, HF |
Auto regressive language |
128K |
|
DeepSeek, HF |
Auto regressive language |
128K |
|
Hugginface |
Text-To-Text Decoder-only |
128K |
|
Meta AI |
Auto regressive language |
4K |
|
Meta AI |
Auto regressive language |
4K |
|
Meta AI |
Auto regressive language |
128K |
|
Huggingface |
Auto regressive language |
4096 |
|
Huggingface |
Auto regressive language |
128K |
|
Huggingface |
Auto regressive language |
32K |
|
Hugginface |
Latent Diffusion Model |
77 |
|
Hugginface |
Latent Adversarial Diffusion Distillation Model |
256 |
|
BERT |
question / answer |
128 |
|
Detectron-V2 |
object instance segmentation |
800x800 |
|
Mobilenet V2 PyTorch |
classification |
224x224 |
|
ResNet-50_v1_ILSVRC-2012 |
classification |
224x224 |
|
ssd-resnet34 onnx model |
object detection |
1200x1200 |
|
Yolov11 |
object detection |
640x640 |

## Where can I purchase the specific hardware used in the benchmarking?

Intel partners with vendors all over the world. For a list of Hardware Manufacturers, see the
[Intel® AI: In Production Partners & Solutions Catalog](https://www.intel.com/content/www/us/en/internet-of-things/ai-in-production/partners-solutions-catalog.html).
For more details, see the [Supported Devices](https://docs.openvino.ai/documentation/compatibility-and-support/supported-devices.html) article.

## How can I optimize my models for better performance or accuracy?

Set of guidelines and recommendations to optimize models are available in the
[optimization guide](https://docs.openvino.ai/openvino-workflow/running-inference/optimize-inference.html).
Join the conversation in the [Community Forum](https://software.intel.com/en-us/forums/intel-distribution-of-openvino-toolkit) for further support.

## Why are INT8 optimized models used for benchmarking on CPUs with no VNNI support?

The benefit of low-precision optimization extends beyond processors supporting VNNI
through Intel® DL Boost. The reduced bit width of INT8 compared to FP32
allows Intel® CPU to process the data faster. Therefore, it offers
better throughput on any converted model, regardless of the
intrinsically supported low-precision optimizations within Intel®
hardware. For comparison on boost factors for different network models
and a selection of Intel® CPU architectures, including AVX-2 with Intel®
Core™ i7-8700T, and AVX-512 (VNNI) with Intel® Xeon® 5218T and Intel®
Xeon® 8270, refer to the [Model Accuracy for INT8 and FP32 Precision](https://docs.openvino.ai/model-accuracy-int8-fp32.html)

## Where can I search for OpenVINO™ performance results based on HW-platforms?

The website format has changed in order to support more common approach of searching for the performance results of a given neural network model on different HW-platforms. As opposed to reviewing performance of a given HW-platform when working with different neural network models.

## How is Latency measured?

Latency is measured by running the OpenVINO™ Runtime in synchronous mode. In this mode, each frame or image is processed through the entire set of stages (pre-processing, inference, post-processing) before the next frame or image is processed. This KPI is relevant for applications where the inference on a single image is required. For example, the analysis of an ultra sound image in a medical application or the analysis of a seismic image in the oil & gas industry. Other use cases include real or near real-time applications, e.g. the response of industrial robot to changes in its environment and obstacle avoidance for autonomous vehicles, where a quick response to the result of the inference is required.