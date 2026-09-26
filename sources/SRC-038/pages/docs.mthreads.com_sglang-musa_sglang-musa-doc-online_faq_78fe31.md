source: https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/faq

# FAQ

## 启动router失败[](https://docs.mthreads.com#启动router失败)

router需要检查prefill和decoder的health，必须都有返回

如果下面打印完这一步不打印了，则手工检查prefill和decoder的health

`2025-10-15 10:45:11 INFO sglang_router_rs::server: src/server.rs:561: Starting router on 0.0.0.0:31000 | mode: PrefillDecode { prefill_urls: [("http://10.202.5.87:30000", None)], decode_urls: ["http://10.202.5.42:30000"], prefill_policy: None, decode_policy: None } | policy: CacheAware { cache_threshold: 0.3, balance_abs_threshold: 64, balance_rel_threshold: 1.5, eviction_interval_secs: 120, max_tree_size: 67108864 } | max_payload: 512MB`

2025-10-15 10:45:11 INFO sglang_router_rs::server: src/server.rs:662: Single router mode (enable_igw=false)

2025-10-15 10:45:11 INFO sglang_router_rs::routers::http::router: src/routers/http/router.rs:202: Waiting for 2 workers to become healthy (timeout: 600s)



**检查health**

`# IP换为PD的主节点IP的端口`

curl http://10.202.5.27:30000/health

curl http://10.202.5.38:30000/health

#如��果不能正常访问则说明有问题 同时检查没有正常结束的节点日志有没有打印报错日志

# 日志可能如下

[2025-10-15 10:47:27] Health check failed. Server couldn't get a response from detokenizer for last 20 seconds. tic start time: 10:47:07. last_heartbeat time: 09:44:42



这种情况说明 detokenizer 服务未启动，重启整个服务即可解决。

如果 Router 显示 "Timeout 600s waiting for workers [xxxxxx] to become healthy"，而 Prefill 和 Decode Server 可以正常访问，则是启动太慢导致 Router 健康检查超时，请单独重启 Router。

## PD分离 RDMA 注册失败[](https://docs.mthreads.com#pd分离-rdma-注册失败)

首先检查驱动配置有无输出5555。以及mt-peermem是否安装。

`# 检查KMD配置`

cat /sys/module/mtgpu/parameters/tp_pci_vender_id

# 结果应输出5555


# 检查mt_peermem是否安装

lsmod | grep mt_peermem

# 正常结果显示类似以下内容

# mt_peermem 16384 0

# mtgpu 4210688 17 mt_peermem

# ib_core 401408 9 rdma_cm,ib_ipoib,mt_peermem,iw_cm,ib_umad,rdma_ucm,ib_uverbs,mlx5_ib,ib_cm



## decode节点启动报错 Segmentation fault[](https://docs.mthreads.com#decode节点启动报错-segmentation-fault)

在卸载驱动后，mtgpu.conf文件的配置会被清除，导致部署decode节点时会出现如下报错：

`musa failed with an illegal memory access was encountered`

Fatal Python error: Segmentation fault



只需重新添加mtgpu.conf文件即可解决。

## triton 算子不匹配[](https://docs.mthreads.com#triton-算子不匹配)

`torch._dynamo.exc.BackendCompilerFailed: backend='inductor' raised:`

TypeError: AttrsDescriptor.__init__() got an unexpected keyword argument 'divisible_by_16'


Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"


[2026-05-27 18:34:22] Scheduler or DataParallelController 1880936 terminated with -3



一般发生在重装triton后，清理缓存即可：

`rm -rf ~/.triton/cache/ && rm -rf /tmp/*`



## DEEPEP_MODE=low_latency 模式异常[](https://docs.mthreads.com#deepep_modelow_latency-模式异常)

若出现以下错误：

`init failed for transport: IBGDA`

`illegal memory access`

`Segmentation fault`


建议处理顺序：

- 先切换 Decode 配置
`DEEPEP_MODE=normal`

，重启服务恢复在线。 - 参考
[GPU 内核模块参数配置](https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/environment_setup)是否已写入,`modinfo mtgpu`

参数是否匹配。 - 参考
[RDMA 网卡检测](https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/environment_setup)，检查`--disaggregation-ib-device`

与`ibdev2netdev`

是否一致。 - 再按需开启
`DEEPEP_MODE=low_latency`

并做小流量验证。

## MCCL bootstrap/connect 错误[](https://docs.mthreads.com#mccl-bootstrapconnect-错误)

`Bootstrap: no socket interface found / cannot connect / Connection refused / Network is unreachable`

`Transport NetSocket: connection failed / timeout`


因为 MCCL 在 bootstrap/控制面阶段需要用一个 Socket 接口做节��点间握手与通信。当机器存在多网卡，或进程跑在容器/K8s overlay 网络里时，自动探测可能选中"有 IP 但不可达对端节点"的接口，于是建连失败或直接 hang。建议参考[业务网络网卡检测](https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/environment_setup)在启动容器或在部署脚本中显式设置环境变量：
`export MCCL_SOCKET_IFNAME=bond0`


如果 MCCL INFO 显示 `NET/IB : No Device found.`

，请联系技术支持确定网卡是否和软件已做好适配。

## mtshmem failed 导致 deep ep dispatch报错[](https://docs.mthreads.com#mtshmem-failed-导致-deep-ep-dispatch报错)

服务日志显示 `mtshmem failed to open shared memory slab`

，导致后面在执行到deep ep的时候dispatch报错。

可在 Prefill 和 Decode 启动脚本中加上 `NVSHMEM_DEBUG=INFO`

`NVSHMEM_DEBUG_SUBSYS=ALL`

两个环境变量。如果 NVSHMEM INFO 日志中（ `host name：xxxx hash xxxxxxxxxx`

），不同机器的 host hash 完全一致，则会导致MPI等工具无法用，mtshmem比mccl先启动，如果mccl启动也会报一样的错。联系运维把 host name 配成不一样的值。

## 启动模型报错 `MUSA dense GEMV autotune profiler returned no GPU kernel time`

[](https://docs.mthreads.com#启动模型报错-musa-dense-gemv-autotune-profiler-returned-no-gpu-kernel-time)

SGLang 在启动部分模型时，默认会对 MUSA 后端的密集矩阵乘法（GEMV/GEMM）进行 autotune（自动调优），调优器（profiler）在子进程中执行测试内核。而当容器以特权模式启动时，其权限或环境状态导致 MUSA 后端的内核探测失败。对于单机可拉起模型，可删除容器的 --privileged 参数重启。

## 多模态模型处理视频文件时报错 502[](https://docs.mthreads.com#多模态模型处理视频文件时报错-502)

推理镜像缺少解码和抽帧的 decord 组件，需要在容器环境中 `pip install decord`

。

## PD 分离部署 mooncake session 和 kvcache 传输异常[](https://docs.mthreads.com#pd-分离部署-mooncake-session-和-kvcache-传输异常)

Prefill / Decode 进程存活，HTTP /health 正常，Mooncake 端口正常。但 prefill 端报错 `remote mooncake session is not alive`

，decode 端报错 `Failed to get kvcache from prefill instance, it might be dead`

。

从日志查查看，如果 Mooncake Transfer Engine 吞吐长期低于 GB/s 级别，则是网络传输问题。需确保各节点在同一个 RDMA 网段，如果已在同一网段，需运维侧定位是否有网络设备故障，或者