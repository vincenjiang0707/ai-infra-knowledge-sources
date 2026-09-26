# [Issue #73] Fine tuning qwen2.5 error[bug]

source: https://github.com/Ascend/pytorch/issues/73
state: open | updated: 2025-07-19T01:47:31Z
labels: 

## 正文

I want to fine-tune qwen2.5-3b, but there is an error in NPU:
<img width="1919" height="1039" alt="Image" src="https://github.com/user-attachments/assets/9d8b793b-b8f5-4075-8729-f87339c81cfa" />
I copied the code and executed it in CPU:
<img width="1919" height="1042" alt="Image" src="https://github.com/user-attachments/assets/d5e22ea3-d26f-41ae-bd50-48abdb3fd328" />
it was successfully executed:
<img width="1919" height="1040" alt="Image" src="https://github.com/user-attachments/assets/35bf817d-8831-443d-9c14-a0c4fe38a736" />
I am trying to edit this file,print it：
<img width="1919" height="1041" alt="Image" src="https://github.com/user-attachments/assets/9d6ecfbc-615e-46b3-90ae-b6feede01f3c" />
But printing the statement also reports an error:
<img width="1919" height="1043" alt="Image" src="https://github.com/user-attachments/assets/7e7fcfed-6eab-49b6-ab18-605da45f0d20" />
code:https://github.com/shaojun0/quen2_5_train
runtime environment：quay.io/ascend/vllm-ascend:v0.9.2rc1

## 评论 (3)

### yunyiyun · 2025-07-15

Currently, conv3d cannot fully support it
https://www.hiascend.com/document/detail/zh/Pytorch/700/apiref/apilist/ptaoplist_001090.html

You can try configuring the following environment variables
torch.npu.config.allow_internal_format = False
torch.npu.set_compile_mode(jit_compile=False)

### shaojun0 · 2025-07-17

> Currently, conv3d cannot fully support it https://www.hiascend.com/document/detail/zh/Pytorch/700/apiref/apilist/ptaoplist_001090.html
> 
> You can try configuring the following environment variables torch.npu.config.allow_internal_format = False torch.npu.set_compile_mode(jit_compile=False)

I understand what you mean, but this doesn't seem to involve conv3d, so why is it still reporting this error?

### yunyiyun · 2025-07-19

> > Currently, conv3d cannot fully support it https://www.hiascend.com/document/detail/zh/Pytorch/700/apiref/apilist/ptaoplist_001090.html
> > You can try configuring the following environment variables torch.npu.config.allow_internal_format = False torch.npu.set_compile_mode(jit_compile=False)
> 
> I understand what you mean, but this doesn't seem to involve conv3d, so why is it still reporting this error?

you cann see this prompt：
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1
