source: https://github.com/vllm-project/guidellm/actions/runs/35834036251/workflow

# fix: preserve resize dimensions for image URLs #3262

#### Workflow file for this run

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)| name: Development | |
| on: | |
| pull_request: | |
| types: [opened, synchronize, reopened] | |
| jobs: | |
| tests: | |
| strategy: | |
| matrix: | |
| python: ["3.10"] | |
| uses: ./.github/workflows/testing.yml | |
| with: | |
| python: ${{ matrix.python }} | |
| quality: | |
| strategy: | |
| matrix: | |
| python: ["3.10"] | |
| uses: ./.github/workflows/quality.yml | |
| with: | |
| python: ${{ matrix.python }} |