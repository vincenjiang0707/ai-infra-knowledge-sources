# [Issue #761] GuideLLM 0.6.0 HTML report displays empty metrics despite valid benchmark data

source: https://github.com/vllm-project/guidellm/issues/761
state: closed | updated: 2026-07-21T09:37:08Z
labels: 

## 正文

### Bug Description

Environment

GuideLLM: 0.6.0
Backend: vLLM (OpenAI-compatible endpoint)
Browser tested:
- Firefox
- Google Chrome
Report served through:
- python3 -m http.server
- Same behavior when opening directly from filesystem

Benchmark execution completes successfully and generates both:

benchmarks.json
benchmarks.html

The generated HTML report loads correctly but displays:

Number of benchmarks: 0
All metrics = 0
No charts rendered

### Expected Behavior

The report should display benchmark results and charts from the generated benchmark data.

What I verified

The generated HTML file contains non-empty benchmark data:

grep -oE '"requestsPerSecond"[[:space:]]*:[[:space:]]*[0-9.]+' benchmarks.html | head

Output:

"requestsPerSecond": 0.2
"requestsPerSecond": 0.13333333333333333
"requestsPerSecond": 0.06666666666666667
...

The HTML also contains:

window.benchmarks = [...]

and:

window.workloadDetails = {...}

with valid TTFT, ITL, throughput and request statistics.

Browser diagnostics

No JavaScript errors are visible in the browser console.

The only warning is:

Manifest: property 'start_url' ignored, should be same origin as document.

which appears unrelated.

### Steps to Reproduce

guidellm benchmark run \ --target "http://<vllm-host>:8510" \ --backend openai_http \ --model "Qwen/Qwen3.5-397B-A17B" \ --processor "<tokenizer-directory>" \ --data '{"prompt_tokens":256,"output_tokens":128}' \ --profile sweep \ --max-seconds 15 \ --output-dir "./results" \ --outputs benchmarks.json,benchmarks.html

### Operating System

Ubuntu 24.04

### Python Version

python 3.10

### GuideLLM Version

guidellm version: 0.6.0

### Installation Method

pip install guidellm[recommended]

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell

```

### Additional Context

_No response_

## 评论 (7)

### sjmonson · 2026-06-10

This might be related to #744 which is fixed on `main` and will be in `v0.7.0`. Note that the current HTML report is not actively maintained and we have plans to replace it.

### sjmonson · 2026-07-01

Closing as v0.7.0 is out now. Please reopen if this is still an issue.

### FabianR-Parat · 2026-07-03

Even with GuideLLM v0.7.1 and v0.7.0 the benchmarks.html report still seems broken.
Backend: vLLM (OpenAI-compatible endpoint)
OS: Ubuntu 26.04

### Expected Behaviour

The report should display benchmark results and charts from the generated benchmark data.

### Actual Behaviour
I have run this benchmark
```
podman run \
  --rm -it \
 -v "./results:/results:rw" \
  -e GUIDELLM__SPEC__BACKEND='{"kind": "openai_http", "target": "http://host.containers.internal:8000"}' \
  -e GUIDELLM__SPEC__PROFILE='{"kind": "sweep"}' \
  -e GUIDELLM__SPEC__CONSTRAINTS='[{"kind": "max_duration", "seconds": 10}]' \
  -e GUIDELLM__SPEC__OUTPUTS='[{"kind": "html", "path": "/results/benchmarks.html"}, {"kind": "json", "path": "/results/benchmarks.json"}, {"kind": "csv", "path": "/results/benchmarks.csv"}]' \
  -e GUIDELLM__SPEC__DATA='[{"kind": "synthetic_text", "prompt_tokens": 512, "output_tokens": 256}]' \
  ghcr.io/vllm-project/guidellm:v0.7.1
```

and the benchmarks.html looks like this:

<img width="1435" height="754" alt="Image" src="https://github.com/user-attachments/assets/8c39abe9-d597-4dcc-8f71-46ec356a68f3" />
The .html file does contain data, but it does not display it in the .html.

Tested with Firefox and Microsoft Edge.
Although the benchmark is short, it was succesful and produced output data.

As stated above, I have also tested this with GuideLLM v0.7.0. It doesn't work either.


### FabianR-Parat · 2026-07-06

@sjmonson What do you think?

### sjmonson · 2026-07-06

So it turns out that #744 didn't apply as we no longer build the UI in CI so it has to be built and pushed manually.

I have pushed a fix but it requires targeting the new template so as a temporary workaround set `GUIDELLM__REPORT_GENERATION__SOURCE=https://vllm-project.github.io/guidellm/ui/v0.7.1/index.html` during benchmarks which should fix the issue. If you have existing `benchmarks.json`s you can run `GUIDELLM__REPORT_GENERATION__SOURCE=https://vllm-project.github.io/guidellm/ui/v0.7.1/index.html guidellm benchmark from-file --output-formats html benchmarks.json` to reconvert them.

### FabianR-Parat · 2026-07-16

works, thank you!

### FalTeaK · 2026-07-21

I can also confirm that it works, thanks!
