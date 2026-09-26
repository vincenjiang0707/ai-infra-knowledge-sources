# [Issue #1093] 部分数据集测试效果与paper差距较大

source: https://github.com/modelscope/evalscope/issues/1093
state: closed | updated: 2026-07-08T06:15:34Z
labels: 

## 正文

首先，测试过程中，感谢大佬的及时响应，并为我解惑。非常感谢大佬。
其次，我测试过程中，遇到一些数据测试出的效果与paper差距较大。在这里罗列了一下，辛苦大佬帮忙看看。

## 问题描述
**1：hallucination_test 测试：**
测试模型：`Qwen3-VL-30B-A3B-Instruct`
大佬今天优化代码之后，这个数据集的结果比paper高出10个点。这个是啥情况。
<img width="745" height="229" alt="Image" src="https://github.com/user-attachments/assets/1e7ea200-f559-4ad5-9840-58ec9e15e4d4" />

<img width="633" height="301" alt="Image" src="https://github.com/user-attachments/assets/81bc892b-7370-4027-a859-042f53bd75e1" />

测试日志：

[hallusion_bench.zip](https://github.com/user-attachments/files/24207163/hallusion_bench.zip)

由于`reviews `太大了，就把这个删了


**2：MultiIF 测试：**
测试模型：Qwen3-Next-80B-A30B-Instruct
<img width="654" height="275" alt="Image" src="https://github.com/user-attachments/assets/e16116d1-bd0e-4fec-978d-f4a785cb243e" />

测试日志：
[multi_if.zip](https://github.com/user-attachments/files/24207232/multi_if.zip)

由于`reviews ` 和 `predictions`太大了，不好上传，就把这个删了

**3：其他数据集也存在5个点左右的差距：**

如图，图中这几个数据集，差距也有5个点左右的差距。

<img width="738" height="535" alt="Image" src="https://github.com/user-attachments/assets/45ba6b42-b2fb-42ad-86b7-30148d2827f9" />

**4：想提一个建议：**
现在 `reports `里面的结果好像默认是第一个。但是实际上，paper里面使用的效果，并不是默认的这个。不知道大佬能不能优化一下，让第一个显示出来的结果，和paper里面用的保持一致呢。

比如，如图：默认的结果是 `chart_aAcc `的结果。但是paper好像用的是 `Overall_aAcc `这个结果。所以能不能让显示的默认结果改成 `Overall_aAcc` 这个结果呢

<img width="687" height="1129" alt="Image" src="https://github.com/user-attachments/assets/d5ec80a1-5fca-4101-b463-1e0b78083548" />

<img width="687" height="1077" alt="Image" src="https://github.com/user-attachments/assets/db5ba79d-ebac-442a-a145-c3eafc31a122" />


## EvalScope 版本（必填）
hallucination_test ：使用的12.17日更新的main分支
其他数据集：使用的是12.11日拉下来的main分支代码

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

<img width="941" height="852" alt="Image" src="https://github.com/user-attachments/assets/ab1efb47-5f5a-4b4d-aa33-7db7f45732b1" />

## 错误日志

见上面的日志

## 运行环境

- 操作系统：ubuntu
- Python版本：3.10

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (7)

### Tian14267 · 2025-12-17

**还有一个补充：**
对于 poly_math 这个数据集。使用`mean_acc `效果进行对比的话，实测出的和paper差距也大。但是使用 `DW-ACC` 这个指标，结果就相差不大。我找不到 paper 真实是使用哪个指标，能否辛苦大佬帮忙确认一下？

<img width="816" height="1138" alt="Image" src="https://github.com/user-attachments/assets/75f8092c-9294-4c75-8f90-30d60289b084" />

<img width="1479" height="620" alt="Image" src="https://github.com/user-attachments/assets/82ec5b19-8d34-4130-a61e-8250842e4010" />

### Tian14267 · 2025-12-17

**我咨询了大模型，给出的答案是用** `DW-ACC`  

<img width="1042" height="853" alt="Image" src="https://github.com/user-attachments/assets/6687be74-3228-4043-bdfb-686f9e50f273" />

### lucky9-cyou · 2026-01-09

There are some benchmarks where the text comes before the image, which can lead to lower benchmark results for VLM.

Please ref: https://github.com/QwenLM/Qwen3-VL/issues/1053

### Yunnglin · 2026-01-09

@lucky9-cyou Thanks for the feedback!

Our evaluation code is intentionally kept model-agnostic without model-specific optimizations to ensure fair comparison across different VLMs. 

If you'd like to customize the input format for your specific needs, feel free to clone the repo and modify the relevant dataset adapter.

### lucky9-cyou · 2026-01-09

> [@lucky9-cyou](https://github.com/lucky9-cyou) Thanks for the feedback!
> 
> Our evaluation code is intentionally kept model-agnostic without model-specific optimizations to ensure fair comparison across different VLMs.
> 
> If you'd like to customize the input format for your specific needs, feel free to clone the repo and modify the relevant dataset adapter.

I think this is not an optimization of some specific models, it might be related to the current model training strategy. At least for our own models, we place images before text, which leads to this bias. Qwen may have taken the same approach.

I'm not sure if this issue exists for other models. Of course, this phenomenon is quite strange. In theory, such bias shouldn't occur because the data seen during decoding is the same. I feel that this kind of bias might lead to a certain degree of decline in the model's understanding ability.

Just some of my findings, thank you for your response.

### xiyuwang-sudo · 2026-01-14

> 首先，测试过程中，感谢大佬的及时响应，也为我解惑。非常感谢大佬。 其次，我测试过程中，遇到一些数据测试出来的效果与论文差距加大。这里罗列一下，辛苦大佬帮忙看看。
> 
> ## 问题描述
> **1：hallucination_test 测试：** 测试模型：`Qwen3-VL-30B-A3B-Instruct` 大佬今天优化代码之后，这个数据集的结果比paper高出10个点。这是啥情况。 <img alt="图像" width="745" height="229" src="https://private-user-images.githubusercontent.com/27938135/527443098-1e7ea200-f559-4ad5-9840-58ec9e15e4d4.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDMwOTgtMWU3ZWEyMDAtZjU1OS00YWQ1LTk4NDAtNThlYzllMTVlNGQ0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ2MjcwOTQ4Mjc1NGQ1MjE1MjMyN2RjODJlN2I1MmM2ZjNmYTEzNGU4MDMyN2VhNGQyN2YxMmM2NmU1MjE4ZjQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.OEPvFVCTrYpoy_vUEbpavhKihOZ_DMwGBv7ul9lKhAA">
> 
> <img alt="图像" width="633" height="301" src="https://private-user-images.githubusercontent.com/27938135/527443464-81bc892b-7370-4027-a859-042f53bd75e1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDM0NjQtODFiYzg5MmItNzM3MC00MDI3LWE4NTktMDQyZjUzYmQ3NWUxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQzYTFmOTkxZGVjODAyMGM1YzllNzBhM2IzOWNkNjY2MWY3YWYyMDE2N2I5MzRhOWU0NGMwNTQ5MGQ5OTM0MWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.NwvQ6lUAwOaDox51IsJIEq5OS8AEM3jFbMuE6nT9qJg">
> 测试日志：
> 
> [幻觉长椅.zip](https://github.com/user-attachments/files/24207163/hallusion_bench.zip)
> 
> 由于`reviews `麻烦了，就把这个删掉了
> 
> **2：MultiIF 测试：** 测试模型：Qwen3-Next-80B-A30B-Instruct <img alt="图像" width="654" height="275" src="https://private-user-images.githubusercontent.com/27938135/527444268-e16116d1-bd0e-4fec-978d-f4a785cb243e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDQyNjgtZTE2MTE2ZDEtYmQwZS00ZmVjLTk3OGQtZjRhNzg1Y2IyNDNlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQxOTVlOTMxODlhOTMzZDQ0NzcxNzIxN2IzMTE3Zjg2NmVkMzRiMjA5NTZmOGI5Yzg4MzE4MjM2N2MyYTdkYmMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.FtnjJmmpG5PEKEzuUnWtMRuuu3IveoVIl4qzGgtaAkY">
> 
> 测试日志： [multi_if.zip](https://github.com/user-attachments/files/24207232/multi_if.zip)
> 
> 由于`reviews `和`predictions`麻烦了，不好上传，就把这个删掉了
> 
> **3：其他数据集也存在5个点左右的差距：**
> 
> 下表，列出这几个数据集，差距也有5个点左右的差距。
> 
> <img alt="图像" width="738" height="535" src="https://private-user-images.githubusercontent.com/27938135/527446383-45ba6b42-b2fb-42ad-86b7-30148d2827f9.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDYzODMtNDViYTZiNDItYjJmYi00MmFkLTg2YjctMzAxNDhkMjgyN2Y5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMzNWQ5MzIyNmExYjIwNjY2Yzc4Nzk5MGMyYmM0OTQyZmNkODgxZWQ5NWZjZDllYmZhOWZmNmQ1M2YzMWFhOTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.e8CJRlEF-YKGLITi_mWplfjoAmwY2XgfZxe-7yvXRuw">
> **4：想提一个建议但是：** 现在`reports `里面的结果默认好像是第一个。实际上，paper里面使用的效果，并不是默认的这个。不知道大佬能不能优化一下，让第一个显示出来的结果，和paper里面用的保持一致呢。
> 
> 例如，如图：默认的结果是`chart_aAcc `这个结果。但是论文希望用的是`Overall_aAcc `这个结果。所以不能让显示的默认结果改成`Overall_aAcc`这个结果呢
> 
> <img alt="图像" width="687" height="1129" src="https://private-user-images.githubusercontent.com/27938135/527447361-d5ec80a1-5fca-4101-b463-1e0b78083548.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDczNjEtZDVlYzgwYTEtNWZjYS00MTAxLWI0NjMtMWUwYjc4MDgzNTQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNjMTAxMzk2ZmVkZDkzM2MxZThjNWQ5YWZmNGI2NDhhMzdkMDgwZGU2ZGViZmJkZjc1N2U3NmFhOWE1ZTI1MDEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.t1yNzw66Obq_R1-jc-Ni_vIApW-YCfAFS7fWUylIleU"> <img alt="图像" width="687" height="1077" src="https://private-user-images.githubusercontent.com/27938135/527447480-db5ba79d-ebac-442a-a145-c3eafc31a122.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDc0ODAtZGI1YmE3OWQtZWJhYy00NDJhLWExNDUtYzNlYWZjMzFhMTIyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZiZDA5OWJhYWRmZTk0NTliODA4NGY1ZWQxM2U5ODMyYzVlYTYyMGI3M2RkNzRkMjlmMzk3NTE0ZWJiMDEyYjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Es3Vx3zMP_6VljMGWzhUH7PUci3yl0BNkr5maWqtlZ8">
> ## EvalScope 版本（必填）
> Hallucination_test ：使用的12.17日更新的主要分支 其他数据集：使用的是12.11日拉下来的主要分支代码
> 
> ## 使用工具
> * [ ] 原生/原生框架[ ] Opencompass 后端[ ] VLMEvalKit 后端[ ] RAGEval 后端[ ] 性能/模型推理压测工具[ ] Arena / 竞技场模式
> 
> ## 执行的代码或指令
> <img alt="图像" width="941" height="852" src="https://private-user-images.githubusercontent.com/27938135/527448151-ab1efb47-5f5a-4b4d-aa33-7db7f45732b1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjgzODE3ODYsIm5iZiI6MTc2ODM4MTQ4NiwicGF0aCI6Ii8yNzkzODEzNS81Mjc0NDgxNTEtYWIxZWZiNDctNWY1YS00YjRkLWFhMzMtN2RiN2Y0NTczMmIxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE0VDA5MDQ0NlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTlhZjYzYjc4NTM1NmE1ZGQ2YmY4NTkyN2U0ODc0MWM0NDMxNTczNWE2OGY0ZTg0ZWM1ZWVhNjlkODhiODNhYzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.woz0dlCfh8kFcTr1k1BBrc87FyWJ-AzkZn-4l4QXwYQ">
> ## 错误日志
> 见上面的日志
> 
> ## 运行环境
> * 操作系统：ubuntu
> * Python版本：3.10
> 
> ## 其他信息
> 如果还有其他相关信息，请在此处提供。

SimpleVQA数据集你测试会不会报图像错误，我这边加载数据跑前向时都会报出图像读取错误avif


### Yunnglin · 2026-07-08

这类“无法复现官方 / paper 分数”的问题，通常需要先对齐评测口径、采样参数和运行环境。当前信息还不足以判断为 EvalScope 框架侧 bug，先关闭该 issue；如果后续能提供最小可复现证据，欢迎 reopen 继续跟进。

建议按下面顺序排查：

1. **上传完整 `outputs/<timestamp>/`**
   - 至少包含 `configs/`、`predictions/`、`reports/`；
   - 如涉及 judge / agent / terminal-bench，请一并提供 `reviews/`、`trials/`、`agent/trajectory.json`、verifier 日志。

2. **先定位差异来源**
   - 模型原始输出错误：优先检查模型服务、采样参数、prompt 或官方口径；
   - 模型输出正确但 `extracted_prediction` 错：可能是答案提取问题；
   - 提取正确但 score 错：可能是 metric / judge / aggregation 配置问题；
   - 大量 error / timeout：先排查运行环境，再比较分数。

3. **对齐官方评测口径**
   请确认 prompt、system prompt、chat template、temperature、top_p、top_k、max_tokens、repeats、pass@k / vote@k / mean aggregation、judge model、benchmark 版本和 subset 都与官方一致。

4. **小样本集需要多次重复**
   AIME 等小样本 benchmark 单题就会带来几个百分点波动，建议使用 `repeats` 多次采样，并明确聚合方式。

5. **Agent / terminal-bench 类任务先查环境**
   请确认 Docker、容器网络、GitHub/PyPI/apt 访问、`timeout_multiplier` 等配置正常。环境不稳定时，总分通常不具备可比性。

6. **如需继续定位**
   请提供“模型输出正确但 EvalScope 提取或评分错误”的具体样本编号和完整 outputs，我们会继续排查。

