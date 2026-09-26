# [Issue #2057] Support for quantizing activations

source: https://github.com/ModelCloud/GPTQModel/issues/2057
state: closed | updated: 2025-12-24T09:14:42Z
labels: 

## 正文

Hi, I see that the GPTQModel library supports GPTAQ/GPTQ v2. In the GPTAQ paper, results for configurations such as W8A8, W4A4 are shown. However, I could test only weight quantization with GPTAQ/GPTQ v2 so far with the library. Are there any plans to add support for activation quantization as well? Thanks.

## 评论 (1)

### Qubitium · 2025-12-24

Maybe out scope for this as this project currently does weight only activation. Activation quantization requires modeling changes at the framework layer. We may consider this at a later time. 
