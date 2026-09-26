# [Issue #95] 捕图stream占用过多

source: https://github.com/Ascend/pytorch/issues/95
state: open | updated: 2026-01-06T02:11:55Z
labels: 

## 正文

问题描述：捕图的update_stream为类变量，本意是大家都使用同一个stream。但__init__时使用的是self.update_stream，而非cls.update_stream，导致实际上每个对象都使用了不同stream。在捕图的不同batch_size过多时，就会导致使用大量的流，从而已经导致了多个现网问题。
<img width="816" height="190" alt="Image" src="https://github.com/user-attachments/assets/7d5e73ae-bdfa-4c4a-83d5-4b0698ece694" />

解决方案：整个类使用同一个update_stream，如下图所示：

<img width="812" height="262" alt="Image" src="https://github.com/user-attachments/assets/6b180038-9516-4c3e-8a2b-e9bc734dc5ae" />


## 评论 (1)

### yunyiyun · 2026-01-06

感谢您的反馈，该问题已在最新版本修复
