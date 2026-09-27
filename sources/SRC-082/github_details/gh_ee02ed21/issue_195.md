# [Issue #195] Invalid Characters

source: https://github.com/mit-han-lab/llm-awq/issues/195
state: open | updated: 2025-10-28T05:30:54Z
labels: 

## 正文

running 
```
python vlm_demo_new.py     --model-path VILA1.5-3b-s2     --quant-path VILA1.5-3b-s2-AWQ/llm     --precision W4A16     --image-file MYPATH
```

I got invalid character:
ASSISTANT: eusentercdnieriieuleteygonenu"/edoiralynkele Croatiaxavieree accidentnel HenriamincalcqaedeneksucheSSN inferredTagged bestowedlungITHliasores factuallybaserilledGER dict formula Kabats Earthquakeholderaveloleandemauer Credbaarfuacesastofuacesastofuacesastofuacesastofuacesordnungaires inst Roberts ObservSEEayeecavasongueodufikhsplotWE 

This happens for VILA1.5-3b-AWQ, Llama-3-VILA1.5-8B-AWQ, and VILA1.5-13b-AWQ

## 评论 (1)

### jagjeet-habilelabs · 2025-10-28



> running
> 
> ```
> python vlm_demo_new.py     --model-path VILA1.5-3b-s2     --quant-path VILA1.5-3b-s2-AWQ/llm     --precision W4A16     --image-file MYPATH
> ```
> 
> I got invalid character: ASSISTANT: eusentercdnieriieuleteygonenu"/edoiralynkele Croatiaxavieree accidentnel HenriamincalcqaedeneksucheSSN inferredTagged bestowedlungITHliasores factuallybaserilledGER dict formula Kabats Earthquakeholderaveloleandemauer Credbaarfuacesastofuacesastofuacesastofuacesastofuacesordnungaires inst Roberts ObservSEEayeecavasongueodufikhsplotWE
> 
> This happens for VILA1.5-3b-AWQ, Llama-3-VILA1.5-8B-AWQ, and VILA1.5-13b-AWQ

Have you solved this? I am also getting same thing.
