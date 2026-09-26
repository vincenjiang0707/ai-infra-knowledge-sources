source: https://docs.mthreads.com/cloud-native/cloud-native-doc-online/faq

# 帮助（FAQ）

## 常见问题及解决方法[](https://docs.mthreads.com#常见问题及解决方法)

### 1. 通过 GPU Operator 安装驱动失败[](https://docs.mthreads.com#1-通过-gpu-operator-安装驱动失败)

当驱动安装失败后，可以查看驱动升级的相关事件：

`$ kubectl get events --sort-by='.lastTimestamp' | grep DriverUpgrade`

...

5m28s Normal DriverUpgrade nodeconfig/node-1 (combined from similar events): Successfully updated nodeconfig state label to ValidateNode

5m19s Warning DriverUpgrade nodeconfig/node-1 Failed to update nodeconfig state label to UpgradeFailed err: timed out waiting for the condition

4m28s Normal DriverUpgrade nodeconfig/node-1 Successfully updated nodeconfig state label to WaitForJobsRequired

79s Normal DriverUpgrade nodeconfig/node-1 Successfully updated nodeconfig state label to InstallDone

29s Normal DriverUpgrade nodeconfig/node-2 Successfully updated nodeconfig state label to InstallDone

...



你也可以单独查看某一个节点上驱动安装事件：

`$ kubectl describe nodeconfig <node-name>`

...

Events:

Type Reason Age From Message

---- ------ ---- ---- -------

Warning DriverUpgrade 12s mt-gpu-operator 2024-01-19 03:29:06: failed reason: timed out waiting for the condition

Normal DriverUpgrade 12s mt-gpu-operator 2024-01-19 03:29:06: disable mt-gpu-operator deploy label successfully, node: yuzhou-system-product-name

Normal DriverUpgrade 12s mt-gpu-operator 2024-01-19 03:29:06: Successfully drained the node

Normal DriverInstall 12s mt-gpu-operator 2024-01-19 03:29:06: Success to clear gpu



### 2. GPU Operator 升级驱动失败[](https://docs.mthreads.com#2-gpu-operator-升级驱动失败)

用户可以通过查看 `mt-controller-manager`

日志来定位问题：

`kubectl logs mt-controller-manager-xxx-xxx | grep controllers.NodeConfig `



在解决升级失败问题后，可以通过将 NodeConfig 标签设置为升级所需的状态来继续升级过程。

### 3. 使用 GPU Operator 后，Kubernetes 节点卡在 RebootNodeRequired 状态[](https://docs.mthreads.com#3-使用-gpu-operator-后kubernetes-节点卡在-rebootnoderequired-状态)

如果节点长时间卡在 `RebootNodeRequired`

状态：

`$ kubectl get nodeconfig`

node-1 RebootNodeRequired



可能是由 Kured 导致的问题。在重启节点之前，Kured 会尝试驱逐节点上的负载，但这一步骤可能会失败。用户可以通过查看节点上的注解和标签来确定 Kured 是否卡在驱逐阶段：

`$ kubectl describe node <node-name> | grep reboot`

mthreads.com/node-need-reboot=true

weave.works/kured-most-recent-reboot-needed: 2024-01-18T04:58:47Z

weave.works/kured-reboot-in-progress: 2024-01-18T04:58:47Z



这些标签和注解是由 Kured 创建的：

`mthreads.com/node-need-reboot=true`

：表示节点需要重启。`weave.works/kured-most-recent-reboot-needed: 2024-01-18T04:58:47Z`

：表示上一次由 Kured 触发节点重启的时间。`weave.works/kured-reboot-in-progress: 2024-01-18T04:58:47Z`

：表示当前 Kured 正在处理节点，可能正在驱逐节点上的负载。

若希望在 Kured 驱逐失败时强制重启节点，在 ClusterPolicy 中添加 Kured 强制重启的参数：

` kured:`

enabled: true

args:

...

- --force-reboot=true



### 4. DCGM Exporter 启动后没有指标[](https://docs.mthreads.com#4-dcgm-exporter-启动后没有指标)

检查 mt-hostengine 是否正常运行：

`curl localhost:5555/health # 远程模式`

# 或检查容器日志

docker logs dcgm-exporter



### 5. DCGM Exporter 输出 "unsupported feature" 警告[](https://docs.mthreads.com#5-dcgm-exporter-输出-unsupported-feature-警告)

摩尔线程 GPU 的部分 DCGM 特性（如 NvLink、ECC）与 NVIDIA 不同，这些警告已降级为 Debug 级别。

### 6. DCGM Exporter 如何修改采集间隔[](https://docs.mthreads.com#6-dcgm-exporter-如何修改采集间隔)

通过命令行或环境变量：

`# 命令行`

dcgm-exporter -c 5000 # 5 秒


# 环境变量

DCGM_EXPORTER_INTERVAL=5000 dcgm-exporter