# [Issue #251] EAGLE-3 Training and Test Data

source: https://github.com/SafeAILab/EAGLE/issues/251
state: open | updated: 2025-08-21T00:21:42Z
labels: 

## 正文

In the newly added code for EAGLE-3 training, there is references to the training data of "/home/lyh/code/nlp/developing/vllmbase/vllm/gedata/l318b.jsonl" and the testing data of "/home/lyh/code/nlp/developing/vllmbase/vllm/gedata/0318.json"?

Do paths refer to the training and test data used in the EAGLE-3 paper? If so, can information be provided on how to access this data, or to extract it ourselves from the relevant datasets?

## 评论 (21)

### jiahe7ay · 2025-07-02

We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.

We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.

https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3

https://huggingface.co/Tengyunw/qwen3_8b_eagle3

Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.

https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA

https://zhuanlan.zhihu.com/p/1923763301432662012


### hongyanz · 2025-07-02

@jiahe7ay That is a great news! Thank you for reproducing EAGLE-3. We will update our Readme to include your link.

### jiahe7ay · 2025-07-02

> [@jiahe7ay](https://github.com/jiahe7ay) That is a great news! Thank you for reproducing EAGLE-3. We will update our Readme to include your link.

Thank you very much. I’m also very happy to contribute to such an outstanding project like Eagle. Thank you for open-sourcing it!

### jiahe7ay · 2025-07-02

<img width="1056" alt="Image" src="https://github.com/user-attachments/assets/3c71b180-2062-411e-bdf5-2270a68c84bd" /> @hongyanz  By the way, this is the accept  length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500. 

### zxyscz · 2025-07-03

> We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.
> 
> We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.
> 
> https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3
> 
> https://huggingface.co/Tengyunw/qwen3_8b_eagle3
> 
> Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.
> 
> https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA
> 
> https://zhuanlan.zhihu.com/p/1923763301432662012

During the training process, is config.json replaced with the one for Qwen3?

### jiahe7ay · 2025-07-03

> > We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.
> > We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.
> > https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3
> > https://huggingface.co/Tengyunw/qwen3_8b_eagle3
> > Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.
> > https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA
> > https://zhuanlan.zhihu.com/p/1923763301432662012
> 
> During the training process, is config.json replaced with the one for Qwen3?

@zxyscz  yes,but the name of architectures is not LlamaForCausalLMEagle3,also is LlamaForCausalLM

### MMuzzammil1 · 2025-07-04

> <img alt="Image" width="1056" src="https://private-user-images.githubusercontent.com/33346376/461611963-3c71b180-2062-411e-bdf5-2270a68c84bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2MDM1MjcsIm5iZiI6MTc1MTYwMzIyNywicGF0aCI6Ii8zMzM0NjM3Ni80NjE2MTE5NjMtM2M3MWIxODAtMjA2Mi00MTFlLWJkZjUtMjI3MGE2OGM4NGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzA0VDA0MjcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZlZTBhZDNkNzQ5ZjQwMmE4NDgzZjMxMTBlOGVjMzczNWQyMTE1NjE1MzE1MGJmNzdhYjIxNTJlMTllMGFjYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.RqmbYcZyz4q_cNg10ULlhNeCObG0WAVmb-8eIoXlfLU"> [@hongyanz](https://github.com/hongyanz) By the way, this is the accept length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500.

@jiahe7ay May I ask which code generation benchmark are you using?

### jiahe7ay · 2025-07-04

> > <img alt="Image" width="1056" src="https://private-user-images.githubusercontent.com/33346376/461611963-3c71b180-2062-411e-bdf5-2270a68c84bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2MDM1MjcsIm5iZiI6MTc1MTYwMzIyNywicGF0aCI6Ii8zMzM0NjM3Ni80NjE2MTE5NjMtM2M3MWIxODAtMjA2Mi00MTFlLWJkZjUtMjI3MGE2OGM4NGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzA0VDA0MjcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZlZTBhZDNkNzQ5ZjQwMmE4NDgzZjMxMTBlOGVjMzczNWQyMTE1NjE1MzE1MGJmNzdhYjIxNTJlMTllMGFjYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.RqmbYcZyz4q_cNg10ULlhNeCObG0WAVmb-8eIoXlfLU"> [@hongyanz](https://github.com/hongyanz) By the way, this is the accept length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500.
> 
> [@jiahe7ay](https://github.com/jiahe7ay) May I ask which code generation benchmark are you using?

just ulral_chat_200k，but But we regenerated it using the model. We have now open-sourced our training data regenerated using Qwen3-8B.  https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3

### MMuzzammil1 · 2025-07-04

> > > <img alt="Image" width="1056" src="https://private-user-images.githubusercontent.com/33346376/461611963-3c71b180-2062-411e-bdf5-2270a68c84bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2MDM1MjcsIm5iZiI6MTc1MTYwMzIyNywicGF0aCI6Ii8zMzM0NjM3Ni80NjE2MTE5NjMtM2M3MWIxODAtMjA2Mi00MTFlLWJkZjUtMjI3MGE2OGM4NGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzA0VDA0MjcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZlZTBhZDNkNzQ5ZjQwMmE4NDgzZjMxMTBlOGVjMzczNWQyMTE1NjE1MzE1MGJmNzdhYjIxNTJlMTllMGFjYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.RqmbYcZyz4q_cNg10ULlhNeCObG0WAVmb-8eIoXlfLU"> [@hongyanz](https://github.com/hongyanz) By the way, this is the accept length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500.
> > 
> > 
> > [@jiahe7ay](https://github.com/jiahe7ay) May I ask which code generation benchmark are you using?
> 
> just ulral_chat_200k，but But we regenerated it using the model. We have now open-sourced our training data regenerated using Qwen3-8B. https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3

Thanks for the reply and the link to the dataset. Another quick question, the tokens/s you've reported is in the held-out test set of ultra_chat_200k right (sequences not used in training)?

### jiahe7ay · 2025-07-04

> > > > <img alt="Image" width="1056" src="https://private-user-images.githubusercontent.com/33346376/461611963-3c71b180-2062-411e-bdf5-2270a68c84bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2MDM1MjcsIm5iZiI6MTc1MTYwMzIyNywicGF0aCI6Ii8zMzM0NjM3Ni80NjE2MTE5NjMtM2M3MWIxODAtMjA2Mi00MTFlLWJkZjUtMjI3MGE2OGM4NGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzA0VDA0MjcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZlZTBhZDNkNzQ5ZjQwMmE4NDgzZjMxMTBlOGVjMzczNWQyMTE1NjE1MzE1MGJmNzdhYjIxNTJlMTllMGFjYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.RqmbYcZyz4q_cNg10ULlhNeCObG0WAVmb-8eIoXlfLU"> [@hongyanz](https://github.com/hongyanz) By the way, this is the accept length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500.
> > > 
> > > 
> > > [@jiahe7ay](https://github.com/jiahe7ay) May I ask which code generation benchmark are you using?
> > 
> > 
> > just ulral_chat_200k，but But we regenerated it using the model. We have now open-sourced our training data regenerated using Qwen3-8B. https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3
> 
> Thanks for the reply and the link to the dataset. Another quick question, the tokens/s you've reported is in the held-out test set of ultra_chat_200k right (sequences not used in training)?

@MMuzzammil1  The test dataset which I used the ShareGPT dataset, not ultra_chat_200k. The code generation example above was just something I wrote casually, mainly to have it generate a bubble sort for me

### jiahe7ay · 2025-07-04

> > > > <img alt="Image" width="1056" src="https://private-user-images.githubusercontent.com/33346376/461611963-3c71b180-2062-411e-bdf5-2270a68c84bd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE2MDM1MjcsIm5iZiI6MTc1MTYwMzIyNywicGF0aCI6Ii8zMzM0NjM3Ni80NjE2MTE5NjMtM2M3MWIxODAtMjA2Mi00MTFlLWJkZjUtMjI3MGE2OGM4NGJkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzA0VDA0MjcwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZlZTBhZDNkNzQ5ZjQwMmE4NDgzZjMxMTBlOGVjMzczNWQyMTE1NjE1MzE1MGJmNzdhYjIxNTJlMTllMGFjYmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.RqmbYcZyz4q_cNg10ULlhNeCObG0WAVmb-8eIoXlfLU"> [@hongyanz](https://github.com/hongyanz) By the way, this is the accept length for Qwen3-8B-Eagle3 in code generation, and its TPS (tokens per second) can reach nearly 500.
> > > 
> > > 
> > > [@jiahe7ay](https://github.com/jiahe7ay) May I ask which code generation benchmark are you using?
> > 
> > 
> > just ulral_chat_200k，but But we regenerated it using the model. We have now open-sourced our training data regenerated using Qwen3-8B. https://huggingface.co/datasets/Tengyunw/qwen3_8b_eagle3
> 
> Thanks for the reply and the link to the dataset. Another quick question, the tokens/s you've reported is in the held-out test set of ultra_chat_200k right (sequences not used in training)?

@MMuzzammil1  Additionally, I tested the performance of eagle3-qwen-8b on an RTX 5090 across eagle official benchmark datasets including GSM8K, MT-Bench, Alpaca, and HumanEval. The performance improvement was even more significant, with tokens per second (TPS) increasing from around 90 to approximately 220. I’ve updated the README on Hugging Face accordingly.

### zxyscz · 2025-07-07

@jiahe7ay dou you have this question when inference with eagle3 ? sglang version==0.4.8

<img width="1027" height="159" alt="Image" src="https://github.com/user-attachments/assets/fcdfbff5-d3ac-41f3-8c7c-094ca9253184" />

### c-dafan · 2025-07-10

I have a question that Qwen3-30B-A3B eagle head_dim is 64, but head_dim of Qwen3-30B-A3B is 128. They are different. 

### c-dafan · 2025-07-14

Hello. I have run this on vLLM with num_spec_tokens=1(draft token=1). When testing with the GSM8K dataset, the accept ratio came out to be 60%. Would you please tell me the accept ratio for Sglang?

### MMuzzammil1 · 2025-07-23

@jiahe7ay do you have some results for temperature=1 for this draft model? Or you have mostly tested it for t=0?


### seohyunwoo-0407 · 2025-07-24

@jiahe7ay Thanks for your description, I successed porting EAGLE3 on model "OLMoE-1B-7B-0125-Instruct"! "https://huggingface.co/wantsleep/OLMoE_1B_7B_Eagle3" Here is draft model of OLMoE! Thank you!

### hongyanz · 2025-07-24

@seohyunwoo-0407  Great. Thanks for open sourcing your EAGLE head weight. We will broadcast your weight on our Readme too.

### fan-niu · 2025-08-07

@jiahe7ay Hi thanks a lot for your works, I use deepspeed zero3, 16384 or 32768 length in llama3-8b 8xh100, batch=1 and still get OOM. How do you avoid OOM problems? thanks. CC: @hongyanz  

### hongyanz · 2025-08-17

@fan-niu We only trained model with 2k context length before.

### fan-niu · 2025-08-20

@hongyanz @jiahe7ay thanks a lot for those works, when I use the ultra_chat 200k data (without regenerating the assistant data from the target model) to train the llama3.1-8b-instruct model, the training acc is only around 35%. After 10 rounds of training, lr dropped from the initial 5e-5 to only 4.7e-5. I used 16xh100 and train_micro_batch_size_per_gpu=1 / gradient_accumulation_steps=2.  I found that there are errors in the loss mask processing.It was found that the loss_mask generation method did not match the tokenizer. This problem has been fixed. Now it is ensured that the token after assistant is set to 1.  Can we have a channel to discuss this issue? Thanks a lot. 

training script:

DS_CONFIG=ds_config.json
#DS_CONFIG=ds_config_zero3.json
#DS_CONFIG=ds_config_zero3_offload.json

torchrun \
    --nnodes ${WORLD_SIZE} \
    --nproc_per_node=${GPU_NUM} \
    --node_rank ${RANK} \
    --master_addr ${MASTER_ADDR} \
    --master_port ${MASTER_PORT} \
        main.py \
        --basepath $model_path \
        --trainpath $train_data_set \
        --testpath $test_data_set \
        --savedir $savedir \
        --deepspeed_config $DS_CONFIG



config.json

{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "bos_token_id": 128000,
  "eos_token_id": [
    128001,
    128008,
    128009
  ],
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 2048,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_key_value_heads": 8,
  "num_hidden_layers": 1,
  "pad_token_id": 128009,
  "rms_norm_eps": 1e-05,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.28.1",
  "use_cache": true,
  "vocab_size": 128256,
  "draft_vocab_size": 32000
}



ds_config.json :

    "bf16": {
        "enabled": "true"
    },
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": 5e-5,
            "weight_decay": 0.0,
            "adam_w_mode": true,
            "betas": [
                    0.9,
                    0.95
                  ]
        }
    },
    "scheduler": {
        "type": "WarmupDecayLR",
        "params": {
            "warmup_min_lr": 5e-7,
            "warmup_max_lr": 5e-5,
            "warmup_num_steps": 12000,
            "total_num_steps": 800000
        }
    },




### fan-niu · 2025-08-20

> We have successfully trained the Eagle3 versions of Qwen3-8B and Qwen3-30B-A3B based on the official training code, and have open-sourced them. On a single H200 GPU using the sglang inference framework, Qwen3-8B with Eagle3 achieves a performance boost from 186 tokens/second to 365 tokens/second, while Qwen3-30B-A3B with Eagle3 improves from 147 tokens/second to 231 tokens/second.
> 
> We used the ultra_200k test set and re-ran inference on Qwen3 to regenerate the data, which was then used as the final training set.A total of 600K dialogues were used as the training set.
> 
> https://huggingface.co/Tengyunw/qwen3_30b_moe_eagle3
> 
> https://huggingface.co/Tengyunw/qwen3_8b_eagle3
> 
> Additionally, we have also published a report detailing how to reproduce the Eagle3 training process. The report link is provided below for your reference if needed.
> 
> https://mp.weixin.qq.com/s/Dmdg6aLgFHZEcm6TY1vKkA
> 
> https://zhuanlan.zhihu.com/p/1923763301432662012

@jiahe7ay Could you please share your code so we can see how you reproduced? Thank you very much. I've read your article on Zhihu and the changes only in dataprocess and load_model (and possibly the hidden idx). Are these the only changes you made? Thanks a again.
