source: https://github.com/aidatatools/ollama-benchmark

LLM Benchmark for Throughput via Ollama (Local LLMs)

Measure how fast your local LLMs *really* are—with a simple, cross-platform CLI tool that tells you the tokens-per-second truth.

Working [Ollama](https://ollama.com) installation.

```
python3 -m venv .venv
## On Linux and macOS
source .venv/bin/activate
## On Windows Powershell or Cmd
.\.venv\Scripts\activate
```

```
uv venv .venv --python 3.13
## On Linux and macOS
source .venv/bin/activate
## On Windows Powershell or Cmd
.\.venv\Scripts\activate
```

Depending on your python setup either

`pip install llm-benchmark`

or

`pipx install llm-benchmark`

or uv

`uv pip install llm-benchmark`

`llm_benchmark run`

It's tested on Python 3.10 and above.

7B model can be run on machines with 8GB of RAM

13B model can be run on machines with 16GB of RAM

On Windows, Linux, and macOS, it will detect memory RAM size to first download required LLM models.

When memory RAM size is greater than or equal to 4GB, but less than 7GB, it will check if gemma:2b exist. The program implicitly pull the model.

```
ollama pull deepseek-r1:1.5b
ollama pull gemma:2b
ollama pull phi:2.7b
ollama pull phi3:3.8b
```

When memory RAM size is greater than 7GB, but less than 15GB, it will check if these models exist. The program implicitly pull these models

```
ollama pull phi3:3.8b
ollama pull gemma2:9b
ollama pull mistral:7b
ollama pull llama3.1:8b
ollama pull deepseek-r1:8b
ollama pull llava:7b
```

When memory RAM size is greater than 15GB, but less than 31GB, it will check if these models exist. The program implicitly pull these models

```
ollama pull gemma2:9b
ollama pull mistral:7b
ollama pull phi4:14b
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:14b
ollama pull llava:7b
ollama pull llava:13b
```

When memory RAM size is greater than 31GB, it will check if these models exist. The program implicitly pull these models

```
ollama pull phi4:14b
ollama pull deepseek-r1:14b
ollama pull gpt-oss:20b
```

[https://python-poetry.org/docs/#installing-manually](https://python-poetry.org/docs/#installing-manually)

```
python3 -m venv .venv
. ./.venv/bin/activate
pip install -U pip setuptools
pip install poetry
```

```
poetry shell
poetry install
llm_benchmark hello jason
```

`llm_benchmark run`

`llm_benchmark run --no-sendinfo`

### Example #3 Benchmark run on explicitly given the path to the ollama executable (When you built your own developer version of ollama)

`llm_benchmark run --ollamabin=~/code/ollama/ollama`

- Create a custom benchmark file like following yaml format, replace with your own benchmark models, remember to use double quote for your model name

```
file_name: "custombenchmarkmodels.yml"
version: 2.0.custom
models:
- model: "deepseek-r1:1.5b"
- model: "qwen:0.5b"
```

- run with the flag and point to the path of custombenchmarkmodels.yml

`llm_benchmark run --custombenchmark=path/to/custombenchmarkmodels.yml`