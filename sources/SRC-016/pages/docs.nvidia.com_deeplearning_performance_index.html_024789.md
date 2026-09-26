source: https://docs.nvidia.com/deeplearning/performance/index.html

NVIDIA Deep Learning Performance Documentation - Last updated February 1, 2023


## NVIDIA Deep Learning Performance

-
[Get Started With Deep Learning Performance](https://docs.nvidia.com/dl-performance-getting-started/index.html) - This is the landing page for our deep learning performance documentation. This page provides recommendations that apply to most deep learning operations. It also provides links, short explanations of other performance documents, and how these pages fit together.

##
[Training](https://docs.nvidia.com#training)

-
[Train With Mixed Precision](https://docs.nvidia.com/mixed-precision-training/index.html) - Mixed precision methods combine the use of different numerical formats in one computational workload. This document describes the application of mixed precision to deep neural network training.

##
[Recommendation Systems](https://docs.nvidia.com#recommendation-systems)

-
[Best Practices for Building and Deploying Recommender Systems](https://docs.nvidia.com/recsys-best-practices/index.html) - This document describes the best practices for building and deploying large-scale recommender systems using NVIDIA GPUs. These practices are the culmination of years of research and development in GPU-accelerated tools for recommender systems, as well as building recommender systems for our in-house products and top-performing solutions for international recommendation systems competitions.

##
[Optimizing Performance](https://docs.nvidia.com#optimizing-performance)

-
[Linear/Fully-Connected Layers User's Guide](https://docs.nvidia.com/dl-performance-fully-connected/index.html) - This guide provides tips for improving the performance of fully-connected (or linear) layers. It also provides an example of the impact of the parameter choice with layers in the Transformer network.
-
[Convolutional Layers User's Guide](https://docs.nvidia.com/dl-performance-convolutional/index.html) - This guide provides tips for improving the performance of convolutional layers. It also provides details on the impact of parameters including batch size, input and filter dimensions, stride, and dilation.
-
[Recurrent Layers User's Guide](https://docs.nvidia.com/dl-performance-recurrent/index.html) - This guide provides tips for improving the performance of recurrent layers. It also provides an example of use cases for persistence with layers in the GNMT system.
-
[Memory-Limited Layers User's Guide](https://docs.nvidia.com/dl-performance-memory-limited/index.html) - This guide describes the performance of memory-limited layers including batch normalization, activations, and pooling. It also provides tips for understanding and reducing the time spent on these layers within a network.

##
[Performance Background](https://docs.nvidia.com#performance-background)

-
[GPU Performance Background User's Guide](https://docs.nvidia.com/dl-performance-gpu-background/index.html) - This guide provides background on the structure of a GPU, how operations are executed, and common limitations with deep learning operations.
-
[Matrix Multiplication Background User's Guide](https://docs.nvidia.com/dl-performance-matrix-multiplication/index.html) - This guide describes matrix multiplications and their use in many deep learning operations. The trends described here form the basis of performance trends in fully-connected, convolutional, and recurrent layers, among others.