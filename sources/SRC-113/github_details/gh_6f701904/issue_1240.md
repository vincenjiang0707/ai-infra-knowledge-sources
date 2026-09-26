# [Issue #1240] pycocotools for retinanet

source: https://github.com/mlcommons/inference/issues/1240
state: closed | updated: 2026-05-16T00:40:26Z
labels: Stale

## 正文

We've been using the standard [`pycocotools`](https://pypi.org/project/pycocotools/) Python package for calculating the Object Detection accuracy since MLPerf Inference v0.5. It used to be OK for SSD-ResNet34 and SSD-MobileNet-v1, but it is rather painful for RetinaNet. First, this calculation is slow: it takes ~7-8 minutes on a decent workstation per scenario per system; in other words, it's ~15-25 minutes per system. Second, this calculation is memory hungry: see below this calculation strangling an Edge appliance with 8G RAM and 4G swap.

![cocotools](https://user-images.githubusercontent.com/6597818/192647810-5a0b0ac2-bbb6-4043-be1f-21b96d8bef27.png)

## 评论 (15)

### arjunsuresh · 2022-10-08

Hi @psyhtest , are you referring to [this script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/tools/accuracy-openimages.py)?

### psyhtest · 2022-10-08

Yes, Arjun.

### arjunsuresh · 2022-10-10

Thank you Anton for your reply. On my laptop while doing the accuracy run for 5000 images, the speed of accuracy script is 60 images per second (faster than the workstation?) which is almost 60 times faster than the CPU inference speed and so hardly noticeable. I tried to call the cocoEval library using multiple threads as the description given [here](https://github.com/NVIDIA/cocoapi/blob/nvidia/master/PythonAPI/pycocotools/cocoeval.py#L19) shows that the images can be processed in parallel and then we can call the accumulate function. But when we split and process the images list, the calculated scores are changing. So the only option to speed up the processing looks like to do parallel processing inside the evaluation function which is done in [this Nvidia fork](https://github.com/NVIDIA/cocoapi/blob/nvidia/master/PythonAPI/pycocotools/ext.cpp). 

### rnaidu02 · 2022-10-11

@pgmpablo157321 To look at Arjun's proposal and give feedback on the feasibility.

### arjunsuresh · 2022-10-12

@pgmpablo157321 To use the Nvidia fork of pycocotools we need to add instructions for using this fork and also update the accuracy numbers - there can be a slight difference here. We can give you an update on these by next week as we'll be checking them.

### arjunsuresh · 2022-10-21

Unfortunately the Nvidia fork is not working well with retinanet. [This](https://github.com/NVIDIA/cocoapi/pull/15/commits/d434218d9ff378e73e399eaf6dc4e5689156dab2) commit fixes the issue with PythonAPI but the C++ extension is giving poor accuracy. 

### rnaidu02 · 2022-11-01

@nv-ananjappa

### arjunsuresh · 2022-11-01

[This](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/get-mlperf-inference-src/patch/coco.patch) is the patch we used on the inference repo when running using nvidia-pycocotools.

### nv-ananjappa · 2022-11-02

@arjunsuresh We are using the (slow) script for MLPerf Inference too. 😁 Since you seem to be familiar with it, would you like to contribute by adding support for the faster NVIDIA cocoapi?

### arjunsuresh · 2022-11-04

Thank you @nv-ananjappa for checking. Unfortunately I'm not familiar with cocoapi to do that change :innocent:   I had tried to parallelize the python API -- but realized that the original implementation is inherently sequential and that is why Nvidia fork with cpp extension made sense. I'll add my accuracy result as an issue in the Nvidia fork - it might be an easy fix for the original developer.
 
Meanwhile we are waiting about an hour for the accuracy run of retinanet on Nvidia T4 GPU (using reference implementation) and so 6-7 extra minutes is hardly noticeable :smile: 

### arjunsuresh · 2023-12-30

@nv-ananjappa This is done now. [This patch](https://github.com/ctuning/mlcommons-ck/commit/bbab1205d562812a81c8f7455b0c9e002828a13f) enables nvidia-pycocotools for openimages accuracy run and speeds up the accuracy check from 7.5 minutes to 2 minutes. 

### psyhtest · 2024-01-02

@arjunsuresh That's great! How about memory consumption?

### arjunsuresh · 2024-01-02

Hi @psyhtest It was about 0.5% on an 768GB system. The original pycocotools had gone upto 1.6% of memory. 

### arjunsuresh · 2024-01-09

@psyhtest Unfortunately even with the new change, the accuracy run fails on Thundercomm RB6 - 8 GB RAM and 4GB swap space. It runs fine on an Intel Sapphire Rapids in 46s with 256 GB RAM (only about 1% getting used). 

### github-actions[bot] · 2026-05-16

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
