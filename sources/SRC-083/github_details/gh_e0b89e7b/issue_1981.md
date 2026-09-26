# [Issue #1981] Support free-threaded Python (cp314t) wheels

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1981
state: closed | updated: 2026-06-30T02:52:37Z
labels: 

## 正文

### Feature request

It would be great if bitsandbytes could publish wheels for free-threaded Python (cp314t).

### Motivation

Free-threaded Python (PEP 703) is becoming production-ready in CPython 3.14t. The ML ecosystem is increasingly adopting it for true multi-threaded inference and data loading. Users on free-threaded Python currently have to build bitsandbytes from source.

### Your contribution

If there's interest, I'd be happy to help with any necessary code changes to make this happen.

## 评论 (2)

### matthewdouglas · 2026-06-29

Hi @leveretconey,

Our existing wheels published to PyPI should work as-is for free-threaded Python. The wheels are tagged as `py3-none`, actually. You shouldn't need to build from source.

Is there a more specific issue that you're experiencing at runtime?

### leveretconey · 2026-06-30

@matthewdouglas Sorry, I missed that the existing wheels are already tagged as py3-none. You're right — they work directly with free-threaded Python without a dedicated cp314t build
