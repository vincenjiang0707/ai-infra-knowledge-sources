# [Issue #1559] [automation and reproducibility taskforce] progress report for 20240116

source: https://github.com/mlcommons/inference/issues/1559
state: closed | updated: 2026-05-09T00:41:15Z
labels: Stale

## 正文

**Current progress:**
* CM coverage to automate and reproduce MLPerf inference: [GitHub](https://github.com/mlcommons/ck/issues/1052)
  * All reference implementations are supported by CM including GPT-J and Stable Diffusion (though didn’t run LLAMA). 
    * Added support to run RNNT via GPU
    * Added AMD GPU support for RNNT and BERT
  * Nvidia implementation v3.1 is supported by CM 
  * Qualcomm implementation v3.1 is supported by CM
  * Intel: only BERT is done (it took us much longer to decompose their container, expose all dependencies and provide CM automation recipes for Conda, OneDNN, etc). We continue working on adding CM for other models including GPT-J. Mostly done but we encountered and reported an issue with some Intel extensions.
* Network reference implementation for BERT is added to inference repo and automated via CM
* The latest MLPerf power measurements are automated by CM and supports Nvidia, Qualcomm, Intel and NeuralMagic
* GitHub actions to test end-to-end submission for all applicable MLPerf inference reference implementations via CM are added to the MLPerf inference repo: https://github.com/mlcommons/ck/tree/master/.github/workflows

**MLCommons offers the following free help to the v4.0 submitters via our taskforce:**
* We can help any submitter automatically benchmark Nvidia, Qualcomm or Intel systems on any cloud via CM using v3.1 implementation
* We can also fully automate submissions for v4.0 implementations via CM if we get public or private access to the code (particularly for Stable Diffusion and LLAMA-2)
* We can provide access to the Thundercom RB6 (Qualcomm AI-100) and Nvidia Jetson AJX Orin with power meter and CM automation
* Automatically generate custom Docker images via CM to run MLPerf out-of-the-box with different OS and software stack (we just need feedback from submitters which implementations and models they need)
* Extend GUI to automate MLPerf inference experimentation and visualization

We also have a proposal for reproducibility badges for MLPerf inference v4.0 based on our experience with artifact evaluation at the recent ACM/IEEE hardware conferences including [MICRO’23](https://ctuning.org/ae/micro2023.html) and ASPLOS - we will send more details later.

Public Discord channel for the automation and reproducibility TF: https://discord.gg/JjWNWXKxwT


## 评论 (1)

### github-actions[bot] · 2026-05-09

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
