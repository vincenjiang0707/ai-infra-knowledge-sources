# [Issue #4542] [Feature Request] Add Multi-Format Tool Calling Support (OpenAI, Anthropic, Auto-Detection)

source: https://github.com/InternLM/lmdeploy/issues/4542
state: closed | updated: 2026-04-22T01:16:17Z
labels: 

## 正文

## Feature Request: Add Multi-Format Tool Calling Support (OpenAI, Anthropic, Auto-Detection)

### Problem Statement

LMDeploy is an outstanding LLM inference toolkit with exceptional performance. We've been running **Qwen2.5-32B-Instruct-AWQ** on NVIDIA Tesla V100 16GB SXM2 GPUs (tp=2), and the performance is remarkable - achieving **159.48 tok/s throughput with 100% success rate** on tool calling tasks. This is 234% faster than vLLM with GPTQ quantization on the same hardware.

However, LMDeploy currently only accepts **OpenAI format** for tool calling input, which limits compatibility with the growing Anthropic ecosystem (Claude Code, Anthropic SDK, etc.). This requires users to implement custom proxy layers for format conversion, adding unnecessary complexity.

### Current Behavior

LMDeploy's API server expects tool definitions in OpenAI format:

```python
# OpenAI format (currently supported)
tools = [{
    'type': 'function',
    'function': {
        'name': 'get_weather',
        'description': 'Get current weather',
        'parameters': {  # OpenAI uses 'parameters'
            'type': 'object',
            'properties': {
                'location': {'type': 'string'}
            }
        }
    }
}]
```

**Output format is already perfect** - LMDeploy correctly returns OpenAI-compatible responses with the standard `tool_calls` array. The issue is only with input format flexibility.

### Desired Behavior

LMDeploy should also accept **Anthropic format** for tool definitions:

```python
# Anthropic format (requested)
tools = [{
    'name': 'get_weather',
    'description': 'Get current weather',
    'input_schema': {  # Anthropic uses 'input_schema'
        'type': 'object',
        'properties': {
            'location': {'type': 'string'}
        }
    }
}]
```

### Proposed Solution

Add a `--tool-format` parameter to `lmdeploy serve api_server`:

```bash
# Option 1: Explicit format selection
lmdeploy serve api_server model_path --tool-format openai  # default
lmdeploy serve api_server model_path --tool-format anthropic
lmdeploy serve api_server model_path --tool-format auto  # auto-detect

# Option 2: Auto-detection (recommended)
# Detect format based on request structure:
# - Has 'input_schema' → Anthropic format
# - Has 'function.parameters' → OpenAI format
```

### Implementation Approach

The implementation would be straightforward - add an input normalization layer before existing parsers:

```python
def normalize_tool_format(tools, format='auto'):
    """Convert various tool formats to internal representation."""
    if format == 'auto':
        format = detect_format(tools)
    
    if format == 'anthropic':
        # Convert: input_schema → parameters
        return [{
            'type': 'function',
            'function': {
                'name': tool['name'],
                'description': tool.get('description', ''),
                'parameters': tool['input_schema']
            }
        } for tool in tools]
    
    return tools  # OpenAI format, no conversion needed

def detect_format(tools):
    """Auto-detect tool format from request structure."""
    if not tools:
        return 'openai'
    
    first_tool = tools[0]
    
    # Anthropic: flat structure with 'input_schema'
    if 'input_schema' in first_tool:
        return 'anthropic'
    
    # OpenAI: nested with 'function' and 'parameters'
    if 'function' in first_tool:
        return 'openai'
    
    return 'openai'  # default
```

**Key points**:
- Input normalization only (output format unchanged)
- Zero breaking changes (OpenAI format remains default)
- Existing tool parsers (qwen2d5, llama3, internlm) work unchanged
- Simple, maintainable code

### Use Case: Claude Code Integration

**Claude Code** is Anthropic's official CLI tool for AI-assisted development, gaining significant adoption in the Chinese developer community. It sends tool definitions in Anthropic format and cannot directly connect to LMDeploy without a custom proxy.

Our current workaround:
```
Claude Code → Custom Proxy (format conversion) → LMDeploy → Qwen2.5-32B-AWQ
```

With this feature:
```
Claude Code → LMDeploy (native support) → Qwen2.5-32B-AWQ
```

### Performance Benefits on Legacy GPUs

LMDeploy's exceptional performance on legacy GPUs makes it the ideal choice for many Chinese users with V100 hardware. Here's our benchmark data:

**Hardware**: NVIDIA Tesla V100 16GB SXM2 (Compute Capability 7.0)  
**Model**: Qwen2.5-32B-Instruct (tp=2)  
**Task**: Tool calling with 71 test cases

| Metric | LMDeploy + AWQ | vLLM + GPTQ | Improvement |
|--------|----------------|-------------|-------------|
| **Throughput** | 159.48 tok/s | 47.69 tok/s | **+234%** |
| **Success Rate** | 100% (71/71) | 71.83% (51/71) | **+28.17%** |
| **Avg Response Time** | 0.864s | 5.37s | **-84%** (6.2x faster) |
| **Quantization** | AWQ 4-bit | GPTQ 4-bit | - |

LMDeploy's AWQ quantization support for V100 (compute capability 7.0) is a game-changer for users with legacy hardware. Adding Anthropic format support would make this outstanding performance accessible to the entire Claude ecosystem.

### Community Benefit

This feature would benefit:

1. **Claude Code users** - Direct integration without custom proxies
2. **Anthropic SDK users** - Native compatibility with LMDeploy's performance
3. **Multi-platform developers** - Easier switching between OpenAI and Anthropic ecosystems
4. **Future compatibility** - Foundation for supporting additional formats (Google, Cohere, etc.)

### Proof of Concept

We've implemented a working custom proxy that demonstrates the feasibility:
- Converts Anthropic format to OpenAI format on input
- Passes through LMDeploy's OpenAI-compatible output unchanged
- Successfully runs Claude Code with Qwen2.5-32B-AWQ backend
- Code: `core/litellm/tool_proxy_anthropic.py` in our ArgoStack project

The conversion logic is simple and could be integrated directly into LMDeploy's API server.

### Related Work

- **vLLM** supports multiple tool calling formats through their tool parser system
- **LiteLLM** has hardcoded routing logic and requires provider-specific support (we've submitted a related feature request: BerriAI/litellm#26173)

### Tested Environment

- **LMDeploy Version**: v0.12.3
- **Models**: Qwen2.5-32B-Instruct-AWQ, Qwen2.5-Coder-32B-Instruct-AWQ
- **Tool Parsers**: qwen2d5, qwen3coder
- **Hardware**: NVIDIA Tesla V100 16GB SXM2 (tp=2)
- **Quantization**: AWQ 4-bit (compute capability 7.0 compatible)

### Conclusion

LMDeploy's performance is outstanding, especially on legacy GPUs. Adding multi-format tool calling support would:
- Eliminate the need for custom proxy layers
- Enable direct Claude Code integration
- Benefit the broader Chinese AI developer community
- Align with LMDeploy's mission as a comprehensive "toolkit for deploying LLMs"

We're happy to contribute code if the maintainers are interested in this feature.

---

Submitted by Zamba Lee @ArgoStack, THINKTOP.

*Co-created with [Claude Code](https://claude.ai/code) (Claude Sonnet 4.6)*


## 评论 (1)

### lvhan028 · 2026-04-21

I think the key point is we should implement Anthropic API.
I am working on it. #4538 

