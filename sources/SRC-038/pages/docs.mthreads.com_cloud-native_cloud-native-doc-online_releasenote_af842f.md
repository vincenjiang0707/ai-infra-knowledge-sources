source: https://docs.mthreads.com/cloud-native/cloud-native-doc-online/releasenote

# KUAE 云原生套件 v2.2.0 发布说明

KUAE 云原生套件的[下载地址](https://developer.mthreads.com/sdk/download/CloudNative?equipment=&os=&driverVersion=&version=)

## 产品组件说明[](https://docs.mthreads.com#产品组件说明)

**重要组件及版本**

| 组件名称 | 版本 |
|---|---|
| MT Container Toolkit | 2.2.0 |
| MT GPU Operator / Device Plugin | 2.2.0 |
| MT DCGM Exporter | 1.1.7 |
| MT sGPU | 1.3.0 |

**安装包文件说明**

| 组件名称 | 组件说明 |
|---|---|
| Container-Toolkit/deb/mt-container-toolkit_2.2.0-1_amd64.deb | MT GPU 容器运行时 deb安装包 |
| Container-Toolkit/deb/sgpu-dkms_1.3.0_amd64.deb | MT sGPU 驱动程序 deb 安装包 |
| Container-Toolkit/rpm/mt-container-toolkit-2.2.0-1.x86_64.rpm | MT GPU 容器运行时 rpm安装包 |
| Container-Toolkit/rpm/sgpu-dkms-1.3.0-1.el8.x86_64.rpm | MT sGPU 驱动程序 rpm 安装包 |
| GPU-Operator/gpu-operator-core/dcgm-metrics-config.yaml | dcgm 默认指标配置文件 |
| GPU-Operator/gpu-operator-core/deployments.yaml | gpu-operator core yaml文件 |
| GPU-Operator/gpu-operator-full/mt-gpu-operator-2.2.0.tgz | MT GPU Operator 软件包 |
| GPU-Operator/gpu-operator-full/mt-gpu-operator-custom-resources-2.2.0.tgz | MT GPU Operator Custom Resources 包 |
| GPU-Operator/gpu-operator-full/mt-gpu-operator.yaml | MT GPU Operator yaml文件 |
| GPU-Operator/gpu-operator-full/mthreads_v1alpha4_clusterconfig.yaml | clusterconfig yaml 文件 |
| GPU-Operator/gpu-operator-full/mthreads_v1beta2_clusterpolicy.yaml | clusterpolicy yaml 文件 |
| GPU-Operator/gpu-operator-full/dcgm-and-exporter.yaml | dcgm 和 dcgm-exporter yaml 文件 |
| GPU-Operator/gpu-operator-full/grafana/dcgm-exporter-dashboard1.1.7.json | Grafana Dashboard 定义示例文件 |
| GPU-Operator/gpu-operator-full/change_image_repo.sh | 修改部署文件中镜像仓库地址的示例脚本 |
| GPU-Operator/gpu-operator-full/sync_image.sh | 同步镜像到内网harbor示例脚本 |

## 功能变动[](https://docs.mthreads.com#功能变动)

**新增功能**

- Container Toolkit 支持 MUSA SDK 5.x，兼容 4.3.x 以及升级到 5.x 场景所需的软链接变动。
- Container Toolkit 优化 MUSA Linux Driver 系统各类型的文件映射机制。
- GPU Operator / Device Plugin 支持 mthreads.com/gpu 以外的自定义标签。
- GPU Operator / Device Plugin 优化 GPU 掉卡情况下的状态上报机制，避免调度异常。
- DCGM Exporter 支持新的 EDC 报告机制并增删对应指标。
- DCGM Exporter 修复 CPU 占用率过高问题。

**功能下线**

- 下线 mt-gpu-exporter，监控统一使用 DCGM Exporter。
- 安装包剔除 mtml，引导用户统一从 MT GPU Management Center 下载。

**升级子组件至最新版本**

`MT Driver Toolkit`

升级至`v2.2.0`

`mt-universal-device-manager`

升级至`v2.2.0`

`MT Container Toolkit`

升级至`v2.2.0`

`MT GPU Feature Discovery`

升级至`v2.2.0`

`MT Universal Device Controller`

升级至`v2.2.0`

`MT AIOps`

升级至`v2.2.0`

`MT DCGM`

升级至`v1.1.7-3.3.6`

`MT DCGM Exporter`

升级至`v1.1.7-3.3.6-3.4.2`