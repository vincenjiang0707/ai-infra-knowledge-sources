# [Issue #1405] PaddleOCR-VL LoRA 微调后 怎么合并模型？

source: https://github.com/PaddlePaddle/ERNIE/issues/1405
state: open | updated: 2026-01-22T08:40:06Z
labels: 

## 正文

erniekit export script/conf/run_ocr_vl_sft_16k_lora.yaml lora=True
报错：
LAUNCH INFO 2025-12-20 02:34:18,837 ------------------------- ERROR LOG DETAIL -------------------------
ation file /kanas/public/zhangfa/sft_paddle/outputs/official_models/PaddleOCR-VL/config.json
Traceback (most recent call last):
  File "/home/ERNIE/erniekit/launcher.py", line 58, in <module>
    launch()
  File "/home/ERNIE/erniekit/launcher.py", line 48, in launch
    run_export()
  File "/home/ERNIE/erniekit/export/export.py", line 171, in run_export
    mergekit.merge_model()
  File "/usr/local/lib/python3.10/dist-packages/paddleformers/mergekit/merge_model.py", line 94, in merge_model
    self.merge_lora_model()
  File "/usr/local/lib/python3.10/dist-packages/paddleformers/mergekit/merge_model.py", line 570, in merge_lora_model
    self.merge_safetensor_lora_model(file_type_list)
  File "/usr/local/lib/python3.10/dist-packages/paddleformers/mergekit/merge_model.py", line 648, in merge_safetensor_lora_model
    import_class = importlib.import_module(f"paddleformers.transformers.{config_dict['model_type']}.modeling")
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 992, in _find_and_load_unlocked

## 评论 (11)

### Jonathans575 · 2025-12-22

您好，请提供enriekit、paddleformers和paddle版本号

### aaiccee · 2025-12-22

> 您好，请提供enriekit、paddleformers和paddle版本号

paddlepaddle-gpu==3.2.0 paddleformers==0.4.0 
------------------------------------------------------------
Welcome to ErnieKit
version : 1.5.0
commit : 9658b15012103b3a22c5732942ff903d49351b7a.dirty
------------------------------------------------------------


### Jonathans575 · 2025-12-23

请确认一下，yaml文件里面的model_name_or_path是源模型路径，output_dir为你训完的checkpoint路径，lora merge后会自动保存在output_dir/export路径下

### forBlank · 2025-12-23

感谢关注，目前 erniekit export 尚未支持 PaddleOCR-VL 模型，相关功能正在开发中，敬请期待，谢谢

### aaiccee · 2025-12-23

> 请确认一下，yaml文件里面的model_name_or_path是源模型路径，output_dir为你训练的checkpoint路径，lora合并完后会自动保存在output_dir/export路径下

是的 

<img width="1115" height="785" alt="Image" src="https://github.com/user-attachments/assets/de19778c-17fd-4be0-8cb4-cd7df0f6e916" />

### aaiccee · 2025-12-23

> 请确认一下，yaml文件里面的model_name_or_path是源模型路径，output_dir为你训练的checkpoint路径，lora合并完后会自动保存在output_dir/export路径下
将 原始模型config.json 中model_type修改为 ernie4_5_moe_vl 是可以运行的，从 paddleformers看，其不支持模型类型为 paddleocr_vl 的类型
<img width="1304" height="532" alt="Image" src="https://github.com/user-attachments/assets/405ed13b-5b31-40cd-86ca-7c22a96f86ed" />

### git-liweichao · 2025-12-24

@aaiccee 大佬，请问你可以将lora的合并了吗？ 我这边也碰到这个问题。还有，你这个erniekit export script/conf/run_ocr_vl_sft_16k_lora.yaml lora=True    中的run_ocr_vl_sft_16k_lora.yaml 官方中没有看到，是自己写的吗？可以共享？

### aaiccee · 2025-12-24

> [@aaiccee](https://github.com/aaiccee) 大佬，请问你可以将lora的合并了吗？ 我这边也碰到这个问题。还有，你这个erniekit export script/conf/run_ocr_vl_sft_16k_lora.yaml lora=True 中的run_ocr_vl_sft_16k_lora.yaml 官方中没有看到，是自己写的吗？可以共享？

将 原始模型config.json 中model_type修改为 ernie4_5_moe_vl ，run_ocr_vl_sft_16k_lora.yaml  跟 run_ocr_vl_sft_16k.yaml 是一样的 output_dir 修改为 你的LoRA 模型地址就可以了

### git-liweichao · 2025-12-24

好的 感谢回答~

### longzeyilang · 2026-01-22

@aaiccee 
在ERNIE-release-v1.5进行lora开启训练后和export后，那如何进行模型测试？
1、export转化后结果

<img width="365" height="464" alt="Image" src="https://github.com/user-attachments/assets/e60c0a81-848a-4506-81ec-bc74fdb8fb5b" />
2、模型测试
`import json
import os
import shutil
from pathlib import Path
import paddle
from paddlex import create_model
import time

def batch_process_ocr(val_path, model_dir, output_folder="./output", batch_size=8):
    """批量处理OCR检测"""
    
    # 1. 加载数据
    with open(val_path, 'r') as f:
        samples = [json.loads(line) for line in f]
    
    print(f"加载 {len(samples)} 个样本")
    
    # 2. 准备batch数据
    batch_data = []
    for i, sample in enumerate(samples):
        sample['image'] = sample['image_info'][0]['image_url']
        sample['query'] = "OCR:"
        
        if os.path.exists(Path(sample['image'])):
            batch_data.append(sample)
        else:
            print(f"文件不存在: {sample['image']}")
    
    print(f"有效样本: {len(batch_data)} 个")
    
    # 3. 初始化模型
    model = create_model("PaddleOCR-VL-0.9B", model_dir=model_dir)   
    # model = create_model("ernie4_5_moe_vl", model_dir=model_dir)
    os.makedirs(output_folder, exist_ok=True)
    
    # 4. Batch处理
    start = time.time()
    results, incorrect = [], 0
    
    for i in range(0, len(batch_data), batch_size):
        batch = batch_data[i:i + batch_size]
        
        # 批量预测
        batch_responses = []
        for sample in batch:
            try:
                res = next(model.predict(sample, max_new_tokens=2048, use_cache=True))
                batch_responses.append(res['result'])
            except Exception as e:
                print(f"预测失败: {e}")
                batch_responses.append("")
        
        # 处理结果
        for j, sample in enumerate(batch):
            if batch_responses[j]:  # 只处理成功预测的
                sample['response'] = batch_responses[j]
                gt_text = sample['text_info'][1]['text']
                print(sample['response'],",",gt_text)
                if gt_text != batch_responses[j]:
                    incorrect += 1
                    filename = Path(sample['image']).stem
                    dest = os.path.join(output_folder, f"{sample['response']}_{gt_text}.png")
                    shutil.copy2(sample['image'], dest)
                
                results.append(sample)
    
    # 5. 保存结果
    # with open("ocr_vl_sft-test_Bengali_response.jsonl", 'w') as f:
    #     for r in results:
    #         f.write(json.dumps(r, ensure_ascii=False) + '\n')
    
    # 6. 输出统计
    elapsed = time.time() - start
    print(f"\n总样本: {len(samples)} | 成功处理: {len(results)}")
    print(f"错误数: {incorrect} | 错误率: {incorrect/len(results):.4f}")
    print(f"耗时: {elapsed:.1f}秒 | 速度: {len(results)/elapsed:.1f} 样本/秒")

if __name__ == "__main__":
    batch_process_ocr(
        "./train/val.jsonl",
        # "./PaddleOCR-VL-SFT-Bengali/checkpoint-12800",
        "./PaddleOCR-VL-SFT-lora/export",
        batch_size=64
    )`
3、报错

<img width="749" height="197" alt="Image" src="https://github.com/user-attachments/assets/494a7030-f503-4a80-813c-d2cf5fcc90b2" />

### forBlank · 2026-01-22

PaddleFormers 1.0 已发布，支持 PaddleOCR-VL LoRA 训练和权重合并，可以参考 [PaddleFormers & PaddleOCR-VL Best Practices](https://github.com/PaddlePaddle/PaddleFormers/tree/release/v1.0/examples/best_practices/PaddleOCR-VL)
