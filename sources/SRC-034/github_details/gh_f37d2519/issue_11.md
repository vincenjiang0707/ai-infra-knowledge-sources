# [Issue #11] 在310P的环境上跑不起来，生成算子失败

source: https://github.com/Ascend/samples/issues/11
state: closed | updated: 2023-07-13T17:38:01Z
labels: 

## 正文

【环境】
**toolkit版本**：
runtime_running_version=[1.84.15.1.310:6.0.1]
compiler_running_version=[1.84.15.1.310:6.0.1]
opp_running_version=[1.84.15.1.310:6.0.1]
toolkit_running_version=[1.84.15.1.310:6.0.1]
aoe_running_version=[1.84.15.1.310:6.0.1]
ncs_running_version=[1.84.15.1.310:6.0.1]
runtime_upgrade_version=[1.84.15.1.310:6.0.1]
compiler_upgrade_version=[1.84.15.1.310:6.0.1]
opp_upgrade_version=[1.84.15.1.310:6.0.1]
toolkit_upgrade_version=[1.84.15.1.310:6.0.1]
aoe_upgrade_version=[1.84.15.1.310:6.0.1]
ncs_upgrade_version=[1.84.15.1.310:6.0.1]
runtime_installed_version=[1.84.15.1.310:6.0.1]
compiler_installed_version=[1.84.15.1.310:6.0.1]
opp_installed_version=[1.84.15.1.310:6.0.1]
toolkit_installed_version=[1.84.15.1.310:6.0.1]
aoe_installed_version=[1.84.15.1.310:6.0.1]
ncs_installed_version=[1.84.15.1.310:6.0.1]
**驱动版本**：23.0.rc2.b020
**芯片**：310P3
**问题描述**：
按照samples/cplusplus/level1_single_api/4_op_dev/2_verify_op/acl_execute_add/README_CN.md设置好所有环境变量。
在目录samples/cplusplus/level1_single_api/4_op_dev/2_verify_op/acl_execute_add/run/out下运行生成算子的命令：atc  --singleop=test_data/config/add_op.json --soc_version=Ascend310P3 --output=op_models
生成算子失败，报错信息如下：
ATC start working now, please wait for a moment.
ATC run failed, Please check the detail log, Try 'atc --help' for more information
EZ3003: No supported Ops kernel and engine are found for [AddDsl], optype [AddDsl].
        Possible Cause: The operator is not supported by the system. Therefore, no hit is found in any operator information library.
        Solution: 1. Check that the OPP component is installed properly. 2. Submit an issue to request for the support of this operator type.
        TraceBack (most recent call last):
        build graph failed, graph id:0, ret:-1[FUNC:BuildModel][FILE:ge_generator.cc][LINE:148

## 评论 (1)

### ascendhuawei · 2023-07-13

您好，算子问题请统一到gitee平台提问，https://gitee.com/Ascend/samples/
