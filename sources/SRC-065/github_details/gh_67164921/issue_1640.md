# [Issue #1640] Is there a plan to support Windows?

source: https://github.com/triton-lang/triton/issues/1640
state: closed | updated: 2026-08-29T18:08:48Z
labels: 

## 正文

I have noticed that the README states Linux as the only compatible platform. https://github.com/openai/triton#compatibility

Some people in the past have managed to compile on Windows https://github.com/openai/triton/issues/871 (there is even a really old PR for Windows support https://github.com/openai/triton/pull/24). But still going by the README, I suppose something changed and Triton doesn't support Windows anymore? I haven't tried to compile it myself yet.

I'm interested in the development of this repository but my main OS is Windows. I'm aware that I can probably use WSL2 but still I would prefer to run it on Windows natively. So my question is: is there a plan to officially support Windows? If so, I can help.

## 评论 (70)

### AlirezaBaf · 2023-05-10

I would also be really grateful if it happens.

### ptillet · 2023-05-11

This is a pretty frequent request. Let me see what we can do about it.

### starstar222 · 2023-05-11

+1


### patrickvonplaten · 2023-05-16

With torch.compile heavily relying on Triton, lots of Hugging Face users are also interested in this it seems :-) 

### hipsterusername · 2023-05-16

We have a number of interested parties optimizing inference times for Invoke AI on Windows. We're currently evaluating alternatives, but as @patrickvonplaten noted above, torch.compile is the most straightforward but requires Triton.

### Li-Yanzhi · 2023-05-28

+1

Get "RuntimeError: Windows not yet supported for torch.compile" in CUDA 12.1 & Pytorch 2.1.0, it seems that Triton is the main main reason which is not available on Windows, how we can get Windows version

### countzero · 2023-06-03

+1

### Pythonpa · 2023-06-04

+1,many python packages  support windows,and hope this as well,

### domef · 2023-06-06

+1

### speedystream · 2023-06-15

+1

### jyizheng · 2023-06-24

+1

### Bigfield77 · 2023-06-25

+1


### patrickvonplaten · 2023-07-04

@ptillet anything we could do to help you implement this? With PyTorch 2.+ becoming more and more dependent on Triton this feature request will only become more and more important I tihnk. 

Can we help you here in any way? 

### FurkanGozukara · 2023-07-04

please add support to windows

i hate to see triton not available on windows message 

### ptillet · 2023-07-04

The way to help here is probably to just submit a PR that adds windows support :) we won't have CI for it though soon

### bartekleon · 2023-08-28

The issues / solutions to them found so far: (also somewhat related to #1560)

- fixing url issue `ValueError: unknown url type: ''` - it seems `LLVM_SYSPATH` is not set in system [path](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/python/setup.py#L104) [and this](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/python/setup.py#L112). I added it but still doesn't work properly for me. Workaround for it was settings up the variable manually in `setup.py` -- `os.environ['LLVM_SYSPATH'] = 'path/to/llvm_build`

- another issue i found was with the target / build type. I couldn't make MSYS / ninja generator working so I am just using my default - Visual Studio 17 2022. I had to force [`get_build_type`](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/python/setup.py#L24) function to return `RelWithDebInfo`

- next issue I got is that [`MLIRGPUOps`](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/lib/Conversion/NVGPUToLLVM/CMakeLists.txt#L17) (and the other 2 files in Conversion) doesn't exist in build. As I am using llvm 17 [built from master] (version 17 is used on [linux](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/python/setup.py#L86) ) it seems it was renamed to [MLIRGPUDialect](https://github.com/llvm/llvm-project/commit/61223c49dd9a7d1d3efd1389db11b433cab38ccb)

- another issue I got is that I couldn't build with VS + clang (i got some error with `-f` flag), so had to stay with MSVC. I got error about `/Werror` value being incorrectly set. Had to change [configuration](https://github.com/openai/triton/blob/1465b573e8d8e4c707d579092001bcff0f1523ed/CMakeLists.txt#L187) to just `set(CMAKE_CXX_FLAGS "/std:c++17")`

- Currently stuck because `'C:\Users\potato\Desktop\llvm-project\build\RelWithDebInfo\bin\mlir-tblgen.exe' is not recognized as an internal or external command, operable program or batch file.` It seems there is some issue with it [not being built](https://github.com/llvm/llvm-project/issues/64150)

### gilberto-BE · 2023-09-12

+1

### DarkAlchy · 2023-09-13

+1

### FurkanGozukara · 2023-09-19

Were there any fork for this? 

There is this repo but i don't know : https://github.com/PrashantSaikia/Triton-for-Windows

### skirdey · 2023-10-01

+1

### Pevernow · 2023-10-01

+1

### ezra-ch · 2023-10-02

+1

### FurkanGozukara · 2023-10-02

+1

### mush42 · 2023-10-05

+1

### DheerajMadda · 2023-10-06

+1

### andreigh · 2023-10-07

I'm also trying to build a llvm-17.0.0-c5dede880d17 compiled for Windows with Github actions here: https://github.com/andreigh/triton-llvm-windows

### FurkanGozukara · 2023-10-07

> I'm also trying to build a llvm-17.0.0-c5dede880d17 compiled for Windows with Github actions here: https://github.com/andreigh/triton-llvm-windows

you don't have any release will you do? i would like to install and test

if i merge your pull request locally how can i install on windows what command?

assume that i cloned repo merged your pull request then  what?

### you74674 · 2023-10-31

>     * Currently stuck because `'C:\Users\potato\Desktop\llvm-project\build\RelWithDebInfo\bin\mlir-tblgen.exe' is not recognized as an internal or external command, operable program or batch file.` It seems there is some issue with it [not being built](https://github.com/llvm/llvm-project/issues/64150)

This seems to be fixed in b1115f8c? I can build it without problem.
Now I can build triton but not any backend. There are some gcc-only code that I have no idea how to modify it for msvc.

### CHEROAD · 2023-12-12

+1

### supracharger · 2024-01-19

+1

### FurkanGozukara · 2024-01-19

there are pre compiled wheels right now but i don't know how accurate and good they are working

still working though 

### DarkAlchy · 2024-01-20

> there are pre compiled wheels right now but i don't know how accurate and good they are working
> 
> still working though

They do nothing except to shut up the programs complaining (such as Kohya, etc...).  It seems it will take an official release but I am not sure it can even be done in Windows as a lot of the *nix stuff can't.

### FurkanGozukara · 2024-01-20

> > there are pre compiled wheels right now but i don't know how accurate and good they are working
> > still working though
> 
> They do nothing except to shut up the programs complaining (such as Kohya, etc...). It seems it will take an official release but I am not sure it can even be done in Windows as a lot of the *nix stuff can't.

well i have to say that this library do not have official support for Windows Python is unacceptable 

### DarkAlchy · 2024-01-20

> > > there are pre compiled wheels right now but i don't know how accurate and good they are working
> > > still working though
> > 
> > 
> > They do nothing except to shut up the programs complaining (such as Kohya, etc...). It seems it will take an official release but I am not sure it can even be done in Windows as a lot of the *nix stuff can't.
> 
> well i have to say that this library do not have official support for Windows Python is unacceptable

I agree with a caveat that it may not be doable on Windows as I mentioned.  Not everything can be done on Windows that can be on *nix and it is the fault of Windows since W95/W98/W2000/WinME/XP/Vista and so on.  For server type stuff, and ML/AI type stuff *nix was made for that.

### FurkanGozukara · 2024-01-20

> > > > there are pre compiled wheels right now but i don't know how accurate and good they are working
> > > > still working though
> > > 
> > > 
> > > They do nothing except to shut up the programs complaining (such as Kohya, etc...). It seems it will take an official release but I am not sure it can even be done in Windows as a lot of the *nix stuff can't.
> > 
> > 
> > well i have to say that this library do not have official support for Windows Python is unacceptable
> 
> I agree with a caveat that it may not be doable on Windows as I mentioned. Not everything can be done on Windows that can be on *nix and it is the fault of Windows since W95/W98/W2000/WinME/XP/Vista and so on. For server type stuff, and ML/AI type stuff *nix was made for that.

well this library obviously possible because i am using pre compiled wheel

### DarkAlchy · 2024-01-20

You are using a dummy pre-compiled, and I know this because I have tried them all and none gave me the speed up it does on Linux.  Sure, we can compile it, but that doesn't make it actually work.  Iow, a dummy file.

### FurkanGozukara · 2024-01-20

> You are using a dummy pre-compiled, and I know this because I have tried them all and none gave me the speed up it does on Linux. Sure, we can compile it, but that doesn't make it actually work. Iow, a dummy file.

i see could be

### DarkAlchy · 2024-01-20

I really wish this worked on Windows, but I swear I remember reading from the devs last year a thread that said they would never be on Windows.

### Bionic-Squash · 2024-01-31

+1

### bitchaser12 · 2024-02-07

+1

### thiagocrepaldi · 2024-02-08

+1

### hubertlu-tw · 2024-02-13

+1

### anveshnathaniou · 2024-03-11

+1

### FurkanGozukara · 2024-03-12

Even bitsandbytes now supports Windows Officially 

### DarkAlchy · 2024-03-12

> Even bitsandbytes now supports Windows Officially

If only the triton devs would just come clean and publicly state NO, and why not, or Yes, and when to expect it.

### umarbutler · 2024-04-04

+1

### Yatagarasu50469 · 2024-04-06

+1

### tiRomani · 2024-04-21

please 🥺 

### dsent · 2024-05-21

+1 to this 🥺

### tin2tin · 2024-06-03

+1

### Adillwma · 2024-06-09

+1

### jetaudio270195 · 2024-06-23

+1

### avielkis · 2024-06-29

+1

### sipie800 · 2024-07-16

+10

### Systemcluster · 2024-07-16

In https://github.com/triton-lang/triton/pull/4045 Windows support was declined with "we don't have the bandwidth to commit to supporting Windows at this time".

### Bionic-Squash · 2024-07-16

That's disappointing to hear 

### skier233 · 2024-07-16

> That's disappointing to hear

I can't imagine any possible feature that'd be more important than this such that "there isn't enough bandwidth".

### FurkanGozukara · 2024-07-16

you have bandwidth money and manpower to support Windows

there are even individual developers published pre-compiled wheels for windows

this is ridiculous 

### biship · 2024-07-16

> there are even individual developers published pre-compiled wheels for windows

Link one...


### FurkanGozukara · 2024-07-16

> > there are even individual developers published pre-compiled wheels for windows
> 
> Link one...

https://github.com/wkpark/triton/actions/runs/7246431088

### biship · 2024-07-16

7 months old. Yeah that's bound to be able to handle all the latest models.

### FurkanGozukara · 2024-07-16

> 7 months old. Yeah that's bound to be able to handle all the latest models.

that is not the point though. point is OpenAI has all the resources on earth to make triton work on windows natively



### darkanubis0100 · 2024-09-08

Where is Triton for Windows? :(

### FurkanGozukara · 2024-09-08

Still we are missing Triton in 2024, in era of ChatGPT 4

### FurkanGozukara · 2024-09-26

Thank you OpenAI taking 10s billions from Microsoft 

![image](https://github.com/user-attachments/assets/36a5329d-8727-4f6e-83b8-b3fd0679898e)


### Obr00007576 · 2024-11-23

+1

### nitinmukesh · 2025-02-14

Shame, still no support. :(

### FurkanGozukara · 2025-02-14

> Shame, still no support. :(

a legendary random developer solo supporting meanwhile 100B + META cant

https://github.com/woct0rdho/triton-windows/releases

### RoyiAvital · 2026-08-29

Is there a reason not to merge https://github.com/triton-lang/triton-windows into this? After all both under `triton-lang` organization.

### ThomasRaoux · 2026-08-29

maintenance overhead
