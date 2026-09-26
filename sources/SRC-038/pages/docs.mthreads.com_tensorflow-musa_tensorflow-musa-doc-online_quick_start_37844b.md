source: https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/quick_start

# 快速开始

本章节提供两个完整的端到端示例：**ResNet50 图像分类推理** 和 **DeepFM 推荐模型训练**，帮助开发者快速验证 TensorFlow-MUSA 环境并上手使用。

## 获取示例代码[](https://docs.mthreads.com#获取示例代码)

开始前，请确保已完成[环境准备](https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/environment_setup)中宿主机环�境的准备，以及容器启动。

从 gitee 上获取示例代码：

`git clone https://gitee.com/mthreadsacademy/tensorflow_musa_playground`

cd tensorflow_musa_playground



## 示例一：ResNet50 图像分类推理[](https://docs.mthreads.com#示例一resnet50-图像分类推理)

本示例使用 TensorFlow 标准 `tf.keras.applications.resnet50`

API 在 MUSA GPU 上运行 ResNet50 图像分类推理。

### 推理脚本代码[](https://docs.mthreads.com#推理脚本代码)

`tensorflow_musa_playground`

示例代码文件夹下，`computer_vision/resnet50/inference.py`

是完整的推理脚本，默认加载 TensorFlow-MUSA 插件并在 `/device:MUSA:0`

上推理：

`import argparse`


import tensorflow as tf



def parse_args():

parser = argparse.ArgumentParser(description="Simple ResNet50 inference demo.")

parser.add_argument("image_path", help="Path to an input image.")

parser.add_argument(

"--device",

choices=("musa", "cpu"),

default="musa",

help="Run inference on musa or cpu.",

)

return parser.parse_args()



def load_image(image_path):

image_bytes = tf.io.read_file(image_path)

image = tf.io.decode_image(image_bytes, channels=3, expand_animations=False)

image = tf.image.resize(image, [224, 224])

image = tf.expand_dims(tf.cast(image, tf.float32), axis=0)

return tf.keras.applications.resnet50.preprocess_input(image)



def device_name(device):

if device == "musa":

import tensorflow_musa # noqa: F401


return "/device:MUSA:0"

return "/device:CPU:0"



def main():

args = parse_args()

device = device_name(args.device)


with tf.device(device):

model = tf.keras.applications.ResNet50(weights="imagenet")

image = load_image(args.image_path)

predictions = model(image, training=False)


top3 = tf.keras.applications.resnet50.decode_predictions(

predictions.numpy(), top=3

)[0]


for rank, (_, label, score) in enumerate(top3, start=1):

print(f"{rank}: {label}, score={score:.6f}")



if __name__ == "__main__":

main()



### 运行推理[](https://docs.mthreads.com#运行推理)

`MUSA_VISIBLE_DEVICES="0" python3 computer_vision/resnet50/inference.py \`

computer_vision/resnet50/cat.jpg



### 说明[](https://docs.mthreads.com#说明)

脚本的关键配置如下：

**设备**：默认在`/device:MUSA:0`

上运行，通过`import tensorflow_musa`

将 MUSA 注册为 TensorFlow 设备；支持`--device cpu`

切换到 CPU 进行对比验证。**模型与权重**：使用`tf.keras.applications.ResNet50(weights="imagenet")`

，首次运行会自动下载 ImageNet 预训练权重。**输入预处理**：输入图片自动缩放为 224×224，并执行 ResNet50 标准预处理（`preprocess_input`

）。**输出**：输出 Top-3 ImageNet 分类结果及置信度。

## 示例二：DeepFM 推荐模型训练[](https://docs.mthreads.com#示例二deepfm-推荐模型训练)

本示例使用 Criteo 广告展示数据集，在 MUSA GPU 上训练 DeepFM 推荐模型。

### 数据集[](https://docs.mthreads.com#数据集)

使用 Kaggle **Criteo Display Ad Challenge** 竞赛数据集，可通过以下两种方式获取：

**（推荐）直接下载处理后的数据**（`.npz`

格式）：百度网盘[https://pan.baidu.com/s/1fxTInhCjw8uASJd3v79Xog?pwd=xp33](https://pan.baidu.com/s/1fxTInhCjw8uASJd3v79Xog?pwd=xp33)**下载原始数据并自行处理**：

处理后的数据文件为 `kaggleAdDisplayChallenge_processed.npz`

，训练时通过 `--data_path`

指定其路径。

数据集信息如下：

| 属性 | 值 |
|---|---|
| 数据集 | Criteo Display Ad Challenge（约 4000 万条广告展示日志） |
| 总样本数 | 45,840,617 |
| 训练集 | 前 39,291,958 条 |
| 验证集 | 后 6,548,659 条 |
| 类别特征（C1–C26） | 26 维 |
| 数值特征（I1–I13） | 13 维 |
| 标签 | 二分类（点击/未点击） |

### 运行单卡训练[](https://docs.mthreads.com#运行单卡训练)

`cd tensorflow_musa_playground/recommendation_system/deepfm`


MUSA_VISIBLE_DEVICES="0" python3 train.py \

--data_path /path/to/kaggleAdDisplayChallenge_processed.npz



### 训练配置说明[](https://docs.mthreads.com#训练配置说明)

| 配置项 | 值 | 说明 |
|---|---|---|
| 模型 | DeepFM | FM + DNN 联合架构 |
| Embedding 维度 | 10 | 稀疏特征嵌入维度 |
| DNN 隐层 | (400, 400, 400) | 三层全连接 |
| 激活函数 | ReLU | |
| Dropout | 0.5 | |
| 参数量 | 371,867,651 | ~3.72 亿 |
| Batch Size | 16,384 | 每步样本数 |
| 训练轮数 | 10 | |
| 优化器 | SGD | 学习率 0.001 |
| 精度 | mixed_bfloat16 | 混合精度训练 |
| 损失函数 | BinaryCrossentropy | from_logits=True |
| 验证指标 | PR-AUC |

### 查看训练曲线[](https://docs.mthreads.com#查看训练曲线)

`tensorboard --logdir ./logs --port 6006`



## 更多信息[](https://docs.mthreads.com#更多信息)

TensorFlow-MUSA Playground 提供了 30+ 搜推广模型的完整训练和推理代码，涵盖 WDL、DCN、DeepFM、DIN、DIEN、MMoE、ESMM、PLE、RankMixer 等经典及前沿架构。更多信息请参考：

-
使用示例代码库：

[https://gitee.com/mthreadsacademy/tensorflow_musa_playground](https://gitee.com/mthreadsacademy/tensorflow_musa_playground) -
支持模型：

[支持的模型列表](https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/compability) -
性能基准：

[S5000 基准性能数据](https://docs.mthreads.com/tensorflow-musa/tensorflow-musa-doc-online/benchmark)