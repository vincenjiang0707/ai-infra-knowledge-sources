# [Issue #3403] [Bug] In Windows nightly cpu build TVM is not found even it it exists. Could not find module 'E:\virtualenv312\mlc_llm_test\Lib\site-packages\tvm\tvm.dll'

source: https://github.com/mlc-ai/mlc-llm/issues/3403
state: closed | updated: 2026-02-08T17:45:48Z
labels: bug

## 正文

## 🐛 Bug

I have installed mlc-llm with this command just like in the documentation:

    python -m pip install --pre -U -f https://mlc.ai/wheels mlc-ai-nightly-cpu

I have installed zstd. When I tried to use:

    python -c "import tvm; print(tvm.__file__)"

It returned to me this error:

    FileNotFoundError: Could not find module 'E:\virtualenv312\mlc_llm_test\Lib\site-packages\tvm\tvm.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The problem is that that file exists in that directory

## Environment

 - CPU:
 - Windows 11:
 - python virtualenv:
 - Installed with pip command by wheel
 - Python version 3.12;

## 评论 (3)

### victor-egg · 2026-01-18

<img width="1626" height="952" alt="Image" src="https://github.com/user-attachments/assets/3d4c6602-09e6-4396-8b41-5e1491c6b9aa" />

### MasterJH5574 · 2026-01-25

Hi @SuperMasterBlasterLaser @victor-egg, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!

### swamy18 · 2026-02-08

Good
