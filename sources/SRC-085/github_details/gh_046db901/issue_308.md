# [Issue #308] EAGLE3的qwen和mixtral模型特征拼接的问题

source: https://github.com/SafeAILab/EAGLE/issues/308
state: closed | updated: 2025-10-15T07:30:46Z
labels: 

## 正文

您好，阅读了EAGLE3的论文，并且查看了项目中llama3的实现，应该是把大模型的高、中、低三个层次的hidden_output拼接，然后经过fc层作为了草稿模型的输入。
```python
        for idx, decoder_layer in enumerate(self.layers):
            if idx==len(self.layers)-3 or idx==len(self.layers)//2 or idx==2:
                all_hidden_states += (hidden_states,)
```

<img width="301" height="459" alt="Image" src="https://github.com/user-attachments/assets/bc34fa48-86da-49e8-a008-6b0195ee5bc0" />

但是我看了一下Mixtral和Qwen2的实现（即model/modeling_qwen2_kv.py和model/modeling_mixtral_kv.py），好像并没有在大模型的实现中硬编码三层特征。这里output_hidden_states=True时，在每一层会把当前 hidden_states 追加到 all_hidden_states。
```python
        for idx, decoder_layer in enumerate(self.layers):
            if output_hidden_states:
                all_hidden_states += (hidden_states,)
```

所以我想问一下，对于Mixtral和Qwen2的多层（三层？）特征拼接是没有实现吗？这部分可以仿照llama3的高、中、低三个层次拼接来实现吗？

## 评论 (1)

### hongyanz · 2025-10-15

model/modeling_qwen2_kv.py和model/modeling_mixtral_kv.py两个文件是针对EAGLE-1和EAGLE-2的代码。如果需要EAGLE-3，可以仿照llama3的高、中、低三个层次拼接来实现。
