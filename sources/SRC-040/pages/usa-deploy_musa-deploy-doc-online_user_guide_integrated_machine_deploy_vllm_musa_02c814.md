source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/integrated_machine_deploy_vllm_musa

# vllm_musa 快速部署大模型推理服务示例

[vLLM-MUSA](https://docs.mthreads.com/vllm-musa/vllm-musa-doc-online/) 是专为摩尔线程 GPU 设计的 vLLM 后端运行插件。本节将介绍如何使用 musa-deploy 工具，在单机环境中快速部署 vLLM-MUSA 推理服务。

🚀 建议在阅读本节前先查看

[demo]使用说明章节，以了解 musa-deploy 工具的基本操作。

## 1. 启动 vllm-musa 容器[](https://docs.mthreads.com#1-启动-vllm-musa-容器)

创建名为 `vllm_musa_test`

的容器，完成端口映射及目录挂载：开发者可通过 手动拉起 vllm 推理服务：

`sudo musa-deploy --demo vllm_musa -f --name vllm_musa_test --port 8000:8000 -v /data:/data`



`-f`

：如驱动不兼容将自动更新驱动（需重启系统, 重连之后再次执行命令）- 📚
[vllm_musa 快速开始指南](https://docs.mthreads.com/vllm-musa/vllm-musa-doc-online/quick_start)

## 2. 单卡推理服务示例[](https://docs.mthreads.com#2-单卡推理服务示例)

部署 `deepSeek-r1-distill-qwen-1.5B`

模型:

`sudo musa-deploy --demo vllm_musa --model /mnt/cephfs/deepSeek-r1-distill-qwen-1.5B -f`



--model

`<model_path>`

会自动将模型路径挂载进容器并执行推理服务

## 3. 多卡并行（如八卡）[](https://docs.mthreads.com#3-多卡并行如八卡)

`sudo musa-deploy --demo vllm_musa --model /mnt/cephfs/QwQ-32B -a="-tp 8"`



等价于在容器内执行：

`vllm serve /mnt/cephfs/QwQ-32B -tp 8`



## 4. 精确控制卡号（如使用第4~7号卡）[](https://docs.mthreads.com#4-精确控制卡号如使用第47号卡)

`sudo musa-deploy --demo vllm_musa --model /mnt/cephfs/QwQ-32B -a="-tp 4" --docker-para="-e MUSA_VISIBLE_DEVICES=4,5,6,7" -f`



## 5. 指定服务 IP、端口及模型名[](https://docs.mthreads.com#5-指定服务-ip端口及模型名)

`sudo musa-deploy --demo vllm_musa --model /mnt/cephfs/QwQ-32B --network host -a="-tp 8 --port 8888 --host 10.1.0.1 --served-model-name qwq-32b" -f`



- --network host 保证容器服务可被外部访问
- -a 用于设置传递给 vllm serve 的运行参数