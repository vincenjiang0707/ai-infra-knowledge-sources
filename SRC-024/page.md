# Intel

source: https://docs.openvino.ai/

# OpenVINO 2026.4[#](https://docs.openvino.ai#openvino-2026-4)

**OpenVINO is an open-source toolkit** for deploying high-performance AI solutions across
cloud, AI PCs, edge devices, and Physical AI alike. Develop your applications
with both generative and conventional AI models, coming from the most popular model frameworks.
Convert, optimize, and run inference utilizing the full potential of Intel® hardware.
There are four main tools in OpenVINO to meet all your deployment needs:

Run and deploy conventional AI models

[./openvino-workflow.html](https://docs.openvino.ai/openvino-workflow.html)

Run and deploy generative AI models

[./openvino-workflow-generative.html](https://docs.openvino.ai/openvino-workflow-generative.html)

Deploy VLA models on robots

[./physical-ai.html](https://docs.openvino.ai/physical-ai.html)

Deploy both generative and conventional AI inference on a server

[./model-server/ovms_what_is_openvino_model_server.html](https://docs.openvino.ai/model-server/ovms_what_is_openvino_model_server.html)

[OpenVINO Toolkit Cheat Sheet [PDF]](https://docs.openvino.ai/2026/_static/download/OpenVINO_Quick_Start_Guide.pdf)and the

[OpenVINO GenAI Quick-start Guide [PDF]](https://docs.openvino.ai/2026/_static/download/GenAI_Quick_Start_Guide.pdf)


## Where to Begin[#](https://docs.openvino.ai#where-to-begin)

This guide introduces installation and learning materials for Intel® Distribution of OpenVINO™ toolkit.

See latest benchmark numbers for OpenVINO and OpenVINO Model Server.

Load models directly (for TensorFlow, ONNX, PaddlePaddle) or convert to OpenVINO format.

Reach for performance with post-training and training-time compression with NNCF.

## Key Features[#](https://docs.openvino.ai#key-features)

You can either link directly with OpenVINO Runtime to run inference locally or use OpenVINO Model Server to serve model inference from a separate server or within Kubernetes environment.

Write an application once, deploy it anywhere, achieving maximum performance from hardware. Automatic device discovery allows for superior deployment flexibility. OpenVINO Runtime supports Linux, Windows and MacOS and provides Python, C++ and C API. Use your preferred language and OS.

Designed with minimal external dependencies reduces the application footprint, simplifying installation and dependency management. Popular package managers enable application dependencies to be easily installed and upgraded. Custom compilation for your specific model(s) further reduces final binary size.

In applications where fast start-up is required, OpenVINO significantly reduces first-inference latency by using the CPU for initial inference and then switching to another device once the model has been compiled and loaded to memory. Compiled models are cached, improving start-up time even more.