# [Issue #78] [Issue]: Error during compilation => (slice indices are of type `usize` or ranges of `usize`)

source: https://github.com/ROCm/amdsmi/issues/78
state: closed | updated: 2025-08-05T09:09:30Z
labels: Under Investigation

## 正文

### Problem Description

Hello again,

You provided a good solution to the problem I reported last time (sensor_id) and it was working for a while, but recently a change was made on amdsmi rust-interface, and a new error occurs when compiling rust-interface with cargo in the amdsmi component :
cargo build command line result in :

```bash
error[E0277]: the type `[&str]` cannot be indexed by `&str`
    --> /usr/local/cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/edd2268/rust-interface/src/amdsmi_wrapper.rs:1892:6
     |
1892 |     ["Offset of field: AmdsmiVersionT::major"]
     |      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ slice indices are of type `usize` or ranges of `usize`
     |
     = help: the trait `SliceIndex<[&str]>` is not implemented for `&str`
     = note: required for `[&str]` to implement `Index<&str>`
     = note: 1 redundant requirement hidden
     = note: required for `[&str; 1]` to implement `Index<&str>`

For more information about this error, try `rustc --explain E0277`.
error: could not compile `amdsmi` (lib) due to 1 previous error
warning: build failed, waiting for other jobs to finish...
```

### Operating System

Ubuntu GNU/Linux

### CPU

13th Gen Intel(R) Core(TM) i5-1345U

### GPU

N/A

### ROCm Version

ROCm 6.3.3

### ROCm Component

amdsmi

### Steps to Reproduce

```bash
git clone https://github.com/ROCm/amdsmi.git
cd amdsmi/rust-interface
cargo build
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### adityas-amd · 2025-06-11

Hello @victoryeagle77 could please also let us know your rust version you are building with? `rustc --verion`? I tried to reproduced the error with **rustc 1.87.0 (17067e9ac 2025-05-09)**, seems there are couple more errors apart from you mentioned: 

<img width="745" alt="Image" src="https://github.com/user-attachments/assets/3be51db5-234a-491d-a803-e41ec15b4957" />


### adityas-amd · 2025-07-10

Closing this issue for now due to inactivity. feel free to reopen is you are still facing the issue

### victoryeagle77 · 2025-08-05

> Closing this issue for now due to inactivity. feel free to reopen is you are still facing the issue

Sorry for the very late reply, I had a serious accident because of which I was unable to retest and reply.
In fact, I just tested it and now, with rust **1.86**, I have this error (the same as the one on your screenshot)
Do you need to have a specific version of rust to avoid these kinds of errors?
