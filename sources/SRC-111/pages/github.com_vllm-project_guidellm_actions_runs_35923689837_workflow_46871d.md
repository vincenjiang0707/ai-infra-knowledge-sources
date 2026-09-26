source: https://github.com/vllm-project/guidellm/actions/runs/35923689837/workflow

# Improvement to team status skill (#1157) #435

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