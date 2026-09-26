# [Issue #107] [Issue]: Compilation errors for Rust interface

source: https://github.com/ROCm/amdsmi/issues/107
state: closed | updated: 2025-11-03T08:11:15Z
labels: Under Investigation

## 正文

### Problem Description

Hello,

We are noticing the following new compilation errors for the Rust interface.
For information, I have **1.86** rust version.
Unfortunatly, the only way for me to test correctly amdsmi in a rust program, is to have a tagged version of the repository, in the **Cargo.toml** project file.

```rust
[dependencies]
amdsmi = { git = "https://github.com/mcharles-brcm/amdsmi", rev = "8e454950ef9713b4316ccea5dcf06983ad5ea822" }
```

### Operating System

Ubuntu 24.04.2 LTS

### CPU

12th Gen Intel(R) Core(TM) i5-1245U

### GPU

N/A

### ROCm Version

6.4.2

### ROCm Component

amdsmi

### Steps to Reproduce

```bash
git clone https://github.com/ROCm/amdsmi.git
cd amdsmi/rust-interface
cargo build
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```bash
error[E0277]: the type `[&str]` cannot be indexed by `&str`
    --> /home/a935499/.cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/e340bf4/rust-interface/src/amdsmi_wrapper.rs:1889:6
     |
1889 |     ["Offset of field: AmdsmiVersionT::major"]
     |      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ slice indices are of type `usize` or ranges of `usize`
     |
     = help: the trait `SliceIndex<[&str]>` is not implemented for `&str`
     = note: required for `[&str]` to implement `Index<&str>`
     = note: 1 redundant requirement hidden
     = note: required for `[&str; 1]` to implement `Index<&str>`

error[E0080]: evaluation of constant value failed
   --> /home/a935499/.cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/e340bf4/rust-interface/src/amdsmi_wrapper.rs:797:5
    |
797 |     ["Size of AmdsmiVbiosInfoT"][::std::mem::size_of::<AmdsmiVbiosInfoT>() - 1056usize];
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ index out of bounds: the length is 1 but the index is 224

error[E0080]: evaluation of constant value failed
    --> /home/a935499/.cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/e340bf4/rust-interface/src/amdsmi_wrapper.rs:1834:5
     |
1834 |     ["Size of AmdsmiDpmPolicyEntryT"][::std::mem::size_of::<AmdsmiDpmPolicyEntryT>() - 36usize];
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ index out of bounds: the length is 1 but the index is 224

error[E0080]: evaluation of constant value failed
    --> /home/a935499/.cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/e340bf4/rust-interface/src/amdsmi_wrapper.rs:1851:5
     |
1851 |     ["Size of AmdsmiDpmPolicyT"][::std::mem::size_of::<AmdsmiDpmPolicyT>() - 1160usize];
     |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ index out of bounds: the length is 1 but the index is 7168

error[E0080]: evaluation of constant value failed
    --> /home/a935499/.cargo/git/checkouts/amdsmi-2c8d59e6e37e072e/e340bf4/rust-interface/src/amdsmi_wrapper.rs:2293:5
     |
2293 | /     ["Offset of field: AmdsmiProcessInfoT::vram_usage"]
2294 | |         [::std::mem::offset_of!(AmdsmiProcessInfoT, vram_usage) - 4usize];
     | |_________________________________________________________________________^ index out of bounds: the length is 1 but the index is 4

Some errors have detailed explanations: E0080, E0277.
For more information about an error, try `rustc --explain E0080`.
error: could not compile `amdsmi` (lib) due to 5 previous errors
```

### Additional Information

_No response_

## 评论 (8)

### ppanchad-amd · 2025-08-05

Hi @victoryeagle77. Internal ticket has been created to investigate this issue. Thanks!

### schung-amd · 2025-08-05

Hi @victoryeagle77, thanks for reporting this. It looks like several of the sizes and offsets defined in amdsmi_wrapper.rs are incorrect, I'm reaching out to the internal team to double check.

> Unfortunatly, the only way for me to test correctly amdsmi in a rust program, is to have a tagged version of the repository, in the Cargo.toml project file.

To clarify, is the tagged commit working and this issue is a regression, or is the tagged commit also broken?

 

### victoryeagle77 · 2025-08-06

No, the commit tagged (8e454950ef9713b4316ccea5dcf06983ad5ea822) works, it's the current version that doesn't. The working commit is old, and unfortunatly I can't see the updates you've made to amdsmi, and newer features that you included inside.

This doesn't work if I have for example a Cargo.toml with :

```rust
[dependencies]
amdsmi = { git = "https://github.com/ROCm/amdsmi" }
```

### schung-amd · 2025-08-06

Thanks for checking. This issue was caused because the wrapper was auto-generated for an older amdsmi version and has not been updated to match changes in the underlying amdsmi header, we'll get this regenerated and adjusted to match the amdsmi changes. Sorry for the inconvenience and thanks for pointing this out!

### victoryeagle77 · 2025-08-12

Moreover, I think making a Rust Crate for AMD SMI would be very interesting at this level. I work for Eviden, part of the Atos group, on an open-source project made in Rust, and this would really be an added value in terms of integration practicality for a project like this (or another).


### victoryeagle77 · 2025-08-25

Hello, sorry to bother you, I just wanted to know if the wrapper will be fixed soon, as I can test the amdsmi functions with the latest advances (my company would like to see them for our PoC).

### schung-amd · 2025-08-25

Sorry for the delay on this, checking on the progress. If it's still a bit far out but possible I'll see if we can provide a patch in the meanwhile.

### schung-amd · 2025-09-02

@victoryeagle77 A fix is in amd-staging (https://github.com/ROCm/amdsmi/commit/51a44bc0c456884f3f0c901cfa2aa3e0095a7d01), pending a merge to amd-mainline.
