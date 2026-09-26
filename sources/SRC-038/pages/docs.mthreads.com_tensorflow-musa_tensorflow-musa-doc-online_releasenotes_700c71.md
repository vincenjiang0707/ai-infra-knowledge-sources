source: https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/releasenotes

# 版本发布信息

## TensorFlow-MUSA v1.5.0[](https://docs.mthreads.com#tensorflow-musa-v150)

### 镜像地址及对应 MUSA 版本[](https://docs.mthreads.com#镜像地址及对应-musa-版本)

针对不��同的 MUSA SDK 和 Linux Driver 版本，提供以下两个镜像版本。镜像内已预置 MUSA SDK、`TensorFlow 2.15.1`

及编译好的 `tensorflow_musa_extension`

，无需手动编译。

| 镜像 | 内置 MUSA SDK | 依赖 Linux Driver | 推荐 |
|---|---|---|---|
`registry.mthreads.com/presale/devtech/tensorflow_musa:5.1.0_20260623` | 5.1.0 | 5.1.0 | ⭐ |
`registry.mthreads.com/presale/devtech/tensorflow_musa:4.3.5_20260624` | 4.3.5 | 3.3.5 | - |

### TensorFlow 版本兼容[](https://docs.mthreads.com#tensorflow-版本兼容)

TensorFlow-MUSA 开源项目兼容 `TensorFlow 2.6.1`

和 `TensorFlow 2.15.1`

，上述镜像并不预置 `TensorFlow 2.6.1`

。

如用户需要在 MUSA 环境使用 `TensorFlow 2.6.1`

，参考 [TensorFlow MUSA Extension](https://github.com/MooreThreads/tensorflow_musa_extension) 的 `README`

自行构建并安装。

### 功能特性[](https://docs.mthreads.com#功能特性)

-
支持 30+ 搜推模型的训练和推理；

-
支持 1000+ TensorFlow 算子；

-
通过算子融合和图优化提升训推性能。