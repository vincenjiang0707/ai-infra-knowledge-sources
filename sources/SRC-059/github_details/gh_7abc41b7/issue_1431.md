# [Issue #1431] ppocr-vl sft后效果变差

source: https://github.com/PaddlePaddle/ERNIE/issues/1431
state: open | updated: 2026-01-27T02:26:07Z
labels: 

## 正文

用ms-swift, ernie-kit都试过sft 100w 业务数据，但是发现训练收敛不了，训完后评测发现效果更差了，这是为什么呢。 业务数据的公式用latex标注，table和chart只标注ocr，文本是只识别print ocr，都用的固定prompt。

## 评论 (2)

### Sunting78 · 2026-01-23

您好，能发出一两条数据和微调后的推理结果看看吗？prompt可以和原来的有区别，比如文本是只识别print ocr,不要再使用原始的OCR指令，而是使用例如Print OCR，尽可能和之前的指令不一致。这样避免您的任务依然还是会输出所有的文本，而不是打印文本。

### Hor1zonz · 2026-01-27

> 您好，能发出一两条数据和微调后的推理结果看看吗？prompt可以和原来的有区别，比如文本是只识别print ocr,不要再使用原始的OCR指令，而是使用例如Print OCR，尽可能和之前的指令不一致。这样避免您的任务依然还是会输出所有的文本，而不是打印文本。

prompt: 按照阅读顺序输出图片中的打印文本内容
结果：1.22 parallel How发光称 date I/S (看到了)
完全不对

<img width="597" height="308" alt="Image" src="https://github.com/user-attachments/assets/490da66f-1a21-4e57-9cd8-eed2242cb64b" />

