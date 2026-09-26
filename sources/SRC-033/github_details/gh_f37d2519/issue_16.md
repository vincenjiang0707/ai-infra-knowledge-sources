# [Issue #16] [ERROR]  acl set device 0 failed, errorCode = 507033

source: https://github.com/Ascend/samples/issues/16
state: open | updated: 2025-09-12T06:28:29Z
labels: 

## 正文

环境：麒麟V10 桌面版 + Atlas 200 EP模式
合设环境下
跑这个样例报错，请问是什么原因？
log：
[INFO]  acl init success
[ERROR]  acl set device 0 failed, errorCode = 507033
[ERROR]  sample init resource failed
[INFO]  end to destroy stream
[INFO]  end to destroy context
[ERROR]  reset device 0 failed, errorCode = 507007
[INFO]  end to reset device 0
[INFO]  end to finalize acl
root@senfetech-pc:/usr/local/samples/cplusplus/level2_simple_inference/1_classification/resnet50_imagenet_classification/out# 
root@senfetech-pc:/usr/local/samples/cplusplus/level2_simple_inference/1_classification/resnet50_imagenet_classification/out# dmesg 
[ 2081.843939] [ascend] [devmm] [devmm_alloc_svm_proc_set_to_file 662] <main:42394,42394> Devmm_set_porcess details. (status=0; proc_idx=3)
[ 2081.844043] [ascend] [devmm] [devmm_svm_release_proc 617] <davinci_recycle:42400,42400> Devmm release create work. (hostpid=-1)
[ 2081.844051] [ascend] [davinci_intf] [drv_davinci_intf_sub_call_release 348] <davinci_recycle:42400> Release module success. (module_name="SVM"; pid=42394)
[ 2081.844061] [ascend] [devmm] [devmm_svm_release_private_proc 2270] <kworker/1:1:38608,38608> Device process exited. (hostpid=-1; times=0)
[ 2081.844066] [ascend] [devmm] [devmm_destory_all_heap_by_proc 1222] <kworker/1:1:38608,38608> Page statistics. (hostpid=-1; alloc_page_cnt=0; free_page_cnt=0; alloc_hugepage_cnt=0; free_huge_page_cnt=0)
[ 2081.844077] [ascend] [devmm] [devmm_free_svm_proc 276] <kworker/1:1:38608,38608> Devmm_free_process details. (hostpid=-1; devid=64; vfid=32; devpid=4294967295; status=0; pro_idx=3)
[ 2082.037305] [ascend] [davinci_intf] [drv_davinci_intf_sub_call_release 348] <davinci_recycle:42401> Release module success. (module_name="DMS"; pid=42394)
[ 2082.037311] [ascend] [devdrv] [devdrv_manager_process_sign_release 797] <main:42394> end devdrv_get_process_sign, count = 0, docker_id = 128



## 评论 (1)

### hazhenyu · 2025-09-12

遇到了同样的问题，请问您解决了吗
