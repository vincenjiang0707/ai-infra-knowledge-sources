# [Issue #3656] Why nvfp4_compute_output_scale use twice rcp?

source: https://github.com/flashinfer-ai/flashinfer/issues/3656
state: closed | updated: 2026-09-22T17:02:18Z
labels: question, needs-triage

## 正文

Hello，may i ask why nvfp4_compute_output_scale use twice rcp?
output_scale = global_scale/block_scale
this function first rcp.approx(global_scale) get 1/global_scale
then mul block_scale with 1/global_scale, get block_scale*(1/global_scale)
finally rcp(block_scale*(1/global_scale)), we get 1/(block_scale*(1/global_scale))
why not rcp(block_scale) and then mul global_scale?
What considerations are involved here? Thank you very much for taking the time to answer my question :)

```
@dsl_user_op
def nvfp4_compute_output_scale(
    fp8_val: Uint32, global_scale: Float32, *, loc=None, ip=None
) -> Float32:
    """Compute NVFP4 output_scale matching the CUDA kernel exactly.

    Converts E4M3 scale factor to float via hardware f16x2 path, then computes
    rcp(float_scale * rcp(global_scale)). Returns 0 when scale is zero.

    This matches quantization_utils.cuh:
        SFValue = static_cast<float>(tmp);
        outputScale = rcp_approx(SFValue * rcp_approx(SFScaleVal));
    """
    return Float32(
        llvm.inline_asm(
            T.f32(),
            [
                Uint32(fp8_val).ir_value(loc=loc, ip=ip),
                Float32(global_scale).ir_value(loc=loc, ip=ip),
            ],
            """
            {
                .reg .pred p_zero;
                .reg .b16 fp8_pair;
                .reg .b32 h2_32;
                .reg .b16 h_lo, h_hi;
                .reg .f32 scale_f32, rcp_gs, product, result;

                cvt.u16.u32 fp8_pair, $1;
                cvt.rn.f16x2.e4m3x2 h2_32, fp8_pair;
                mov.b32 {h_lo, h_hi}, h2_32;
                cvt.f32.f16 scale_f32, h_lo;

                rcp.approx.ftz.f32 rcp_gs, $2;
                mul.f32 product, scale_f32, rcp_gs;
                rcp.approx.ftz.f32 result, product;

                setp.eq.f32 p_zero, scale_f32, 0f00000000;
                selp.f32 $0, 0f00000000, result, p_zero;
            }
            """,
            "=f,r,f",
            has_side_effects=False,
            is_align_stack=False,
            asm_dialect=llvm.AsmDialect.AD_ATT,
        )
    )
```


## 评论 (2)

### bkryu · 2026-09-17

Hi @Ugo1998 this is a good question. The two-rcp form is needed for numerics.

It's the encode/decode symmetry recipe (the same one `TransformerEngine` uses — see the "Match TE's encode scale" comment in `quantization_utils.cuh`). The key is that `SFValue * rcp(SFScaleVal)` is exactly the dequantization factor the consumer computes. The stored E4M3 block scale is encoded premultiplied by the global scale, so at dequant time the effective scale is reconstructed as `fp32(stored_fp8) * reciprocal(SFScaleVal)`, with exactly those ops and roundings.

Your alternative, `rcp(SFValue) * SFScaleVal`, is mathematically equal but rounds differently. That introduces a systematic few-ulp mismatch.

On cost: `rcp(SFScaleVal)` is a per-tensor constant, so there isn't much of a cost.

Please let me know if you need further clarification 😄 

### bkryu · 2026-09-22

Closing as the question has been answered. @Ugo1998, please feel to reopen if you have any further questions.
