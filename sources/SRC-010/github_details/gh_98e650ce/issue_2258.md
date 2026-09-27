# [Issue #2258] [Bug] Intel MKL FATAL ERROR /torch/lib/libtorch_cpu.so

source: https://github.com/InternLM/lmdeploy/issues/2258
state: closed | updated: 2026-03-24T16:26:28Z
labels: 

## 正文

### Checklist

- [ ] 1. I have searched related issues but cannot get the expected help.
- [ ] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

V0.5.3

lmdeploy lite auto_awq internlm/internlm2_5-20b-chat --work-dir /home/ma/work/models/internlm2_5-20b-chat-4bit --batch-size 8 --search-scale True
Intel MKL FATAL ERROR: Cannot load /home/ma/miniconda3/envs/lmdeploy/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so.

### Reproduction

lmdeploy lite auto_awq internlm/internlm2_5-20b-chat --work-dir /home/ma/work/models/internlm2_5-20b-chat-4bit --batch-size 8 --search-scale True

### Environment

```Shell
cuda 12.5
```


### Error traceback

_No response_

## 评论 (5)

### Luchen-077 · 2024-11-03

I meet the same bug, have you resolved?

### Luchen-077 · 2024-11-03

The bug has been solved.
When I tried to 'conda activate xxx' I got the info 'sh: 0: getcwd() failded: No such file or directory', and then the info like this while training a model.
About the first info, use 'cd ~' command and run what you want (for example: 'conda activate xxx' for me) then cd back your directory and train. It works

### PixelChen24 · 2025-06-25

> The bug has been solved. When I tried to 'conda activate xxx' I got the info 'sh: 0: getcwd() failded: No such file or directory', and then the info like this while training a model. About the first info, use 'cd ~' command and run what you want (for example: 'conda activate xxx' for me) then cd back your directory and train. It works

This really works for me, but I still wonder the reason behind this and why does this work

### Elena-TKO · 2025-09-03

> > The bug has been solved. When I tried to 'conda activate xxx' I got the info 'sh: 0: getcwd() failded: No such file or directory', and then the info like this while training a model. About the first info, use 'cd ~' command and run what you want (for example: 'conda activate xxx' for me) then cd back your directory and train. It works
> 
> This really works for me, but I still wonder the reason behind this and why does this work

In my situation this was because I tried to launch code from the deleted folder.

### RiverGao · 2026-03-24

> The bug has been solved. When I tried to 'conda activate xxx' I got the info 'sh: 0: getcwd() failded: No such file or directory', and then the info like this while training a model. About the first info, use 'cd ~' command and run what you want (for example: 'conda activate xxx' for me) then cd back your directory and train. It works

This also works for me. I get the error when I was trying to run a inference script after an NFS failure and reconnect
