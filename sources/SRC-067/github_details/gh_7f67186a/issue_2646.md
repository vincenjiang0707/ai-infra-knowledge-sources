# [Issue #2646] CuteDSL profiling for FA4

source: https://github.com/Dao-AILab/flash-attention/issues/2646
state: closed | updated: 2026-06-12T06:22:33Z
labels: 

## 正文

I have made a tool to profile the fa4 traces: https://github.com/deciding/cutez.
Wondering if the team insterested in integrating for optimization?
Different from what quack.trace have done, this is a smem-based profiling tool, using the same algorithm as KPerfIR/proton.
Following are some demos:

<img width="2438" height="400" alt="Image" src="https://github.com/user-attachments/assets/74552cd6-35d4-450f-b6b4-824f753d612a" />

Below is the analysis of split_P:

<img width="1440" height="360" alt="Image" src="https://github.com/user-attachments/assets/1982d42b-e7c6-4770-9da3-277e8741eb28" />


## 评论 (3)

### Johnsonms · 2026-06-11

Thanks @deciding for the offer! At the moment, we don't have plans to formally integrate it. That said, we're happy to use [[cutez](https://github.com/deciding/cutez)](https://github.com/deciding/cutez) whenever it fits our needs—it’s a really cool project.

### tridao · 2026-06-11

@deciding this profiler is great work! 
We should eventually have some kind of support for profiler in FA4, but currently we're focusing on implementing the rest of the features of FA4 (different headdim etc, different arch). 

### deciding · 2026-06-11

@Johnsonms @tridao Thanks for the feedback! Totally makes sense. Looking forward to new features of FA4!
