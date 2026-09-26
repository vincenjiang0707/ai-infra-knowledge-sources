# [Issue #9] Medusa can't find accelerate or bitsandbytes

source: https://github.com/FasterDecoding/Medusa/issues/9
state: closed | updated: 2023-09-13T16:43:42Z
labels: 

## 正文

Hi,
I am trying to run one of the medusa models loaded in 8 bit. I absolutley have installed accelerate and bitsandbytes, but when I run the example script:
` python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-33b-v1.3 --load-in-8bit`

I get errors saying that I need to install the most recent version of each.

Here is the error in full:
`Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Noelle's PC\OneDrive\LLM\story-engine\Medusa\medusa\inference\cli.py", line 226, in <module>
    main(args)
  File "C:\Users\Noelle's PC\OneDrive\LLM\story-engine\Medusa\medusa\inference\cli.py", line 37, in main
    model = MedusaModel.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Noelle's PC\OneDrive\LLM\story-engine\Medusa\medusa\model\medusa_model.py", line 124, in from_pretrained
    base_model = KVLlamaForCausalLM.from_pretrained(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Noelle's PC\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\transformers\modeling_utils.py", line 2482, in from_pretrained
    raise ImportError(
ImportError: Using load_in_8bit=True requires Accelerate: pip install accelerate and the latest version of bitsandbytes pip install -i https://test.pypi.org/simple/ bitsandbytes or pip install bitsandbytes`

## 评论 (6)

### leeyeehoo · 2023-09-13

Hi there!

You just need to do `pip install bitsandbytes accelerate scipy`. 

Tested it on 7b ` CUDA_VISIBLE_DEVICES=0 python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-7b-v1.3 --load-in-8bit` and it works. I don't have the 33b on my side yet since it is slow to download. See if you have any further questions.

### beingPurple · 2023-09-13

Thanks for the response @leeyeehoo ! Sadly, I couldnt get this to work, I wound up with the same issues. Also, if I try to specify the device, it just doesnt get recognized as a command or variable.
Is there a certain terminal I should be running this in? I have tried with powershell and comand prompt on windows 11

### leeyeehoo · 2023-09-13

No problem! And apologize we didn't test the codebase on a Windows machine (sometimes very weird things might happen to Windows and I personally can't install certain Python libraries on my desktop but can install it on my laptop which is also a Win machine). If you can provide further details like what environment you use, and what GPU you have, I can try my best (or ask ChatGPT) to help you address it :)

### beingPurple · 2023-09-13

I'm using an nvidia4090, but I have WSL, would bedusa be easier there?
I'm using a pretty default environment, I havent done much to set it up. 

### leeyeehoo · 2023-09-13

Yes, you can try it! Personally, I suggest using conda to manage the environment.

### beingPurple · 2023-09-13

ah!
I've managed to set up everything within conda, that seems to fix it! Although I had to download the pypi version of bitsandbytes.
