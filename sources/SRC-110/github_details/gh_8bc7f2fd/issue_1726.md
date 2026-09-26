# [Issue #1726] 希望在压测的多模态数据集类型中加入支持一次输入多张图片的数据集模式

source: https://github.com/modelscope/evalscope/issues/1726
state: closed | updated: 2026-09-17T10:54:38Z
labels: enhancement

## 正文

## 功能描述 / Feature Description

希望在压测的多模态数据集类型中加入支持一次输入多张图片的数据集模式

## 需求背景 / Background

我方在使用evalscope进行压测时需要在一次请求中输入多张图片，同时不使用random_vl随机生成，因此需要evalscope支持一种一次可输入多张图片的数据集模式。现有的flickr8k和kontext_bench两种多模态数据集模式都是一次只能输入一张图片。

## 预期行为 / Expected Behavior

使用evalscope进行压测时支持使用一次可输入多张图片的开源数据集，并可根据此模式自行构造数据集。




## 评论 (1)

### Yunnglin · 2026-09-17

Resolved and merged via #1729.

The new `mmmu_multi_image` perf dataset round-robins all 30 MMMU validation subjects to generate real multi-image requests.

For custom multi-image traffic, `line_by_line` can replay OpenAI messages or complete request bodies. Use HTTP(S) URLs or data URLs supported by the serving backend.

Targeted tests and CI checks passed.
