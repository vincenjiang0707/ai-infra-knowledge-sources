# [Issue #5] E19010 error code when trying to convert onnx model to offline model with atc.

source: https://github.com/Ascend/samples/issues/5
state: closed | updated: 2022-04-20T19:38:10Z
labels: 

## 正文

Downloaded your samples from samples/cplusplus/level1_single_api/4_op_dev/1_custom_op.
Get Add(Just changed name in onnx plugin from ai.onnx::11::Add to ai.onnx::11::AddCust, https://pastebin.com/82u5t0TD) builded on Ascend310 with default sample script(just changed ASCEND_OPP_PATH and other env to my toolkit), install it. After that I did onnx model with code like this(https://pastebin.com/FF5XWuNV). Then tried to convert onnx model to om model with this script(https://pastebin.com/iaZJiZEq). It failed with that error:
![image](https://user-images.githubusercontent.com/47770844/156731335-797ef17b-610c-4f86-9644-700a4b047bed.png)


## 评论 (1)

### ascendhuawei · 2022-03-04

Hi, 
As explained in the sample Readme of samples/cplusplus/level1_single_api/4_op_dev/1_custom_op, the sample is for Caffe/Tensorflow. For onnx, it might not work directly. From your error message, it seems something wrong with the plugin/parser, please refer to https://support.huaweicloud.com/intl/en-us/tbedevg-cann504alpha1infer/atlaste_10_0077.html 

