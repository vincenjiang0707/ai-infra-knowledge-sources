# [Issue #1435] paddleocr-vl，SFT数据准备

source: https://github.com/PaddlePaddle/ERNIE/issues/1435
state: open | updated: 2026-02-09T11:59:57Z
labels: 

## 正文

<img width="799" height="238" alt="Image" src="https://github.com/user-attachments/assets/81e87724-2d28-4d9a-afaa-80e79921d05a" />

<img width="463" height="573" alt="Image" src="https://github.com/user-attachments/assets/f7eb19f2-340c-4f10-ba10-122b00827028" />

<img width="621" height="652" alt="Image" src="https://github.com/user-attachments/assets/eab03d4f-da6b-4ba6-a0ba-c1372ff80e5c" />

image图像应该采用整图的裁切还是应该给整图，如果图像里面是纯文本的情况，如果图像里面有表格有图片有文本呢



## 评论 (1)

### Sunting78 · 2026-02-09

原始模型的训练是基于切分的图，不是整图，如果整图的结果微调也可以，加一个全图文档解析的指令。如果希望裁剪图片可以用PP-DocLayoutV2模型进行推理，得到的结果文件是包含坐标以及类型的，根据坐标裁剪子图就可以了。
