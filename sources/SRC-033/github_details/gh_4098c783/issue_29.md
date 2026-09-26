# [Issue #29] pytorch_npu-2.1 可以推理，训练出错，tbe.common无法加载

source: https://github.com/Ascend/pytorch/issues/29
state: open | updated: 2025-08-27T08:28:08Z
labels: 

## 正文

1. torch_npu可正常加载计算，测试代码如下：

import torch
import torch_npu

x = torch.randn(2, 2).npu()
y = torch.randn(2, 2).npu()
z = x.mm(y)
print(z)

tensor([[-0.1196,  0.2381],
        [-0.4408,  0.6469]], device='npu:0')

2. 可正常加载大模型，并进行推理
3. 进行lora 微调时，报错如下：

[TRACE] GE(2440326,python):2024-04-08-15:18:42.280.217 [status:INIT] [ge_api.cc:208]2440326 GEInitializeImpl:GEInitialize start
[TRACE] GE(2440326,python):2024-04-08-15:18:42.590.702 [status:RUNNING] [ge_api.cc:276]2440326 GEInitializeImpl:Initializing environment
[ERROR] TUNE(2440326,python):2024-04-08-15:18:43.444.270 [pywrapper.cpp:94][CANNKB][Tid:2440326]"ModuleNotFoundError: No module named 'tbe.common'
"
[ERROR] TUNE(2440326,python):2024-04-08-15:18:43.444.523 [cann_kb_pyfunc_mgr.cpp:98][CANNKB][Tid:2440326]"PyObjectInit: Import repository_manager_log error"
[ERROR] TUNE(2440326,python):2024-04-08-15:18:43.444.535 [py_interface.cpp:28][CANNKB][Tid:2440326]"PyObjectInit of CannKbPyfuncMgr Error!"
[ERROR] TUNE(2440326,python):2024-04-08-15:18:43.444.539 [cann_kb_api.cpp:24][CANNKB][Tid:2440326]"Run PyInterfaceInit Error!"
[ERROR] TEFUSION(2440326,python):2024-04-08-15:18:43.444.546 [fusion_manager.cc:660]2440326 InitCannKB call CannKbInit failed. res = [3]. init params: [Ascend910B2, 24, ].
[ERROR] TEFUSION(2440326,python):2024-04-08-15:18:43.444.552 [fusion_manager.cc:497]2440326 TbeInit Failed to call InitCannKB.
[ERROR] TEFUSION(2440326,python):2024-04-08-15:18:43.444.585 [fusion_api.cc:78]2440326 TbeInitialize failed to initialize tbe.
[ERROR] FE(2440326,python):2024-04-08-15:18:43.444.623 [tbe_op_store_adapter.cc:1623]2440326 InitializeInner:"[GraphOpt][InitializeInner][InitTbeFunc] Failed to init tbe."
[ERROR] FE(2440326,python):2024-04-08-15:18:43.444.648 [op_store_adapter_manager.cc:85]2440326 InitializeAdapter:"[SubGraphOpt][PreCompileOp][InitAdapter] InitializeAdapter adapter [tbe_op_adapter] failed! Ret [4294967295]"
[ERROR] FE(2440326,python):2024-04-08-15:18:43.444.712 [op_store_adapter_manager.cc:126]2440326 Initialize:"[SubGraphOpt][PreCompileOp][Init] Initialize op store adapter failed, OpsStoreName[tbe-custom]."
[ERROR] FE(2440326,python):2024-04-08-15:18:43.444.728 [fusion_manager.cc:124]2440326 Initialize:"[FusionMngr][Init] Op store adapter manager init failed."
[ERROR] GE(2440326,python):2024-04-08-15:18:43.444.808 [ops_kernel_manager.cc:95]2440326 Initialize: ErrorNo: 1343250441(There is no valid so about OpsKernelInfoStore or GraphOptimizer.) [INIT][OPS_KER][Invoke][OpsKernelInfo]PluginManager InvokeAll failed.
[ERROR] GE(2440326,python):2024-04-08-15:18:43.444.834 [gelib.cc:236]2440326 InnerInitialize: ErrorNo: 1343250441(There is no valid so about OpsKernelInfoStore or GraphOptimizer.) [INIT][OPS_KER][Init][OpsManager]GE ops manager initial failed.
[ERROR] GE(2440326,python):2024-04-08-15:18:43.456.811 [gelib.cc:164]2440326 Initialize: ErrorNo: 1343250441(There is no valid so about OpsKernelInfoStore or GraphOptimizer.) [INIT][OPS_KER][Init][GeLib]GeLib initial failed.
[ERROR] GE(2440326,python):2024-04-08-15:18:43.456.850 [ge_api.cc:282]2440326 GEInitializeImpl: ErrorNo: 1343229953(GEInitialize Failed.) [INIT][OPS_KER][Init][GELib]Failed, error code = 1343250441
[ERROR] ASCENDCL(2440326,python):2024-04-08-15:18:43.456.865 [local_compiler.cpp:76]2440326 Init: [INIT][OPS_KER][Initialize][Ge]GEInitialize failed. ge result = 4294967295
[ERROR] ASCENDCL(2440326,python):2024-04-08-15:18:43.456.895 [op_compile_service.cpp:73]2440326 SetCompileStrategy: [INIT][OPS_KER][Init][Compiler]Init compiler failed
[ERROR] ASCENDCL(2440326,python):2024-04-08-15:18:43.456.913 [op_compile_processor.cpp:67]2440326 Init: [INIT][OPS_KER][Set][Options]OpCompileProcessor init failed!

## 评论 (9)

### yunyiyun · 2024-04-08

请确认下cann是否正常安装，一般出现这种情况的原因是cann安装的不正确

### sly123197811 · 2024-04-08

> 请确认下cann是否正常安装，一般出现这种情况的原因是cann安装的不正确

您好，cat ascend_toolkit_install^@.info，信息如下：
package_name=Ascend-cann-toolkit
version=7.0.0.alpha003
innerversion=V100R001C77B220SPC008
compatible_version=[V100R001C80,V100R001C84],[V100R001C77,V100R001C79],[V100R001C29],[V100R001C11,V100R001C50]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/7.0.0.alpha003/aarch64-linux
^@
另外，目前我的环境可以使用glm3进行推理，基础环境为：python3.10，torch2.1，torch_npu2.1

不知道这样能否代表cann已经正常安装，请教一下，有没有什么方法可以判断cann是否是正常安装的？

### yunyiyun · 2024-04-09

出现这种问题一般为你的python环境和cann环境不匹配，建议你参考社区资料重新安装cann包。
同时你可以python进入解释器import tbe.common看下是否正常。

### sly123197811 · 2024-04-09

> 出现这种问题一般为你的python环境和cann环境不匹配，建议你参考社区资料重新安装cann包。 同时你可以python进入解释器import tbe.common看下是否正常。

谢谢，问题解决了，确实是python版本的问题。
另外，由于服务器是多用户的，以下这个警告是否影响训练过程
/home/cnki/miniconda3/envs/cann/lib/python3.9/site-packages/torch_npu/utils/path_manager.py:77: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current user.


### yunyiyun · 2024-04-09

一般没有影响，但是还是建议安装和使用是同一个用户



### zuoyanzhang · 2024-11-20

> > 出现这种问题一般为你的python环境和cann环境不匹配，建议你参考社区资料重新安装cann包。 同时你可以python进入解释器import tbe.common看下是否正常。
> 
> 谢谢，问题解决了，确实是python版本的问题。 另外，由于服务器是多用户的，以下这个警告是否影响训练过程 /home/cnki/miniconda3/envs/cann/lib/python3.9/site-packages/torch_npu/utils/path_manager.py:77: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current user.

请问python version版本号是多少，我也遇到这个问题了，我现在是python3.9.11,cann version是8.0.RC3.beta1

### zlianzhuang · 2024-11-26

PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:

### WeiHea · 2024-12-18

> > 出现这种问题一般为你的python环境和cann环境不匹配，建议你参考社区资料重新安装cann包。 同时你可以python进入解释器import tbe.common看下是否正常。
> 
> 谢谢，问题解决了，确实是python版本的问题。 另外，由于服务器是多用户的，以下这个警告是否影响训练过程 /home/cnki/miniconda3/envs/cann/lib/python3.9/site-packages/torch_npu/utils/path_manager.py:77: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current user.

同出现该问题，请问该问题是否有解决。以及是否影响模型的训练

### hz920120 · 2025-08-27

> PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:

pycharm中加入该环境变量，已解决
