# [Issue #106] 编译安装的时候报错：FileNotFoundError-v2r6/op_plugin_functions.yaml

source: https://github.com/Ascend/pytorch/issues/106
state: open | updated: 2026-02-13T01:30:52Z
labels: 

## 正文

当我使用分支 pytorch-7.3.0-pytorch2.6.0，进行编译安装的时候` bash ci/build.sh --python=3.11` 会出现如下的报错。

```
FileNotFoundError: [Errno 2] No such file or directory: 'pytorch/third_party/op-plugin/op_plugin/config/v2r6//op_plugin_functions.yaml

FileNotFoundError: [Errno 2] No such file or directory: 'pytorch/third_party/op-plugin/op_plugin/config/v2r6/derivatives.yaml

```

请问如何解决？

## 评论 (1)

### yunyiyun · 2026-02-13

看下编译过程中是否有其他报错，或者使用干净的环境重新编译下，注意使用推荐的编译环境，防止编译环境差异带来问题
https://www.hiascend.com/document/detail/zh/Pytorch/730/configandinstg/instg/docs/zh/installation_guide/compilation_installation_using_source_code.md
