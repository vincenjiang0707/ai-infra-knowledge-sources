# [Issue #81] 910B pytorch在transformers, diffuser, wan2.1，cogvideo等package上加载，推理缓慢问题

source: https://github.com/Ascend/pytorch/issues/81
state: closed | updated: 2025-10-24T02:22:51Z
labels: 

## 正文

**问题：
使用910B3加载模型，推理模型极其缓慢，速度仅为a100同模型，同数据下的1/7，使用MindStudio Insight分析profiling，发现attn部分花费时间很长，是不是算子没优化？**

<img width="1384" height="416" alt="Image" src="https://github.com/user-attachments/assets/058a9584-ee5f-450d-9e5c-6840e9ad786a" />

<img width="1292" height="96" alt="Image" src="https://github.com/user-attachments/assets/c4c7d10c-5c1e-4ad0-8734-1c534536f744" />

<img width="1481" height="545" alt="Image" src="https://github.com/user-attachments/assets/58b3932f-11c2-4427-860c-ffff3b2183f5" />

<img width="1050" height="399" alt="Image" src="https://github.com/user-attachments/assets/0998bc86-d87c-40fd-8fba-9ee0225c9c50" />

<img width="495" height="250" alt="Image" src="https://github.com/user-attachments/assets/a5b81b30-7850-474c-9dd7-00ef99baba39" />

系统环境：
cpu：Kunpeng-920
显卡：910B3
cann_toolkit: 8.0.RC2

<img width="1298" height="426" alt="Image" src="https://github.com/user-attachments/assets/bedc0fee-3520-4d67-9779-918353556abd" />

<img width="1135" height="707" alt="Image" src="https://github.com/user-attachments/assets/b6e68f2e-fa35-42ae-91ee-8d5cd8fea021" />

<img width="1529" height="205" alt="Image" src="https://github.com/user-attachments/assets/10538f31-59cc-4f2e-84e3-d9377b02485a" />

conda 环境：

Name Version Build Channel
_libgcc_mutex 0.1 main
_openmp_mutex 5.1 51_gnu
absl-py 2.3.1 pypi_0 pypi
accelerate 1.10.0 pypi_0 pypi
antlr4-python3-runtime 4.9.3 pypi_0 pypi
asttokens 3.0.0 pypi_0 pypi
attrs 25.3.0 pypi_0 pypi
av 12.0.0 pypi_0 pypi
bzip2 1.0.8 h998d150_6
ca-certificates 2025.7.15 hd43f75c_0
certifi 2025.8.3 pypi_0 pypi
cffi 1.17.1 pypi_0 pypi
charset-normalizer 3.4.3 pypi_0 pypi
contourpy 1.3.2 pypi_0 pypi
cycler 0.12.1 pypi_0 pypi
decorator 5.2.1 pypi_0 pypi
diffusers 0.30.1 pypi_0 pypi
einops 0.8.1 pypi_0 pypi
exceptiongroup 1.3.0 pypi_0 pypi
executing 2.2.0 pypi_0 pypi
expat 2.7.1 h419075a_0
fastcore 1.8.7 pypi_0 pypi
filelock 3.18.0 pypi_0 pypi
fonttools 4.59.0 pypi_0 pypi
fsspec 2025.7.0 pypi_0 pypi
hf-xet 1.1.7 pypi_0 pypi
huggingface-hub 0.34.4 pypi_0 pypi
idna 3.10 pypi_0 pypi
imageio 2.37.0 pypi_0 pypi
imageio-ffmpeg 0.6.0 pypi_0 pypi
importlib-metadata 8.7.0 pypi_0 pypi
ipython 8.37.0 pypi_0 pypi
jedi 0.19.2 pypi_0 pypi
jinja2 3.1.6 pypi_0 pypi
kiwisolver 1.4.9 pypi_0 pypi
lazy-loader 0.4 pypi_0 pypi
ld_impl_linux-aarch64 2.40 h48e3ba3_0
libffi 3.4.4 h419075a_1
libgcc-ng 11.2.0 h1234567_1
libgomp 11.2.0 h1234567_1
libstdcxx-ng 11.2.0 h1234567_1
libuuid 1.41.5 h998d150_0
libxcb 1.17.0 hf66535e_0
lovely-numpy 0.2.13 pypi_0 pypi
lovely-tensors 0.1.18 pypi_0 pypi
markdown-it-py 3.0.0 pypi_0 pypi
markupsafe 3.0.2 pypi_0 pypi
matplotlib 3.10.5 pypi_0 pypi
matplotlib-inline 0.1.7 pypi_0 pypi
mdurl 0.1.2 pypi_0 pypi
mediapy 1.2.4 pypi_0 pypi
mpmath 1.3.0 pypi_0 pypi
ncurses 6.5 h419075a_0
networkx 3.4.2 pypi_0 pypi
numpy 1.26.4 pypi_0 pypi
omegaconf 2.3.0 pypi_0 pypi
opencv-python 4.9.0.80 pypi_0 pypi
openssl 3.0.17 h998d150_0
packaging 25.0 pypi_0 pypi
parso 0.8.4 pypi_0 pypi
pathlib2 2.3.7.post1 pypi_0 pypi
pexpect 4.9.0 pypi_0 pypi
pillow 11.3.0 pypi_0 pypi
pip 25.2 pypi_0 pypi
prompt-toolkit 3.0.51 pypi_0 pypi
protobuf 6.31.1 pypi_0 pypi
psutil 7.0.0 pypi_0 pypi
pthread-stubs 0.3 hfd63f10_1
ptyprocess 0.7.0 pypi_0 pypi
pure-eval 0.2.3 pypi_0 pypi
pycparser 2.22 pypi_0 pypi
pygments 2.19.2 pypi_0 pypi
pyparsing 3.2.3 pypi_0 pypi
pyquaternion 0.9.9 pypi_0 pypi
python 3.10.18 hbb0f47a_0
python-dateutil 2.9.0.post0 pypi_0 pypi
pyyaml 6.0.2 py310h998d150_0
readline 8.3 h886d1d0_0
regex 2025.7.33 pypi_0 pypi
requests 2.32.4 pypi_0 pypi
rich 14.1.0 pypi_0 pypi
safetensors 0.6.2 pypi_0 pypi
scikit-image 0.25.2 pypi_0 pypi
scipy 1.15.3 pypi_0 pypi
sentencepiece 0.2.0 pypi_0 pypi
setuptools 78.1.1 py310hd43f75c_0
six 1.17.0 pypi_0 pypi
sqlite 3.50.2 h998d150_1
stack-data 0.6.3 pypi_0 pypi
sympy 1.14.0 pypi_0 pypi
tifffile 2025.5.10 pypi_0 pypi
tk 8.6.14 hb5ae6a8_1
tokenizers 0.21.4 pypi_0 pypi
torch 2.4.0 pypi_0 pypi
torch-npu 2.4.0.post2 pypi_0 pypi
torchaudio 2.4.0 pypi_0 pypi
torchvision 0.19.0 pypi_0 pypi
tqdm 4.67.1 pypi_0 pypi
traitlets 5.14.3 pypi_0 pypi
transformers 4.47.0 pypi_0 pypi
typing-extensions 4.14.1 pypi_0 pypi
tzdata 2025b h04d1e81_0
urllib3 2.5.0 pypi_0 pypi
wcwidth 0.2.13 pypi_0 pypi
wheel 0.45.1 py310hd43f75c_0
xformers 0.0.23.post1 pypi_0 pypi
xorg-libx11 1.8.12 hf66535e_1
xorg-libxau 1.0.12 hf66535e_0
xorg-libxdmcp 1.1.5 hf66535e_0
xorg-xorgproto 2024.1 h998d150_1
xz 5.6.4 h998d150_1
yaml 0.2.5 hfd63f10_0
zipp 3.23.0 pypi_0 pypi
zlib 1.2.13 h998d150_1



## 评论 (2)

### yunyiyun · 2025-10-14

当前您这边遇到的感觉非常慢的具体是哪个算子呢

### yiiizuo · 2025-10-24

I have resolved this issue.
