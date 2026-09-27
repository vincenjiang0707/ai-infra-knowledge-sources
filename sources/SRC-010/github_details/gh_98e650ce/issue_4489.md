# [Issue #4489] [Bug] corrupted size vs. prev_size in fastbins

source: https://github.com/InternLM/lmdeploy/issues/4489
state: open | updated: 2026-04-10T03:42:17Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

Run Qwen3.5 with turbomind engine.

After several time, lmdeploy crash with logs:

corrupted size vs. prev_size in fastbins
Aborted (core dumped)

### Reproduction

It is currently unknown.

### Environment

```Shell
-
```

### Error traceback

```Shell

```

## 评论 (3)

### lzhangzz · 2026-04-08

Having trouble reproducing the issue. 

What setting you are testing? e.g. model / GPU used, prompt length and any parameter setting that is different from the default.

### lzhangzz · 2026-04-08

@tuilakhanh Also, you may pass `--async 0` to see if disabling the async model execution helps.

### tuilakhanh · 2026-04-10

@lzhangzz I haven't encountered this error lately, however, I am having an issue with dense models like Qwen-27B. In some cases, the model's response gets stuck in a loop like this."


<img width="487" height="1215" alt="Image" src="https://github.com/user-attachments/assets/1ebe645a-f5a7-4367-b248-2e1178c81b1a" />

