# [Issue #270] 如何进行图像-文本通过CLIP嵌入在同一Embedding空间进行测试？

source: https://github.com/modelscope/evalscope/issues/270
state: closed | updated: 2026-07-08T06:28:17Z
labels: enhancement

## 正文

## 功能描述 / Feature Description

您好，现在我在评测多模态RAG的检索和生成时遇见了问题：
我们的数据集模态多样，既有文本(text)，也有图像(image)，现在想构建image_queries.jsonl的时候发现，该queires构建只能为：
纯文本：queries.jsonl
纯图像：image_queries.jsonl
但是对于图像、文本混合的并没有涉及到检索方式。（事实上这很容易，因为CLIP能够实现图像、文本嵌入到同一空间）

## 需求背景 / Background

我们新的工作引用到了您的评测工具和方法，但是无法在关键实现：混合数据下的RAG。因此希望您能更新方法，或者提供混合检索评测的queries.jsonl构建

## 预期行为 / Expected Behavior

这个功能可以混合图像、文本，比如：
{"_id": "doc4", "text": "随着技术的进步，风能和太阳能等可再生能源变得越来越普及。"}
{"image_path": "custom_eval/multimodal/images/AMNH.jpg", "query": ["building"]}
然后可以自动进行评测

## 其他信息 / Additional Information

还有其他相关信息吗？ / Any other relevant information?


## 评论 (5)

### Yunnglin · 2025-01-02

你是希望可以评测CLIP模型的文本、图像混合检索能力吗

### Nomothings · 2025-01-02

是的是的没错，就是图像和文本通过CLIP嵌入到一个库中评测

### Yunnglin · 2025-01-03

好的，我们会尽快补充这部分功能

### Nomothings · 2025-01-03

好的感谢，期待您和团队的更新


### Yunnglin · 2026-07-08

Thanks for the suggestion. This is a feature request for multimodal RAG / CLIP-style mixed text-image retrieval, rather than a bug in the current evaluation flow.

The old Clip_Benchmark / RAGEval-related path is no longer the main direction after the RAG eval refactor, so we'll close this issue for now as a roadmap item. If this capability is still needed, please reopen or create a new issue with a concrete expected input/output format, for example:

1. Mixed text/image query format
2. Corpus format
3. Expected retrieval metric
4. Target model or embedding backend
5. A minimal example dataset

That will make it easier to evaluate whether it should be added as a new native benchmark / retrieval evaluation capability.

