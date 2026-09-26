# [Issue #73] [Issue]: `sensor_ind` error during compilation

source: https://github.com/ROCm/amdsmi/issues/73
state: closed | updated: 2025-03-20T15:59:28Z
labels: Under Investigation

## 正文

### Problem Description

Hi

I noticed that an error occurs when compiling `rust-interface` with cargo in the `amdsmi` component :
`cargo build` command line result in :

```Bash
  error[E0425]: cannot find value `sensor_ind` in this scope
      --> src/amdsmi.rs:5745:9
       |
  5745 |         sensor_ind,
       |         ^^^^^^^^^^ not found in this scope
```

### Operating System

Ubuntu GNU/Linux

### CPU

13th Gen Intel(R) Core(TM) i5-1345U

### GPU

N/A

### ROCm Version

ROCm 6.3.2

### ROCm Component

amdsmi

### Steps to Reproduce

```Bash
git clone https://github.com/ROCm/amdsmi.git
cd amdsmi/rust-interface
cargo build
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (5)

### ppanchad-amd · 2025-02-18

Hi @victoryeagle77. Internal ticket has been created to investigate this issue. Thanks!

### victoryeagle77 · 2025-02-25

Ok thanks to you, the modifications @mcharles-brcm allow to compile without error now. Thank you for your responsiveness.
And just a little question for you to finish, if you plan to release amdsmi in a Rust crate in the near future.

### dmitrii-galantsev · 2025-02-25

> And just a little question for you to finish, if you plan to release amdsmi in a Rust crate in the near future.

@victoryeagle77 AFAIK - No. Is there a demand? We're trying to take over python-pip packaging soon, maybe we can take on cargo as well :)

### victoryeagle77 · 2025-02-26

@dmitrii-galantsev Yes it will be very appreciated by many Rust developers, especially by my work team.

### dmitrii-galantsev · 2025-03-20

related - https://github.com/ROCm/amdsmi/commit/4a3c70136fcd22f724660abcf9a3b1be2f42efba

