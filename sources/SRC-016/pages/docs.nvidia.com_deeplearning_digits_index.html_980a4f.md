source: https://docs.nvidia.com/deeplearning/digits/index.html

Note: We are not adding features, fixing bugs, or supporting the NVIDIA Deep Learning GPU Training System (DIGITS) software. You may continue to use the software if it meets your needs. However:

For developers creating vision AI applications, we suggest NVIDIA TAO, an open-source toolkit for AI model training and customization.

You can pull (download) an NVIDIA container that is already built, tested, tuned, and ready to run. DIGITS container includes the code required to build the framework so that you can make changes to the internals. Before you can run DIGITS, there are some setup requirements that you must first meet. This guide provides instructions on pulling and using the DIGITS container.

This guide provides a detailed overview about using the DIGITS container. DIGITS is a training platform that can be used with the NVIDIA TensorFlow deep learning framework. Using this framework, DIGITS will train your deep learning models on your dataset.

These release notes describe the key features, software enhancements and improvements, known issues, and how to run DIGITS 6.1.1 for the 21.09 and earlier releases. The DIGITS application is used by engineers and data scientists. DIGITS can be used to rapidly train highly accurate deep neural networks for image classification, segmentation, and object detection tasks. The DIGITS application is released, much like the NVIDIA optimized framework containers, on a monthly basis to provide you with the latest NVIDIA deep learning software libraries and GitHub code contributions that have been sent upstream; which are all tested, tuned, and optimized.

This guide provides a detailed overview about installing and running DIGITS. This guide also provides examples using DIGITS with TensorFlow deep learning frameworks.

This tutorial provides step-by-step instructions for writing a custom plugin. DIGITS data plug-ins enable a mechanism by which you can extend DIGITS to ingest data from custom sources. Likewise, DIGITS offers a number of model output visualization types such as Image Classification, Object Detection or Image Segmentation. DIGITS visualization plug-ins make it possible to visualize the output of non-standard models. This guide walks you through the process of adding your own plugin.

This document is the Software License Agreement (SLA) for NVIDIA DIGITS. The following contains specific license terms and conditions for NVIDIA DIGITS. By accepting this agreement, you agree to comply with all the terms and conditions applicable to the specific product(s) included herein.