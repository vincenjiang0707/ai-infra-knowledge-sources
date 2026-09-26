source: https://github.com/sgl-project/genai-bench

Genai-bench is a powerful benchmark tool designed for comprehensive token-level performance evaluation of large language model (LLM) serving systems.

It provides detailed insights into model serving performance, offering both a user-friendly CLI and a live UI for real-time progress monitoring.

- 🛠️
**CLI Tool**: Validates user inputs and initiates benchmarks seamlessly. - 📊
**Live UI Dashboard**: Displays current progress, logs, and real-time metrics. - 📝
**Rich Logs**: Automatically flushed to both terminal and file upon experiment completion. - 📈
**Experiment Analyzer**: Generates comprehensive Excel reports with pricing and raw metrics data, plus flexible plot configurations (default 2x4 grid) that visualize key performance metrics including throughput, latency (TTFT, E2E, TPOT), error rates, and RPS across different traffic scenarios and concurrency levels. Supports custom plot layouts and multi-line comparisons.

**Quick Start**: Install with `pip install genai-bench`

.
Alternatively, check [Installation Guide](https://docs.sglang.ai/genai-bench/getting-started/installation) for other options.

-
**Run a benchmark**against your model:# Text generation (chat completions) genai-bench benchmark --api-backend "your-backend" \ --api-base "http://localhost:8080" \ --api-key "your-api-key" \ --api-model-name "your-model" \ --task text-to-text \ --max-time-per-run 5 \ --max-requests-per-run 100 # Image generation (OpenAI-compatible /v1/images/generations) genai-bench benchmark --api-backend openai \ --api-base "http://localhost:8080" \ --api-key "your-api-key" \ --api-model-name "your-model" \ --model-tokenizer "gpt2" \ --task text-to-image \ --traffic-scenario "I(1024,1024)" \ --max-time-per-run 60 \ --max-requests-per-run 10 \ --dataset-path /path/to/image_prompts.txt

-
**Generate Excel reports**from your results:genai-bench excel --experiment-folder ./experiments/your_experiment \ --excel-name results --metric-percentile mean

-
**Create visualizations**:genai-bench plot --experiments-folder ./experiments \ --group-key traffic_scenario --preset 2x4_default


If you're new to GenAI Bench, check out the [Getting Started](https://docs.sglang.ai/genai-bench/getting-started/) page.

For detailed instructions, advanced configuration options, and comprehensive examples, check out the [User Guide](https://docs.sglang.ai/genai-bench/user-guide/).

If you are interested in contributing to GenAI-Bench, you can use the [Development Guide](https://docs.sglang.ai/genai-bench/developer-guide/).