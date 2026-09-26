# [Issue #1565] 【bert】result exact_match and f1 abnormal

source: https://github.com/mlcommons/inference/issues/1565
state: closed | updated: 2026-05-09T00:41:09Z
labels: Stale

## 正文

In bert Offline accuracy test，I submit multi batch size.
when exec response on lg.QuerySamplesComplete one by one, can get right result. 
```python
def issue_queries(self, query_samples):
        batch_size = self.batch_size
        if len(query_samples) < batch_size:
            batch_size = len(query_samples)

        batch_input_1 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        batch_input_2 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        batch_input_3 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        query_id = np.empty([batch_size], dtype=int)

        batch_counter = 0

        with torch.no_grad():
            for i in range(len(query_samples)):
                print(i)
                eval_features = self.qsl.get_features(query_samples[i].index)

                # import pdb
                # pdb.set_trace()
                batch_input_1[batch_counter % batch_size] = torch.IntTensor(eval_features.input_ids).numpy()
                batch_input_2[batch_counter % batch_size] = torch.IntTensor(eval_features.input_mask).numpy()
                batch_input_3[batch_counter % batch_size] = torch.IntTensor(eval_features.segment_ids).numpy()
                query_id[i % batch_size] = query_samples[i].id

                batch_counter += 1

                if batch_counter % batch_size == 0 or i == (len(query_samples) - 1):

                    model_output = self.model([batch_input_1, batch_input_2, batch_input_3])

                    response = []
                    for idx_output in range(batch_counter):

                        start_scores, end_scores = torch.from_numpy(model_output[0][idx_output]), torch.from_numpy(model_output[1][idx_output])
                        output = torch.stack([start_scores, end_scores], axis=-1).squeeze(0).cpu().numpy()

                        response_array = array.array("B", output.tobytes())
                        bi = response_array.buffer_info()
                        response = lg.QuerySampleResponse(query_id[idx_output], bi[0], bi[1])

                        lg.QuerySamplesComplete([response])

                    batch_counter = 0
```
when exec lg.QuerySamplesComplete for list of response，the exact_match and f1 will be low
```python
def issue_queries(self, query_samples):
        batch_size = self.batch_size
        if len(query_samples) < batch_size:
            batch_size = len(query_samples)

        batch_input_1 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        batch_input_2 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        batch_input_3 = np.empty([batch_size, self.max_seq_length], dtype=np.int32)
        query_id = np.empty([batch_size], dtype=int)

        batch_counter = 0

        with torch.no_grad():
            for i in range(len(query_samples)):
                print(i)
                eval_features = self.qsl.get_features(query_samples[i].index)

                # import pdb
                # pdb.set_trace()
                batch_input_1[batch_counter % batch_size] = torch.IntTensor(eval_features.input_ids).numpy()
                batch_input_2[batch_counter % batch_size] = torch.IntTensor(eval_features.input_mask).numpy()
                batch_input_3[batch_counter % batch_size] = torch.IntTensor(eval_features.segment_ids).numpy()
                query_id[i % batch_size] = query_samples[i].id

                batch_counter += 1

                if batch_counter % batch_size == 0 or i == (len(query_samples) - 1):

                    model_output = self.model([batch_input_1, batch_input_2, batch_input_3])

                    response = []
                    for idx_output in range(batch_counter):

                        start_scores, end_scores = torch.from_numpy(model_output[0][idx_output]), torch.from_numpy(model_output[1][idx_output])
                        output = torch.stack([start_scores, end_scores], axis=-1).squeeze(0).cpu().numpy()

                        response_array = array.array("B", output.tobytes())
                        bi = response_array.buffer_info()
                        response.append(lg.QuerySampleResponse(query_id[idx_output], bi[0], bi[1]))

                    lg.QuerySamplesComplete(response)

                    batch_counter = 0
```

## 评论 (4)

### kevue2627 · 2024-01-29

@arjunsuresh Please help, thanks!


### arjunsuresh · 2024-01-30

[This](https://github.com/mlcommons/inference/blob/master/language/bert/ray_SUT.py) is a backend reference implementation for bert which does support batching. If you are working on a fork of the inference repository can you please share the fork link so that I can test out the run?

### kevue2627 · 2024-01-31

@arjunsuresh I think batching not affect，the diff is
![image](https://github.com/mlcommons/inference/assets/54271065/3bbf2674-74d1-43f6-8a96-f127a97c7098)
![image](https://github.com/mlcommons/inference/assets/54271065/d5a0594c-78dd-4355-a96c-2f9ccda1beb4)
the first one i can get right accuracy, the second one accuracy will be low。maybe it relative to loadgen, I'm confused. Thanks for help me!

### github-actions[bot] · 2026-05-09

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
