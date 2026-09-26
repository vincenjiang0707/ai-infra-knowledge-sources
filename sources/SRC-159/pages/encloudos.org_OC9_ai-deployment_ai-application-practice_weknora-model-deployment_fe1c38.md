source: https://docs.opencloudos.org/OC9/ai-deployment/ai-application-practice/weknora-model-deployment/

# WeKnora大模型部署指南

WeKnora 是腾讯开源的 LLM 文档理解与语义检索框架：面向结构复杂、来源异构的企业文档，采用模块化流水线把解析→向量索引→智能召回→大模型生成串成可控的 RAG（检索增强生成）流程，支持深度内容理解与上下文感知回答，可用于知识库问答、资料检索与多格式文档场景的落地部署。

本文档将展示如何在 OpenCloudOS 9 操作系统上，通过一键安装脚本和容器镜像拉取，快速启动 WeKnora 框架和相关推理服务。

## 1.安装容器依赖

### 一键安装容器依赖

脚本下载地址：[点击下载执行脚本](https://ocweb-1319394267.cos.ap-guangzhou.myqcloud.com/docs/scripts/auto_install_vllm.sh)

```
sudo ./auto_install.sh
```


## 2.安装 ollama

### 2.1 安装方式

** 方式一：使用docker镜像（推荐）**

```
docker run -d --name ollama --restart=always \
-p 11434:11434 \
-e OLLAMA_HOST=0.0.0.0:11434 \
ollama/ollama:latest
```


方式二：下载安装脚本并安装（此方式比较慢）

```
curl -fsSL https://ollama.com/install.sh | sh
```


### 2.2 验证

```
curl -sS http://localhost:11434/api/tags || echo "tags not ready"
```


## 3.准备模型（以 Qwen2.5 为例）

```
docker run -d --name ollama --restart=always \
-p 11434:11434 \
-e OLLAMA_HOST=0.0.0.0:11434 \
ollama/ollama:latest
```


## 4.启动 WeKnora

### 4.1 下载WeKnora

```
git clone https://github.com/Tencent/WeKnora.git
cd WeKnora
cp .env.example .env
```


### 4.2 修改WeKnora/scripts/start_all.sh

如果过docker形式启动ollama，需要修改start_ollama，删除下面部分

```
if ! command -v ollama &> /dev/null; then
install_ollama
if [ $? -ne 0 ]; then
return 1
fi
fi
```


### 4.3 启动WeKnora

```
./scripts/start_all.sh
```


## 5.Web访问

### 5.1 新建知识库

### 5.2 选择模型

### 5.3 上传文件

### 5.4 访问

## 6.自动化脚本

```
yum update -y
yum install docker git docker-compose git -y
mkdir -p /etc/docker
tee /etc/docker/daemon.json >/dev/null <<'EOF'
{
"registry-mirrors": [
"https://mirror.ccs.tencentyun.com",
"https://docker.mirrors.ustc.edu.cn",
"https://registry.docker-cn.com"
],
"dns": ["119.29.29.29","223.5.5.5"],
"max-concurrent-downloads": 3
}
EOF
systemctl daemon-reload
systemctl restart docker
#推荐容器方式部署ollama：
docker run -d --name ollama --restart=always \
-p 11434:11434 \
-e OLLAMA_HOST=0.0.0.0:11434 \
ollama/ollama:latest
curl -sS http://localhost:11434/api/tags || echo "tags not ready"
docker exec -it ollama ollama pull qwen2.5:7b-instruct
git clone https://github.com/Tencent/WeKnora.git
cd WeKnora
cp .env.example .env
ROOT="$(pwd)"
SH="$ROOT/scripts/start_all.sh"
ENVF="$ROOT/.env"
URL="http://localhost:11434"
TS="$(date +%s)"
[[ -f "$SH" ]] || { echo "找不到 $SH"; exit 1; }
# 备份
cp -a "$SH" "$SH.bak.$TS"
[[ -f "$ENVF" ]] && cp -a "$ENVF" "$ENVF.bak.$TS" || true
# 1) 在 start_ollama() 的 get_ollama_base_url 后注入“容器托管→直接返回”
if ! grep -q '容器托管.*跳过本地安装/启动' "$SH"; then
# 仅在 start_ollama() 函数体范围内查找并插入
if grep -q '^[[:space:]]*start_ollama[[:space:]]*()[[:space:]]*{' "$SH"; then
sed -i '/^[[:space:]]*start_ollama[[:space:]]*()[[:space:]]*{/,/^[[:space:]]*}[[:space:]]*$/{
/get_ollama_base_url/ a\
\ \ \ \ # 容器托管：跳过本地安装/启动（由容器/Compose 负责）\
\ \ \ \ IS_REMOTE=1; log_info "Ollama服务地址: $OLLAMA_URL (容器托管)"; return 0
}' "$SH"
else
echo "未找到 start_ollama() 函数定义，放弃打补丁"; exit 1
fi
fi
chmod +x "$SH"
exec "$SH"
```