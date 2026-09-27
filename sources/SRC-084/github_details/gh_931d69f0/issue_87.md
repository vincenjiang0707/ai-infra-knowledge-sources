# [Issue #87] Group_Size setting

source: https://github.com/dropbox/hqq/issues/87
state: closed | updated: 2024-06-26T07:04:04Z
labels: 

## 正文

Hello, I have a question about the group_size. In a high level, it seems the larger the group size, the lower the accuracy of the quantized model. But is this true in real? Let's say we have a 4096by4096 weight matrix, if we could set the group size to 4096, then all the elements in 1 row or 1 column can share the same zero point and scale, then this becomes row/column-wise quantization. Does hqq support such a large group size? Or if not, what is the usual group size of hqq? Thanks!

## 评论 (1)

### mobicham · 2024-06-26

Hi! Yes, for row/column-wise group-sizes you can just set `group_size=None`: https://github.com/mobiusml/hqq/blob/master/examples/backends/marlin_int4_demo.py#L22 , this should work for both the torchao and the marlin backned.
You need a lower group-size to get usable quantized models, especially at lower bits. I recommend you simply use a group-size of 64 which is a good balance between performance and vram.
