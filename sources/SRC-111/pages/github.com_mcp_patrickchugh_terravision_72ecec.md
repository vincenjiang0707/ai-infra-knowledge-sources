source: https://github.com/mcp/patrickchugh/terravision

TerraVision

By [patrickchugh](https://github.com/patrickchugh)·1,637

Cloud architecture diagrams generated from terraform plan, with official AWS, Azure, GCP icons

# TerraVision

**Turn Terraform code into professional cloud architecture diagrams that stay in sync with your infrastructure — automatic, secure, living documents**

## Watch a 4-Minute Intro

## What is TerraVision?

TerraVision automatically converts your Terraform code into professional-grade cloud architecture diagrams using the official AWS, GCP, and Azure icon sets. Your diagrams stay in sync with your infrastructure — no more outdated Visio, draw.io or Lucidchart files.

## Why TerraVision?

- ✅
**Always up-to-date**— diagrams generated directly from your Terraform code - ✅
**100% client-side**— no cloud access required, runs locally, your code never leaves your machine - ✅
**CI/CD ready**— automate diagram updates on every PR merge - ✅
**Free & open source**— no expensive diagramming tool licenses - ✅
**Multi-cloud**— AWS (full), GCP, and Azure (core services) - ✅
**Interactive HTML output**— clickable nodes, pan/zoom, search, animated data flow - ✅
**Editable draw.io export**— open in draw.io, Lucidchart, or any mxGraph editor - ✅
**Optional AI annotations**— labels, titles, and flow sequences from Ollama (local) or AWS Bedrock - ✅
**Terragrunt compatible**— auto-detects single- and multi-module Terragrunt projects - ✅
**MCP server**— let AI agents generate diagrams from your Terraform,[see the guide](https://github.com/patrickchugh/terravision/blob/main/docs/mcp-server.md)

## Supported Cloud Providers

| Provider | Status | Resources |
|---|---|---|
AWS |
✅ Full support | 200+ services |
Google Cloud |
🔄 Partial support | Core services |
Azure |
🔄 Partial support | Core services |

## Quick Start

### Install

`pipx install terravision # or: pip install terravision if in a virtual env`

You also need **Python 3.10+**, **Terraform 1.x**, **Graphviz**, and **Git**. See the [Installation Guide](https://patrickchugh.github.io/terravision/installation/) for platform-specific instructions, Docker, and Nix.

### Generate your first diagram

```
git clone https://github.com/patrickchugh/terravision.git
cd terravision
# EKS cluster example
terravision draw --source tests/fixtures/aws_terraform/eks_automode --show
# Azure VM scale set
terravision draw --source tests/fixtures/azure_terraform/test_vm_vmss --show
# From a public Git repo (note the // for subfolder)
terravision draw --source https://github.com/patrickchugh/terraform-examples.git//aws/wordpress_fargate --show
```

That's it — your diagram is saved as `architecture.png`

and opens automatically.

### Generate an interactive HTML diagram

`terravision visualise --source ./path-to-your-terraform --show`

Click any resource to see its Terraform metadata, search resources, pan/zoom, and watch animated data flow on edges. The HTML is a single self-contained file that works fully offline.

## Try the Interactive Demos

Click any of these to see the interactive HTML output TerraVision produces:

- 🟧
— Wordpress on ECS Fargate with CloudFront, RDS, EFS[AWS demo](https://patrickchugh.github.io/terravision/demo-aws.html) - 🟦
— VM scale set with load balancer and VNet[Azure demo](https://patrickchugh.github.io/terravision/demo-azure.html) - 🟩
— Core GCP networking and compute[GCP demo](https://patrickchugh.github.io/terravision/demo-gcp.html)

## Basic Usage

### Generate a diagram

```
# From a local directory
terravision draw --source ./path-to-your-terraform
# From a Git repository
terravision draw --source https://github.com/user/repo.git
# Custom format and filename
terravision draw --source ./path-to-your-terraform --format svg --outfile my-architecture
# Editable draw.io file
terravision draw --source ./path-to-your-terraform --format drawio --outfile my-architecture
```

### Use a pre-generated Terraform plan (no cloud credentials needed)

```
# Step 1: in your Terraform environment
terraform plan -out=tfplan.bin
terraform show -json tfplan.bin > plan.json
terraform graph > graph.dot
# Step 2: diagram generation, no Terraform or cloud access required
terravision draw --planfile plan.json --graphfile graph.dot --source ./path-to-your-terraform
```

### AI-powered annotations (optional)

```
terravision draw --source ./path-to-your-terraform --ai-annotate ollama # local LLM (no data leaves your machine)
terravision draw --source ./path-to-your-terraform --ai-annotate bedrock # AWS Bedrock via boto3 (uses your AWS credentials)
terravision draw --source ./path-to-your-terraform --ai-annotate restapi # any OpenAI-compatible endpoint (OpenAI, LiteLLM, vLLM, ...)
```

Only metadata and the summary graph are sent to the LLM — never your `.tf`

source. The `bedrock`

backend authenticates via the standard AWS credential chain (no infrastructure to deploy); `restapi`

is configured via `TV_RESTAPI_URL`

, `TV_RESTAPI_KEY`

, and `TV_RESTAPI_MODEL`

. See the [Annotations Guide](https://patrickchugh.github.io/terravision/annotations/) and [AI-Powered Annotations](https://patrickchugh.github.io/terravision/usage-guide/#ai-powered-annotations) for the full configuration.

### Simplified view

`terravision draw --source ./path-to-your-terraform --simplified`

Strips VPCs, subnets, and networking plumbing. Great for executive presentations.

### Common options

`terravision --help`

shows full help text details.

| Option | Description | Example |
|---|---|---|
`--source` |
Terraform directory or Git URL | `./path-to-your-terraform` |
`--format` |
Output format: `png` , `svg` , `pdf` , `drawio` ,
|
`svg` |
`--outfile` |
Output filename | `my-architecture` |
`--workspace` |
Terraform workspace | `production` |
`--varfile` |
Variable file (repeatable) | `prod.tfvars` |
`--planfile` |
Pre-generated plan JSON | `plan.json` |
`--graphfile` |
Pre-generated graph DOT | `graph.dot` |
`--ai-annotate` |
AI annotation backend | `ollama` , `bedrock` , `restapi` |
`--simplified` |
High-level view (no networking) | (flag) |
`--show` |
Open after generation | (flag) |

## Documentation

The complete documentation lives at ** patrickchugh.github.io/terravision**.

**For users:**

[Installation Guide](https://github.com/patrickchugh/terravision/blob/main/docs/installation.md)[Usage Guide](https://github.com/patrickchugh/terravision/blob/main/docs/usage-guide.md)[Annotations Guide](https://github.com/patrickchugh/terravision/blob/main/docs/annotations.md)[CI/CD Integration](https://github.com/patrickchugh/terravision/blob/main/docs/cicd-integration.md)[MCP Server Guide](https://github.com/patrickchugh/terravision/blob/main/docs/mcp-server.md)[FAQ](https://github.com/patrickchugh/terravision/blob/main/docs/faq.md)[Troubleshooting](https://github.com/patrickchugh/terravision/blob/main/docs/troubleshooting.md)

**For contributors:**

## FAQ

Common questions — cloud credentials, LLM data privacy, offline use, Terragrunt, output formats, and more — are answered in the ** FAQ on the documentation site**.

## Contributing

Contributions are very welcome. See [CONTRIBUTING.md](https://github.com/patrickchugh/terravision/blob/main/docs/CONTRIBUTING.md) for development setup, coding standards, and the PR process.

## Support

**Issues**:[GitHub Issues](https://github.com/patrickchugh/terravision/issues)**Discussions**:[GitHub Discussions](https://github.com/patrickchugh/terravision/discussions)**Documentation**:[patrickchugh.github.io/terravision](https://patrickchugh.github.io/terravision/)

## License

See [LICENSE](https://github.com/patrickchugh/terravision/blob/main/LICENSE).

## Acknowledgments

[Graphviz](https://graphviz.org/)— diagram rendering[Terraform](https://www.terraform.io/)— infrastructure parsing[Terragrunt](https://terragrunt.gruntwork.io/)— multi-module orchestration- Cloud provider icons from official AWS, GCP, and Azure icon sets