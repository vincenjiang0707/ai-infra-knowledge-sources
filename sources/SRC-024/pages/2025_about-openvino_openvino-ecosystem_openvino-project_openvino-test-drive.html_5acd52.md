source: https://docs.openvino.ai/2025/about-openvino/openvino-ecosystem/openvino-project/openvino-test-drive.html
lastmod: 

# OpenVINO™ Test Drive[#](https://docs.openvino.ai#openvino-test-drive)

OpenVINO™ Test Drive is a cross-platform **graphic user interface** application for running and
testing AI models, both generative and vision based.
It can run directly on your computer or on edge devices using
[OpenVINO™ Runtime](https://github.com/openvinotoolkit/openvino).

OpenVINO™ Test Drive is developed under the [openvino_testdrive repository](https://github.com/openvinotoolkit/openvino_testdrive).

Use OpenVINO™ Test Drive to:

**Chat with LLMs**and evaluate model performance on your computer or edge device;**Experiment with different text prompts**to generate images, using Stable Diffusion and Stable DiffusionXL models;**Transcribe speech from video**, using Whisper models, including generation of timestamps;**Run inference of models**trained by Geti™ and**visualize the results**.

## Installation (Windows)[#](https://docs.openvino.ai#installation-windows)

Important

For Intel® NPU, use the latest available version of
[Intel® NPU Driver](https://www.intel.com/content/www/us/en/download/794734/intel-npu-driver-windows.html).

Download the latest archive from the

[release repository](https://storage.openvinotoolkit.org/repositories/openvino_testdrive/packages). To verify the integrity of the downloaded package, use the SHA-256 file attached.Extract the zip file and run the

*MSIX*installation package. Click the Install button to proceed.Launch OpenVINO™ Test Drive, clicking the application name in the Windows app list.


## Quick start[#](https://docs.openvino.ai#quick-start)

When starting the application, you can import an LLM model from Hugging Face Hub or upload a Geti™ model from a local drive.

### Text generation and LLM performance evaluation[#](https://docs.openvino.ai#text-generation-and-llm-performance-evaluation)

Find a model on

[Hugging Face](https://huggingface.co/)and import it.Chat with LLMs via the Playground tab. You can export an LLM by clicking the Export model button.

Use the Performance metrics tab to get model performance metrics on your computer or an edge device.


### Retrieval-Augmented Generation with LLMs[#](https://docs.openvino.ai#retrieval-augmented-generation-with-llms)

Upload files and create knowledge base for RAG (Retrieval-Augmented Generation), using Knowledge base tab.

The knowledge base can be used for text generation with LLM models.

You can also upload a document directly, using the Playground` tab.


### Image analysis with Visual Language Models (VLMs)[#](https://docs.openvino.ai#image-analysis-with-visual-language-models-vlms)

Import a VLM for image analysis.

Select the VLM from the My models section, upload an image and analyze it.


### Video transcription with Whisper models[#](https://docs.openvino.ai#video-transcription-with-whisper-models)

Import a Whisper model for video transcription.

Select the speech-to-text LLM from the My models section, and upload a video for transcription.

You can search for words in the transcript or download it.

Use the Performance metrics tab to get performance metrics of the LLM on your computer or an edge device.


### Image generation with LLMs[#](https://docs.openvino.ai#image-generation-with-llms)

Import an image generation LLM from a predefined set of popular models or from

[Hugging Face](https://huggingface.co/), using Import model -> Hugging Face.Select the LLM from the My models section and start the chat to generate an image. You can export the model by clicking the Export model button.

You can download the generated image.

Use the Performance metrics tab to get performance metrics of the LLM on your computer or an edge device.


### Inference of models trained with Intel® Geti™[#](https://docs.openvino.ai#inference-of-models-trained-with-intel-geti)

Download the deployment code for a model in the OpenVINO IR format trained by Geti™ (refer to the

[Geti™ documentation](https://docs.geti.intel.com)for more details).Import the deployment code into OpenVINO™ Test Drive, using the

*Import model*and then*Local disk*buttons.Use the

*Live inference*tab to run and visualize results of inference of individual images.For batch inference, use the

*Batch inference*tab and provide paths to the folder with input images, as well as one for batch inference results. You can do so by filling out the*Source folder*and*Destination folder*fields. Click*Start*to start batch inference.

## Build the Application[#](https://docs.openvino.ai#build-the-application)

Make sure you

[Install flutter SDK](https://docs.flutter.dev/get-started/install)and all its platform-specific dependencies.Build the bindings and place them in the

**./bindings**folder.OpenVINO™ Test Drive uses bindings to

[OpenVINO™ GenAI](https://github.com/openvinotoolkit/openvino.genai)and[OpenVINO™ Model API](https://github.com/openvinotoolkit/model_api), which are located in the**./openvino_bindings**folder. Refer to the[GitHub page](https://github.com/openvinotoolkit/openvino_testdrive/blob/main/openvino_bindings/)for more details.Start the application, using the following command:

`flutter run`


## Additional Resources[#](https://docs.openvino.ai#additional-resources)

[OpenVINO™](https://github.com/openvinotoolkit/openvino)- a software toolkit for optimizing and deploying deep learning models.[GenAI Repository](https://github.com/openvinotoolkit/openvino.genai)and[OpenVINO Tokenizers](https://github.com/openvinotoolkit/openvino_tokenizers)- resources and tools for developing and optimizing Generative AI applications.[Geti™](https://docs.geti.intel.com/)- software for building computer vision models.[OpenVINO™ Model API](https://github.com/openvinotoolkit/model_api)- a set of wrapper classes for particular tasks and model architectures. It simplifies routine procedures, preprocessing and postprocessing of data.