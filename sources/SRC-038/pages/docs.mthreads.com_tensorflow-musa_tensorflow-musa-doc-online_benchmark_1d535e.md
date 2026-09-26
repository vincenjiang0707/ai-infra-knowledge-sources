source: https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/benchmark

# 基准性能数据

## 测试环境[](https://docs.mthreads.com#测试环境)

| 项目 | 配置 |
|---|---|
| 硬件 | MTT S5000 × 1 |
| MUSA SDK | 5.1.0 |
| TensorFlow | 2.15.1 |
| tensorflow_musa_extension | v1.5.0 |
| Python | 3.10 |
| 精度 | mixed_bfloat16 |
| XLA | 关闭 |

## 搜推广模型训练性能[](https://docs.mthreads.com#搜推广模型训练性能)

| 模型 | Batch Size | Mean/step | Samples/s | 参数量 |
|---|---|---|---|---|
| DeepFM | 16,384 | ~150 ms | ~109,000 | 3.72 亿 |
| RankMixer | 4,096 | 140.8 ms | 27,715 | — |
| OneTrans | 4,096 | 40.2 ms | 101,937 | — |
| TokenMixerLarge | 4,096 | 138.0 ms | 29,671 | — |

## 推理性能[](https://docs.mthreads.com#推理性能)

| 模型 | Batch Size | 推理延迟 | 吞吐量 |
|---|---|---|---|
| ResNet50 | 1 | ~5 ms | — |
| DeepFM | 16,384 | — | ~130,000 samples/s |


注意：性能数据受硬件配置、驱动版本、batch size 等因素影响，以上数据为参考值。完整基准测试结果持续更新中。