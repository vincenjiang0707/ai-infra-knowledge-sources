# [Issue #1396] PaddleOCR-VL 微调表格标注

source: https://github.com/PaddlePaddle/ERNIE/issues/1396
state: open | updated: 2026-08-01T16:11:24Z
labels: 

## 正文

复杂表格格式如何进行标注，有什么标注工具直接标注吗

## 评论 (14)

### qzkq · 2025-12-08

+1

### qzkq · 2025-12-08

什么时候出一个表格的微调示例，合并单元格怎么弄成OTSL 格式

### Sunting78 · 2025-12-17

您好，表格一般我们建议使用PPOCRLabel标注，这里有标注的教程。标注完成后会保留html格式的表格。使用脚本将HTML格式转化为OTSL格式即可。https://github.com/PaddlePaddle/PaddleX/blob/18e94f852749b27e2e70abfd3a646d1ddccee478/docs/data_annotations/ocr_modules/table_recognition.md
脚本如下：

[html_to_otsl.py](https://github.com/user-attachments/files/24203712/html_to_otsl.py)



另外表格微调案例在准备中，ready后会发布，感谢您的持续关注。

### adoresever · 2026-01-01

请问一下paddle0.9b的vl模型可以进行训练吗？不知道有没有官方教程

### nepeplwu · 2026-01-08

@adoresever  模型的微调教程参考：https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/paddleocr_vl_sft.md

### adoresever · 2026-01-08

我已经实现啦，帮你们录了一个视频

On Wed, Jan 7, 2026 at 9:07 PM wuzewu ***@***.***> wrote:

> *nepeplwu* left a comment (PaddlePaddle/ERNIE#1396)
> <https://github.com/PaddlePaddle/ERNIE/issues/1396#issuecomment-3721584456>
>
> @adoresever <https://github.com/adoresever> 模型的微调教程参考：
> https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/paddleocr_vl_sft.md
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/PaddlePaddle/ERNIE/issues/1396#issuecomment-3721584456>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/BIAPQF3XQFYFVNR6E6FKMQ34FW3VVAVCNFSM6AAAAACOLDGYS2VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTOMRRGU4DINBVGY>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


### nepeplwu · 2026-01-08

@adoresever 感谢~

### hustzxl · 2026-01-22

> 您好，表格一般我们建议使用PPOCRLabel标注，这里有标注的教程。标注完成后会保留html格式的表格。使用脚本将HTML格式转化为OTSL格式即可。https://github.com/PaddlePaddle/PaddleX/blob/18e94f852749b27e2e70abfd3a646d1ddccee478/docs/data_annotations/ocr_modules/table_recognition.md 脚本如下：
> 
> [html_to_otsl.py](https://github.com/user-attachments/files/24203712/html_to_otsl.py)
> 
> 另外表格微调案例在准备中，ready后会发布，感谢您的持续关注。

请问微调的话大概需要多少数据。目前2000多张微调 性能反而下降了，可以有那些建议

### Sunting78 · 2026-01-26

您好， 性能下降您是指表格性能还是其他任务的能力呢？如果希望也保持其他任务的能力比如ocr和公式识别，建议也适当为其他任务加一定的数据进行混合任务的微调。
另外2000张表格是结构比较相似的吗？vlm模型的训练数据建议最好不少于几万的量级，如果没有那么大标注量，也可以考虑合成相似的表格数据来进行训练。

### zodiac50 · 2026-02-11

> 您好， 性能下降您是指表格性能还是其他任务的能力呢？如果希望也保持其他任务的能力比如ocr和公式识别，建议也适当为其他任务加一定的数据进行混合任务的微调。 另外2000张表格是结构比较相似的吗？vlm模型的训练数据建议最好不少于几万的量级，如果没有那么大标注量，也可以考虑合成相似的表格数据来进行训练。

我也遇到了类似的情形，PaddleOCR-VL-1.5，基于5800多张表格识别训练数据，进行sft后，性能也下降了，主要的问题显示在一些符号和数值的数字上，请问这种情形的话，是需要继续增大数据量级么，还是考虑做强化学习，或者说其他策略呢？

### zodiac50 · 2026-02-11

> > 您好， 性能下降您是指表格性能还是其他任务的能力呢？如果希望也保持其他任务的能力比如ocr和公式识别，建议也适当为其他任务加一定的数据进行混合任务的微调。 另外2000张表格是结构比较相似的吗？vlm模型的训练数据建议最好不少于几万的量级，如果没有那么大标注量，也可以考虑合成相似的表格数据来进行训练。
> 
> 我也遇到了类似的情形，PaddleOCR-VL-1.5，基于5800多张表格识别训练数据，进行sft后，性能也下降了，主要的问题显示在一些符号和数值的数字上，请问这种情形的话，是需要继续增大数据量级么，还是考虑做强化学习，或者说其他策略呢？

只针对的表格性能

### Sunting78 · 2026-02-24

您提到的表格性能下降的类型（符号和数字），在5800训练集合里面这种训练数据存在吗？ 如果针对特定场景的表格，保障特定场景的表格数据训练集合都能覆盖就可以，特定场景下表格类型比较固定数据量在万级即可，可以看下您提到的符号和数字在训练集合里面是否存在，不存在进行添加这类型的数据进行训练。如果想满足通用的表格场景，那么数量级就会比较大了，建议用几十万甚至百万量级的分布类型和丰富度都比较高的训练数据。



### WiwilZ · 2026-06-06

如果单元格中有OTSL的结构标签字符该怎么转义呢

### 1flyingpig · 2026-08-01

> 我已经实现啦，帮你们录了一个视频
> […](#)
请问能分享一下吗
