source: https://docs.openvino.ai/2025/about-openvino/openvino-ecosystem/openvino-project/openvino-training-extensions.html
lastmod: 

# OpenVINO™ Training Extensions[#](https://docs.openvino.ai#openvino-training-extensions)

OpenVINO™ Training Extensions provide a suite of advanced algorithms to train
Deep Learning models and convert them using the [OpenVINO™
toolkit](https://software.intel.com/en-us/openvino-toolkit) for optimized
inference. It allows you to export and convert the models to the needed format. OpenVINO Training Extensions independently create and train the model. It is open-sourced and available on [GitHub](https://github.com/openvinotoolkit/training_extensions). Read the OpenVINO Training Extensions [documentation](https://openvinotoolkit.github.io/training_extensions/stable/guide/get_started/introduction.html) to learn more.

## Detailed Workflow[#](https://docs.openvino.ai#detailed-workflow)

To start working with OpenVINO Training Extensions, prepare and annotate your dataset. For example, on CVAT.

OpenVINO Training Extensions train the model, using training interface, and evaluate the model quality on your dataset, using evaluation and inference interfaces.

Note

Prepare a separate dataset or split the dataset you have for more accurate quality evaluation.

Having successful evaluation results received, you have an opportunity to deploy your model or continue optimizing it, using NNCF. For more information about these frameworks, go to

[Optimization Guide](https://docs.openvino.ai/openvino-workflow/model-optimization.html).

If the results are unsatisfactory, add datasets and perform the same steps, starting with dataset annotation.