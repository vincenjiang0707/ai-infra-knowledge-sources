# [Issue #10] decoder.embed_tokens.weight.pt not found 

source: https://github.com/LLMServe/DistServe/issues/10
state: open | updated: 2025-04-06T10:15:35Z
labels: help wanted

## 正文

Hi, when I using `distserve_api_server.py` to start a server, it always raise an error during lauching it:
```
ray.exceptions.RayTaskError(RuntimeError): ray::ParaWorker.init_model() (pid=129376, ip=172.17.0.7, actor_id=27f5ee672314d5dfcee7384701000000, repr=<distserve.worker.ParaWorker object at 0x7efea016a110>)
  File "/share/share/DistServe/distserve/worker.py", line 100, in init_model
    self.model.load_weight(path)
RuntimeError
```
When I shut it down, it will output the following error:
```
(ParaWorker pid=129375) Gpt<T>::load() - /llama-2-13b-hf/decoder.embed_tokens.weight.pt not found [repeated 5x across cluster]
```
The model is llama-2-13b-hf, I can run it in vLLM.


## 评论 (14)

### interestingLSY · 2024-06-11

May I have your startup command? I suspect that your `model` argument is incorrect.

### llx-08 · 2024-06-13

I have found the cause that led to this issue. I discovered that the model weights need to be converted via the `converter` under the `downloader`. However, the function `download_and_convert_weights` returns immediately when encountering model path, without converting the weights. This led to the error where the weights could not be run.

### KylinC · 2024-06-14

but how can I run converter.py with a local model dir? it seems the converter get a parameter '--input' to get 'model.bin', but I have several *.bin files

### interestingLSY · 2024-06-14

> but how can I run converter.py with a local model dir? it seems the converter get a parameter '--input' to get 'model.bin', but I have several *.bin files

You can use globs like /data/weights/*.bin

NOTE. In some shells you may need to wrap it in quotation marks to avoid being expanded by the shell.

### KylinC · 2024-06-14

> > but how can I run converter.py with a local model dir? it seems the converter get a parameter '--input' to get 'model.bin', but I have several *.bin files
> 
> You can use globs like /data/weights/*.bin
> 
> NOTE. In some shells you may need to wrap it in quotation marks to avoid being expanded by the shell.

I convert the model like this:

`python distserve/downloader/converter.py --input /data/Llama-2-7b/pytorch_model.bin --output /data/Llama-2-7b --model llama`

then run the model_server like this:

`python distserve/api_server/distserve_api_server.py --model /data/llama-2-7B/`

but it's still missing something:

(ParaWorker pid=715665) INFO 13:35:56 runtime peak memory: 12.922 GB
(ParaWorker pid=715665) INFO 13:35:56 total GPU memory: 39.392 GB
(ParaWorker pid=715665) INFO 13:35:56 kv cache size for one token: 0.50000 MB
(ParaWorker pid=715665) INFO 13:35:56 num_gpu_blocks: 2883
(ParaWorker pid=715665) INFO 13:35:56 num_cpu_blocks: 128
(ParaWorker pid=715665) Gpt<T>::load() - /data/fx/cql/llama-2-7B/decoder.output_projection.weight.pt not found




### interestingLSY · 2024-06-14

> > > but how can I run converter.py with a local model dir? it seems the converter get a parameter '--input' to get 'model.bin', but I have several *.bin files
> > 
> > 
> > You can use globs like /data/weights/*.bin
> > NOTE. In some shells you may need to wrap it in quotation marks to avoid being expanded by the shell.
> 
> I convert the model like this:
> 
> `python distserve/downloader/converter.py --input /data/Llama-2-7b/pytorch_model.bin --output /data/Llama-2-7b --model llama`
> 
> then run the model_server like this:
> 
> `python distserve/api_server/distserve_api_server.py --model /data/llama-2-7B/`
> 
> but it's still missing something:
> 
> (ParaWorker pid=715665) INFO 13:35:56 runtime peak memory: 12.922 GB (ParaWorker pid=715665) INFO 13:35:56 total GPU memory: 39.392 GB (ParaWorker pid=715665) INFO 13:35:56 kv cache size for one token: 0.50000 MB (ParaWorker pid=715665) INFO 13:35:56 num_gpu_blocks: 2883 (ParaWorker pid=715665) INFO 13:35:56 num_cpu_blocks: 128 (ParaWorker pid=715665) Gpt::load() - /data/fx/cql/llama-2-7B/decoder.output_projection.weight.pt not found

Paths and file names are case-sensitive under Linux. Please correct your path when running the API server.

### KylinC · 2024-06-14

thx, I correct my spelling, but it seems missing decoder.output_projection.weight.pt

`Gpt<T>::load() - /data/fx/cql/Llama-2-7b-hf/decoder.output_projection.weight.pt not found`

I carefully check the conversion and its output files, they are three types:

decoder.embed_tokens.weight.pt
decoder.layer_norm.weight.pt
decoder.layers.*

but no file named decoder.output_projection, 

### KylinC · 2024-06-14

> I have found the cause that led to this issue. I discovered that the model weights need to be converted via the `converter` under the `downloader`. However, the function `download_and_convert_weights` returns immediately when encountering model path, without converting the weights. This led to the error where the weights could not be run.

I am still missing decoder.output_projection.weight.pt not found,even I've converted weights 

### interestingLSY · 2024-06-14

Sorry but I am unable to reproduce your issue. I have tried the following steps:

- Cloning `meta-llama/Llama-2-7b-hf` to some directory
- Running `python3 distserve/downloader/converter.py --input "PATH/TO/DOWNLOADED_WEIGHTS/*.bin" --output PATH/TO/OUTPUT --dtype float16 --model llama`. 
- Listing all files under the output directory, and finds out that it do generate `decoder.output_projection.weight.pt`.

May you check all your commands again?

### llx-08 · 2024-06-14

I have changed the `convert_weights` function like this:
```
def convert_weights(
    input: str, 
    output: str, 
    dtype: torch.dtype, 
    model: str
) -> None :
    """Function used by `downloader.py` to convert weights"""
    os.makedirs(output, exist_ok=True)
    print(f"Converting {input} into torch.jit.script format")

    # Load the state dict (tensor_dict)
    # If the whole model is saved in a single file, then load the state dict directly
    # otherwise, load them separately and merge them into a single state dict

    bin_files = glob(input + '*.bin')
    # input_files = glob(input)
    # print("input files: ", input_files)

    if len(bin_files) == 0:
        ValueError(f"Input {input} does not match any files")
        print(f"Input {input} does not match any files")
        exit(1)
    
    # Load file(s)
    state_dict = {}
    for file in bin_files:
        print(f"Loading {file}")
        state_dict.update(torch.load(file, torch.device("cpu")))

    # Change dtype
    for key in state_dict:
        state_dict[key] = state_dict[key].to(dtype)

    # Preprocess
    print("Preprocessing")
    preprocessor = PREPROCESSOR[model]
    tensor_dict, num_q_heads, head_dim = preprocessor(state_dict)

    # The final step: divide the weights and save them to files
    print("Resharding and saving weights")
    name_translator = NAME_TRANSLATOR[model]
    divideWeightAndSave(output, tensor_dict, name_translator, num_q_heads, head_dim)
```
and manually convert before running server

### TianDe11 · 2024-07-09

Hi, I find *.bin not exist in weights of Llama-2-7b, I only find consolidated.00.pth, and unfortunately it can not be converted by converter.py

$ python distserve/downloader/converter.py --input /debug/Llama-2-7b/consolidated.00.pth --output /debug/Llama-2-7b/ --model llama

Converting /debug/Llama-2-7b/consolidated.00.pth into torch.jit.script format
Loading /debug/Llama-2-7b/consolidated.00.pth
Preprocessing
Traceback (most recent call last):
  File "/ktd/DistServe/distserve/downloader/converter.py", line 463, in <module>
    convert_weights(args.input, args.output, dtype, args.model)
  File "/ktd/DistServe/distserve/downloader/converter.py", line 439, in convert_weights
    tensor_dict, num_q_heads, head_dim = preprocessor(state_dict)
  File "/ktd/DistServe/distserve/downloader/converter.py", line 117, in preprocess_llama2
    num_layers = max(int(regex.findall(x)[0]) for x in filter(regex.match, tensor_dict)) + 1
ValueError: max() arg is an empty sequence

how to fix this problem...

### TZHelloWorld · 2024-08-15

> Hi, I find *.bin not exist in weights of Llama-2-7b, I only find consolidated.00.pth, and unfortunately it can not be converted by converter.py
> 
> $ python distserve/downloader/converter.py --input /debug/Llama-2-7b/consolidated.00.pth --output /debug/Llama-2-7b/ --model llama
> 
> Converting /debug/Llama-2-7b/consolidated.00.pth into torch.jit.script format Loading /debug/Llama-2-7b/consolidated.00.pth Preprocessing Traceback (most recent call last): File "/ktd/DistServe/distserve/downloader/converter.py", line 463, in convert_weights(args.input, args.output, dtype, args.model) File "/ktd/DistServe/distserve/downloader/converter.py", line 439, in convert_weights tensor_dict, num_q_heads, head_dim = preprocessor(state_dict) File "/ktd/DistServe/distserve/downloader/converter.py", line 117, in preprocess_llama2 num_layers = max(int(regex.findall(x)[0]) for x in filter(regex.match, tensor_dict)) + 1 ValueError: max() arg is an empty sequence
> 
> how to fix this problem...

maybe use ` meta-llama/Llama-2-7b-hf`？ https://huggingface.co/meta-llama/Llama-2-7b-hf/tree/main

### Liaukx · 2025-02-28

> > Hi, I find *.bin not exist in weights of Llama-2-7b, I only find consolidated.00.pth, and unfortunately it can not be converted by converter.py
> > $ python distserve/downloader/converter.py --input /debug/Llama-2-7b/consolidated.00.pth --output /debug/Llama-2-7b/ --model llama
> > Converting /debug/Llama-2-7b/consolidated.00.pth into torch.jit.script format Loading /debug/Llama-2-7b/consolidated.00.pth Preprocessing Traceback (most recent call last): File "/ktd/DistServe/distserve/downloader/converter.py", line 463, in convert_weights(args.input, args.output, dtype, args.model) File "/ktd/DistServe/distserve/downloader/converter.py", line 439, in convert_weights tensor_dict, num_q_heads, head_dim = preprocessor(state_dict) File "/ktd/DistServe/distserve/downloader/converter.py", line 117, in preprocess_llama2 num_layers = max(int(regex.findall(x)[0]) for x in filter(regex.match, tensor_dict)) + 1 ValueError: max() arg is an empty sequence
> > how to fix this problem...
> 
> maybe use ` meta-llama/Llama-2-7b-hf`？ https://huggingface.co/meta-llama/Llama-2-7b-hf/tree/main

I am using Llama-2-7b https://www.modelscope.cn/models/shakechen/Llama-2-7b-chat-hf/files (cause I am not allowed to access to the model in HF),
the CLI like below can be done successfully
 `python3 distserve/downloader/converter.py --input //model/llama2/pytorch_model-00001-of-00002.bin --output /data/lkx/model/DistServe_V/ --dtype float16 --model llama`
however when it comes to pytorch_model-00002-of-00002.bin I got an error like
```
distserve/downloader/converter.py", line 120, in preprocess_llama2
    num_q_heads = tensor_dict[Q_WEIGHT.format(1)].size(0) // head_dim
KeyError: 'model.layers.1.self_attn.q_proj.weight'
```

I have solved my error. It is caused by the logic of convert.py and I propose a PR to fix it

### sjlgaga · 2025-04-06

modify the code and propose a PR for the problem
