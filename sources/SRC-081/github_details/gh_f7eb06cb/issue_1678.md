# [Issue #1678] [FEATURE] Add FOEM Support

source: https://github.com/ModelCloud/GPTQModel/issues/1678
state: closed | updated: 2026-04-02T04:47:10Z
labels: 

## 正文

First-Order Error Matters: Accurate Compensation for Quantized Large Language Models.：https://arxiv.org/abs/2507.11017

https://github.com/Xingyu-Zheng/FOEM

FOEM+GPTAQ+SpinQuant  will be better.



FOEM can be seamlessly integrated with advanced techniques such as GPTAQ and SpinQuant, yielding additional improvements under
the challenging W4A4KV4 setting, and further narrowing the accuracy gap with
full-precision baselines beyond what current state-of-the-art methods achieve.

## 评论 (5)

### Qubitium · 2025-08-18

@Xingyu-Zheng Would you be interested in helping to add FOEM quant + kernel support to GPTQModel? 

### Xingyu-Zheng · 2025-08-18

We are very glad to see that our FOEM has attracted attention! We believe we can complete the adaptation on GPTQModel within a few days, as the implementation of FOEM is quite simple.

However, unlike methods such as GPTQ and GPTAQ that have already been accepted at conferences, FOEM is still undergoing continuous improvements. We would like to ask whether the maintainers would prefer us to first integrate the current version into the repository and then continue maintaining it as updates are made? @Qubitium 

### Qubitium · 2025-08-19

@Xingyu-Zheng Awesome! No problem with the rolling updates and `non-final` status of the FOEM base code. I consider all software forever `beta` so no worries about stability. So yes, I would definitely recommend just merging what your team have into the current gptqmodel structure, confirm working status, create a small ci test to validate. 

Unlike the original autogptq or gptq code, gptqmodel is structured like a pipeline with multiple serial stages. This allows the current code to adapt to many different quantization techniques in a modular way, i.e. Nvidia's `EoRA`. If you have MS Teams, feel free to msg me at qubitium@modelcloud.ai as I am always on teams for the most-part if you have any questions and issues during integration. 

### Xingyu-Zheng · 2026-04-01

@Qubitium Sorry for the delayed reply. Our paper was published at AAAI 2026 last month (https://ojs.aaai.org/index.php/AAAI/article/view/40123), and we have now completed the adaptation to the latest version of GPTQModel.

You are welcome to review the latest pull request #2639 . We have made a thorough effort to ensure compatibility with the current codebase. Please feel free to reach out if you notice any issues or have further questions.

### sankexin · 2026-04-01

这是来自QQ邮箱的假期自动回复邮件。
 
您好，我最近正在休假中，无法亲自回复您的邮件。我将在假期结束后，尽快给您回复。
