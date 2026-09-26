source: https://github.com/vllm-project/guidellm/actions/runs/35879667178/workflow

# docs: move English docs under en (#1170) #434

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| name: Main | |
| on: | |
| push: | |
| branches: | |
| - main | |
| jobs: | |
| tests: | |
| strategy: | |
| matrix: | |
| python: ["3.10", "3.11", "3.12", "3.13"] | |
| uses: ./.github/workflows/testing.yml | |
| with: | |
| python: ${{ matrix.python }} | |
| args: -m "smoke" | |
| quality: | |
| strategy: | |
| matrix: | |
| python: ["3.10", "3.11", "3.12", "3.13"] | |
| uses: ./.github/workflows/quality.yml | |
| with: | |
| python: ${{ matrix.python }} |