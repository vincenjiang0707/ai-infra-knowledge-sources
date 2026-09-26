source: https://github.com/vllm-project/guidellm/blob/main/docs/en/getting-started/install.md

| weight | -10 |
|---|

GuideLLM can be installed using several methods depending on your requirements. Below are the detailed instructions for each installation pathway.

Before installing GuideLLM, ensure you have the following prerequisites:

-
**Operating System:**Linux or MacOS -
**Python Version:**3.10 – 3.13 -
**Pip Version:**Ensure you have the latest version of pip installed. You can upgrade pip using the following command:python -m pip install --upgrade pip


The simplest way to install GuideLLM is via pip from the Python Package Index (PyPI):

`pip install guidellm[recommended]`

This will install the latest stable release of GuideLLM with recommended dependencies.

If you need a specific version of GuideLLM, you can specify the version number during installation. For example, to install version `0.2.0`

:

`pip install guidellm==0.2.0`

To install the latest development version of GuideLLM from the main branch, use the following command:

`pip install git+https://github.com/vllm-project/guidellm.git`

This will clone the repository and install GuideLLM directly from the main branch.

If you want to install GuideLLM from a specific branch (e.g., `feature-branch`

), use the following command:

`pip install git+https://github.com/vllm-project/guidellm.git@feature-branch`

Replace `feature-branch`

with the name of the branch you want to install.

If you have cloned the GuideLLM repository locally and want to install it, navigate to the repository directory and run:

`pip install .`

Alternatively, for development purposes, you can install it in editable mode:

`pip install -e .`

This allows you to make changes to the source code and have them reflected immediately without reinstalling.

After installation, you can verify that GuideLLM is installed correctly by running:

`guidellm --help`

This should display the installed version of GuideLLM.

To use the vLLM Python backend (in-process inference), see [vLLM Python backend](https://github.com/vllm-project/guidellm/blob/main/docs/en/guides/vllm-python-backend.md) for recommended installation (container or existing vLLM environment) and pip installation notes.

If you encounter any issues during installation, ensure that your Python and pip versions meet the prerequisites. For common runtime errors (debug logging, tokenizer loading, macOS worker crashes), see the [Troubleshooting guide](https://github.com/vllm-project/guidellm/blob/main/docs/en/guides/troubleshooting.md). For further assistance, please refer to the [GitHub Issues](https://github.com/vllm-project/guidellm/issues) page.