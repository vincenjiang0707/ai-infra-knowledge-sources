# [Issue #58] smaple code doesn't run

source: https://github.com/dropbox/hqq/issues/58
state: closed | updated: 2024-05-06T16:32:11Z
labels: 

## 正文

I followed the installation guide using ```pip install hqq``` and then copied the code from huggingface: https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-2bit_g16_s128-HQQ

It gave me this error:
Traceback (most recent call last):
  File "/home/alden/hqq/hqq.py", line 4, in <module>
    from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
  File "/home/alden/hqq/hqq.py", line 4, in <module>
    from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
ModuleNotFoundError: No module named 'hqq.engine'; 'hqq' is not a package

I've tried to install it in another way which is ```pip install git+https://github.com/mobiusml/hqq.git```, got the same result. 

OS is Ubuntu 22.04, CUDA version is 12.2 and torch version is 2.2.2

Does anyone face this and solve it? Thanks

## 评论 (6)

### mobicham · 2024-04-22

Hi @LiangA, the sample code runs but hqq is not installed on your system. 
Can you try
`pip uninstall hqq -y; pip install git+https://github.com/mobiusml/hqq.git;` 
and let me know what error do you get

### LiangA · 2024-04-22

Hi mobicham, thanks for replying!
I tried to run the command you gave, and got the same error:

Traceback (most recent call last):
  File "/home/alden/hqq/hqq.py", line 4, in <module>
    from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
  File "/home/alden/hqq/hqq.py", line 4, in <module>
    from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
ModuleNotFoundError: No module named 'hqq.engine'; 'hqq' is not a package


I'm wondering if my code is outdated, here is my testing code (copied form huggingface):

```
model_id = 'mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-2bit_g16_s128-HQQ'

#Load the model
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = HQQModelForCausalLM.from_quantized(model_id)

#Optional
from hqq.core.quantize import *
HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE) 

#Text Generation
prompt = "<s> [INST] How do I build a car? [/INST] "

inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
outputs = model.generate(**(inputs.to('cuda')), max_new_tokens=1000)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


### mobicham · 2024-04-22

Hi @LiangA it's not related to the sample code, the library (hqq) is not installed.
Try this instead:
```
git clone https://github.com/mobiusml/hqq.git; 
cd hqq; pip install -e .; cd ..
# run your code now
```

### LiangA · 2024-04-25

Hi mobicham, 
Thanks for your patient and kindness. The error still goes as it was. I tend to try another loader/quantizer to do a 2-bit quantization now. I'll be back and check this project again.

### mobicham · 2024-04-25

I think there's an issue with your python environment. Can you try on Google colab with the free gpu? 

### mobicham · 2024-05-06

Closing since this is an issue related to the environment and not the library.
