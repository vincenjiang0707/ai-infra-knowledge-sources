# [Issue #232] [Feature Request] Pip install support

source: https://github.com/deepseek-ai/DeepGEMM/issues/232
state: closed | updated: 2026-05-28T18:22:00Z
labels: 

## 正文

Hi, vLLM has already set DeepGEMM as the default engine, could we setup PYPI and make it installed through pip?

This would be greatly helpful for better integration of vLLM, thanks!

## 评论 (4)

### bbartels · 2025-11-22

There is already pre-built wheels here: https://github.com/deepseek-ai/DeepGEMM/releases
Though they are not published to PYPI. Whats missing is ARM64 prebuilt wheels though as i had raised here: https://github.com/deepseek-ai/DeepGEMM/issues/223

### LyricZhao · 2025-12-05

Sorry, we are planing a community wheel release refactor in January. Before that, please build it by yourself.

### yewentao256 · 2026-05-05

Hi @LyricZhao , are we going to support this recently?

### yewentao256 · 2026-05-28

Close this issue as not scheduled
