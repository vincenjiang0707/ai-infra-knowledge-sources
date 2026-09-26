# [PR #7] [wishlist] 3D FFT on packed Hermitian half-spectra (fp32 + fp64, r2c + c2r)

source: https://github.com/NVlabs/kda/pull/7
state: open | updated: 2026-09-22T09:02:15Z
labels: 

## 正文

## Request

Request directories:

- `requests/jasvixban-fft3d-r2c/` and `requests/jasvixban-fft3d-c2r/` (fp32)
- `requests/jasvixban-fft3d-r2c-f64/` and `requests/jasvixban-fft3d-c2r-f64/` (fp64 twins)

## Summary

Four paired requests (fp32 + fp64) for unnormalized 3D FFTs on packed
Hermitian half-spectra (x innermost, output row stride exactly nx//2+1 with
no even-row padding): real-to-complex (`fft3d_r2c_halfspec_f32/_f64`) and
inverse (`fft3d_c2r_halfspec_f32/_f64`). These are the inner kernels of
structured-grid spectral solvers, which call them every timestep on fixed,
caller-owned device buffers and are sensitive to per-call overhead, padding
waste, and plan-time stalls. The eight workloads per request (cubic
32^3..256^3 plus anisotropic 80x80x112 and 96x96x144) are composite numbers
of small factors, the regime where a hand-tuned implementation can beat a
general plan chooser. The fp64 twins share the identical contract and
grids, differing only in the dtype pair. The baseline is cuFFT reached
through `torch.fft` (source/version/license recorded in the READMEs).

Validation status: all 32 workloads pass correctness (fp32: rel-L2 ~2e-7 vs
the float64 reference; fp64: bit-exact against the reference, which is the
same cuFFT D2Z/Z2D path) with baseline latencies measured on an NVIDIA
GeForce RTX 5090 (sm_120) as a pre-submission smoke test, labeled as such in
all four request READMEs. I do not currently have access to a B200/B300; I
would be grateful if maintainers could run the documented flashinfer-bench
command from each README on the evaluation cluster, and I will append the
resulting B200 latency tables to the READMEs as soon as they are available.

## Target hardware

- [x] NVIDIA B200
- [ ] NVIDIA B300

## 评论 (0)
