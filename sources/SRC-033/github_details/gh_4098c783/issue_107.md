# [Issue #107] Acend 910b和 nvidia H20 相同超参数，同一条训练数据， 对qwen-3vl-8b sft训练forward阶段loss差距在1%以内，backward后最后一层(35层)main_grad的误差小于1%， 传播到第一层 main_grad误差超50%-100%+

source: https://github.com/Ascend/pytorch/issues/107
state: open | updated: 2026-02-13T01:24:16Z
labels: 

## 正文

# 环境配置：
* cann版本 8.2.RC2 
* Megatron-LM: core_v0.12.1 分支
* MindSpeed: https://gitcode.com/Ascend/MindSpeed.git   git checkout 0016137f0dcfeab3308e0d16994046740c0e4ad9
* torch_npu == 2.8.0
* ms-swift==3.12.1
* 机器： 单机8卡910b

# 现象
   1. forward阶段debug参数和loss计算，差别在1%以内
   2. backward后main_grad从第一层开始差别超过50%+ 
   
# 复现步骤
1. 使用带图片的数据(base64编码)对qwen3-vl-8b 进行sft训练
2. 执行了这个函数custom_backward(https://github.com/NVIDIA/Megatron-LM/blob/core_v0.12.1/megatron/core/pipeline_parallel/schedules.py#L130) 后
3. 在https://github.com/NVIDIA/Megatron-LM/blob/core_v0.12.1/megatron/core/pipeline_parallel/schedules.py#L516 
      加如下的debug代码

    ```
    if torch.distributed.get_rank() == 0:
      for name, p in model.named_parameters():
              if p.main_grad is not None:
                  logger.info(
                      f"[DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] {name} "
                      f"norm={p.main_grad.float().norm().item()}"
                  )
    ```
4. 输出结果如下：
     * H20的输出结果
     
     ```
     [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.embedding.word_embeddings.weight norm=369.5640563964844
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_proj.weight norm=293.06585693359375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_qkv.layer_norm_weight norm=1350.11767578125
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_qkv.weight norm=314.1548156738281
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.q_layernorm.weight norm=33.10734558105469
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.k_layernorm.weight norm=7.902230739593506
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc1.layer_norm_weight norm=95.43716430664062
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc1.weight norm=214.80056762695312
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc2.weight norm=321.8753356933594
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_proj.weight norm=115.25340270996094
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_qkv.layer_norm_weight norm=368.7085266113281
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_qkv.weight norm=278.9192199707031
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.q_layernorm.weight norm=2.3332505226135254
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.k_layernorm.weight norm=2.9240903854370117
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc1.layer_norm_weight norm=38.53182601928711
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc1.weight norm=516.7760620117188
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc2.weight norm=269.7215270996094
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_proj.weight norm=136.2752685546875
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_qkv.layer_norm_weight norm=273.37445068359375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_qkv.weight norm=218.71156311035156
     ```
    * 910b的输出结果
    
    ```
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.embedding.word_embeddings.weight norm=547.50244140625
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_proj.weight norm=353.19720458984375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_qkv.weight norm=396.1068115234375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.linear_qkv.layer_norm_weight norm=2109.36181640625
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.q_layernorm.weight norm=24.216489791870117
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.self_attention.k_layernorm.weight norm=9.54883861541748
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc1.weight norm=260.2996826171875
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc1.layer_norm_weight norm=144.19183349609375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.0.mlp.linear_fc2.weight norm=460.2349853515625
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_proj.weight norm=130.13572692871094
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_qkv.weight norm=316.7453918457031
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.linear_qkv.layer_norm_weight norm=518.222900390625
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.q_layernorm.weight norm=2.4155359268188477
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.self_attention.k_layernorm.weight norm=2.4080817699432373
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc1.weight norm=575.1859130859375
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc1.layer_norm_weight norm=47.92668151855469
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.1.mlp.linear_fc2.weight norm=288.777587890625
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_proj.weight norm=149.91061401367188
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_qkv.weight norm=242.90208435058594
    [DEBUG_GRAD_NORM][POST_BACKWARD_LAYER] module.module.language_model.decoder.layers.2.self_attention.linear_qkv.layer_norm_weight norm=372.5679931640625
    
    ```
    
# 训练超参数：
    > --seed 2025 \
    --data_seed 2025 \
    --load ./Qwen3-VL-8B-Instruct-mcore/ \
    --tensor_model_parallel_size 8 \
    --sequence_parallel true \
    --pipeline_model_parallel_size 1 \
    --packing true \
    --freeze_llm false \
    --freeze_vit false \
    --freeze_aligner false \
    --micro_batch_size 1 \
    --global_batch_size 1 \
    --recompute_granularity full \
    --recompute_method uniform \
    --recompute_num_layers 1 \
    --no_load_optim true \
    --no_load_rng true \
    --finetune true \
    --train_type full \
    --cross_entropy_loss_fusion true \
    --lr 2e-5 \
    --lr_warmup_fraction 0.05 \
    --min_lr 2e-6 \
    --max_epochs 3 \
    --dataset ./test1.jsonl \
    --save ./model_out/model_out_v6/run_0017 \
    --save_interval 500 \
    --vit_gradient_checkpointing true \
    --max_length 64000 \
    --seq_length 64000 \
    --num_workers 16 \
    --no_save_optim false \
    --no_save_rng false \
    --dataset_num_proc 16 \
    --log_interval 1

## 评论 (1)

### yunyiyun · 2026-02-13

精度调试可参考
https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/LMaccuracy_0002.html

