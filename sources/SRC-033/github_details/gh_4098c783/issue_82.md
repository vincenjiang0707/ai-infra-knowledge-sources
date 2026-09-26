# [Issue #82] torch_npu的日志会输出在哪个路径？

source: https://github.com/Ascend/pytorch/issues/82
state: open | updated: 2025-09-04T06:37:05Z
labels: 

## 正文

torch_npu的日志会输出在哪个路径？需要查看OpParmaMaker.cpp 中ASCEND_LOGD("Op %s Run.", opName.c_str());的日志输出

## 评论 (1)

### yunyiyun · 2025-09-04

默认可在“$HOME/ascend/log/debug/plog”下查看
详细可参考 https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/maintenref/logreference/logreference_0002.html
