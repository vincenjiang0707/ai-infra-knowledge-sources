source: https://docs.mthreads.com/playbook/playbook-doc-online/yolo_training_and_inference

# 【中级】MTT AIBOOK YOLO PyTorch MUSA 训练与推理

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更说明 |
|---|---|---|
| 1.0.0 | 2026-08-21 | 首次发布 |

## 1. 教程简介[](https://docs.mthreads.com#1-教程简介)

本文介绍如何在 MTT AIBOOK 上使用预装的 PyTorch 和 MUSA 软件栈，完成 YOLO11n 模型训练、验证、推理和性能测试。训练使用 COCO8 数据集，推理和性能测试在 MUSA 设备上运行。

完成本文操作后，您可以：

- 验证 PyTorch MUSA 环境。
- 使用 COCO8 数据集训练并验证 YOLO11n 模型。
- �对测试图片执行目标检测。
- 测试不同 YOLO 模型、批次大小和数据精度的推理性能。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

开始前，请确认满足以下条件。

### 硬件条件[](https://docs.mthreads.com#硬件条件)

| 项目 | 要求 |
|---|---|
| 设备 | MTT AIBOOK A141 |

### 软件要求[](https://docs.mthreads.com#软件要求)

| 软件或环境 | 版本 |
|---|---|
| 操作系统 | MTT AIOS 1.5.0 |
| MUSA 驱动 | 5.2.1-M1000 |
| MUSA SDK | 5.1.2 |
| Python | 3.12.3 |
| PyTorch | `2.9.0.post1+musa5.1.2mp22` |
| TorchMUSA | `2.9.0.post1+musa5.1.2mp22` |
| torchvision | `0.22.1.post1+musa5.1.2mp22` |
| torchaudio | `2.7.1.post1+musa5.1.2mp22` |
| Ultralytics | 8.4.121 |
| torch_compat | 1.0.0 |
| NumPy | 1.26.1 |

可打开 **设置** > **系统** > **关于** 查看 MTT AIOS 版本。

MTT AIBOOK 已预装 MUSA 驱动、MUSA SDK、PyTorch、TorchMUSA、torchvision 和 torchaudio。请勿使用 pip 单独替换这些基础组件，否则可能因版本不匹配导致 MUSA 设备不可用或运行时异常。

### 其他准备[](https://docs.mthreads.com#其他准备)

- 确保设备可以访问本文使用的软件源和模型资源。
- 确保当前用户具有安装 Python 软件包的权限。
- 预留足够的磁盘空间，用于保存软件包、模型权重、数据集和训练结果。

## 3. 配置运行环境[](https://docs.mthreads.com#3-配置运行环境)

### 3.1 检查预装环境[](https://docs.mthreads.com#31-检查预装环境)

执行以下命令查看预装组件的版本：

`mthreads-gmi`

mcc --version

python3 --version

/usr/bin/python3 -m pip show torch

/usr/bin/python3 -m pip show torchvision

/usr/bin/python3 -m pip show torchaudio

/usr/bin/python3 -m pip show torch_musa



### 3.2 安装依赖[](https://docs.mthreads.com#32-安装依赖)

-
创建工作目录：

mkdir ~/yolo_trainingcd ~/yolo_training -
下载并安装

`torch_compat`

：wget -O torch_compat-1.0.0-cp312-cp312-linux_aarch64.whl \https://apollo-appstore-pre.tos-cn-beijing.volces.com/appstore/release/pip/torch_compat/torch_compat-1.0.0-cp312-cp312-linux_aarch64.whl/usr/bin/python3 -m pip install --user --break-system-packages --no-deps \./torch_compat-1.0.0-cp312-cp312-linux_aarch64.whl -
安装 Ultralytics：

/usr/bin/python3 -m pip install ultralytics==8.4.121 -
安装 NumPy：

/usr/bin/python3 -m pip install numpy==1.26.1

### 3.3 验证 MUSA 环境[](https://docs.mthreads.com#33-验证-musa-环境)

-
在工作目录中新建

`test_musa.py`

文件，并写入以下内容：import torchimport torch_musax = torch.randn(2, 3)y1 = x.to("musa:0")print(f"y1 device: {y1.device}")y2 = x.to(device="musa:0")print(f"y2 device: {y2.device}")y3 = x.to("cpu")print(f"y3 device: {y3.device}")y4 = x.to(0)print(f"y4 device: {y4.device}")y5 = x.to(device=0)print(f"y5 device: {y5.device}")y6 = x.to(dtype=torch.float64, device="musa:0")print(f"y6 device: {y6.device}, dtype: {y6.dtype}")y7 = x.to(device="musa:0", non_blocking=True)print(f"y7 device: {y7.device}, non_blocking: {y7.is_pinned()}")x = torch.tensor([1]).to('musa:0')print(x.device)print(torch.__version__)print(torch.musa.is_available())device = torch.device('musa:0')print(device) -
运行测试脚本：

/usr/bin/python3 test_musa.py

如果终端依次显示张量设备、PyTorch 版本、`True`

和 `musa:0`

，则 MUSA 环境可用。

## 4. 运行 YOLO 训练和推理[](https://docs.mthreads.com#4-运行-yolo-训练和推理)

### 4.1 准备测试图片[](https://docs.mthreads.com#41-准备测试图片)

在工作�目录中执行以下命令下载测试图片：

`wget https://ultralytics.com/images/bus.jpg`



### 4.2 训练、验证和推理[](https://docs.mthreads.com#42-训练验证和推理)

-
新建

`yolo_training.py`

文件，并写入以下内容：import torch_compat as torchimport torch_musaimport torch_musa.core._utilsimport torch_musa.core.devicedef get_musa_device_index(*args, **kwargs):return 0torch_musa.core._utils._get_musa_device_index = get_musa_device_indextorch_musa.core.device._get_musa_device_index = get_musa_device_indexfrom ultralytics import YOLOmodel = YOLO("yolo11n.pt")model.train(data="coco8.yaml",epochs=100,imgsz=640,device="0",amp=False,)model.val()results = model("./bus.jpg") # 对测试图片执行推理results[0].show() # 显示检测结果 -
运行脚本：

/usr/bin/python3 yolo_training.py

脚本将依次完成以下任务：

- 加载
`yolo11n.pt`

预训练模型。 - 在 MUSA 设备上使用 COCO8 数据集训练 100 个 epoch。
- 在验证集上评估模型。
- 对
`bus.jpg`

执行目标检测并显示结果。

如果终端持续输出训练进度且没有出现异常堆栈，则训练任务已开始运行。训练完成后，终端会输出验证指标、单张图片推理耗时和结果保存目录。

### 4.3 测试推理性能[](https://docs.mthreads.com#43-测试推理性能)

-
新建

`yolo_inference.py`

文件，并写入以下内容：import argparseimport platformimport timefrom itertools import productfrom typing import Listfrom pathlib import Pathimport torch_compat as torchimport torch_musaimport torch_musa.core._utilsimport torch_musa.core.device_orig_get_idx = torch_musa.core._utils._get_musa_device_indexdef _safe_get_musa_device_index(device=None, optional=False, allow_cpu=False):try:return _orig_get_idx(device, optional, allow_cpu)except ValueError:passidx = getattr(device, "index", None)if isinstance(device, str):idx = torch.device(device).indexif idx is None:idx = torch.musa.current_device()return int(idx)torch_musa.core._utils._get_musa_device_index = _safe_get_musa_device_indextorch_musa.core.device._get_musa_device_index = _safe_get_musa_device_indexfrom ultralytics import YOLOfrom ultralytics.cfg import TASK2DATA, TASK2METRICfrom ultralytics.engine.exporter import export_formatsfrom ultralytics.utils import ASSETS, LOGGERfrom ultralytics.utils.checks import check_imgsz, check_yolofrom ultralytics.utils.files import file_sizeDEFAULT_MODELS = ["yolov5n.pt","yolov5s.pt","yolov5m.pt","yolov5l.pt","yolov8n.pt","yolov8s.pt","yolov8m.pt","yolov8l.pt","yolov10n.pt","yolov10s.pt","yolov10m.pt","yolov10l.pt","yolo11n.pt","yolo11s.pt","yolo11m.pt","yolo11l.pt","yolo12n.pt","yolo12s.pt","yolo12m.pt","yolo12l.pt",]DEFAULT_BATCHES = [1, 2, 4, 8, 16, 32]DEFAULT_DTYPES = [False, True] # False: fp32, True: fp16def benchmark(model,data=None,imgsz=160,batch=1,half=False,int8=False,device="cpu",verbose=False,eps=1e-3,format="-",):imgsz = check_imgsz(imgsz)assert imgsz[0] == imgsz[1] if isinstance(imgsz, list) else True, "benchmark() only supports square imgsz."import pandas as pd # scope for faster 'import ultralytics'pd.options.display.max_columns = 10pd.options.display.width = 120if isinstance(model, (str, Path)):model = YOLO(model)is_end2end = getattr(model.model.model[-1], "end2end", False)data = data or TASK2DATA[model.task] # task to dataset, i.e. coco8.yaml for task=detectkey = TASK2METRIC[model.task] # task to metric, i.e. metrics/mAP50-95(B) for task=detecty = []t0 = time.time()format_arg = format.lower()if format_arg:formats = frozenset(export_formats()["Argument"])assert format in formats, f"Expected format to be one of {formats}, but got '{format_arg}'."ef = export_formats()for i, (name, format, suffix, cpu, gpu) in enumerate(zip(ef["Format"], ef["Argument"], ef["Suffix"], ef["CPU"], ef["GPU"])):emoji, filename = "❌", None # export defaultstry:if format_arg and format_arg != format:continue# Exportif format == "-":filename = model.pt_path or model.ckpt_path or model.model_nameexported_model = model # PyTorch formatelse:filename = model.export(imgsz=imgsz, format=format, half=half, int8=int8, data=data, device=device, verbose=False)exported_model = YOLO(filename, task=model.task)assert suffix in str(filename), "export failed"emoji = "❎" # indicates export succeeded# Predictassert model.task != "pose" or i != 7, "GraphDef Pose inference is not supported"assert i not in {8}, "inference not supported" # Edge TPU is unsupported (TF.js removed from table)assert i != 5 or platform.system() == "Darwin", "inference only supported on macOS>=10.13" # CoreMLif i in {11}:assert not is_end2end, "End-to-end torch.topk operation is not supported for NCNN prediction yet"exported_model.predict(ASSETS / "bus.jpg", imgsz=imgsz, device=device, half=half, verbose=False)# Validateresults = exported_model.val(data=data, batch=batch, imgsz=imgsz, plots=False, device=device, half=half, int8=int8, verbose=False)metric, speed = results.results_dict[key], results.speed["inference"]fps = round(1000 / (speed + eps), 2) # frames per secondy.append([name, "✅", round(file_size(filename), 1), round(metric, 4), round(speed, 2), fps])except Exception as e:if verbose:assert type(e) is AssertionError, f"Benchmark failure for {name}: {e}"LOGGER.warning(f"ERROR ❌️ Benchmark failure for {name}: {e}")y.append([name, emoji, round(file_size(filename), 1), None, None, None]) # mAP, t_inference# Print resultscheck_yolo(device=device) # print system infodf = pd.DataFrame(y, columns=["Format", "Status❔", "Size (MB)", key, "Inference time (ms/im)", "FPS"])name = model.model_namedt = time.time() - t0legend = "Benchmarks legend: - ✅ Success - ❎ Export passed but validation failed - ❌️ Export failed"s = f"\nBenchmarks complete for {name} on {data} at imgsz={imgsz} ({dt:.2f}s)\n{legend}\n{df.fillna('-')}\n"LOGGER.info(s)with open("benchmarks.log", "a", errors="ignore", encoding="utf-8") as f:f.write(s)if verbose and isinstance(verbose, float):metrics = df[key].array # values to compare to floorfloor = verbose # minimum metric floor to pass, i.e. = 0.29 mAP for YOLOv5nassert all(x > floor for x in metrics if pd.notna(x)), f"Benchmark failure: metric(s) < floor {floor}"return dfdef main(models: List[str], batches: List[int], dtypes: List[bool], dataset: str = "coco128.yaml", imgsz: int = 640, device: str = "0"):if isinstance(device, str) and device.lower().startswith("musa"):device = device.split(":")[-1] if ":" in device else "0"for half, model, batch in product(dtypes, models, batches):print(f"Benchmarking model: {model} with half:{half} batch:{batch} dataset:{dataset} imgsz:{imgsz}")benchmark(model=model, data=dataset, imgsz=imgsz, batch=batch, half=half, int8=False, device=device)time.sleep(5)if __name__ == "__main__":parser = argparse.ArgumentParser(description="Run YOLO benchmarks.")parser.add_argument("--models", nargs="+", default=DEFAULT_MODELS, help="List of models to benchmark.")parser.add_argument("--batches", nargs="+", type=int, default=DEFAULT_BATCHES, help="List of batch to test.")parser.add_argument("--dtypes", nargs="+", type=lambda x: x.lower() == 'true', default=DEFAULT_DTYPES, help="List of dtypes to test (False for fp32, True for fp16).")parser.add_argument("--dataset", default="coco128.yaml", help="Dataset configuration file (e.g., coco128.yaml).")parser.add_argument("--imgsz", type=int, default=640, help="Image size.")parser.add_argument("--device", default="0", help="Device to run on.")args = parser.parse_args()main(args.models, args.batches, args.dtypes, args.dataset, args.imgsz, args.device) -
运行性能测试：

/usr/bin/python3 yolo_inference.py

测试完成后，终端会输出模型格式、状态、模型大小、mAP、单张图片推理耗时和 FPS。在上述软件和硬件环境中，YOLO12n FP32 的参考结果如下：

| 批次大小 | 单张图片推理耗时 | FPS |
|---|---|---|
| 1 | 约 30.84 ms | 约 32.43 |
| 2 | 约 19.06 ms | 约 52.46 |

实际结果会受软件版本、系统负载、温度和功耗状态等因素影响。

## 5. 最佳实践[](https://docs.mthreads.com#5-最佳实践)

- 请使用 MTT AIOS 预装的 PyTorch、TorchMUSA 和 MUSA SDK，避免单独替换基础组件。
- 在安装其他 Python 软件包前，记录当前环境的组件版本。
- 开发和调试时，优先使用 YOLO11n、YOLO12n 等轻量模型，缩短验证周期。
- 首次运行性能测试时，从较小的批次大小开始，再根据内存占用逐步调整。
- 如果出现内存不足，可减小批次大小或输入图片尺寸。

## 6. 常见问题[](https://docs.mthreads.com#6-常见问题)

| 问题 | 处理方法 |
|---|---|
缺少 `torch_compat` | 按照本文步骤安装与 Python 3.12 和 ARM64 架构匹配的 `torch_compat` 安装包。安装时使用 `--no-deps` ，避免覆盖预装组件。 |
| PyTorch、TorchMUSA 或 MUSA SDK 版本不一致 | 确认当前 MTT AIOS 版本，并使用系统预装的软件栈。请勿单独替换其中某个基础组件。 |
| 运行性能测试时内存不足 | 减小 `--batches` 或 `--imgsz` 参数后重试。 |