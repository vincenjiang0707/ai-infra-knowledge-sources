source: https://github.com/mcp/ChromeDevTools/chrome-devtools-mcp

# Chrome DevTools for agents

Chrome DevTools for agents (`chrome-devtools-mcp`

) lets your coding agent (such as Antigravity, Claude, Cursor or Copilot)

control and inspect a live Chrome browser. It acts as a Model-Context-Protocol

(MCP) server, giving your AI coding assistant access to the full power of

Chrome DevTools for reliable automation, in-depth debugging, and performance analysis.

A [CLI](https://github.com/docs/cli.md) is also provided for use without MCP.

[Tool reference](https://github.com/docs/tool-reference.md) | [Changelog](https://github.com/CHANGELOG.md) | [Contributing](https://github.com/CONTRIBUTING.md) | [Troubleshooting](https://github.com/docs/troubleshooting.md) | [Design Principles](https://github.com/docs/design-principles.md)

## Key features

**Get performance insights**: Uses[Chrome](https://github.com/ChromeDevTools/devtools-frontend)to record

DevTools

traces and extract actionable performance insights.**Advanced browser debugging**: Analyze network requests, take screenshots and

check browser console messages (with source-mapped stack traces).**Reliable automation**. Uses

[puppeteer](https://github.com/puppeteer/puppeteer)to automate actions in

Chrome and automatically wait for action results.

## Disclaimers

`chrome-devtools-mcp`

exposes content of the browser instance to the MCP clients

allowing them to inspect, debug, and modify any data in the browser or DevTools.

Avoid sharing sensitive or personal information that you don't want to share with

MCP clients.

`chrome-devtools-mcp`

officially supports Google Chrome and [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) only.

Other Chromium-based browsers may work, but this is not guaranteed, and you may encounter unexpected behavior. Use at your own discretion.

We are committed to providing fixes and support for the latest version of [Extended Stable Chrome](https://chromiumdash.appspot.com/schedule).

Performance tools may send trace URLs to the Google CrUX API to fetch real-user

experience data. This helps provide a holistic performance picture by

presenting field data alongside lab data. This data is collected by the [Chrome
User Experience Report (CrUX)](https://developer.chrome.com/docs/crux). To disable

this, run with the

`--no-performance-crux`

flag.**Usage statistics**

Google collects usage statistics (such as tool invocation success rates, latency, and environment information) to improve the reliability and performance of Chrome DevTools MCP.

Data collection is **enabled by default**. You can opt-out by passing the `--no-usage-statistics`

flag when starting the server:

`"args": ["-y", "chrome-devtools-mcp@latest", "--no-usage-statistics"]`

Google handles this data in accordance with the [Google Privacy Policy](https://policies.google.com/privacy).

Google's collection of usage statistics for Chrome DevTools MCP is independent from the Chrome browser's usage statistics. Opting out of Chrome metrics does not automatically opt you out of this tool, and vice-versa.

Collection is disabled if `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS`

or `CI`

env variables are set.

## Update checks

By default, the server periodically checks the npm registry for updates and logs a notification when a newer version is available.

You can disable these update checks by setting the `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS`

environment variable.

## Requirements

## Getting started

Add the following config to your MCP client:

```
{
"mcpServers": {
"chrome-devtools": {
"command": "npx",
"args": ["-y", "chrome-devtools-mcp@latest"]
}
}
}
```

Note

Using `chrome-devtools-mcp@latest`

ensures that your MCP client will always use the latest version of the Chrome DevTools MCP server.

If you are interested in doing only basic browser tasks, use the `--slim`

mode:

```
{
"mcpServers": {
"chrome-devtools": {
"command": "npx",
"args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
}
}
}
```

See [Slim tool reference](https://github.com/docs/slim-tool-reference.md).

### MCP Client configuration

For setup instructions specific to your editor or agent (e.g. Antigravity, Claude Code, Cursor, VS Code), please see our [Client Configurations Guide](https://github.com/docs/client-configurations.md).

### Your first prompt

Enter the following prompt in your MCP Client to check if everything is working:

```
Check the performance of https://developers.chrome.com
```


Your MCP client should open the browser and record a performance trace.

Note

The MCP server will start the browser automatically once the MCP client uses a tool that requires a running browser instance. Connecting to the Chrome DevTools MCP server on its own will not automatically start the browser.

## Tools

If you run into any issues, checkout our [troubleshooting guide](https://github.com/docs/troubleshooting.md).

See the full [Tool Reference](https://github.com/docs/tool-reference.md) for a complete list of all supported MCP capabilities.

## Configuration

Find the complete list of server parameters (e.g., `--headless`

, `--isolated`

, `--slim`

) and how to configure WebSocket connections in the [Configuration Guide](https://github.com/docs/configuration.md).

## Advanced Usage

For advanced features such as handling concurrent sessions, persistent user data directories, connecting to a running Chrome instance instead of starting a new one, or debugging on Android, see our [Advanced Usage Guide](https://github.com/docs/advanced-usage.md).

## Integrating as a browser subagent

If you are developing agentic tooling and want to provide an integrated browser subagent as part of your product, we recommend building on top of Chrome DevTools for agents.

For a reference implementation, see the [Gemini CLI browser agent documentation](https://geminicli.com/docs/core/subagents/#browser-agent).