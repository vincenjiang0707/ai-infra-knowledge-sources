# [Issue #1364] ERNIE-4.5-VL-28B-A3B-Thinking坐标框还原问题

source: https://github.com/PaddlePaddle/ERNIE/issues/1364
state: closed | updated: 2026-03-02T12:01:57Z
labels: 

## 正文

您好！感谢paddle团队做的这么好的多模态大模型。
目前我有个疑问就是坐标框的还原问题，比如我想让大模型检测图片所有文字，并定位出来，我的prompt是:
'''把图中的文字抽取出来,并给出每个文字块的坐标,格式为一个json:{"res":[{'text':'***文字内容1***', 'pos':[x1,y1,x2,y2]]},{'text':'***文字内容2***', 'pos':[x1,y1,x2,y2]]}, ...]}\n\n其中x1,y1是文字框左上角点坐标,x2,y2是文字框右下角点坐标"}}'''

我是按qwen3vl的方法，qwen3vl还原是用"输出的相对位置/1000*原始宽高计算"的
x1 = int(x1 / 1000 * width_original)
y1 = int(y1 / 1000 * height_original)
x2 = int(x2 / 1000 * width_original)
y2 = int(y2 / 1000 * height_original)

下图是ERNIE-4.5-VL-28B-A3B还原效果的例子：
<img width="1075" height="620" alt="Image" src="https://github.com/user-attachments/assets/3b899989-3b5d-429e-a1db-1ead21e9f09c" />
虽然能部分还原，但还原效果不太好。请问ERNIE-4.5-VL是如何归一化模型的bbox输出的呢？


## 评论 (2)

### dongZheX · 2025-12-01

您好！感谢您对ERNIE-4.5-VL-28B-A3B-Thinking模型的关注和使用。
关于坐标框还原的问题，ERNIE-4.5-VL-28B-A3B-Thinking的bbox归一化方法与Qwen3-VL
是一致的，都是采用相对坐标系统，即：
```
x1 = int(x1 / 1000 * width_original)
y1 = int(y1 / 1000 * height_original)
x2 = int(x2 / 1000 * width_original)
y2 = int(y2 / 1000 * height_original)
```
您提到的还原效果问题我们已经注意到了。目前在一些复杂场景下（如文字密集、多方向文
字、复杂排版等)，模型的定位精度确实还有优化空间。我们团队正在持续改进模型在这些场
景下的表现，后续版本会进一步提升复杂场景下的检测和定位准确性。

### nepeplwu · 2026-03-02

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
