# [Issue #34] where can I find the code of itrative refinements decribed in the paper?

source: https://github.com/ScalingIntelligence/KernelBench/issues/34
state: closed | updated: 2025-05-25T06:42:28Z
labels: 

## 正文

Did you publish the scripts that pass compilation errors, profiling and output mismatch info to LM in iterative manner?

## 评论 (2)

### mposter1 · 2025-04-27

bump^
I do not see the iterative refinement prompt in ```src/prompt_constructor.py``` with all the other prompts, and ```grep``` is unable to locate any files that match the prompt pattern in appendix C.3.

### simonguozirui · 2025-05-25

Hi @agnonchik @mposter1, thanks for taking interest in our project, especially the iterative refinement part `5.1.2` in our [paper](https://arxiv.org/abs/2502.10517).  

Sorry for the delayed response and release, had been busy with some paper deadlines.
I cleaned up the code for multi-turn generation, evaluation, and visualization.
Check it out: https://github.com/ScalingIntelligence/caesar

The reason this part wasn't included in this repo is we want to keep the `KernelBench` repo relatively lightweight and minimal as many uses it as benchmarking / training environment. 
The multi-turn generation system was quite challenging to design for me and @alexzhang13, especially when evaluating on 250 problems across many turns and different configurations. We designed the system to be throughput-oriented and easy to visualize / analyze. 

The trajectories generated for the paper could be fine on our previous [HuggingFace release](https://huggingface.co/datasets/ScalingIntelligence/kernelbench-samples/tree/main/iterative_refinement).

Hope this helps and let me know if you have any more questions.
