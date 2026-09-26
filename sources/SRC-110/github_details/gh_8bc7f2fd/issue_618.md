# [Issue #618] FewCLUE/cluewsc数据集支持

source: https://github.com/modelscope/evalscope/issues/618
state: open | updated: 2026-09-15T06:56:25Z
labels: enhancement

## 正文

## 功能描述 / Feature Description
- FewCLUE/cluewsc数据集：http://opencompass.oss-cn-shanghai.aliyuncs.com/datasets/data/FewCLUE.zip"


## 评论 (1)

### JerryChaox · 2026-09-15

I’d like to work on this issue. I found that CLUEWSC is already available through EvalScope’s OpenCompass backend, so I assume this issue requests a native EvalScope benchmark adapter.  

My proposed scope is:
- use the official FewCLUE dev_few_all / test_public splits;
- convert true/false into an A/B multiple-choice task;
- evaluate with accuracy;
- add unit tests, a mock-eval smoke test, and generated documentation.

Could you confirm:
1. Which stable dataset source / dataset_id should the native adapter use?
2. Should it reproduce the zero-shot OpenCompass configuration, or the FewCLUE few-shot protocol?
3. Should the native benchmark name be cluewsc?
