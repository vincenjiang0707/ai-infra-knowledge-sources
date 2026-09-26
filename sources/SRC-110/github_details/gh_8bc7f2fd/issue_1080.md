# [Issue #1080] 使用官方推理脚本评测 qwen3-reranker 模型加载有问题，结果很差

source: https://github.com/modelscope/evalscope/issues/1080
state: closed | updated: 2026-08-25T06:56:11Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [✅ ] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [ ✅] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ ✅] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
v2.0.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [✅ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令
python cross_encoder.py


## 错误日志
2025-12-15 04:54:50 - evalscope - INFO: Args: Task config is provided with TaskConfig type.
2025-12-15 04:54:57 - evalscope - INFO: Dump task config to outputs/20251215_045450/configs/task_config_d7aae6.yaml
2025-12-15 04:54:57 - evalscope - INFO: {
    "model": "text_generation",
    "model_id": "text_generation",
    "model_args": {},
    "model_task": "text_generation",
    "chat_template": null,
    "datasets": [],
    "dataset_args": {},
    "dataset_dir": "/root/.cache/modelscope/hub/datasets",
    "dataset_hub": "modelscope",
    "repeats": 1,
    "generation_config": {
        "batch_size": 1
    },
    "eval_type": "mock_llm",
    "eval_backend": "RAGEval",
    "eval_config": {
        "tool": "MTEB",
        "model": [
            {
                "model_name_or_path": "Qwen/Qwen3-Embedding-0.6B",
                "is_cross_encoder": false,
                "max_seq_length": 512,
                "model_kwargs": {
                    "torch_dtype": "auto"
                },
                "encode_kwargs": {
                    "batch_size": 256
                }
            },
            {
                "model_name_or_path": "Qwen/Qwen3-Reranker-0.6B",
                "is_cross_encoder": true,
                "max_seq_length": 2042,
                "prompt": "",
                "model_kwargs": {
                    "torch_dtype": "auto"
                },
                "encode_kwargs": {
                    "batch_size": 256
                }
            }
        ],
        "eval": {
            "tasks": [
                "T2Retrieval"
            ],
            "verbosity": 2,
            "overwrite_results": true,
            "top_k": 100,
            "limits": 500,
            "output_folder": "outputs/20251215_045450"
        }
    },
    "limit": null,
    "eval_batch_size": 1,
    "use_cache": null,
    "rerun_review": false,
    "work_dir": "outputs/20251215_045450",
    "ignore_errors": false,
    "debug": false,
    "seed": 42,
    "api_url": null,
    "timeout": null,
    "stream": null,
    "judge_strategy": "auto",
    "judge_worker_num": 1,
    "judge_model_args": {},
    "analysis_report": false,
    "use_sandbox": false,
    "sandbox_type": "docker",
    "sandbox_manager_config": {},
    "sandbox_config": {}
}
2025-12-15 04:54:57 - evalscope - INFO: Check `mteb` Installed
2025-12-15 04:54:57 - evalscope - INFO: Loading model Qwen/Qwen3-Embedding-0.6B from modelscope
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Embedding-0.6B
2025-12-15 04:54:58,371 - sentence_transformers.SentenceTransformer - INFO: Use pytorch device_name: cuda:0
2025-12-15 04:54:58,371 - sentence_transformers.SentenceTransformer - INFO: Load pretrained SentenceTransformer: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Embedding-0___6B
`torch_dtype` is deprecated! Use `dtype` instead!
2025-12-15 04:55:00,769 - sentence_transformers.SentenceTransformer - INFO: 1 prompt is loaded, with the key: query
2025-12-15 04:55:00 - evalscope - INFO: Loading model Qwen/Qwen3-Reranker-0.6B from modelscope
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Reranker-0.6B
2025-12-15 04:55:01,376 - sentence_transformers.cross_encoder.util - WARNING: The CrossEncoder `automodel_args` argument was renamed and is now deprecated, please use `model_kwargs` instead.
Some weights of Qwen3ForSequenceClassification were not initialized from the model checkpoint at /root/.cache/modelscope/hub/models/Qwen/Qwen3-Reranker-0___6B and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
2025-12-15 04:55:01,744 - sentence_transformers.cross_encoder.CrossEncoder - INFO: Use pytorch device: cuda:0
2025-12-15 04:55:03,645 - mteb.evaluation.MTEB - INFO: 

## Evaluating 1 tasks:
──────────────────────────────────────────────────────────────────────────────────────── Selected tasks  ────────────────────────────────────────────────────────────────────────────────────────
Retrieval
    - T2Retrieval, s2p


2025-12-15 04:55:03,657 - mteb.evaluation.MTEB - INFO: 

********************** Evaluating T2Retrieval **********************

## 运行环境

- 操作系统：linux
- Python版本：Python 3.10.12

## 其他信息

使用官方脚本结果非常不符合预期


















**换机器运行，一阶段结果看着略合理，二阶段仍非常差**


2025-12-15 13:56:57 - evalscope - INFO: Args: Task config is provided with TaskConfig type.
2025-12-15 13:57:02 - evalscope - INFO: Using RAGEvalBackendManager
2025-12-15 13:57:02 - evalscope - INFO: Dump task config to outputs/20251215_135657/configs/task_config_c01b5f.yaml
2025-12-15 13:57:02 - evalscope - INFO: {
    "model": "text_generation",
    "model_id": "text_generation",
    "model_args": {},
    "model_task": "text_generation",
    "chat_template": null,
    "datasets": [],
    "dataset_args": {},
    "dataset_dir": "/root/.cache/modelscope/hub/datasets",
    "dataset_hub": "modelscope",
    "repeats": 1,
    "generation_config": {
        "batch_size": 1
    },
    "eval_type": "mock_llm",
    "eval_backend": "RAGEval",
    "eval_config": {
        "tool": "MTEB",
        "model": [
            {
                "model_name_or_path": "Qwen/Qwen3-Embedding-0.6B",
                "is_cross_encoder": false,
                "max_seq_length": 512,
                "model_kwargs": {
                    "torch_dtype": "auto"
                },
                "encode_kwargs": {
                    "batch_size": 256
                }
            },
            {
                "model_name_or_path": "Qwen/Qwen3-Reranker-0.6B",
                "is_cross_encoder": true,
                "max_seq_length": 2042,
                "prompt": "",
                "model_kwargs": {
                    "torch_dtype": "auto"
                },
                "encode_kwargs": {
                    "batch_size": 256
                }
            }
        ],
        "eval": {
            "tasks": [
                "T2Retrieval"
            ],
            "verbosity": 2,
            "overwrite_results": true,
            "top_k": 100,
            "limits": 500,
            "output_folder": "outputs/20251215_135657"
        }
    },
    "limit": null,
    "eval_batch_size": 1,
    "use_cache": null,
    "rerun_review": false,
    "work_dir": "outputs/20251215_135657",
    "ignore_errors": false,
    "debug": false,
    "seed": 42,
    "api_url": null,
    "timeout": null,
    "stream": null,
    "judge_strategy": "auto",
    "judge_worker_num": 1,
    "judge_model_args": {},
    "analysis_report": false,
    "use_sandbox": false,
    "sandbox_type": "docker",
    "sandbox_manager_config": {},
    "sandbox_config": {},
    "evalscope_version": "1.2.0"
}
2025-12-15 13:57:02 - evalscope - INFO: Check `mteb` Installed
2025-12-15 13:57:02 - evalscope - INFO: Loading model Qwen/Qwen3-Embedding-0.6B from modelscope
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Embedding-0.6B
Downloading [1_Pooling/config.json]: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 313/313 [00:00<00:00, 477B/s]
Downloading [modules.json]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 349/349 [00:00<00:00, 452B/s]
Downloading [configuration.json]: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 73.0/73.0 [00:01<00:00, 62.9B/s]
Downloading [generation_config.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 117/117 [00:01<00:00, 97.4B/s]
Downloading [config.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 727/727 [00:01<00:00, 596B/s]
Downloading [config_sentence_transformers.json]: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 215/215 [00:01<00:00, 175B/s]
Downloading [merges.txt]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.59M/1.59M [00:01<00:00, 1.35MB/s]
Downloading [README.md]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 16.8k/16.8k [00:00<00:00, 28.0kB/s]
Downloading [tokenizer_config.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 9.48k/9.48k [00:00<00:00, 18.8kB/s]
Downloading [tokenizer.json]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10.9M/10.9M [00:00<00:00, 12.6MB/s]
Downloading [vocab.json]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.65M/2.65M [00:00<00:00, 5.02MB/s]
Downloading [model.safetensors]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.11G/1.11G [00:16<00:00, 72.1MB/s]
Processing 12 items: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 12.0/12.0 [00:16<00:00, 1.38s/it]
2025-12-15 13:57:19,487 - sentence_transformers.SentenceTransformer - INFO: Use pytorch device_name: cuda:0
2025-12-15 13:57:19,487 - sentence_transformers.SentenceTransformer - INFO: Load pretrained SentenceTransformer: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Embedding-0___6B
`torch_dtype` is deprecated! Use `dtype` instead!██████████████████████████▏                                                                        | 1.00M/2.65M [00:00<00:00, 1.97MB/s]
2025-12-15 13:57:23,264 - sentence_transformers.SentenceTransformer - INFO: 1 prompt is loaded, with the key: query██▉                              | 8.00M/10.9M [00:00<00:00, 12.4MB/s]
2025-12-15 13:57:23 - evalscope - INFO: Loading model Qwen/Qwen3-Reranker-0.6B from modelscope                                                      | 46.0M/1.11G [00:01<00:20, 55.8MB/s]
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-Reranker-0.6B█████████████████████████▍| 1.10G/1.11G [00:16<00:00, 87.1MB/s]
Downloading [README.md]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 13.0k/13.0k [00:00<00:00, 19.9kB/s]
Downloading [config.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 727/727 [00:00<00:00, 920B/s]
Downloading [tokenizer_config.json]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 9.48k/9.48k [00:00<00:00, 11.6kB/s]
Downloading [generation_config.json]: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 214/214 [00:00<00:00, 254B/s]
Downloading [configuration.json]: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 73.0/73.0 [00:01<00:00, 72.8B/s]
Downloading [merges.txt]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.59M/1.59M [00:01<00:00, 1.66MB/s]
Downloading [tokenizer.json]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10.9M/10.9M [00:01<00:00, 10.8MB/s]
Downloading [vocab.json]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.65M/2.65M [00:00<00:00, 3.68MB/s]
Downloading [model.safetensors]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.11G/1.11G [00:15<00:00, 77.3MB/s]
Processing 9 items: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9.00/9.00 [00:15<00:00, 1.71s/it]
2025-12-15 13:57:39,467 - sentence_transformers.cross_encoder.util - WARNING: The CrossEncoder `automodel_args` argument was renamed and is now deprecated, please use `model_kwargs` instead.oading [model.safetensors]:   0%|                                                                                                               | 1.00M/1.11G [00:01<19:52, 998kB/s]
Some weights of Qwen3ForSequenceClassification were not initialized from the model checkpoint at /root/.cache/modelscope/hub/models/Qwen/Qwen3-Reranker-0___6B and are newly initialized: ['score.weight']l.safetensors]: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▊| 1.11G/1.11G [00:15<00:00, 85.8MB/s]
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
2025-12-15 13:57:39,845 - sentence_transformers.cross_encoder.CrossEncoder - INFO: Use pytorch device: cuda:0
2025-12-15 13:57:43,267 - mteb.evaluation.MTEB - INFO: 

## Evaluating 1 tasks:
──────────────────────────────────────────────────────────────────────────────────── Selected tasks  ────────────────────────────────────────────────────────────────────────────────────
Retrieval
    - T2Retrieval, s2p


2025-12-15 13:57:43,277 - mteb.evaluation.MTEB - INFO: 

********************** Evaluating T2Retrieval **********************
Downloading [README.md]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 590/590 [00:00<00:00, 8.28MB/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 157M/157M [00:01<00:00, 79.5MB/s]
Downloading data: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 817k/817k [00:00<00:00, 35.2MB/s]
Downloading [README.md]: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 505/505 [00:00<00:00, 7.13MB/s]
Downloading data: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.15M/1.15M [00:00<00:00, 38.1MB/s]
2025-12-15 13:58:14,720 - mteb.abstasks.AbsTaskRetrieval - INFO: Subset: default
2025-12-15 13:58:14,720 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: Encoding Queries.
Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:22<00:00, 11.06s/it]
2025-12-15 13:58:36,863 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: Sorting Corpus by document length (Longest first)...
2025-12-15 13:58:36,863 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: Encoding Corpus in batches... Warning: This might take a while!
2025-12-15 13:58:36,864 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: Encoding Batch 1/1...
Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:03<00:00,  1.69s/it]
2025-12-15 13:58:42,111 - mteb.abstasks.AbsTaskRetrieval - INFO: Time taken to retrieve: 27.39 seconds
2025-12-15 13:58:42,675 - root - INFO: 

2025-12-15 13:58:42,779 - mteb.evaluation.MTEB - INFO: Evaluation for T2Retrieval on dev took 28.06 seconds
2025-12-15 13:58:42,779 - mteb.evaluation.MTEB - INFO: Scores: {'default': {'ndcg_at_1': 0.202, 'ndcg_at_3': 0.19798, 'ndcg_at_5': 0.19756, 'ndcg_at_10': 0.19862, 'ndcg_at_20': 0.19958, 'ndcg_at_100': 0.19982, 'ndcg_at_1000': 0.2001, 'map_at_1': 0.07227, 'map_at_3': 0.1448, 'map_at_5': 0.17027, 'map_at_10': 0.19102, 'map_at_20': 0.19699, 'map_at_100': 0.19735, 'map_at_1000': 0.19737, 'recall_at_1': 0.07227, 'recall_at_3': 0.1448, 'recall_at_5': 0.17027, 'recall_at_10': 0.19327, 'recall_at_20': 0.20095, 'recall_at_100': 0.202, 'recall_at_1000': 0.204, 'precision_at_1': 0.202, 'precision_at_3': 0.16867, 'precision_at_5': 0.136, 'precision_at_10': 0.0892, 'precision_at_20': 0.0494, 'precision_at_100': 0.00998, 'precision_at_1000': 0.001, 'mrr_at_1': 0.202, 'mrr_at_3': 0.202, 'mrr_at_5': 0.202, 'mrr_at_10': 0.202, 'mrr_at_20': 0.202, 'mrr_at_100': 0.202, 'mrr_at_1000': 0.20201470588235293, 'nauc_ndcg_at_1_max': np.float64(0.9493417645791185), 'nauc_ndcg_at_1_std': np.float64(0.6304393275159451), 'nauc_ndcg_at_1_diff1': np.float64(0.4015219985397563), 'nauc_ndcg_at_3_max': np.float64(0.9445243696743642), 'nauc_ndcg_at_3_std': np.float64(0.630793643831853), 'nauc_ndcg_at_3_diff1': np.float64(0.3868321190451967), 'nauc_ndcg_at_5_max': np.float64(0.9441238113958046), 'nauc_ndcg_at_5_std': np.float64(0.6294239727695294), 'nauc_ndcg_at_5_diff1': np.float64(0.38705432680650925), 'nauc_ndcg_at_10_max': np.float64(0.9459116275915851), 'nauc_ndcg_at_10_std': np.float64(0.6293664844686931), 'nauc_ndcg_at_10_diff1': np.float64(0.39202983979938794), 'nauc_ndcg_at_20_max': np.float64(0.946741816679458), 'nauc_ndcg_at_20_std': np.float64(0.6299059896669699), 'nauc_ndcg_at_20_diff1': np.float64(0.39354362989492564), 'nauc_ndcg_at_100_max': np.float64(0.9470317208443303), 'nauc_ndcg_at_100_std': np.float64(0.630420548815139), 'nauc_ndcg_at_100_diff1': np.float64(0.3942257836692681), 'nauc_ndcg_at_1000_max': np.float64(0.9455477420410077), 'nauc_ndcg_at_1000_std': np.float64(0.6291092002754137), 'nauc_ndcg_at_1000_diff1': np.float64(0.3930432188496693), 'nauc_map_at_1_max': np.float64(0.7576577859672788), 'nauc_map_at_1_std': np.float64(0.30081488419292984), 'nauc_map_at_1_diff1': np.float64(0.599202643252436), 'nauc_map_at_3_max': np.float64(0.832712778277914), 'nauc_map_at_3_std': np.float64(0.4444359329728862), 'nauc_map_at_3_diff1': np.float64(0.48934280718986106), 'nauc_map_at_5_max': np.float64(0.8893409994002643), 'nauc_map_at_5_std': np.float64(0.5320415474697521), 'nauc_map_at_5_diff1': np.float64(0.4408810743343672), 'nauc_map_at_10_max': np.float64(0.931654140105406), 'nauc_map_at_10_std': np.float64(0.608926028947637), 'nauc_map_at_10_diff1': np.float64(0.3986890382361982), 'nauc_map_at_20_max': np.float64(0.9435959199466725), 'nauc_map_at_20_std': np.float64(0.6284293516037005), 'nauc_map_at_20_diff1': np.float64(0.3870677279340249), 'nauc_map_at_100_max': np.float64(0.9442657059480968), 'nauc_map_at_100_std': np.float64(0.629548106495099), 'nauc_map_at_100_diff1': np.float64(0.3868288839758548), 'nauc_map_at_1000_max': np.float64(0.9441906815974053), 'nauc_map_at_1000_std': np.float64(0.6294817663054669), 'nauc_map_at_1000_diff1': np.float64(0.3867692412598441), 'nauc_recall_at_1_max': np.float64(0.7576577859672788), 'nauc_recall_at_1_std': np.float64(0.30081488419292984), 'nauc_recall_at_1_diff1': np.float64(0.599202643252436), 'nauc_recall_at_3_max': np.float64(0.832712778277914), 'nauc_recall_at_3_std': np.float64(0.4444359329728862), 'nauc_recall_at_3_diff1': np.float64(0.48934280718986106), 'nauc_recall_at_5_max': np.float64(0.8893409994002643), 'nauc_recall_at_5_std': np.float64(0.5320415474697521), 'nauc_recall_at_5_diff1': np.float64(0.4408810743343672), 'nauc_recall_at_10_max': np.float64(0.9340428699333194), 'nauc_recall_at_10_std': np.float64(0.6090741299878732), 'nauc_recall_at_10_diff1': np.float64(0.4064022250832529), 'nauc_recall_at_20_max': np.float64(0.9476356163361913), 'nauc_recall_at_20_std': np.float64(0.6277289674973732), 'nauc_recall_at_20_diff1': np.float64(0.3997699818907322), 'nauc_recall_at_100_max': np.float64(0.9493417645791185), 'nauc_recall_at_100_std': np.float64(0.6304393275159451), 'nauc_recall_at_100_diff1': np.float64(0.4015219985397563), 'nauc_recall_at_1000_max': np.float64(0.9388076151662533), 'nauc_recall_at_1000_std': np.float64(0.6211384301889695), 'nauc_recall_at_1000_diff1': np.float64(0.3931063649820259), 'nauc_precision_at_1_max': np.float64(0.9493417645791185), 'nauc_precision_at_1_std': np.float64(0.6304393275159451), 'nauc_precision_at_1_diff1': np.float64(0.4015219985397563), 'nauc_precision_at_3_max': np.float64(0.9487862286932608), 'nauc_precision_at_3_std': np.float64(0.7027495070151043), 'nauc_precision_at_3_diff1': np.float64(0.2904232218364289), 'nauc_precision_at_5_max': np.float64(0.9367859594768252), 'nauc_precision_at_5_std': np.float64(0.7482132483672789), 'nauc_precision_at_5_diff1': np.float64(0.20912211523227756), 'nauc_precision_at_10_max': np.float64(0.9355499566529519), 'nauc_precision_at_10_std': np.float64(0.8034529432055306), 'nauc_precision_at_10_diff1': np.float64(0.14144974562299742), 'nauc_precision_at_20_max': np.float64(0.9392691846952702), 'nauc_precision_at_20_std': np.float64(0.8198795258623224), 'nauc_precision_at_20_diff1': np.float64(0.12155038741463776), 'nauc_precision_at_100_max': np.float64(0.9384620036013449), 'nauc_precision_at_100_std': np.float64(0.8203659138572706), 'nauc_precision_at_100_diff1': np.float64(0.12264341277727421), 'nauc_precision_at_1000_max': np.float64(0.9365593334572838), 'nauc_precision_at_1000_std': np.float64(0.8185460630287257), 'nauc_precision_at_1000_diff1': np.float64(0.12131286604071767), 'nauc_mrr_at_1_max': np.float64(0.9493417645791185), 'nauc_mrr_at_1_std': np.float64(0.6304393275159451), 'nauc_mrr_at_1_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_3_max': np.float64(0.9493417645791185), 'nauc_mrr_at_3_std': np.float64(0.6304393275159451), 'nauc_mrr_at_3_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_5_max': np.float64(0.9493417645791185), 'nauc_mrr_at_5_std': np.float64(0.6304393275159451), 'nauc_mrr_at_5_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_10_max': np.float64(0.9493417645791185), 'nauc_mrr_at_10_std': np.float64(0.6304393275159451), 'nauc_mrr_at_10_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_20_max': np.float64(0.9493417645791185), 'nauc_mrr_at_20_std': np.float64(0.6304393275159451), 'nauc_mrr_at_20_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_100_max': np.float64(0.9493417645791185), 'nauc_mrr_at_100_std': np.float64(0.6304393275159451), 'nauc_mrr_at_100_diff1': np.float64(0.4015219985397563), 'nauc_mrr_at_1000_max': np.float64(0.949264009115006), 'nauc_mrr_at_1000_std': np.float64(0.6303706750258413), 'nauc_mrr_at_1000_diff1': np.float64(0.40145988042585495), 'main_score': 0.19862}}
2025-12-15 13:58:42,833 - mteb.evaluation.MTEB - INFO: 

## Evaluating 1 tasks:
──────────────────────────────────────────────────────────────────────────────────── Selected tasks  ────────────────────────────────────────────────────────────────────────────────────
Retrieval
    - T2Retrieval, s2p


2025-12-15 13:58:42,842 - mteb.evaluation.MTEB - INFO: 

********************** Evaluating T2Retrieval **********************
2025-12-15 13:58:42,846 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: The custom predict function of the model will be used if not a SentenceTransformer CrossEncoder
2025-12-15 13:58:42,901 - mteb.abstasks.AbsTaskRetrieval - INFO: Subset: default
2025-12-15 13:58:43,128 - mteb.evaluation.evaluators.RetrievalEvaluator - INFO: Reranking the top 100 in batches... This might take a while!
... ...
2025-12-15 15:15:36,106 - mteb.abstasks.AbsTaskRetrieval - INFO: Time taken to retrieve: 4613.20 seconds                                                                                 
2025-12-15 15:15:36,274 - root - INFO: 

2025-12-15 15:15:36,310 - mteb.evaluation.MTEB - INFO: Evaluation for T2Retrieval on dev took 4613.46 seconds
2025-12-15 15:15:36,311 - mteb.evaluation.MTEB - INFO: Scores: {'default': {'ndcg_at_1': 0.012, 'ndcg_at_3': 0.00853, 'ndcg_at_5': 0.01006, 'ndcg_at_10': 0.01456, 'ndcg_at_20': 0.02125, 'ndcg_at_100': 0.06573, 'ndcg_at_1000': 0.06573, 'map_at_1': 0.00218, 'map_at_3': 0.00284, 'map_at_5': 0.00405, 'map_at_10': 0.00614, 'map_at_20': 0.0083, 'map_at_100': 0.01711, 'map_at_1000': 0.01711, 'recall_at_1': 0.00218, 'recall_at_3': 0.0041, 'recall_at_5': 0.00882, 'recall_at_10': 0.01997, 'recall_at_20': 0.03884, 'recall_at_100': 0.202, 'recall_at_1000': 0.202, 'precision_at_1': 0.012, 'precision_at_3': 0.00733, 'precision_at_5': 0.0084, 'precision_at_10': 0.0098, 'precision_at_20': 0.0091, 'precision_at_100': 0.00998, 'precision_at_1000': 0.001, 'mrr_at_1': 0.012, 'mrr_at_3': 0.016666666666666666, 'mrr_at_5': 0.020266666666666665, 'mrr_at_10': 0.023779365079365077, 'mrr_at_20': 0.02605000595379852, 'mrr_at_100': 0.028638698583713682, 'mrr_at_1000': 0.028638698583713682, 'nauc_ndcg_at_1_max': np.float64(-0.23987121008854306), 'nauc_ndcg_at_1_std': np.float64(-0.40747696985958326), 'nauc_ndcg_at_1_diff1': np.float64(0.1875503085591628), 'nauc_ndcg_at_3_max': np.float64(-0.15583720592170744), 'nauc_ndcg_at_3_std': np.float64(-0.3536352402259292), 'nauc_ndcg_at_3_diff1': np.float64(0.2560628680830475), 'nauc_ndcg_at_5_max': np.float64(-0.08756227836395074), 'nauc_ndcg_at_5_std': np.float64(-0.1137462637300806), 'nauc_ndcg_at_5_diff1': np.float64(0.13088786426971247), 'nauc_ndcg_at_10_max': np.float64(-0.0861297683165672), 'nauc_ndcg_at_10_std': np.float64(-0.04765525833205302), 'nauc_ndcg_at_10_diff1': np.float64(0.06365977964952514), 'nauc_ndcg_at_20_max': np.float64(-0.058632798694416156), 'nauc_ndcg_at_20_std': np.float64(-0.061841100017689214), 'nauc_ndcg_at_20_diff1': np.float64(0.007304431909071098), 'nauc_ndcg_at_100_max': np.float64(-0.044786114561680086), 'nauc_ndcg_at_100_std': np.float64(0.0018072103701367566), 'nauc_ndcg_at_100_diff1': np.float64(0.04557376573583587), 'nauc_ndcg_at_1000_max': np.float64(-0.044786114561680086), 'nauc_ndcg_at_1000_std': np.float64(0.0018072103701367566), 'nauc_ndcg_at_1000_diff1': np.float64(0.04557376573583587), 'nauc_map_at_1_max': np.float64(-0.1248820589633115), 'nauc_map_at_1_std': np.float64(-0.43295508333854976), 'nauc_map_at_1_diff1': np.float64(0.43747140202032814), 'nauc_map_at_3_max': np.float64(-0.015306817288617566), 'nauc_map_at_3_std': np.float64(-0.4120256173276552), 'nauc_map_at_3_diff1': np.float64(0.4408896394917247), 'nauc_map_at_5_max': np.float64(-0.0244535297426149), 'nauc_map_at_5_std': np.float64(-0.18359970599998832), 'nauc_map_at_5_diff1': np.float64(0.26243450093413073), 'nauc_map_at_10_max': np.float64(-0.05842139534654668), 'nauc_map_at_10_std': np.float64(-0.12452232707039987), 'nauc_map_at_10_diff1': np.float64(0.14819988355952846), 'nauc_map_at_20_max': np.float64(-0.043845907402438544), 'nauc_map_at_20_std': np.float64(-0.13206260792719893), 'nauc_map_at_20_diff1': np.float64(0.06574220937876643), 'nauc_map_at_100_max': np.float64(-0.05081749334621512), 'nauc_map_at_100_std': np.float64(-0.05571306295063277), 'nauc_map_at_100_diff1': np.float64(0.055034807825767786), 'nauc_map_at_1000_max': np.float64(-0.05081749334621512), 'nauc_map_at_1000_std': np.float64(-0.05571306295063277), 'nauc_map_at_1000_diff1': np.float64(0.055034807825767786), 'nauc_recall_at_1_max': np.float64(-0.1248820589633115), 'nauc_recall_at_1_std': np.float64(-0.43295508333854976), 'nauc_recall_at_1_diff1': np.float64(0.43747140202032814), 'nauc_recall_at_3_max': np.float64(0.1109885893405749), 'nauc_recall_at_3_std': np.float64(-0.40475338857058935), 'nauc_recall_at_3_diff1': np.float64(0.4400258295080257), 'nauc_recall_at_5_max': np.float64(0.020949977644053278), 'nauc_recall_at_5_std': np.float64(0.026292637634821727), 'nauc_recall_at_5_diff1': np.float64(0.12029377833335436), 'nauc_recall_at_10_max': np.float64(-0.04689322104666373), 'nauc_recall_at_10_std': np.float64(0.02568289063700469), 'nauc_recall_at_10_diff1': np.float64(0.01852511276097216), 'nauc_recall_at_20_max': np.float64(-0.03781630861141582), 'nauc_recall_at_20_std': np.float64(-0.03557870612369707), 'nauc_recall_at_20_diff1': np.float64(-0.04276452250479467), 'nauc_recall_at_100_max': np.float64(-0.022862142055341397), 'nauc_recall_at_100_std': np.float64(0.016615901218049095), 'nauc_recall_at_100_diff1': np.float64(0.04974156258945588), 'nauc_recall_at_1000_max': np.float64(-0.022862142055341397), 'nauc_recall_at_1000_std': np.float64(0.016615901218049095), 'nauc_recall_at_1000_diff1': np.float64(0.04974156258945588), 'nauc_precision_at_1_max': np.float64(-0.23987121008854306), 'nauc_precision_at_1_std': np.float64(-0.40747696985958326), 'nauc_precision_at_1_diff1': np.float64(0.1875503085591628), 'nauc_precision_at_3_max': np.float64(-0.14820596629021646), 'nauc_precision_at_3_std': np.float64(-0.3260970314901092), 'nauc_precision_at_3_diff1': np.float64(0.23099251164719367), 'nauc_precision_at_5_max': np.float64(-0.08578328030970912), 'nauc_precision_at_5_std': np.float64(-0.011844072214343268), 'nauc_precision_at_5_diff1': np.float64(-0.011537429568017286), 'nauc_precision_at_10_max': np.float64(-0.10717160489095025), 'nauc_precision_at_10_std': np.float64(0.010858435136866653), 'nauc_precision_at_10_diff1': np.float64(0.0012210948237625615), 'nauc_precision_at_20_max': np.float64(-0.06976090347058438), 'nauc_precision_at_20_std': np.float64(-0.02600200652861682), 'nauc_precision_at_20_diff1': np.float64(-0.06754721113238665), 'nauc_precision_at_100_max': np.float64(-0.08811782921578004), 'nauc_precision_at_100_std': np.float64(0.028800293968357663), 'nauc_precision_at_100_diff1': np.float64(0.004072880430579931), 'nauc_precision_at_1000_max': np.float64(-0.08811782921578017), 'nauc_precision_at_1000_std': np.float64(0.02880029396835765), 'nauc_precision_at_1000_diff1': np.float64(0.00407288043057982), 'nauc_mrr_at_1_max': np.float64(-0.23987121008854306), 'nauc_mrr_at_1_std': np.float64(-0.40747696985958326), 'nauc_mrr_at_1_diff1': np.float64(0.1875503085591628), 'nauc_mrr_at_3_max': np.float64(-0.19470351489133342), 'nauc_mrr_at_3_std': np.float64(-0.31767104910115374), 'nauc_mrr_at_3_diff1': np.float64(0.2074268848940167), 'nauc_mrr_at_5_max': np.float64(-0.17481341702794692), 'nauc_mrr_at_5_std': np.float64(-0.17048070269583274), 'nauc_mrr_at_5_diff1': np.float64(0.14146060751556924), 'nauc_mrr_at_10_max': np.float64(-0.14982698682439846), 'nauc_mrr_at_10_std': np.float64(-0.1327537911494977), 'nauc_mrr_at_10_diff1': np.float64(0.09816054096032607), 'nauc_mrr_at_20_max': np.float64(-0.13947184639675192), 'nauc_mrr_at_20_std': np.float64(-0.1158270878858878), 'nauc_mrr_at_20_diff1': np.float64(0.08532879658489265), 'nauc_mrr_at_100_max': np.float64(-0.12901049138852355), 'nauc_mrr_at_100_std': np.float64(-0.11359082026066536), 'nauc_mrr_at_100_diff1': np.float64(0.09111958086994935), 'nauc_mrr_at_1000_max': np.float64(-0.12901049138852355), 'nauc_mrr_at_1000_std': np.float64(-0.11359082026066536), 'nauc_mrr_at_1000_diff1': np.float64(0.09111958086994935), 'main_score': 0.01456}}
2025-12-15 15:15:36 - evalscope - INFO: Evaluation results:
+-----------------------+------------+-------------+-------------+---------+----------+--------------+
| Model                 | Revision   | Task Type   | Task        | Split   | Subset   |   Main Score |
+=======================+============+=============+=============+=========+==========+==============+
| Qwen3-Reranker-0___6B | master     | Retrieval   | T2Retrieval | dev     | default  |      0.01456 |
+-----------------------+------------+-------------+-------------+---------+----------+--------------+

## 评论 (1)

### Yunnglin · 2026-08-24

`Qwen3-Reranker-0.6B` is a generative (CausalLM-based) reranker: it scores via its own yes/no token logits, which `CrossEncoder` only supports through the `LogitScore` module added in **sentence-transformers 5.4.0**. On anything older, `CrossEncoder` silently falls back to `AutoModelForSequenceClassification` with a randomly-initialised head — that's the `Some weights of Qwen3ForSequenceClassification were not initialized ... ['score.weight']` line in your log — and returns meaningless scores without erroring. It's the sentence-transformers version, not evalscope.

```
pip install -U "sentence-transformers>=5.4.0"
```

Verified on 5.6.0: the model then loads the correct chain (`['Transformer', 'LogitScore']`) and separates relevant from irrelevant documents cleanly (`[7.625, -11.375]`). No config change needed.

Keeping this open until we raise the floor in `requirements/rag.txt` so an unsupported version fails loudly instead of silently (#1620).

