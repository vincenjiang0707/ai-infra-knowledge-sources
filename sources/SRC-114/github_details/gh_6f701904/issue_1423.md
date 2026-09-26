# [Issue #1423] inputs and outputs parameter of vision/classification and detection benchmark

source: https://github.com/mlcommons/inference/issues/1423
state: closed | updated: 2026-05-12T00:39:50Z
labels: Stale

## 正文

Hi, in the README of `vision/classifcation and detection` benchmark, there are two parameters:

`--inputs INPUTS` comma separated input name list in case the model format does not provide the input names. This is needed for tensorflow since the graph does not specify the inputs.

`--outputs OUTPUTS` comma separated output name list in case the model format does not provide the output names. This is needed for tensorflow since the graph does not specify the outputs.

I'm a little confused about the meaning of `--outputs`, does that mean the outputs of inference? If so, how should I know the output of model inference?
And if I use tensorflow, do I must provide these two parameters? It would be better if you could provide an example of what these two parameters should look like on Imagenet dataset. 

Thank you very much!

## 评论 (2)

### arjunsuresh · 2023-07-03

Preparation of the required inputs (like models, datasets etc) for the different backends is done in CM. You can find the instructions to run different backends like `onnxruntime` or `tf` [here](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/resnet50/README_reference.md). By running them, you can see the exact run commands being generated.

`main.py` is called by [this script](https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/run_local.sh) which takes care of the inputs/outputs. 

### github-actions[bot] · 2026-05-12

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
