# [Issue #59] UI scripts fail to launch due to Gradio version incompatibility

source: https://github.com/meta-pytorch/KernelAgent/issues/59
state: closed | updated: 2025-12-16T03:24:41Z
labels: bug

## 正文

### 🐛 Describe the bug

KernelAgent UI scripts (fuser_ui.py, pipeline_ui.py, triton_ui.py) fail to launch with recent Gradio versions due to deprecated/removed API usage and missing dependency pinning.
Errors encountered
Error 1: show_api parameter removed in Gradio 5.x
TypeError: Blocks.launch() got an unexpected keyword argument 'show_api'
Error 2: Non-integer scale values deprecated
UserWarning: 'scale' value should be an integer. Using 1.5 will cause issues.
Error 3: Gradio 5.x internal bug triggered by UI components
TypeError: argument of type 'bool' is not iterable
Root cause

UI files use show_api=False in app.launch() - removed in Gradio 5.x
UI files use scale=1.5 in gr.Column() - must be integer in Gradio 5.x
No Gradio version pinning in pyproject.toml 

Expected behavior
UI scripts should launch without errors across supported Gradio versions.
Suggested fix
Option A: Pin Gradio to 4.x in dependencies:
gradio>=4.31.0,<5.0.0
Option B: Update code for Gradio 5.x compatibility:

Remove show_api=False from all app.launch() calls
Change scale=1.5 to scale=2 (integer)

### Platform and Version

Ubuntu 25.10 , Python 3.12, main KernelAgent branch 

## 评论 (2)

### Jack-Khuu · 2025-12-10

Thanks for the flag @sandlbn 

Updating Gradio 5.x and updating the deps to reflect this sounds like a good option

Feel free to toss up a PR if you have it fixed, else i can put one up in a bit

### sandlbn · 2025-12-10

I have working code, but let me test it one more time Today. 
