source: https://github.com/vllm-project/guidellm/commit/02902219f9fd6915952834fda4295c58b4acce42

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

|`--target`| URL of the OpenAI-compatible server |`--target "http://localhost:8000"`|

61

+

|`--model`| Model name to benchmark |`--model "Meta-Llama-3.1-8B-Instruct"`|

62

+

|`--data`| Data configuration for benchmarking |`--data "prompt_tokens=256,output_tokens=128"`|

63

+

|`--profile`| Type of benchmark profile to run |`--profile sweep`|

64

+

|`--rate`| Request rate or number of benchmarks for sweep |`--rate 10`|

65

+

|`--images-per-request`| Number of images per request for vision benchmarks |`--images-per-request "1,2,5"`|

66

+

|`--random-seed`| Random seed for reproducibility |`--random-seed 42`|

67

+

|`--max-seconds`| Duration for each benchmark in seconds |`--max-seconds 30`|

68

+

|`--max-requests`| Maximum number of requests for each benchmark |`--max-requests 1000`|

69

+

|`--output-dir`| Directory path to save output files |`--output-dir results/`|

70

+

|`--outputs`| Output formats to generate |`--outputs json csv html`|

70

71

71

72

### Random Seed (`--random-seed`)

72

73

@@ -209,6 +210,55 @@ guidellm benchmark \

209

210

--rate 5

210

211

```

211

212

213

+

### Multi-Image Benchmarking

214

+

215

+

When benchmarking vision-language models with multiple images per request, use `--images-per-request` to measure latency impact. This is useful for understanding how TTFT and ITL scale with increasing frame/image counts:

216

+

217

+

```bash

218

+

guidellm benchmark \

219

+

--target "http://localhost:8000" \

220

+

--data "prompt_tokens=256,output_tokens=128" \

221

+

--images-per-request 1,2,5 \

222

+

--profile constant \

223

+

--rate 10 \

224

+

--max-seconds 30

225

+

```

226

+

227

+

This runs three sequential benchmarks (1, 2, and 5 images per request) with synthetic 720p images and outputs comparative latency metrics in the report.

228

+

229

+

**Single image count:**

230

+

231

+

```bash

232

+

guidellm benchmark \

233

+

--target "http://localhost:8000" \

234

+

--images-per-request 3 \

235

+

--profile constant \

236

+

--rate 5

237

+

```

238

+

239

+

**Programmatic usage:**

240

+

241

+

```python

242

+

from guidellm.benchmark import MultiImageBenchmark

**Note:** Multi-image benchmarking requires the vision dependencies (`pip install guidellm[vision]`).

261

+

212

262

## Output Options

213

263

214

264

By default, complete results are saved to `benchmarks.json`, `benchmarks.csv`, and `benchmarks.html` in your current directory. Use the `--output-dir` parameter to specify a different location and `--outputs` to control which formats are generated.

## 0 commit comments