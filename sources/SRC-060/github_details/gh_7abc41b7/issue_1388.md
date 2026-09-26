# [Issue #1388] CUDA device is not set properly

source: https://github.com/PaddlePaddle/ERNIE/issues/1388
state: closed | updated: 2025-12-07T12:31:13Z
labels: 

## 正文

I am trying to finetune PaddleOCR-VL-0.9B for devanagari recognition. I am trying this on wsl system

error :  "/home/username/ocr/.venv/lib/python3.12/site-packages/paddle/base/framework.py:824: UserWarning: You are using GPU version Paddle, but your CUDA device is not set properly. CPU device will be used by default."

I have already installed cuda toolkit 12.9, i also have same version cuda toolkit installed on the base windows system, the base windows system also has NVIDIA drivers installed. I have a NVIDIA Geforce RTX 5060, it has 8gb ram. Since this is my first time doing anything remotely related to ML/AI, any help will be greatly appreciated.

Thanks in adavance, if you need more details, please ask me for it, i do not know what is relevant so i just mentioned minimum information.


## 评论 (2)

### WYB27 · 2025-12-02

Thank you for your question. You can try our pre-configured Docker image. Please refer to https://github.com/PaddlePaddle/ERNIE/blob/develop/docs/erniekit.md#22-installing-paddlepaddle. If you have any further questions, feel free to ask.

### DOOMBOT0 · 2025-12-02

@WYB27 is my NVIDIA Geforce RTX 5060 GPU with 8 gb vram sufficient for fine-tuning paddleocr-vl-0.9b, if it is not enough, what can i do? Can i fine-tune using google colab, is that possible?
