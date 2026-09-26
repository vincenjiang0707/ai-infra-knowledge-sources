# [Issue #83] Inaccuracy in documentation regarding installation through pip

source: https://github.com/triton-inference-server/perf_analyzer/issues/83
state: closed | updated: 2024-12-18T00:02:49Z
labels: 

## 正文

Hello!

I’ve noticed that the information in the [install section](https://github.com/triton-inference-server/perf_analyzer/blob/r24.08/docs/install.md#pip) for pip is outdated. Specifically, after running

```
pip install tritonclient
```

i got error whe try to run `perf_analyzer` command. As I understand it, this is related to the latest refactoring that the triton team did to move perf_analyzer to a separate repository.

This might confuse users who are working with the project.

## 评论 (5)

### azsh1725 · 2024-09-11

Overall, this is very strange, because as far as I can see, your [CMakeLists](https://github.com/triton-inference-server/perf_analyzer/blob/r24.08/CMakeLists.txt#L40) by default build should happen in such a way that the perf-analyzer is added to the python client wheel

### azsh1725 · 2024-09-11

I'd like to share some feedback and seek clarification regarding the process of building from source as documented, too.

It appears the documentation might not clearly specify the necessary details for building from sources. I successfully built `perf_analyzer` using the following command:

```
cmake -DOPENSSL_ROOT_DIR=/usr/lib/ssl \
-DOPENSSL_LIBRARIES=/usr/lib/x86_64-linux-gnu \
-DTRITON_COMMON_REPO_TAG=r24.08 \
-DTRITON_THIRD_PARTY_REPO_TAG=r24.08 \
-DTRITON_CORE_REPO_TAG=r24.08 ..
```

From my understanding, the OpenSSL options could be optional, whereas the Triton-specific options are crucial to ensure the build does not default to the main branch. Could you confirm if my understanding is correct?

Additionally, I encountered an issue with a missing `libb64-dev` dependency, which I resolved by running `apt install libb64-dev`.

If we could also discuss the pip issue and any other outstanding questions, I would be happy to contribute a small PR to enhance the documentation based on our discussion.

### the-david-oy · 2024-10-21

CC: @matthewkotila @fpetrini15 

### fpetrini15 · 2024-10-23

@azsh1725 can you share more details regarding the error you encountered when you pip installed tritonclient? What environment are you running in? One of our release images? Custom location? I installed `tritonclient` in our 24.09 base container and it seems to work OOTB. If the error arose from not having `libb64-dev` installed, I believe this is a known issue when running in a custom environment--tools team can confirm. 

I believe the OpenSSL libs are required to build the client. If you remove that option from the build does it fail? Regarding the Triton-specific options, you are correct--they will default to main unless specifically overwritten.

### the-david-oy · 2024-12-18

Closing due to inactivity. If you would like to reopen the issue, let us know.
