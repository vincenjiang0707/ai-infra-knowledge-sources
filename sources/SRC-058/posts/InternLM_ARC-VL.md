# InternLM/ARC-VL

source: https://github.com/InternLM/ARC-VL

<div align="center">
  <h1 align="center">
    <div style="display: flex; align-items: center; justify-content: center;">
      <div style="text-align: left; line-height: 1.3;">
        Think Visually, Reason Textually: Vision-Language Synergy in ARC
      </div>
    </div>
  </h1>
  <p align="center">
    <a href="https://beichenzbc.github.io/"><strong>Beichen Zhang</strong></a >
    ·
    <a href="https://yuhangzang.github.io/"><strong>Yuhang Zang<sup>&dagger;</sup></strong></a >
    ·
    <a href="https://lightdxy.github.io/"><strong>Xiaoyi Dong</strong></a >
    ·
    <a href="https://scholar.google.com/citations?user=sJkqsqkAAAAJ"><strong>Yuhang Cao</strong></a >
    </br>
    <a href="https://github.com/kennymckormick"><strong>Haodong Duan</strong></a >
    ·
    <a href="http://dahua.site/"><strong>Dahua Lin</strong></a >
    ·
     <a href="https://myownskyw7.github.io/"><strong>Jiaqi Wang<sup>&dagger;</sup></strong></a >
  </p >
  <p align="center" style="font-size: 1em; margin-top: -1em">  <sup>&dagger;</sup>Corresponding authors. </p >
  </p > 
</div>

## 📢 News
- 🚀 [2025/11/26] We have released the Inference Code
- 🚀 [2025/11/19] We have released the paper [Think Visually, Reason Textually: Vision-Language Synergy in ARC
](https://arxiv.org/pdf/2511.15703)

  
## 🌈 Overview
We integrate <strong>Visual Intelligence</strong> into ARC-AGI to leverage the respective advantages of vision and text: vision supports global pattern abstraction and verification, whereas language specializes in precise execution.

We achieve this by introducing two synergistic strategies:
(1) <strong>Vision-Language Synergy Reasoning (VLSR)</strong> which decomposes ARC-AGI into modality-aligned subtasks; and
(2) <strong>Modality-Switch Self-Correction (MSSC)</strong>, which leverages vision to verify text-based reasoning for intrinsic error correction.

</p>
<p style="text-align: center;"> 
  <img src="figs/method.png" alt="Method" width="100%"> 
</p>



## 🛠️ Inference
Prepare your environment
```bash
git clone https://github.com/InternLM/Arc-VL
conda create -n arcvl python==3.11
conda activate arcvl
pip install -r requirements.txt
```

Modify `setup_api_key.sh`and fill in your base_url and API keys. Activate it by running:

```bash
source setup_api_key.sh
```

Prepare for the data. The data can be downloaded in the following link:

***ARC-AGI:*** [https://github.com/fchollet/ARC-AGI](https://github.com/fchollet/ARC-AGI)

***BARC:*** [https://github.com/xu3kev/BARC](https://github.com/xu3kev/BARC)

***Re-ARC:*** [https://github.com/michaelhodel/re-arc](https://github.com/michaelhodel/re-arc)

Specify the test dataset, test model and dataset path, and run our vision-language synergy reasoning with the following code.

```bash
python inference.py --dataset_name="arc-agi" --model="gpt-4o" --data_path="Your_data_path"
--result_file="result_arcagi_4o.json"
--save_root="images/ARC-AGI/"
```

Finally, score the inference results.

```bash
python score.py --input_file="result.json" --output_file="result_scored.json"
```

## Cases

We conduct an in-depth analysis of the specific outputs of different models (GPT-4o, Gemini-2.5-Pro-thinking-8192, o4-mini) when employing visual thinking versus textual thinking in the ARC-AGI task. Visual thinking demonstrates numerous unique advantages, such as the integration of 2D structural information, a global perspective, and long-range perception capabilities.

<p style="text-align: center;"> 
  <img src="figs/app_eg_1.jpg" alt="case1" width="100%"> 
</p>
<p style="text-align: center;"> 
  <img src="figs/app_eg_2.jpg" alt="case2" width="100%"> 
</p>
<p style="text-align: center;"> 
  <img src="figs/app_eg_3.jpg" alt="case3" width="100%"> 
</p>
<p style="text-align: center;"> 
  <img src="figs/app_eg_4.jpg" alt="case4" width="100%"> 
</p>

## ✒️Citation
If you find this project useful, please kindly cite:
```
@article{zhang2025think,
  title={Think Visually, Reason Textually: Vision-Language Synergy in ARC},
  author={Zhang, Beichen and Zang, Yuhang and Dong, Xiaoyi and Cao, Yuhang and Duan, Haodong and Lin, Dahua and Wang, Jiaqi},
  journal={arXiv preprint arXiv:2511.15703},
  year={2025}
}
```

## 📄 License
![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)

**Usage and License Notices**: The code is intended and licensed for research use only.


