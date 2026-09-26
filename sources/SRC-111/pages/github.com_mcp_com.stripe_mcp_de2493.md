source: https://github.com/mcp/com.stripe/mcp

Stripe

By [stripe](https://github.com/stripe)·1,830

MCP server integrating with Stripe - tools for customers, products, payments, and more.

# Stripe AI

This repo is the one-stop shop for building AI-powered products and businesses on top of Stripe.

It contains a collection of SDKs to help you integrate Stripe with LLMs and agent frameworks, including:

- for integrating Stripe's billing infrastructure with Vercel's`@stripe/ai-sdk`

and`ai`

libraries.`@ai-sdk`

- for integrating Stripe's billing infrastructure with native SDKs from OpenAI, Anthropic, and Google Gemini, without any framework dependencies.`@stripe/token-meter`


## Model Context Protocol (MCP)

Stripe hosts a remote MCP server at `https://mcp.stripe.com`

. This allows secure MCP client access via OAuth. View the docs [here](https://docs.stripe.com/mcp#connect).

You can also [build autonomous agents](https://docs.stripe.com/mcp#agents) with MCP as well.

## Agent skills

[Agent skills](https://agentskills.io/home) are instructions that agents can use to build faster and more accurately. Stripe offers a collection of skills that help your agents use the latest best practices when building with Stripe.

If you use one of these popular agent harnesses, we recommend installing the official Stripe plugins, which include additional agent tools and update automatically.

### Claude Code

Run this command in your project:

`claude plugin install stripe@claude-plugins-official`

### Codex

Run this command in your project:

`codex plugin add stripe@openai-curated`

### Cursor

Run this command in your project:

`/add-plugin stripe`

You can also install through the [Cursor marketplace](https://cursor.com/marketplace/stripe).

### Grok Build

Run this command in your project:

`grok plugin install stripe --trust`

### Agent Plugins

Installation methods currently vary by client for the new [Agent Plugins](https://agent-plugins.org/) standard, but you can point your client to our package via:

- Git URL:
`https://github.com/stripe/ai`

- Subdirectory:
.`providers/agent-plugins/plugin/`


## Manual installation

Manually installed skills don’t auto-update. Run

`npx skills update -y`

to get the latest versions.

Run this command in your project:

`npx skills add https://docs.stripe.com`