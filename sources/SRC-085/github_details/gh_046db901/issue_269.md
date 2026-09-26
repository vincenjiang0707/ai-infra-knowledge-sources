# [Issue #269] The results are less optimal than expected

source: https://github.com/SafeAILab/EAGLE/issues/269
state: closed | updated: 2025-08-09T00:56:54Z
labels: 

## 正文

Hello, I'm using Eagle 3 to perform concurrent dynamic tests on the ShareGPT dataset. As concurrency increases, although each step does yield additional token gains, the latency per step also increases significantly—up to more than 3× in some cases. As a result, both the average and total throughput fall short of the baseline. Could this be related to Tree Attention? It's possible that the number of verification tokens per step is too high, leading to longer GPU computation times.

]

<img width="703" height="296" alt="Image" src="https://github.com/user-attachments/assets/3f77ac4f-f066-4d8a-84cc-7a7f4bb62a38" />






## 评论 (3)

### hongyanz · 2025-08-02

For bs > 1, we suggest not using the tree.

### ggg-s · 2025-08-03

thank your response,

Is vLLM currently not supporting loading Qwen3 with Eagle3? I got this message.

Value error, Eagle3 is only supported for Llama models. Got self.target_model_config.hf_text_config.model_type='qwen3' [type=value_error, input_value=ArgsKwargs((), {'method':...able_log_stats': False}), input_type=ArgsKwargs]

### hongyanz · 2025-08-09

We are not sure about the plan of vLLM. Perhaps better to consult them?
