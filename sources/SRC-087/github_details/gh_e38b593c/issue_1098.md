# [Issue #1098] [Bug]: Hardcoded Qwen3RMSNorm causes weight mismatch for non-Qwen3 models (e.g., Qwen3.5)

source: https://github.com/vllm-project/speculators/issues/1098
state: closed | updated: 2026-09-10T17:08:00Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:



### 🐛 Describe the bug

Description In `src/speculators/models/dflash/core.py at line 126`, the normalization layer is currently hardcoded to use `Qwen3RMSNorm`:
https://github.com/vllm-project/speculators/blob/main/src/speculators/models/dflash/core.py#L126
```
 self.norm = Qwen3RMSNorm(
            config.transformer_layer_config.hidden_size,
            eps=config.transformer_layer_config.rms_norm_eps,  # type: ignore[arg-type]
        )
```
If the target model is not Qwen3 (for instance, Qwen3.5), this hardcoded implementation leads to incorrect numerical results when loading the model weights.

Root Cause The RMSNorm implementations between Qwen3 and Qwen3.5 have fundamental structural differences in how the weight parameter is applied and initialized.

Here is the Qwen3RMSNorm implementation:
```
class Qwen3RMSNorm(nn.Module):
    def __init__(self, hidden_size, eps: float = 1e-6) -> None:
        """
        Qwen3RMSNorm is equivalent to T5LayerNorm
        """
        super().__init__()
        self.weight = nn.Parameter(torch.ones(hidden_size))
        self.variance_epsilon = eps

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:
        input_dtype = hidden_states.dtype
        hidden_states = hidden_states.to(torch.float32)
        variance = hidden_states.pow(2).mean(-1, keepdim=True)
        hidden_states = hidden_states * torch.rsqrt(variance + self.variance_epsilon)
        return self.weight * hidden_states.to(input_dtype)

    def extra_repr(self):
        return f"{tuple(self.weight.shape)}, eps={self.variance_epsilon}"
```
And here is the Qwen3_5RMSNorm implementation:
```
class Qwen3_5RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.zeros(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        output = self._norm(x.float())
        # Llama does x.to(float16) * w whilst Qwen3_5 is (x * w).to(float16)
        # See https://github.com/huggingface/transformers/pull/29402
        output = output * (1.0 + self.weight.float())
        return output.type_as(x)

    def extra_repr(self):
        return f"{tuple(self.weight.shape)}, eps={self.eps}"
```
Key Differences:

**1.Weight Initialization**: Qwen3RMSNorm initializes self.weight to ones, whereas Qwen3_5RMSNorm initializes to zeros.
**2.Forward Pass Calculation**:
Qwen3 calculates: self.weight * hidden_states
Qwen3.5 calculates: output * (1.0 + self.weight)
Because of these differences, if a Qwen3.5 checkpoint is force-loaded into a Qwen3RMSNorm module, the norm.weight values will mismatch mathematically. For example, a weight value of 0.5 in Qwen3.5 is meant to scale the output by 1.5 (1.0 + 0.5), but if loaded into Qwen3's module, it will scale the output by 0.5. This completely breaks the model's inference accuracy.

Suggested Fix The normalization layer should not be hardcoded to Qwen3RMSNorm. It should dynamically select the correct RMSNorm class based on the target model's architecture/configuration, or utilize a generic normalization wrapper that adapts to the specific weight format of the target model.


## 评论 (2)

### LOGO127 · 2026-09-08

There is an existing related implementation in @minziyu's PR #1090, `fix(models): resolve verifier_norm class by verifier family`. I checked its current diff at `21bdc0a90b85b45916cb9cfa2c93dda6490ca9e0`: it replaces the hardcoded **`verifier_norm`** constructor with a verifier-family resolver and includes local-config/architecture detection, raw-weight loading, and a float32 norm-equivalence test.

One scope distinction may help: `DFlashDraftModel` has separate `norm`, `hidden_norm`, and `verifier_norm` members. #1090 changes only `verifier_norm`, the one used for reconstructed verifier targets; it does not change every Qwen3RMSNorm in the draft model. If this report instead concerns the draft's own `norm`, that would need separate weight-provenance evidence rather than assuming the same change applies to all three.

Sharing the link to avoid duplicate implementation work. This is an AI-assisted source/diff cross-check, not an independent real-checkpoint or training validation of #1090, and I am not claiming authorship of that fix.


### fynnsu · 2026-09-10

I believe this has been handled by #1090 
