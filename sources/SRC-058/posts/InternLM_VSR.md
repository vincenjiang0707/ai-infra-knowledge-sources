# InternLM/VSR

source: https://github.com/InternLM/VSR

<div align="center">

<h1>🏆 ICLR 2026</h1>

<p align="center">
  <img src="assets/vsr_logo.png" height="110">
</p>

<h1>Visual Self-Refine: A Pixel-Guided Paradigm<br>for Accurate Chart Parsing</h1>

<div>
    <a href="https://li-jinsong.github.io/" target="_blank">Jinsong Li</a><sup>1,2</sup> | 
    <a href="https://lightdxy.github.io/" target="_blank">Xiaoyi Dong</a><sup>1,2</sup> | 
    <a href="https://yuhangzang.github.io/" target="_blank">Yuhang Zang</a><sup>2</sup> | 
    <a href="https://scholar.google.com/citations?hl=zh-CN&user=sJkqsqkAAAAJ" target="_blank">Yuhang Cao</a><sup>2</sup> | 
    <a href="https://myownskyw7.github.io/" target="_blank">Jiaqi Wang</a><sup>2</sup> |
    <a href="http://dahua.site/" target="_blank">Dahua Lin</a><sup>1,2</sup>
</div>
<br>
<div>
    <sup></sup><sup>1</sup> The Chinese University of Hong Kong<br><sup>2</sup> Shanghai AI Laboratory
</div>

<br>

[![arXiv](https://img.shields.io/badge/arXiv-2602.16455-b31b1b.svg)](https://arxiv.org/abs/2602.16455) 

---

</div>

<strong>Visual Self-Refine (VSR) turns chart parsing into a pixel-guided feedback loop: predict anchors, render them, inspect the rendered chart, and refine the final parsing from the verified pixels.</strong>

## 💻 Overview

<div style="width: 100%; text-align: center; margin: auto;">
  <img style="width: 100%;" src="assets/teaser.png">
</div>


<div style="width: 70%; text-align: center; margin: auto;">
  <img style="width: 78%;" src="assets/case_vsr.png">
</div>

## 🎈 Quick Start

From the repository root:

```bash
pip install -r requirements.txt
```

### Chart generation
```bash
cd chart_generation
python setup_fonts.py
bash gen.sh
```

### Data pipeline
```bash
cd data_pipeline
python resize_and_remap.py
python render_anchors.py
```

### Benchmark evaluation
```bash
cd benchmark
python eval_api.py \
  --input-json <path/to/chartp_annotations.json> \
  --image-folder <path/to/chartp_images> \
  --output-json outputs/chartp_gpt-4o.json
```

## 📎 Citation

```bibtex
@article{li2026visual,
  title={Visual self-refine: A pixel-guided paradigm for accurate chart parsing},
  author={Li, Jinsong and Dong, Xiaoyi and Zang, Yuhang and Cao, Yuhang and Wang, Jiaqi and Lin, Dahua},
  journal={arXiv preprint arXiv:2602.16455},
  year={2026}
}
```

