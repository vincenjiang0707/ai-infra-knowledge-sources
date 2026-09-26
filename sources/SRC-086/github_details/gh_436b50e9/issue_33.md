# [Issue #33] [New feature] mlc-llm support

source: https://github.com/FasterDecoding/Medusa/issues/33
state: open | updated: 2023-12-08T01:17:01Z
labels: enhancement

## 正文

https://github.com/mlc-ai/mlc-llm
https://github.com/mlc-ai/llm-perf-bench

## 评论 (8)

### kmn1024 · 2023-12-07

This issue (and repos) feels pretty dead. What's happening? Are the maintainers working on something that obsoletes Medusa (https://github.com/FasterDecoding/REST)? Is the roadmap still active? @ctlllll @leeyeehoo 

### leeyeehoo · 2023-12-07

Indeed we are working on Medusa... will release a new version soon :)

### kmn1024 · 2023-12-07

Thanks Yuhong =) Looking forwards!!

### kmn1024 · 2023-12-07

I want to ask for some advice regarding model performance. My goal is to run a custom model on pretty cheap, OpenCL-compatible, hardware. Using MLC, the current speed is ~ 3 toks/sec, which is insufficient for fluid interaction.

What would you recommend? Getting Medusa to work on MLC would help a lot, and I would love to try working on it (though it looks pretty daunting). However, if Medusa v2 is coming out, perhaps I should just wait?

### leeyeehoo · 2023-12-07

You can refer to [this branch](https://github.com/FasterDecoding/Medusa/tree/v1.0-prerelease). No significant change on the model side. We are working on fully finetuning the models (including new models like Zephyr) and will release the finetuning recipe. Supporting more libraries will be the next step.

### kmn1024 · 2023-12-07

Thanks for the heads up! If you have a chance, please also include a recipe for adding new types of models too.

### leeyeehoo · 2023-12-07

[Check this](https://github.com/FasterDecoding/Medusa/blob/0ac14da96a87f69d063b003bf8b9bec129610987/medusa/model/medusa_model.py#L304) Not sure if you talked about a template to add new model support?

### kmn1024 · 2023-12-08

Yes! Thanks for pointing that out.
