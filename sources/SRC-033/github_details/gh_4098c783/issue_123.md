# [Issue #123] torch_npu/_inductor 中 MLIRProcessor 使用 shell=True 执行由环境变量拼接的命令，存在条件性命令注入风险

source: https://github.com/Ascend/pytorch/issues/123
state: open | updated: 2026-04-22T03:46:23Z
labels: 

## 正文

描述：
  在 torch_npu/_inductor/ascend_npu_ir/ascend_npu_ir/npu/utils.py 中，MLIRProcessor 会从环境变量 BISHENG_INSTALL_PATH 读取
  路径，拼接出 bishengir-opt 可执行文件路径，然后进一步构造字符串命令，并通过 subprocess.check_output(..., shell=True) 执
  行。

  相关代码片段：

  class MLIRProcessor:
      def __init__(self, bisheng_install_path: str = None):
          bisheng_install_path = os.getenv('BISHENG_INSTALL_PATH', '')
          self.bisheng_torch_mlir_path = os.path.join(bisheng_install_path, "bishengir-opt")

  cmd = (f"{self.bisheng_torch_mlir_path} "
          "--torch-backend-to-named-op-backend-pipeline="
          "\"ensure-no-implicit-broadcast=true\" "
          f"{torch_mlir_path}")

  result = subprocess.check_output(
      cmd, text=True, shell=True
  )

  位置：

  - targets/2026-04-22-pytorch/torch_npu/_inductor/ascend_npu_ir/ascend_npu_ir/npu/utils.py:435
  - targets/2026-04-22-pytorch/torch_npu/_inductor/ascend_npu_ir/ascend_npu_ir/npu/utils.py:436
  - targets/2026-04-22-pytorch/torch_npu/_inductor/ascend_npu_ir/ascend_npu_ir/npu/utils.py:535
  - targets/2026-04-22-pytorch/torch_npu/_inductor/ascend_npu_ir/ascend_npu_ir/npu/utils.py:542

  风险说明：

  - BISHENG_INSTALL_PATH 来自环境变量
  - 命令通过字符串拼接生成
  - 最终使用 shell=True 执行

  如果运行环境可被外部影响，例如共享 CI、调试环境或不可信启动脚本场景，攻击者可能通过构造 BISHENG_INSTALL_PATH 注入额外
  shell 命令。

  建议修复：

  - 改为参数列表形式调用，使用 shell=False
  - 对 BISHENG_INSTALL_PATH 做路径合法性校验
  - 避免将外部可控内容直接拼入 shell 命令字符串

## 评论 (2)

### ycaibb · 2026-04-22

还有两个也麻烦看看：
 问题：
  ARM Docker 构建脚本使用 curl -k 下载 yum repo 配置，存在供应链篡改风险

  描述：
  在 ci/docker/ARM/Dockerfile 中，当 CONFIG_FOR_LCOV=1 时，会使用 curl -k 下载 yum repo 配置文件，并立即用于后续 yum 流
  程。

  相关代码片段：

  ARG CONFIG_FOR_LCOV=0

  RUN if [ "$CONFIG_FOR_LCOV" = "1" ]; then \
      mkdir -p /etc/yum.repos.d/backup && \
      mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/backup/ && \
      curl -o /etc/yum.repos.d/Centos7-aliyun.repo https://mirrors.wlnmp.com/centos/Centos7-aliyun-altarch.repo -k && \
      yum clean all && \
      yum makecache; \
      fi

  位置：

  - targets/2026-04-22-pytorch/ci/docker/ARM/Dockerfile:17
  - targets/2026-04-22-pytorch/ci/docker/ARM/Dockerfile:22

  风险说明：

  - curl -k 会关闭 TLS 证书校验
  - 下载得到的 repo 配置会直接进入 /etc/yum.repos.d/
  - 随后会继续执行 yum makecache

  这会导致在特定网络条件下存在中间人篡改风险，进而影响构建阶段的软件包来源，属于供应链安全问题。

  建议修复：

  - 去掉 -k
  - 使用证书校验正常的可信镜像源
  - 或将 repo 配置文件固定到仓库内，避免构建时动态下载

### ycaibb · 2026-04-22

问题：
  X86 Docker 构建脚本使用 curl -k 下载 yum repo 配置，存在供应链篡改风险

  描述：
  在 ci/docker/X86/Dockerfile 中，也存在同样的问题。当 CONFIG_FOR_LCOV=1 时，会使用 curl -k 下载 repo 配置文件并参与后续
  yum 构建流程。

  相关代码片段：

  ARG CONFIG_FOR_LCOV=0

  RUN if [ "$CONFIG_FOR_LCOV" = "1" ]; then \
      mkdir -p /etc/yum.repos.d/backup && \
      mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/backup/ && \
      curl -o /etc/yum.repos.d/Centos7-aliyun.repo https://mirrors.wlnmp.com/centos/Centos7-aliyun-altarch.repo -k && \
      yum clean all && \
      yum makecache; \
      fi

  位置：

  - targets/2026-04-22-pytorch/ci/docker/X86/Dockerfile:20
  - targets/2026-04-22-pytorch/ci/docker/X86/Dockerfile:25

  风险说明：

  - 关闭 HTTPS 证书校验后，外部下载内容可信度下降
  - repo 配置会影响后续包管理行为
  - 一旦链路被劫持，可能污染构建输入来源

  建议修复：

  - 删除 -k
  - 使用受信仓库和正常 TLS 校验
  - 或改为内置 repo 配置，避免构建期动态拉取
