# [Issue #35] fail to run  examples/offline.py , unable to download the model to reproduce

source: https://github.com/LLMServe/DistServe/issues/35
state: open | updated: 2024-08-13T07:32:28Z
labels: 

## 正文

Hi ,
I am trying to reproduce the result, but it's unable to download the llama2-7b-hf model as below logs printed,


`root@d7b9ced7ced8:/workspace/DistServe# python3 examples/offline.py 
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_errors.py", line 304, in hf_raise_for_status
    response.raise_for_status()
  File "/usr/local/lib/python3.10/dist-packages/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://huggingface.co/meta-llama/Llama-2-7b-hf/resolve/main/config.json

The above exception was the direct cause of the following exception:
Cannot access gated repo for url https://huggingface.co/meta-llama/Llama-2-7b-hf/resolve/main/config.json.
Your request to access model meta-llama/Llama-2-7b-hf has been rejected by the repo's authors.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/workspace/DistServe/examples/offline.py", line 32, in <module>
    model_config=ModelConfig(
  File "/workspace/DistServe/distserve/config.py", line 177, in __init__
    self.hf_config = self._get_hf_config()
  File "/workspace/DistServe/distserve/config.py", line 192, in _get_hf_config
    raise ValueError(
ValueError: Failed to load the model config, please check the model name or path: meta-llama/Llama-2-7b-hf`

, although I login into successfully huggingface-cli login, is there alternative way to acquire the model? thanks

`Token has not been saved to git credential helper.
Your token has been saved to /root/.cache/huggingface/token
Login successful`


## 评论 (13)

### William12github · 2024-08-06

is there alternative way to provide the model except for downloading online directly

### RobertLou · 2024-08-06

You can use this website to download model：https://modelscope.cn/my/overview

### William12github · 2024-08-06

thanks , I have downloaded it manually through meata.com, and convert it into hf format using  convert_llama_weights_to_hf.py, and got the files as following:


root@d7b9ced7ced8:/workspace/DistServe# ls -lt ../lama2-7b-hf/
total 13163352
-rw-r--r-- 1 root root      23950 Aug  6 02:00 model.safetensors.index.json
-rw-r--r-- 1 root root 3590488816 Aug  6 02:00 model-00003-of-00003.safetensors
-rw-r--r-- 1 root root 4947390880 Aug  6 02:00 model-00002-of-00003.safetensors
-rw-r--r-- 1 root root 4938985352 Aug  6 02:00 model-00001-of-00003.safetensors
-rw-r--r-- 1 root root        659 Aug  6 02:00 config.json
-rw-r--r-- 1 root root        111 Aug  6 02:00 generation_config.json
-rw-r--r-- 1 root root    1842622 Aug  6 01:59 tokenizer.json
-rw-r--r-- 1 root root        414 Aug  6 01:59 special_tokens_map.json
-rw-r--r-- 1 root root     499723 Aug  6 01:59 tokenizer.model
-rw-r--r-- 1 root root        960 Aug  6 01:59 tokenizer_config.json

but when I started it with :
$python distserve/api_server/distserve_api_server.py --model ../lama2-7b-hf/
   
it report another issue:

`(ParaWorker pid=30741) INFO 02:18:28 runtime peak memory: 12.706 GB
(ParaWorker pid=30741) INFO 02:18:28 total GPU memory: 44.521 GB
(ParaWorker pid=30741) INFO 02:18:28 kv cache size for one token: 0.50000 MB
(ParaWorker pid=30741) INFO 02:18:28 num_gpu_blocks: 3502
(ParaWorker pid=30741) INFO 02:18:28 num_cpu_blocks: 2048
(ParaWorker pid=30742) Gpt<T>::load() - ../lama2-7b-hf/decoder.embed_tokens.weight.pt not found`

### RobertLou · 2024-08-06

> thanks , I have downloaded it manually through meata.com, and convert it into hf format using convert_llama_weights_to_hf.py, and got the files as following:
> 
> root@d7b9ced7ced8:/workspace/DistServe# ls -lt ../lama2-7b-hf/ total 13163352 -rw-r--r-- 1 root root 23950 Aug 6 02:00 model.safetensors.index.json -rw-r--r-- 1 root root 3590488816 Aug 6 02:00 model-00003-of-00003.safetensors -rw-r--r-- 1 root root 4947390880 Aug 6 02:00 model-00002-of-00003.safetensors -rw-r--r-- 1 root root 4938985352 Aug 6 02:00 model-00001-of-00003.safetensors -rw-r--r-- 1 root root 659 Aug 6 02:00 config.json -rw-r--r-- 1 root root 111 Aug 6 02:00 generation_config.json -rw-r--r-- 1 root root 1842622 Aug 6 01:59 tokenizer.json -rw-r--r-- 1 root root 414 Aug 6 01:59 special_tokens_map.json -rw-r--r-- 1 root root 499723 Aug 6 01:59 tokenizer.model -rw-r--r-- 1 root root 960 Aug 6 01:59 tokenizer_config.json
> 
> but when I started it with : $python distserve/api_server/distserve_api_server.py --model ../lama2-7b-hf/
> 
> it report another issue:
> 
> `(ParaWorker pid=30741) INFO 02:18:28 runtime peak memory: 12.706 GB (ParaWorker pid=30741) INFO 02:18:28 total GPU memory: 44.521 GB (ParaWorker pid=30741) INFO 02:18:28 kv cache size for one token: 0.50000 MB (ParaWorker pid=30741) INFO 02:18:28 num_gpu_blocks: 3502 (ParaWorker pid=30741) INFO 02:18:28 num_cpu_blocks: 2048 (ParaWorker pid=30742) Gpt<T>::load() - ../lama2-7b-hf/decoder.embed_tokens.weight.pt not found`

I encountered the same question before. I can tell you that is because distserver needs to convert the model into another form first. I changed the file distserve/downloader/downloader.py to solve this. You can replace the same part in this file. Here's my code:
```
        if is_local:
            if model_name_or_path[-1] == '/':
                allow_patterns = "*.bin"
                hf_files = os.path.join(model_name_or_path, allow_patterns)
                cache_dir = DISTSERVE_CACHE
                storage_folder = \
                    os.path.join(cache_dir, 
                                repo_folder_name(repo_id=model_name_or_path)) + '/'
                done_file = os.path.join(storage_folder, "done")
                if os.path.exists(done_file):
                    logger.info(f"Find cached model weights in {storage_folder}.")    
                    return storage_folder
                
                # download and convert model weights
                convert_weights(hf_files, storage_folder, dtype, model)
                file = open(done_file, 'w')
                file.close()
                return storage_folder
            else:
                return model_name_or_path + '/'
```

### William12github · 2024-08-06

but I don't have the .bin file in the folder , only got these files:

> root@d7b9ced7ced8:/workspace/DistServe# ls -lt ../lama2-7b-hf/
total 13163352
-rw-r--r-- 1 root root      23950 Aug  6 02:00 model.safetensors.index.json
-rw-r--r-- 1 root root 3590488816 Aug  6 02:00 model-00003-of-00003.safetensors
-rw-r--r-- 1 root root 4947390880 Aug  6 02:00 model-00002-of-00003.safetensors
-rw-r--r-- 1 root root 4938985352 Aug  6 02:00 model-00001-of-00003.safetensors
-rw-r--r-- 1 root root        659 Aug  6 02:00 config.json
-rw-r--r-- 1 root root        111 Aug  6 02:00 generation_config.json
-rw-r--r-- 1 root root    1842622 Aug  6 01:59 tokenizer.json
-rw-r--r-- 1 root root        414 Aug  6 01:59 special_tokens_map.json
-rw-r--r-- 1 root root     499723 Aug  6 01:59 tokenizer.model
-rw-r--r-- 1 root root        960 Aug  6 01:59 tokenizer_config.json

### RobertLou · 2024-08-06

> but I don't have the .bin file in the folder , only got these files:
> 
> > root@d7b9ced7ced8:/workspace/DistServe# ls -lt ../lama2-7b-hf/
> > total 13163352
> > -rw-r--r-- 1 root root      23950 Aug  6 02:00 model.safetensors.index.json
> > -rw-r--r-- 1 root root 3590488816 Aug  6 02:00 model-00003-of-00003.safetensors
> > -rw-r--r-- 1 root root 4947390880 Aug  6 02:00 model-00002-of-00003.safetensors
> > -rw-r--r-- 1 root root 4938985352 Aug  6 02:00 model-00001-of-00003.safetensors
> > -rw-r--r-- 1 root root        659 Aug  6 02:00 config.json
> > -rw-r--r-- 1 root root        111 Aug  6 02:00 generation_config.json
> > -rw-r--r-- 1 root root    1842622 Aug  6 01:59 tokenizer.json
> > -rw-r--r-- 1 root root        414 Aug  6 01:59 special_tokens_map.json
> > -rw-r--r-- 1 root root     499723 Aug  6 01:59 tokenizer.model
> > -rw-r--r-- 1 root root        960 Aug  6 01:59 tokenizer_config.json

https://modelscope.cn/models/shakechen/Llama-2-7b-hf/files It has *.bin files, maybe download it again?

### William12github · 2024-08-06

Hi Robert,
Appreciated for your great help.

Is it necessary to download all the files ? it will take too much time to download all.
and if I want to run examples/offline.py ,how to specify the local dir in the code?

### RobertLou · 2024-08-06

> Hi Robert, Appreciated for your great help.
> 
> Is it necessary to download all the files ? it will take too much time to download all. and if I want to run examples/offline.py ,how to specify the local dir in the code?

I'm not sure, but according to the code, *.bin is necessary. You can use --model to specify the local dir, like 

> python offfline.py --model ../Llama2-7b-hf/
By the way, if you have any question, checking the code is the fastest way. You can find '--model' args in offline.py which helps you to specify the local dir.

### William12github · 2024-08-06

Hi Robert ,
Thank you for your enthusiastic help and good advice!

### William12github · 2024-08-06

I am able to run the examples/offline.py code, got following result :

> INFO 13:00:01 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 13:00:01 (decoding) GPU blocks: 3 / 941 (0.32%) used, (0 swapping out)
INFO 13:00:01 (decoding) 0 unaccepted, 0 waiting, 2 processing
INFO 13:00:02 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
INFO 13:00:02 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 13:00:02 (decoding) GPU blocks: 2 / 941 (0.21%) used, (0 swapping out)
INFO 13:00:02 (decoding) 0 unaccepted, 0 waiting, 1 processing
INFO 13:00:03 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
INFO 13:00:03 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 13:00:03 (decoding) GPU blocks: 3 / 941 (0.32%) used, (0 swapping out)
INFO 13:00:03 (decoding) 0 unaccepted, 0 waiting, 1 processing
Prompt: 'Life blooms like a flower. Far away or by the road. Waiting', Generated text: for the right time to blo om . Ћ 
 (10 tokens generated).
Prompt: 'A quick brown fox', Generated text: j umps over the lazy dog . 
 (8 tokens generated).
Prompt: 'Artificial intelligence is', Generated text: a hot topic in the te ch world . The term is thrown around a lot , but what does it really mean ? 
 (25 tokens generated).
Prompt: 'To be or not to be,', Generated text: that is the question . 
 (6 tokens generated).
Prompt: 'one two three four', Generated text: five six seven eight nine ten eleven eleven twelve th ir teen fifteen six teen sevent een eigh teen nin ete en twenty one twenty - one twenty - two twenty - three twenty - four twenty - five twenty - six twenty - se ven twenty - one twenty - two 
 (53 tokens generated).
(ParaWorker pid=5130) INFO 13:00:00 (worker context.#0) model /workspace/Llama-2-7b-hf/ loaded
(ParaWorker pid=5130) INFO 13:00:00 runtime peak memory: 12.497 GB
(ParaWorker pid=5130) INFO 13:00:00 total GPU memory: 22.059 GB
(ParaWorker pid=5130) INFO 13:00:00 kv cache size for one token: 0.50000 MB
(ParaWorker pid=5130) INFO 13:00:00 num_gpu_blocks: 941
(ParaWorker pid=5130) INFO 13:00:00 num_cpu_blocks: 128
root@5a65df8f9a43:/workspace/DistServe# 

but I'm still confused :
1. how to know the performance of the testing?
2. if I want to comapre it with colocate solution (both prefill and decoding phase run in the single GPU) , how to launch the testing ?

### Youhe-Jiang · 2024-08-12

> I am able to run the examples/offline.py code, got following result :
> 
> > INFO 13:00:01 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
> > INFO 13:00:01 (decoding) GPU blocks: 3 / 941 (0.32%) used, (0 swapping out)
> > INFO 13:00:01 (decoding) 0 unaccepted, 0 waiting, 2 processing
> > INFO 13:00:02 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > INFO 13:00:02 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
> > INFO 13:00:02 (decoding) GPU blocks: 2 / 941 (0.21%) used, (0 swapping out)
> > INFO 13:00:02 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > INFO 13:00:03 (context) 0 waiting, 0 finished but unaccepted, 0 blocks occupied by on-the-fly requests
> > INFO 13:00:03 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
> > INFO 13:00:03 (decoding) GPU blocks: 3 / 941 (0.32%) used, (0 swapping out)
> > INFO 13:00:03 (decoding) 0 unaccepted, 0 waiting, 1 processing
> > Prompt: 'Life blooms like a flower. Far away or by the road. Waiting', Generated text: for the right time to blo om . Ћ
> > (10 tokens generated).
> > Prompt: 'A quick brown fox', Generated text: j umps over the lazy dog .
> > (8 tokens generated).
> > Prompt: 'Artificial intelligence is', Generated text: a hot topic in the te ch world . The term is thrown around a lot , but what does it really mean ?
> > (25 tokens generated).
> > Prompt: 'To be or not to be,', Generated text: that is the question .
> > (6 tokens generated).
> > Prompt: 'one two three four', Generated text: five six seven eight nine ten eleven eleven twelve th ir teen fifteen six teen sevent een eigh teen nin ete en twenty one twenty - one twenty - two twenty - three twenty - four twenty - five twenty - six twenty - se ven twenty - one twenty - two
> > (53 tokens generated).
> > (ParaWorker pid=5130) INFO 13:00:00 (worker context.#0) model /workspace/Llama-2-7b-hf/ loaded
> > (ParaWorker pid=5130) INFO 13:00:00 runtime peak memory: 12.497 GB
> > (ParaWorker pid=5130) INFO 13:00:00 total GPU memory: 22.059 GB
> > (ParaWorker pid=5130) INFO 13:00:00 kv cache size for one token: 0.50000 MB
> > (ParaWorker pid=5130) INFO 13:00:00 num_gpu_blocks: 941
> > (ParaWorker pid=5130) INFO 13:00:00 num_cpu_blocks: 128
> > root@5a65df8f9a43:/workspace/DistServe#
> 
> but I'm still confused :
> 
> 1. how to know the performance of the testing?
> 2. if I want to comapre it with colocate solution (both prefill and decoding phase run in the single GPU) , how to launch the testing ?

Hi mate, have you ever met this problem:

(ParaWorker pid=1955026) Error: Peer-to-peer access is unsupported on this platform.
(ParaWorker pid=1955026) In the current version of distserve, it is necessary to use a platform that supports GPU P2P access.
(ParaWorker pid=1955026) Exiting...

I checked the P2P access, it should be supported actually...

Thank you for any help!

### William12github · 2024-08-13

you can use below command to check your system if it's support P2P:
`nvidia-smi topo -p2p wr
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7
 GPU0   X       OK      OK      OK      OK      OK      OK      OK
 GPU1   OK      X       OK      OK      OK      OK      OK      OK
 GPU2   OK      OK      X       OK      OK      OK      OK      OK
 GPU3   OK      OK      OK      X       OK      OK      OK      OK
 GPU4   OK      OK      OK      OK      X       OK      OK      OK
 GPU5   OK      OK      OK      OK      OK      X       OK      OK
 GPU6   OK      OK      OK      OK      OK      OK      X       OK
 GPU7   OK      OK      OK      OK      OK      OK      OK      X

Legend:

  X    = Self
  OK   = Status Ok
  CNS  = Chipset not supported
  GNS  = GPU not supported
  TNS  = Topology not supported
  NS   = Not supported
  U    = Unknown`

### Youhe-Jiang · 2024-08-13

Thank you for response, I checked this, seems that the framework cannot run
on 4090 machines, I ran it successfully on A100 machines.

On Tue, 13 Aug 2024 at 02:54, William12github ***@***.***>
wrote:

> you can use below command to check the your if it's support P2P:
> `nvidia-smi topo -p2p wr
> GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7
> GPU0 X OK OK OK OK OK OK OK
> GPU1 OK X OK OK OK OK OK OK
> GPU2 OK OK X OK OK OK OK OK
> GPU3 OK OK OK X OK OK OK OK
> GPU4 OK OK OK OK X OK OK OK
> GPU5 OK OK OK OK OK X OK OK
> GPU6 OK OK OK OK OK OK X OK
> GPU7 OK OK OK OK OK OK OK X
>
> Legend:
>
> X = Self
> OK = Status Ok
> CNS = Chipset not supported
> GNS = GPU not supported
> TNS = Topology not supported
> NS = Not supported
> U = Unknown`
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/LLMServe/DistServe/issues/35#issuecomment-2285195413>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AUK4KHT3I7DBMZI3VJV62RTZRFRPFAVCNFSM6AAAAABMBIF2RSVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDEOBVGE4TKNBRGM>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>

