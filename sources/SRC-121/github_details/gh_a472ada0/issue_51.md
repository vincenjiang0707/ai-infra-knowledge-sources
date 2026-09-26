# [Issue #51] Lecture 14 weird result with TRITON_INTERPRET=1

source: https://github.com/gpu-mode/lectures/issues/51
state: open | updated: 2025-04-16T12:38:31Z
labels: 

## 正文

<img width="567" alt="Image" src="https://github.com/user-attachments/assets/09d641ef-ed28-4c1a-a8b4-f8efb69fce89" />

The matmul result is obviously wrong. Then I execute the next cell with (512,512), which produce a correct result surprisingly.

<img width="703" alt="Image" src="https://github.com/user-attachments/assets/00731cc2-eb8a-4f60-8eae-5f6b2c86c769" />

I suspect there are some bug with the index or missing guard clause. See another example with (16,16), which match the batch size also passed.

<img width="1011" alt="Image" src="https://github.com/user-attachments/assets/38787c1f-9771-4431-bd95-c2b3890a51eb" />


p.s. I do not have a GPU and running this on a Mac so everything is run in CPU mode and `TRITON_INTERPRET=1`

## 评论 (1)

### noklam · 2025-04-16

Reading the code again, should `mask` be applied in `tl.load` so that the dot product only calculate element within the bound?

Adding the mask will pass all 3 cases.

```python
    # Get 1d mask for 
    for _ in range(0, k, bk):
        mask_a = get_2d_mask(rm, rn, m, k) # add mask
        mask_b = get_2d_mask(rm, rn, k, n)  # add mask
            
        a = tl.load(offs_a, mask_a)
        b = tl.load(offs_b, mask_b)
        acc += tl.dot(a, b, allow_tf32=False) # matmul in block ; Weirdness: allow_tf32 must be set to False for older GPUs, otherwise won't compile
        
        # print_if(f"pid: {pid_m, pid_n} |\na: {a} | \nb: {b}", "")
        
        # increase offets, so next iteration loads next chunks
        offs_a += bk * stride_ak
        offs_b += bk * stride_bk
```
