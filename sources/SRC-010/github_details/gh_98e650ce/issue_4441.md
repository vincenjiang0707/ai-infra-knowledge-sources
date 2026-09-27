# [Issue #4441] [Docs]  Help for adding new models .

source: https://github.com/InternLM/lmdeploy/issues/4441
state: closed | updated: 2026-03-21T14:17:21Z
labels: 

## 正文

### 📚 The doc issue

I have tried adding models to pytorch engine many times but failed , would request , if you could give an example on how to add models from hugging face in detail , i wanted to add liquid ai model but failed multiple times . thanks 

### Suggest a potential alternative/fix

_No response_

## 评论 (2)

### windreamer · 2026-03-21

Hi @w-ahmadai 

Thank you for your patience and for trying to add models to the PyTorch engine — we really appreciate your contribution!

For adding new models from Hugging Face, please refer to this guide:
https://lmdeploy.readthedocs.io/en/latest/advance/pytorch_new_model.html

However, please note that this documentation may be slightly outdated due to recent architectural upgrades in the codebase. Additionally, adding a model that fully meets the PythonEngine performance standards is non-trivial, as it requires careful optimization to align with our execution framework.

That said, a successful integration is always valuable to the community and can serve as a starting point for further optimization efforts. If you encounter discrepancies while following the steps, feel free to open a follow-up issue with specific error messages or blockers you hit — we're happy to help refine both the docs and the process.

Looking forward to your success with the Liquid AI model! 🙌


### w-ahmad1a10 · 2026-03-21

thanks 
