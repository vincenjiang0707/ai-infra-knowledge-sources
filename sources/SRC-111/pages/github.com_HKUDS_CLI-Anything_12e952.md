source: https://github.com/HKUDS/CLI-Anything

**Today's Software Serves Humans👨💻. Tomorrow's Users will be Agents🤖.
CLI-Anything: Bridging the Gap Between AI Agents and the World's Software**

**🌐 CLI-Hub**:

`pip install cli-anything-hub`

then `cli-hub install <name>`

— browse, install, and manage all community-built CLIs. Want to add your own? [Open a PR](https://github.com/HKUDS/CLI-Anything/blob/main/CONTRIBUTING.md)— the hub updates instantly.

**🎬 See Demos**: Watch AI agents use generated CLIs plus preview, live preview, and trajectory loops to produce real artifacts — CAD builds, 3D scenes, diagrams, gameplay, subtitles, and more.

**🙋 [Become a Contributor, or Request a CLI]**: [Join us](https://github.com/HKUDS/CLI-Anything/issues/new?template=contributor-signup.yml)! Sign up to build a new CLI harness — once reviewed and merged, you'll gain access as one of our community contributors! Wish CLI-Anything supported a specific software or service? Submit a [wishlist request](https://github.com/HKUDS/CLI-Anything/issues/new?template=cli-wishlist.yml)!

**One Command Line**: Make any software agent-ready for Pi, OpenClaw, nanobot, Cursor, Claude Code, etc. [ 中文文档](https://github.com/HKUDS/CLI-Anything/blob/main/README_CN.md) |

[|](https://github.com/HKUDS/CLI-Anything/blob/main/README_JA.md)

**日本語ドキュメント**

**Deutsch**Thanks to all invaluable efforts from the community! More updates continuously on the way everyday..


-
**2026-05-30**🧭**Hermes skill**proposed (#320), adding a CLI-Anything orchestration skill with installer scripts and HARNESS fallback guidance. 🗺️**ArcGIS Pro**was proposed for the public registry (#318) as a Windows/ArcPy CLI for cartography, geoprocessing, feature editing, and live-Pro MCP workflows. -
**2026-05-27**🔧**CLI-Hub**registry date updates now handle`python -m pip`

install commands (#312), improving package-date detection for registry automation. -
**2026-05-23**📝**Obsidian Agent CLI**was proposed for the public registry (#307), bringing a PyPI-installed Obsidian automation CLI with persistent agent memory workflows and a pinned skill link. -
**2026-05-21**🔒**Sketch CLI**token-file handling was hardened against path traversal and symlink escapes (#304). -
**2026-05-20**📓**Joplin CLI**was proposed (#300) with notebooks, notes, to-dos, tags, attachments, search/sync, import/export, server/E2EE helpers, full docs, packaged skill docs, and a 134-test validation baseline. -
**2026-05-20**🎛️**Rekordbox CLI**merged (#252) with guarded SQLCipher write paths, backup-required forced writes, smoke coverage, and root skill sync. 📚**Calibre CLI**merged (#223) with library/search/metadata/conversion/export workflows, 41 unit tests, real-Calibre E2E evidence, and root skill validation. 🧊**3MF CLI**merged (#209) with mesh inspection, hole resizing, repair, comparison, and preserved triangle attributes. 🎙️**MiniMax CLI**merged (#189) with chat/TTS workflows, JSON-safe model/voice listing, REPL quote handling, and smoke/E2E coverage. 🎮**UEAtelier**joined the registry (#297) as an Unreal Editor MCP self-extension workbench with a Python CLI proxy. -
**2026-05-19**🛠️ Existing harnesses got a quality/security pass —**Zoom**downloads recordings from direct URLs (#294),**Obsidian**search now uses the Local REST API vendor content types (#289),**LibreOffice**headless conversion is more robust on macOS (#290), and XML/SVG/ODF/MLT/MusicXML/CSL parsing now routes untrusted input through`defusedxml`

(#296). -
**2026-05-18**📈 README presentation refreshed with the Trendshift badge and centered project header polish (#285, #286), keeping the landing section focused on discovery and project momentum. -
**2026-05-17**🌐**CLI-Hub**registry handling was hardened (#281) — registry entries are now copied before`_source`

tagging, preventing cached or mocked registry data from being mutated in place. -
**2026-05-16**🔧**n8n**received the REPL banner crash fix that later merged into main (#280), restoring the no-subcommand interactive startup path with regression coverage.

## Earlier news (Apr 10–18)

-
**2026-04-18**🧩**All SKILL.md files are now being unified under the top-level**— every CLI skill can be installed from one canonical source with`skills/`

directory`npx skills add HKUDS/CLI-Anything --skill <skill-name> -g -y`

. We also added root-skill validation CI, synced contribution / PR docs and REPL skill-path hints to the new layout, and refreshed the**CLI-Hub**install-first frontend around the new`npx skills`

flow. -
**2026-04-17**🌐**CLI-Hub**received another install UX pass — public registry metadata and skill coverage were tightened, visit counting was corrected, and the web hub was further refined. 🧪**Shotcut**render output duration was fixed (#92). 📝**SKILL**contribution paths were corrected for the new docs flow (#224), and the skill generator now safely handles empty intros (#203). -
**2026-04-16**🗺️**QGIS CLI**merged (#207) — a full GIS / map authoring harness landed. 🧬**UniMol Tools CLI**merged (#219) for molecular modeling workflows. 🌐**CLI-Hub**also added more public CLIs, including**py4csr**, refreshed its generated meta-skill, corrected SKILL contribution docs, and fixed`apt-get`

package extraction in skill generation (#204). -
**2026-04-16**📈**Unreal Insights CLI**expanded — added background capture session control (`capture start/status/snapshot/stop`

), engine-root-matched`UnrealInsights.exe`

resolution/build flows, and refreshed docs/tests for the new orchestration workflow. -
**2026-04-15**🌐**CLI-Hub**updated to**v0.2.0**— the PyPI package now supports public CLIs from multiple install sources (`pip`

,`npm`

,`brew`

, bundled/system tools), backed by a new`public_registry.json`

. The Hub frontend was redesigned with separate**CLI-Anything CLIs**and**Public CLIs**decks, and live end-to-end checks now cover real install, update, and uninstall flows across both pip and npm packages. -
**2026-04-14**🧭**Safari CLI**merged (#212) and added to the Hub registry — browser automation via`safari-mcp`

. 🎬**Kdenlive**also received compatibility fixes for Gen 5 project output and invalid project generation. -
**2026-04-13**📓**Obsidian CLI**merged (#211) — knowledge management harness via the Local REST API, with 48 unit tests and 7 E2E tests. ⛓️**Eth2-Quickstart CLI**merged (#195) — Ethereum staking node management harness. 📚**Zotero CLI**updated to v0.4.1 (#201) — now shipped from its standalone repo, and CLI-Hub gained support for remote`skill_md`

URLs. -
**2026-04-11**🔗**n8n CLI**merged (#188) — workflow automation harness for self-hosted automation flows. 🔧**Exa CLI**fix (#205) added the`x-exa-integration`

header for usage tracking. 📦**CLI-Hub**also gained its PyPI auto-publish workflow and package refresh pipeline. -
**2026-04-10**📦**CLI-Hub package manager**launched —`pip install cli-anything-hub`

to browse, search, install, update, and uninstall CLI-Anything harnesses from one command. The web Hub also shipped its first install-focused frontend refresh and "Empower yourself" toolkit card.

## Earlier news (Apr 1–9)

-
**2026-04-09**🧹 Cleanup and docs pass (#200) — fixed Openscreen test subtotals, added Openscreen to the Chinese README and project structure, and clarified`/cli-anything`

command syntax in the docs. -
**2026-04-08**🎬**Openscreen CLI**merged (#183) — screen recording editor harness with 101 tests. ☁️**CloudAnalyzer CLI**merged (#181) — cloud cost analysis harness with 27 commands. 🌊**SeaClip / PM2 / ChromaDB**harnesses merged (#129). -
**2026-04-07**🔄**Dify Workflow CLI**merged (#191) — workflow automation wrapper. 🔧**Inkscape**auto-save fix (#193, fixes #182). 🛡️**DomShell security hardening**(#156) — URL validation and DOM sanitization for the browser CLI. 🥧**Pi Coding Agent extension**merged (#178). -
**2026-04-06**🔍**Exa CLI**merged (#172) — AI-powered web search and answers harness. 🎮**Godot CLI**merged (#140) — game engine harness with a full demo-game E2E pipeline. ☁️**CloudAnalyzer**review fixes and frontend improvements also landed. -
**2026-04-03**🧪**WireMock CLI**merged (#170) — HTTP mock server harness for API testing. 🥧**Pi Coding Agent**extension support also landed, and CLI demo recordings were added to the docs. -
**2026-04-01**⚔️**Slay the Spire II CLI**merged (#148) — deck-building roguelike harness. 🎥**VideoCaptioner CLI**merged (#166) — AI-powered video captioning harness. 🛰️**IntelWatch**was added to the registry for B2B OSINT workflows.

## Earlier news (Mar 23–30)

-
**2026-03-30**🏗️**CLI-Anything v0.2.0**— HARNESS.md progressive disclosure redesign. Detailed guides extracted into`guides/`

for on-demand loading. Phases 1–7 now contiguous. Key Principles and Rules merged into a single authoritative section. -
**2026-03-29**📐 Blender skill docs updated — enforce absolute render paths and correct prerequisites. -
**2026-03-28**🌐**CLIBrowser**added to CLI-Hub registry for agent-accessible browser automation. -
**2026-03-27**📚 Zotero SKILL.md enhanced with agent-facing constraints; REPL config and executable resolution fixes. -
**2026-03-26**📖**Zotero CLI**harness landed for Zotero desktop (library management, collections, citations). Draw.io custom ID bugfix (#132) and registry.json syntax fix. -
**2026-03-25**🎮**RenderDoc CLI**merged for GPU frame capture analysis. FreeCAD updated for v1.1. Blender EEVEE engine name corrected. Zoom token permissions hardened. -
**2026-03-24**🏭**FreeCAD CLI**added with 258 commands across 17 groups.**iTerm2**and**Teltonika RMS**harnesses added to registry. -
**2026-03-23**🤖 Launched**CLI-Hub meta-skill**— agents can now discover and install CLIs autonomously.**Krita CLI**harness merged for digital painting.

## Earlier news (Mar 11–22)

-
**2026-03-22**🎵**MuseScore CLI**merged with transpose, export, and instrument management. -
**2026-03-21**🔧 Infrastructure improvements — refined test harnesses and documentation across multiple CLIs. Enhanced Windows compatibility for several backends. -
**2026-03-20**🌐**Novita AI**CLI added for OpenAI-compatible API access. Registry metadata improvements for better hub discovery. -
**2026-03-19**📦 Package structure refinements across harnesses. Improved SKILL.md generation with better command documentation. -
**2026-03-18**🧪 Test coverage expansion — additional E2E scenarios and edge case validation across multiple CLIs. -
**2026-03-17**🌐 Launched the— a central registry where you can browse, search, and install any CLI with a single[CLI-Hub](https://hkuds.github.io/CLI-Anything/)`pip`

command. -
**2026-03-16**🤖 Added**SKILL.md generation**(Phase 6.5) — every generated CLI now ships with an AI-discoverable skill definition. -
**2026-03-15**🐾 Support for**OpenClaw**from the community! Merged Windows`cygpath`

guard for cross-platform support. -
**2026-03-14**🔒 Fixed a GIMP Script-Fu path injection vulnerability and added**Japanese README**translation. -
**2026-03-13**🔌**Qodercli**plugin officially merged as a community contribution with dedicated setup scripts. -
**2026-03-12**📦**Codex skill**integration landed, bringing CLI-Anything to yet another AI coding platform. -
**2026-03-11**📞**Zoom**video conferencing harness added as the 11th supported application.

CLI is the universal interface for both humans and AI agents:

• **Structured & Composable** - Text commands match LLM format and chain for complex workflows

• **Lightweight & Universal** - Minimal overhead, works across all systems without dependencies

• **Self-Describing** - --help flags provide automatic documentation agents can discover

• **Proven Success** - Claude Code runs thousands of real workflows through CLI daily

• **Agent-First Design** - Structured JSON output eliminates parsing complexity

• **Deterministic & Reliable** - Consistent results enable predictable agent behavior

CLI-Anything has two equally useful starting points:

| Goal | Start Here |
|---|---|
Use the existing CLI ecosystem now |
Install `cli-anything-hub` , browse the registry, and install ready-made CLIs. |
Build a new agent-native CLI |
Install the CLI-Anything plugin/skill for your agent, then run the 7-phase harness generator. |

**Phase 1: Empower yourself — your CLI toolkit**

Install the CLI-Hub package manager first. It lets you browse, search, inspect, install, update, uninstall, and launch CLI-Anything harnesses plus public third-party CLIs from one command.

**PIP**

`pip install cli-anything-hub`

| Command | What it does |
|---|---|
`cli-hub list` |
Browse the registry |
`cli-hub search <query>` |
Search by keyword |
`cli-hub info <name>` |
Inspect one CLI |
`cli-hub install <name>` |
Install from CLI-Hub |
`cli-hub update <name>` |
Update an install |
`cli-hub uninstall <name>` |
Remove an install |
`cli-hub launch <name> [args...]` |
Run an installed CLI |

```
# Browse what is available
cli-hub list
cli-hub search image
# Install and try a CLI immediately
cli-hub install gimp
cli-hub info gimp
cli-hub launch gimp
```

Some CLIs wrap real desktop or backend software. If a selected CLI needs GIMP, Blender, LibreOffice, or another upstream tool, install that upstream application too.


**Phase 1.5: Empower your agents — install in one command**

Give SKILL-compatible agents the CLI-Hub meta-skill so they can discover and install the right CLI for a task.

**Also available on:** [ClawHub](https://clawhub.ai/yuh-yang/cli-anything-hub), [SkillHub](https://www.skillhub.club/web/skills/itsyuhao-cli-anything-hub), [SkillHub.cn](https://skillhub.cn/skills/cli-hub-meta-skill)

**NPX SKILLS**

`npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`

**Works with:** OpenClaw, Nanobot, Claude Code, Codex, Reasonix, Antigravity, and other SKILL-compatible agents.

Then prompt:

```
Find appropriate CLI software in CLI-Hub and complete the task: ...
```


**Phase 3: Build a new CLI when the registry does not have one yet**

Use the CLI-Anything generator when you need a new harness for software, a codebase, or an internal tool that is not already available through CLI-Hub.

**Prerequisites**

**Python 3.10+**- Target software or source repo available locally or online
- A supported AI coding agent:
[Claude Code](https://github.com#-claude-code)|[Cursor](https://github.com#-cursor)|[Pi](https://github.com#-pi-coding-agent)|[OpenClaw](https://github.com#-openclaw)|[OpenCode](https://github.com#-opencode)|[Codex](https://github.com#-codex)|[Hermes](https://github.com#-hermes)|[Reasonix](https://github.com#-reasonix)|[Qodercli](https://github.com#-qodercli)|[GitHub Copilot CLI](https://github.com#-github-copilot-cli)|[More Platforms](https://github.com#-more-platforms-coming-soon)

**Step 1: Add the Marketplace**

CLI-Anything is distributed as a Claude Code plugin marketplace hosted on GitHub.

```
# Add the CLI-Anything marketplace
/plugin marketplace add HKUDS/CLI-Anything
```

**Step 2: Install the Plugin**

```
# Install the cli-anything plugin from the marketplace
/plugin install cli-anything
```

That's it. The plugin is now available in your Claude Code session.


Note for Win Users:Claude Code runs shell commands via`bash`

. On Windows, install Git for Windows (includes`bash`

and`cygpath`

) or use WSL; otherwise commands may fail with`cygpath: command not found`

.

**Step 3: Build a CLI in One Command**

```
# /cli-anything <software-path-or-repo>
# Generate a complete CLI for GIMP (all 7 phases)
/cli-anything ./gimp
```

Command compatibility across Claude Code versions:

- Use
`/cli-anything`

as the primary entrypoint. - On older builds where
`/cli-anything`

isn't recognized**after confirming the plugin is installed and loaded**, try the legacy entry form`/cli-anything:cli-anything`

. - Auxiliary commands keep the
`:subcommand`

form (e.g.`/cli-anything:refine`

).

If you see `Unknown skill: cli-anything`

, focus on plugin install/load first (both entry forms reference the same skill, so swapping forms won't help):

- Reload plugin commands:
`/reload-plugins`

- Verify the plugin is loaded:
`/help cli-anything`

(CLI-Anything help/commands should appear) - Reinstall from marketplace if needed:
`/plugin marketplace add HKUDS/CLI-Anything`

`/plugin install cli-anything`


- After confirming the plugin is available, retry the entry command:
- Preferred:
`/cli-anything ./gimp`

- Older builds only:
`/cli-anything:cli-anything ./gimp`


- Preferred:

This runs the full pipeline:

- 🔍
**Analyze**— Scans source code, maps GUI actions to APIs - 📐
**Design**— Architects command groups, state model, output formats - 🔨
**Implement**— Builds Click CLI with REPL, JSON output, undo/redo - 📋
**Plan Tests**— Creates TEST.md with unit + E2E test plans - 🧪
**Write Tests**— Implements comprehensive test suite - 📝
**Document**— Updates TEST.md with results - 📦
**Publish**— Creates`setup.py`

, installs to PATH

**Step 4 (Optional): Refine and Improve the CLI**

After the initial build, you can iteratively refine the CLI to expand coverage and add missing capabilities:

```
# Broad refinement — agent analyzes gaps across all capabilities
/cli-anything:refine ./gimp
# Focused refinement — target a specific functionality area
/cli-anything:refine ./gimp "I want more CLIs on image batch processing and filters"
```

The refine command performs gap analysis between the software's full capabilities and current CLI coverage, then implements new commands, tests, and documentation for the identified gaps. You can run it multiple times to steadily expand coverage — each run is incremental and non-destructive.

**Alternative: Manual Installation**

If you prefer not to use the marketplace:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Copy plugin to Claude Code plugins directory
cp -r CLI-Anything/cli-anything-plugin ~/.claude/plugins/cli-anything
# Reload plugins
/reload-plugins
```

**Step 1: Install the Extension**

The extension lives at `.pi-extension/cli-anything/`

in this repository. Install it globally so `/cli-anything`

commands are available in **all** Pi projects:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything
# Install globally into Pi's extensions directory
bash .pi-extension/cli-anything/install.sh
```

To uninstall:

`bash .pi-extension/cli-anything/install.sh --uninstall`


How it works:`install.sh`

copies the extension files (including HARNESS.md, commands, guides, scripts, and templates from`cli-anything-plugin/`

) into`~/.pi/agent/extensions/cli-anything/`

, which Pi auto-discovers on startup. Run`/reload`

in Pi or restart Pi to activate.

**Step 2: Build a CLI in One Command**

Once the extension is loaded, the following commands are available:

```
# Generate a complete CLI for GIMP (all 7 phases)
/cli-anything ./gimp
# Build from a GitHub repo
/cli-anything https://github.com/blender/blender
```

**Step 3 (Optional): Refine and Improve the CLI**

```
# Broad refinement — agent analyzes gaps across all capabilities
/cli-anything:refine ./gimp
# Focused refinement — target a specific functionality area
/cli-anything:refine ./gimp "batch processing and filters"
```

**Available Commands**

| Command | Description |
|---|---|
`/cli-anything <path-or-repo>` |
Build a complete CLI harness |
`/cli-anything:refine <path> [focus]` |
Refine an existing CLI harness |
`/cli-anything:test <path-or-repo>` |
Run tests for a CLI harness |
`/cli-anything:validate <path-or-repo>` |
Validate a CLI harness |
`/cli-anything:list [options]` |
List all CLI-Anything tools |

**Step 1: Install the Commands**


Note:Please upgrade to the latest OpenCode. Older versions may use a different commands path.

Copy the CLI-Anything commands **and** `HARNESS.md`

to your OpenCode commands directory:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Global install (available in all projects)
cp CLI-Anything/opencode-commands/*.md ~/.config/opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md ~/.config/opencode/commands/
# Or project-level install
cp CLI-Anything/opencode-commands/*.md .opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md .opencode/commands/
```


Note:Please upgrade to the latest OpenCode. Older versions use`command/`

(singular) instead of`commands/`

. If`commands/`

does not exist, use`command/`

for both global and project-level installs.


Note:`HARNESS.md`

is the methodology spec that all commands reference. It must be in the same directory as the commands.

This adds 5 slash commands: `/cli-anything`

, `/cli-anything-refine`

, `/cli-anything-test`

, `/cli-anything-validate`

, and `/cli-anything-list`

.

**Step 2: Build a CLI in One Command**

```
# Generate a complete CLI for GIMP (all 7 phases)
/cli-anything ./gimp
# Build from a GitHub repo
/cli-anything https://github.com/blender/blender
```

The command runs as a subtask and follows the same 7-phase methodology as Claude Code.

**Step 3 (Optional): Refine and Improve the CLI**

```
# Broad refinement — agent analyzes gaps across all capabilities
/cli-anything-refine ./gimp
# Focused refinement — target a specific functionality area
/cli-anything-refine ./gimp "batch processing and filters"
```

**Step 1: Install Goose**

Install Goose (Desktop or CLI) using the official Goose instructions for your OS.

**Step 2: Configure a CLI Provider**

Configure Goose to use a CLI provider such as Claude Code, and make sure that CLI is installed and authenticated.

**Step 3: Use CLI-Anything in a Goose Session**

Once Goose is configured, start a session and use the same CLI-Anything commands described above for Claude Code, for example:

```
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
```

Note: When Goose runs through a CLI provider, it uses that provider's capabilities and command format.


**Step 1: Register the Plugin**

```
git clone https://github.com/HKUDS/CLI-Anything.git
bash CLI-Anything/qoder-plugin/setup-qodercli.sh
```

This registers the cli-anything plugin in `~/.qoder.json`

. Start a new Qodercli session after registration.

**Step 2: Use CLI-Anything from Qodercli**

```
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
/cli-anything:validate ./gimp
```

**Step 1: Install the Skill**

CLI-Anything provides a native OpenClaw `SKILL.md`

file. Copy it to your OpenClaw skills directory:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Install to the global skills folder
mkdir -p ~/.openclaw/skills/cli-anything
cp CLI-Anything/openclaw-skill/SKILL.md ~/.openclaw/skills/cli-anything/SKILL.md
```

**Step 2: Build a CLI**

Now you can invoke the skill inside OpenClaw:

`@cli-anything build a CLI for ./gimp`


The skill follows the same 7-phase methodology as Claude Code and OpenCode.

Cursor gets **both** tracks:

| Track | Purpose | Install |
|---|---|---|
Generator |
Build new harnesses with `/cli-anything` (and refine/test/validate/list) |
Cursor plugin in `cursor-plugin/` |
Consumer |
Find/install/use published CLIs from CLI-Hub | `npx skills` + `cli-hub` (unchanged) |

**Generator — install the Cursor plugin**

```
git clone https://github.com/HKUDS/CLI-Anything.git
bash CLI-Anything/cursor-plugin/scripts/install.sh
```

Windows PowerShell:

`.\CLI-Anything\cursor-plugin\scripts\install.ps1`

Upgrade with `--force`

/ `-Force`

. Default install path is
`~/.cursor/plugins/local/cli-anything`

(override with `CURSOR_PLUGINS_HOME`

pointing at a
directory named `plugins`

). The installer vendors `cli-anything-plugin/`

methodology
resources and writes `PLUGIN_ROOT.txt`

plus `~/.cursor/cli-anything-generator.root`

so Cursor agents can resolve absolute methodology paths.

Reload the Cursor window (**Developer: Reload Window**), then:

```
/cli-anything ./gimp
/cli-anything-refine ./shotcut "picture-in-picture workflows"
/cli-anything-test ./libreoffice
/cli-anything-validate ./libreoffice
/cli-anything-list
```


**Consumer — Hub / skills (separate from the generator plugin)**

```
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
# or a per-app skill, e.g. cli-anything-blender
pip install cli-anything-hub
```

Verify the plugin installer locally:

`bash CLI-Anything/cursor-plugin/tests/test_install.sh`

See [ cursor-plugin/README.md](https://github.com/HKUDS/CLI-Anything/blob/main/cursor-plugin/README.md) for troubleshooting local plugin loading.

**Step 1: Install the Skill**

Run the bundled installer:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Install the skill
bash CLI-Anything/codex-skill/scripts/install.sh
```

On Windows PowerShell, use:

`.\CLI-Anything\codex-skill\scripts\install.ps1`

This installs the skill to `$CODEX_HOME/skills/cli-anything`

(or `~/.codex/skills/cli-anything`

if `CODEX_HOME`

is unset).
The installer also vendors the canonical `HARNESS.md`

, command specifications,
on-demand guides, reusable helper scripts, skill template, and preview protocol
into the installed skill's `references/`

and `scripts/`

directories.
This keeps the Codex skill self-contained while using `cli-anything-plugin/`

as
the source of truth.

Restart Codex after installation so it is discovered.

**Step 2: Use CLI-Anything from Codex**

Describe the task in natural language, for example:

```
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
Use CLI-Anything to list generated harnesses under the current directory
```


The Codex skill adapts the same methodology used by the Claude Code plugin and OpenCode commands, while keeping the generated Python harness format unchanged.

To verify the self-contained Codex installation locally:

`bash CLI-Anything/codex-skill/tests/test_install.sh`

**Step 1: Install the Skill**

Run the bundled installer:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Install the skill
bash CLI-Anything/hermes-skill/scripts/install.sh
```

On Windows PowerShell, use:

`.\CLI-Anything\hermes-skill\scripts\install.ps1`

This installs the skill to `$HERMES_HOME/skills/cli-anything-hermes`

(or `~/.hermes/skills/cli-anything-hermes`

if `HERMES_HOME`

is unset).

Restart [Hermes Agent](https://github.com/NousResearch/hermes-agent) after installation so it is discovered.

**Step 2: Use CLI-Anything from Hermes**

Describe the task in natural language, for example:

```
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
```


The Hermes skill adapts the same methodology used by the Claude Code plugin and
Codex skill, binding Hermes's `terminal`

, `execute_code`

, `delegate_task`

, and
`read_file`

/ `write_file`

/ `patch`

tools to the 7-phase harness workflow while
keeping the generated Python harness format unchanged.

**Step 1: Install the Skill**

Run the bundled installer:

```
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git
# Install the skill
bash CLI-Anything/reasonix-skill/scripts/install.sh
```

On Windows PowerShell, use:

`.\CLI-Anything\reasonix-skill\scripts\install.ps1`

This installs the skill to Reasonix's global skill directory at `~/.reasonix/skills/cli-anything`

.

Restart Reasonix after installation so it is discovered.

**Step 2: Use CLI-Anything from Reasonix**

Describe the task in natural language, for example:

```
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
```


The Reasonix skill adapts the same methodology used by the Claude Code plugin and
Codex/Hermes skills, binding Reasonix's `bash`

, `write_file`

, `edit_file`

,
`multi_edit`

, `grep`

, `glob`

, and optional `mcp__codegraph__search`

/ `mcp__codegraph__context`

tools to the
7-phase harness workflow while keeping the generated Python harness format unchanged.

**Step 1: Install the Plugin**

```
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything
copilot plugin install ./cli-anything-plugin
```

This installs the CLI-Anything plugin to GitHub Copilot CLI. The plugin should now be available in your GitHub Copilot CLI session.

**Step 2: Use CLI-Anything from GitHub Copilot CLI**

```
/cli-anything ./gimp
/cli-anything:refine ./gimp "batch processing and filters"
/cli-anything:validate ./gimp
```

CLI-Anything is designed to be platform-agnostic. Support for more AI coding agents is planned:

**Cursor**— available via the Cursor plugin in`cursor-plugin/`

(generator) plus Hub/skills (consumer)**Codex**— available via the bundled skill in`codex-skill/`

**Windsurf**— coming soon**Your favorite tool**— contributions welcome! See the`opencode-commands/`

directory for a reference implementation.

Regardless of which platform you used to build it, the generated CLI works the same way:

```
# Install to PATH
cd gimp/agent-harness && pip install -e .
# Use from anywhere
cli-anything-gimp --help
cli-anything-gimp project new --width 1920 --height 1080 -o poster.json
cli-anything-gimp --json layer add -n "Background" --type solid --color "#1a1a2e"
# Enter interactive REPL
cli-anything-gimp
```

Each in-repo harness now has a canonical [ SKILL.md](https://github.com#-skillmd-generation) at

`skills/cli-anything-<software>/SKILL.md`

, which makes the monorepo directly discoverable via `npx skills add HKUDS/CLI-Anything --list`

. Installed harness packages still ship a compatibility copy at `cli_anything/<software>/skills/SKILL.md`

, and the REPL banner prefers the repo-root canonical file when present, falling back to the packaged copy otherwise.CLI-Hub lets agents autonomously discover, install, and use the CLIs they need.

`npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y`

**Also available on:** [ClawHub](https://clawhub.ai/yuh-yang/cli-anything-hub), [SkillHub](https://www.skillhub.club/web/skills/itsyuhao-cli-anything-hub), [SkillHub.cn](https://skillhub.cn/skills/cli-hub-meta-skill)

Then prompt:

```
Find appropriate CLI software in CLI-Hub and complete the task: ...
```


The meta-skill points agents to the live CLI-Hub catalog, where they can choose a CLI, install it, and read its own `SKILL.md`

for task-specific usage.

• 🌐 **Universal Access** - Every software becomes instantly agent-controllable through structured CLI.

• 🔗 **Seamless Integration** - Agents control any application without APIs, GUI, rebuilding or complex wrappers.

• 🚀 **Future-Ready Ecosystem** - Transform human-designed software into agent-native tools with one command.

| Category | How to be Agent-native | Notable Examples |
|---|---|---|
📂 GitHub Repositories |
Transform any open-source project into agent-controllable tools through automatic CLI generation | VSCodium, WordPress, Calibre, Zotero, Joplin, Logseq, Penpot, Super Productivity |
🤖 AI/ML Platforms |
Automate model training, inference pipelines, and hyperparameter tuning through structured commands | Stable Diffusion WebUI, ComfyUI, Ollama, InvokeAI, Text-generation-webui, Open WebUI, Fooocus, Kohya_ss, AnythingLLM, SillyTavern |
📊 Data & Analytics |
Enable programmatic data processing, visualization, and statistical analysis workflows | JupyterLab, Apache Superset, Metabase, Redash, DBeaver, KNIME, Orange, OpenSearch Dashboards, Lightdash |
💻 Development Tools |
Streamline code editing, building, testing, and deployment processes via command interfaces | Jenkins, Gitea, Hoppscotch, Portainer, pgAdmin, SonarQube, ArgoCD, OpenLens, Insomnia, Beekeeper Studio,
|
🎨 Creative & Media |
Control content creation, editing, and rendering workflows programmatically | Blender, GIMP, OBS Studio, Audacity, WaveTone, Krita, Kdenlive, Shotcut, Inkscape, Darktable, LMMS, Ardour |
🎮 Game Development |
Manage game projects, scenes, exports, and scripting through headless engine interfaces | ,
|
🔬 Scientific Computing |
Automate research workflows, simulations, and complex calculations | ImageJ, FreeCAD, QGIS, ParaView, Gephi, LibreCAD, Stellarium, KiCad, JASP, Jamovi |
🏢 Enterprise & Office |
Convert business applications and productivity tools into agent-accessible systems | NextCloud, GitLab, Grafana, Mattermost, LibreOffice, AppFlowy, NocoDB, Odoo (Community), Plane, ERPNext |
📞 Communication & Collaboration |
Automate meeting scheduling, participant management, recording retrieval, and reporting through structured CLI | Zoom, Jitsi Meet, BigBlueButton, Mattermost |
📐 Diagramming & Visualization |
Create and manipulate diagrams, flowcharts, architecture diagrams, and visual documentation programmatically | Draw.io (diagrams.net), Mermaid, PlantUML, Excalidraw, yEd |
🌐 Network & Infrastructure |
Manage network services, DNS, ad-blocking, and infrastructure through structured CLI commands | AdGuardHome |
🧪 Testing & Mocking |
Control HTTP mock servers, manage test stubs, record and replay API traffic for integration testing |
|
🔬 Graphics & GPU Debugging |
Analyze GPU frame captures, inspect pipeline state, export shaders, and diff rendering state | RenderDoc |
⚙️ Fabrication & Machine Control |
Drive real hardware from design file to physical output — safety-gated detect, preflight, jog, and framing commands with machine profiles over the software's real backend | MeerK40t (laser), Ink/Stitch (embroidery) |
🎬 Video & Subtitles |
Transcribe speech, translate subtitles, burn styled captions into video — full captioning pipeline | VideoCaptioner |
🔍 AI-Native Search |
Neural and deep web search with structured content retrieval through embedding-based APIs |
|

**✨ AI Content Generation**[AnyGen](https://www.anygen.io), Gamma, Beautiful.ai, TomeAI agents are great at reasoning but terrible at using real professional software. Current solutions are fragile UI automation, limited APIs, or dumbed-down reimplementations that miss 90% of functionality.

**CLI-Anything's Solution**: Transform any professional software into agent-native tools without losing capabilities.

Current Pain Point |
CLI-Anything's Fix |
|---|---|
| 🤖 "AI can't use real tools" | Direct integration with actual software backends (Blender, LibreOffice, FFmpeg) — full professional capabilities, zero compromises |
| 💸 "UI automation breaks constantly" | No screenshots, no clicking, no RPA fragility. Pure command-line reliability with structured interfaces |
| 📊 "Agents need structured data" | Built-in JSON output for seamless agent consumption + human-readable formats for debugging |
| 🔧 "Custom integrations are expensive" | One Claude plugin auto-generates CLIs for ANY codebase through proven 7-phase pipeline |
| ⚡ "Prototype vs Production gap" | 2,280+ tests with real software validation. Battle-tested across 18 major applications |

|
Professional or everyday — just throw the codebase at |
Tired of juggling fragmented web service APIs? Feed the docs or SDK manuscripts to |
CLI-Anything can flat-out |

|
From codebase analysis to PyPI publishing — the plugin handles architecture design, implementation, test planning, test writing, and documentation completely automatically. |
Direct calls to real applications for actual rendering. LibreOffice generates PDFs, Blender renders 3D scenes, Audacity processes audio via sox. |
|
Persistent project state with undo/redo capabilities, plus unified REPL interface (ReplSkin) that delivers consistent interactive experience across all CLIs. |
Simple pip install -e . puts cli-anything- directly on PATH. Agents discover tools via standard which commands. No setup, no wrappers. |
|
Multi-layered validation: unit tests with synthetic data, end-to-end tests with real files and software, plus CLI subprocess verification of installed commands. |
All CLIs organized under cli_anything.* namespace — conflict-free, pip-installable, with consistent naming: cli-anything-gimp, cli-anything-blender, etc. |

Each generated CLI now has a canonical `SKILL.md`

at `skills/cli-anything-<software>/SKILL.md`

. This makes the current monorepo directly consumable by `npx skills`

, while a packaged compatibility copy at `cli_anything/<software>/skills/SKILL.md`

preserves installed-harness behavior.

**What SKILL.md provides:**

**YAML frontmatter**with name and description for agent skill discovery**Command groups**with all available subcommands documented**Usage examples**for common workflows**Agent-specific guidance**for JSON output, error handling, and programmatic use

SKILL.md files are auto-generated during Phase 6.5 of the pipeline using `skill_generator.py`

, which extracts metadata directly from the CLI's Click decorators, setup.py, and README. The generator now writes the canonical repo-root skill file and refreshes the package-local compatibility copy used by installed harnesses. Inside this repo, the REPL banner points agents to the canonical root skill path; after `pip install`

, it falls back to the packaged copy.

AI agents using generated CLIs to produce complete, useful artifacts — no GUI needed.


Harness:`cli-anything-freecad`

|Preview Stack:`preview`

+`preview live`

+`trajectory.json`

|Artifact:Agent-built Curiosity-style rover

An agent incrementally assembles a Curiosity-inspired rover while publishing real FreeCAD preview bundles, refreshing a live preview session, and recording command-to-preview history for later replay. The resulting demo shows the artifact evolving step by step before the final showcase.

README GIF generated from the full local demo video with a speed-adjusted, high-quality ffmpeg palette workflow.


Harness:`cli-anything-blender`

|Preview Stack:`preview`

+`preview live`

+`trajectory.json`

|Artifact:Agent-built orbital relay drone

An agent uses the Blender harness to grow a hard-surface orbital relay drone under a real preview loop: each stage pushes new render-backed bundles, the live session tracks the current head, and the trajectory ties every command to the matching visual state. The demo finishes with the completed scene ready for a polished turntable.

README GIF generated from the full local demo video with a speed-adjusted, high-quality ffmpeg palette workflow.


Harness:`cli-anything-drawio`

|Time:~4 min |Artifact:`.drawio`

+`.png`


An agent creates a full HTTPS connection lifecycle diagram from scratch — TCP three-way handshake, TLS negotiation, encrypted data exchange, and TCP four-way termination — entirely through CLI commands.

*Contributed by @zhangxilong-43*


Harness:`cli-anything-slay-the-spire-ii`

|Artifact:Automated gameplay session

An agent plays through a Slay the Spire II run using the CLI harness — reading game state, selecting cards, choosing paths, and making strategic decisions in real-time.

*Contributed by @TianyuFan0504*


Harness:`cli-anything-videocaptioner`

|Artifact:Captioned video frames

An agent uses the VideoCaptioner CLI to automatically generate and overlay styled subtitles onto video content, with bilingual text rendering and customizable formatting.

Sub A |
Sub B |

*Contributed by @WEIFENG2333*


Harness:[(registered in]`arcgis-pro`

[) |]`public_registry.json`

Mode:live-Pro MCP bridge |Artifact:Agent-driven map navigation in a running ArcGIS Pro session

An agent drives a **live, open ArcGIS Pro session** through an MCP bridge — reading the project, zooming the map to feature layers, running geoprocessing, and exporting layouts — while each step executes inside Pro as you watch. ArcGIS Pro is Esri's commercial GIS desktop (Windows-only, licensed), so this wraps its official **ArcPy / ArcGIS Pro SDK** rather than being generated from source — the ArcGIS Pro counterpart to the QGIS harness.

README GIF generated from the full local demo video with a high-quality ffmpeg palette workflow.

*Contributed by @Jasper0122*

*More CLI demos coming soon.*

CLI-Anything works on any software with a codebase — no domain restrictions or architectural limitations.

Tested across 18 diverse, complex applications spanning creative, productivity, communication, diagramming, AI image generation, AI content generation, network ad blocking, local LLM inference, native debugging, and graphics profiling domains previously inaccessible to AI agents.

From creative workflows (image editing, 3D modeling, vector graphics) to production tools (audio, office, live streaming, video editing).

Each application received complete, production-ready CLI interfaces — not demos, but comprehensive tool access preserving full capabilities.

| Software | Domain | CLI Command | Backend | Tests |
|---|---|---|---|---|
🎨 GIMP |
Image Editing | `cli-anything-gimp` |
Pillow + GEGL/Script-Fu | ✅ 107 |
🧊 Blender |
3D Modeling & Rendering | `cli-anything-blender` |
bpy (Python scripting) | ✅ 208 |
✏️ Inkscape |
Vector Graphics | `cli-anything-inkscape` |
Direct SVG/XML manipulation | ✅ 202 |
🎵 Audacity |
Audio Production | `cli-anything-audacity` |
Python wave + sox | ✅ 161 |
WaveTone |
Audio Transcription | `cli-anything-wavetone` |
JSON manifest + real WaveTone launch |
|

**🌐 Browser**`cli-anything-browser`

[New](https://github.com/HKUDS/CLI-Anything/blob/main/browser/agent-harness)[Web Yu-pri](https://github.com/HKUDS/CLI-Anything/blob/main/web-yu-pri/agent-harness)`cli-anything-web-yu-pri`

[New](https://github.com/HKUDS/CLI-Anything/blob/main/web-yu-pri/agent-harness)**📄 LibreOffice**`cli-anything-libreoffice`

[OpenRefine](https://github.com/HKUDS/CLI-Anything/blob/main/openrefine/agent-harness)`cli-anything-openrefine`

**⚡**[n8n](https://github.com/HKUDS/CLI-Anything/blob/main/n8n/agent-harness)`cli-anything-n8n`

[55+ cmds](https://github.com/HKUDS/CLI-Anything/blob/main/n8n/agent-harness)**📧**[Mailchimp](https://github.com/HKUDS/CLI-Anything/blob/main/mailchimp/agent-harness)`cli-anything-mailchimp`

[303 cmds](https://github.com/HKUDS/CLI-Anything/blob/main/mailchimp/agent-harness)**📚**[Zotero](https://github.com/HKUDS/CLI-Anything/blob/main/zotero/agent-harness)`cli-anything-zotero`

[New](https://github.com/HKUDS/CLI-Anything/blob/main/zotero/agent-harness)**📖**[Calibre](https://github.com/HKUDS/CLI-Anything/blob/main/calibre/agent-harness)`cli-anything-calibre`

[58](https://github.com/HKUDS/CLI-Anything/blob/main/calibre/agent-harness)**📓**[Joplin](https://github.com/HKUDS/CLI-Anything/blob/main/joplin/agent-harness)`cli-anything-joplin`

**📝**[Mubu](https://github.com/HKUDS/CLI-Anything/blob/main/mubu/agent-harness)`cli-anything-mubu`

**📹 OBS Studio**`cli-anything-obs-studio`

**📱**[NSLogger](https://github.com/HKUDS/CLI-Anything/blob/main/nslogger/agent-harness)`cli-anything-nslogger`

**🎞️ Kdenlive**`cli-anything-kdenlive`

**🎬 Shotcut**`cli-anything-shotcut`

**🎬**[Openscreen](https://github.com/HKUDS/CLI-Anything/blob/main/openscreen/agent-harness)`cli-anything-openscreen`

**📞 Zoom**`cli-anything-zoom`

**🎵 MuseScore**`cli-anything-musescore`

**📐 Draw.io**`cli-anything-drawio`

[EEZ Studio](https://github.com/HKUDS/CLI-Anything/blob/main/eez-studio/agent-harness)`cli-anything-eez-studio`

[New](https://github.com/HKUDS/CLI-Anything/blob/main/eez-studio/agent-harness)**⛓️ ETH2 QuickStart**`cli-anything-eth2-quickstart`

**🧜 Mermaid Live Editor**`cli-anything-mermaid`

**✨ AnyGen**`cli-anything-anygen`

**🧠 NotebookLM**`cli-anything-notebooklm`

**🧩**[Dify Workflow](https://github.com/HKUDS/CLI-Anything/blob/main/dify-workflow/agent-harness)`cli-anything-dify-workflow`

**🖼️ ComfyUI**`cli-anything-comfyui`

**🛡️ AdGuard Home**`cli-anything-adguardhome`

**🦙 Ollama**`cli-anything-ollama`

**🧬**[Uni-Mol Tools](https://github.com/HKUDS/CLI-Anything/blob/main/unimol_tools/agent-harness)`cli-anything-unimol-tools`

**🎬**[VideoCaptioner](https://github.com/HKUDS/CLI-Anything/blob/main/videocaptioner/agent-harness)`cli-anything-videocaptioner`

**🎨 Sketch**`sketch-cli`

**🎮 Godot Engine**`cli-anything-godot`

**📦**[s&box](https://github.com/HKUDS/CLI-Anything/blob/main/sbox/agent-harness)`cli-anything-sbox`

**🐞**[LLDB](https://github.com/HKUDS/CLI-Anything/blob/main/lldb/agent-harness)`cli-anything-lldb`

**🟩**[Nsight Graphics CLI](https://github.com/HKUDS/CLI-Anything/blob/main/nsight-graphics/agent-harness)`cli-anything-nsight-graphics`

**🔍**[Exa](https://github.com/HKUDS/CLI-Anything/blob/main/exa/agent-harness)`cli-anything-exa`

**📈**[Unreal Insights](https://github.com/HKUDS/CLI-Anything/blob/main/unrealinsights/agent-harness)`cli-anything-unrealinsights`

**☁️**[CloudAnalyzer](https://github.com/HKUDS/CLI-Anything/blob/main/cloudanalyzer/agent-harness)`cli-anything-cloudanalyzer`

**🗺️**[QGIS](https://github.com/HKUDS/CLI-Anything/blob/main/QGIS/agent-harness)`cli-anything-qgis`

**🔩**[3MF](https://github.com/HKUDS/CLI-Anything/blob/main/3MF/agent-harness)`cli-anything-3mf`

**🗄️**[Tigris](https://github.com/HKUDS/CLI-Anything/blob/main/tigris/agent-harness)`cli-anything-tigris`

`tigris`

CLI[New](https://github.com/HKUDS/CLI-Anything/blob/main/tigris/agent-harness)**Total****✅ 2,461**

100% pass rateacross all 2,461 tests — 1,732 unit tests + 579 end-to-end tests + 19 Node.js tests.

Each CLI harness undergoes rigorous multi-layered testing to ensure production reliability:

| Layer | What it tests | Example |
|---|---|---|
Unit tests |
Every core function in isolation with synthetic data | `test_core.py` — project creation, layer ops, filter params |
E2E tests (native) |
Project file generation pipeline | Valid ODF ZIP structure, correct MLT XML, SVG well-formedness |
E2E tests (true backend) |
Real software invocation + output verification | LibreOffice → PDF with `%PDF-` magic bytes, Blender → rendered PNG |
CLI subprocess tests |
Installed command via `subprocess.run` |
`cli-anything-gimp --json project new` → valid JSON output |

```
================================ Test Summary ================================
gimp 107 passed ✅ (64 unit + 43 e2e)
blender 208 passed ✅ (150 unit + 58 e2e)
inkscape 202 passed ✅ (148 unit + 54 e2e)
audacity 161 passed ✅ (107 unit + 54 e2e)
wavetone 30 passed ✅ (24 unit + 6 default e2e, 2 backend-gated e2e skipped; 32 passed opt-in)
libreoffice 158 passed ✅ (89 unit + 69 e2e)
mubu 96 passed ✅ (85 unit + 11 e2e)
obs-studio 153 passed ✅ (116 unit + 37 e2e)
nslogger 139 passed ✅ (97 unit + 42 e2e)
kdenlive 155 passed ✅ (111 unit + 44 e2e)
shotcut 154 passed ✅ (110 unit + 44 e2e)
zoom 22 passed ✅ (22 unit + 0 e2e)
drawio 138 passed ✅ (116 unit + 22 e2e)
eth2-quickstart 18 passed ✅ (18 unit + 3 e2e skipped)
mermaid 10 passed ✅ (5 unit + 5 e2e)
anygen 50 passed ✅ (40 unit + 10 e2e)
notebooklm 21 passed ✅ (21 unit + 0 e2e)
comfyui 73 passed ✅ (63 unit + 10 e2e)
adguardhome 36 passed ✅ (24 unit + 12 e2e)
ollama 98 passed ✅ (87 unit + 11 e2e)
sketch 19 passed ✅ (19 jest, Node.js)
renderdoc 59 passed ✅ (45 unit + 14 e2e)
cloudcompare 88 passed ✅ (49 unit + 39 e2e)
openscreen 101 passed ✅ (78 unit + 23 e2e)
lldb 27 passed ✅ (23 unit + 4 e2e)
nsight-graphics 51 passed ✅ (46 unit/CLI + 5 local e2e)
unrealinsights 50 passed ✅ (49 unit + 1 e2e, 9 backend-gated e2e skipped)
cloudanalyzer 14 passed ✅ (7 unit + 7 e2e)
3mf 50 passed ✅ (50 unit)
joplin 134 passed ✅ (107 unit + 27 e2e, 1 skipped on Windows)
──────────────────────────────────────────────────────────────────────────────
TOTAL 2,464 passed ✅ 100% pass rate
```


-
**Authentic Software Integration**— The CLI generates valid project files (ODF, MLT XML, SVG) and delegates to real applications for rendering.**We build structured interfaces TO software, not replacements**. -
**Flexible Interaction Models**— Every CLI operates in dual modes: stateful REPL for interactive agent sessions + subcommand interface for scripting/pipelines.**Run bare command → enter REPL mode**. -
**Consistent User Experience**— All generated CLIs share unified REPL interface (repl_skin.py) with branded banners, styled prompts, command history, progress indicators, and standardized formatting. -
**Agent-Native Design**— Built-in --json flag on every command delivers structured data for machine consumption, while human-readable tables serve interactive use.**Agents discover capabilities via standard --help and which commands**. -
**Zero Compromise Dependencies**— Real software is a hard requirement — no fallbacks, no graceful degradation.**Tests fail (not skip) when backends are missing, ensuring authentic functionality**.

```
cli-anything/
├── 📄 README.md # You are here
├── 📁 assets/ # Images and media
│ ├── icon.png # Project icon
│ └── teaser.png # Teaser figure
│
├── 🔌 cli-anything-plugin/ # The Claude Code plugin
│ ├── HARNESS.md # Methodology SOP (source of truth)
│ ├── README.md # Plugin documentation
│ ├── QUICKSTART.md # 5-minute getting started
│ ├── PUBLISHING.md # Distribution guide
│ ├── repl_skin.py # Unified REPL interface
│ ├── commands/ # Plugin command definitions
│ │ ├── cli-anything.md # Main build command
│ │ ├── refine.md # Expand existing harness coverage
│ │ ├── test.md # Test runner
│ │ └── validate.md # Standards validation
│ └── scripts/
│ └── setup-cli-anything.sh # Setup script
│
├── 🖱️ cursor-plugin/ # Cursor Desktop generator plugin
│ ├── .cursor-plugin/plugin.json # Cursor plugin manifest
│ ├── commands/ # /cli-anything slash commands
│ ├── skills/ # Supporting generator skill
│ ├── rules/ # Phase-gate guidance
│ ├── scripts/ # Bash/PowerShell installers + vendored helpers
│ └── tests/ # Installer resource-sync regression tests
├── 🤖 codex-skill/ # Self-contained Codex skill installer
│ ├── SKILL.md # Codex workflow entry point
│ ├── agents/ # Codex UI metadata
│ ├── scripts/ # Bash and PowerShell installers
│ └── tests/ # Installer resource-sync regression test
├── 🧭 hermes-skill/ # Hermes Agent skill entry point
├── 🧠 reasonix-skill/ # Reasonix skill entry point
├── 🎨 gimp/agent-harness/ # GIMP CLI (107 tests)
├── 🧊 blender/agent-harness/ # Blender CLI (208 tests)
├── ✏️ inkscape/agent-harness/ # Inkscape CLI (202 tests)
├── 🎵 audacity/agent-harness/ # Audacity CLI (161 tests)
├── wavetone/agent-harness/ # WaveTone CLI (32 tests: 30 default + 2 backend-gated e2e)
├── 🌐 browser/agent-harness/ # Browser CLI (DOMShell MCP, new)
├── 🌐 web-yu-pri/agent-harness/ # Japan Post Web Yu-pri CLI (new)
├── 📄 libreoffice/agent-harness/ # LibreOffice CLI (158 tests)
├── 🧹 openrefine/agent-harness/ # OpenRefine CLI (76 tests: 64 unit + 12 real backend e2e)
├── 📧 mailchimp/agent-harness/ # Mailchimp Marketing API CLI (303 commands, 36 unit tests)
├── 📚 zotero/agent-harness/ # Zotero CLI (new, write import support)
├── 📖 calibre/agent-harness/ # Calibre CLI (58 tests: 38 unit + 20 E2E)
├── 📓 joplin/agent-harness/ # Joplin CLI (134 tests: 107 unit + 27 e2e)
├── 📝 mubu/agent-harness/ # Mubu CLI (96 tests)
├── 📹 obs-studio/agent-harness/ # OBS Studio CLI (153 tests)
├── 📱 nslogger/agent-harness/ # NSLogger CLI (139 tests)
├── 🎞️ kdenlive/agent-harness/ # Kdenlive CLI (155 tests)
├── 🎬 shotcut/agent-harness/ # Shotcut CLI (154 tests)
├── 📞 zoom/agent-harness/ # Zoom CLI (22 tests)
├── 🎵 musescore/agent-harness/ # MuseScore CLI (56 tests)
├── 📐 drawio/agent-harness/ # Draw.io CLI (138 tests)
├── 🧪 eez-studio/agent-harness/ # EEZ Studio CLI (project, LVGL, SCPI automation)
├── ⛓️ eth2-quickstart/agent-harness/ # ETH2 QuickStart CLI (18 unit, 3 e2e skipped)
├── 🧜 mermaid/agent-harness/ # Mermaid Live Editor CLI (10 tests)
├── ✨ anygen/agent-harness/ # AnyGen CLI (50 tests)
├── 🖼️ comfyui/agent-harness/ # ComfyUI CLI (73 tests)
├── 🧠 notebooklm/agent-harness/ # NotebookLM CLI (experimental, 21 tests)
├── 🧩 dify-workflow/agent-harness/ # Dify Workflow CLI wrapper (11 tests)
├── 🛡️ adguardhome/agent-harness/ # AdGuard Home CLI (36 tests)
├── 🦙 ollama/agent-harness/ # Ollama CLI (98 tests)
├── 🎮 godot/agent-harness/ # Godot Engine CLI (24 tests)
├── 📦 sbox/agent-harness/ # s&box CLI (244 tests: 157 unit + 17 orchestrator + 50 e2e + 20 exit-code)
├── 🎨 sketch/agent-harness/ # Sketch CLI (19 tests, Node.js)
├── 🔬 renderdoc/agent-harness/ # RenderDoc CLI (59 tests)
├── 🟩 nsight-graphics/agent-harness/ # Nsight Graphics CLI (51 tests)
├── 🐞 lldb/agent-harness/ # LLDB CLI (27 tests)
├── 📈 unrealinsights/agent-harness/ # Unreal Insights CLI (50 tests)
├── 🎬 videocaptioner/agent-harness/ # VideoCaptioner CLI (26 tests)
├── 🎬 openscreen/agent-harness/ # Openscreen CLI — screen recording editor (101 tests)
├── ☁️ cloudcompare/agent-harness/ # CloudCompare CLI (88 tests)
├── 🔍 exa/agent-harness/ # Exa CLI (40 tests)
└── ⛅ cloudanalyzer/agent-harness/ # CloudAnalyzer CLI (14 tests)
└── 🔩 3MF/agent-harness/ # 3MF Mesh Editor CLI (50+ tests)
```


Each `agent-harness/`

contains an installable Python package under `cli_anything.<software>/`

with Click CLI, core modules, utils (including `repl_skin.py`

and backend wrapper), and comprehensive tests.

| Command | Description |
|---|---|
`/cli-anything <software-path-or-repo>` |
Build complete CLI harness — all 7 phases |
`/cli-anything:refine <software-path> [focus]` |
Refine an existing harness — expand coverage with gap analysis |
`/cli-anything:test <software-path-or-repo>` |
Run tests and update TEST.md with results |
`/cli-anything:validate <software-path-or-repo>` |
Validate against HARNESS.md standards |

```
# Build a complete CLI for GIMP from local source
/cli-anything /home/user/gimp
# Build from a GitHub repo
/cli-anything https://github.com/blender/blender
# Refine an existing harness — broad gap analysis
/cli-anything:refine /home/user/gimp
# Refine with a specific focus area
/cli-anything:refine /home/user/shotcut "vid-in-vid and picture-in-picture compositing"
# Run tests and update TEST.md
/cli-anything:test /home/user/inkscape
# Validate against HARNESS.md standards
/cli-anything:validate /home/user/audacity
```

Here's what an agent can do with `cli-anything-libreoffice`

:

```
# Create a new Writer document
$ cli-anything-libreoffice document new -o report.json --type writer
✓ Created Writer document: report.json
# Add content
$ cli-anything-libreoffice --project report.json writer add-heading -t "Q1 Report" --level 1
✓ Added heading: "Q1 Report"
$ cli-anything-libreoffice --project report.json writer add-table --rows 4 --cols 3
✓ Added 4×3 table
# Export to real PDF via LibreOffice headless
$ cli-anything-libreoffice --project report.json export render output.pdf -p pdf --overwrite
✓ Exported: output.pdf (42,831 bytes) via libreoffice-headless
# JSON mode for agent consumption
$ cli-anything-libreoffice --json document info --project report.json
{
"name": "Q1 Report",
"type": "writer",
"pages": 1,
"elements": 2,
"modified": true
}
```

```
$ cli-anything-blender
╔══════════════════════════════════════════╗
║ cli-anything-blender v1.0.0 ║
║ Blender CLI for AI Agents ║
╚══════════════════════════════════════════╝
blender> scene new --name ProductShot
✓ Created scene: ProductShot
blender[ProductShot]> object add-mesh --type cube --location 0 0 1
✓ Added mesh: Cube at (0, 0, 1)
blender[ProductShot]*> render execute --output render.png --engine CYCLES
✓ Rendered: render.png (1920×1080, 2.3 MB) via blender --background
blender[ProductShot]> exit
Goodbye! 👋
```


HARNESS.md is our definitive SOP for making any software agent-accessible via automated CLI generation.

It encodes proven patterns and methodologies refined through automated generation processes.

The playbook distills key insights from successfully building all 18 diverse, production-ready harnesses.

| Lesson | Description |
|---|---|
Use the real software |
The CLI MUST call the actual application for rendering. No Pillow replacements for GIMP, no custom renderers for Blender. Generate valid project files → invoke the real backend. |
The Rendering Gap |
GUI apps apply effects at render time. If your CLI manipulates project files but uses a naive export tool, effects get silently dropped. Solution: native renderer → filter translation → render script. |
Filter Translation |
When mapping effects between formats (MLT → ffmpeg), watch for duplicate filter merging, interleaved stream ordering, parameter space differences, and unmappable effects. |
Timecode Precision |
Non-integer frame rates (29.97fps) cause cumulative rounding. Use `round()` not `int()` , integer arithmetic for display, and ±1 frame tolerance in tests. |
Output Verification |
Never trust that export worked because it exited 0. Verify: magic bytes, ZIP/OOXML structure, pixel analysis, audio RMS levels, duration checks. |

See the full methodology:

`cli-anything-plugin/HARNESS.md`


```
# Install the package manager
pip install cli-anything-hub
# Browse, search, inspect, and install CLIs
cli-hub list
cli-hub search <query>
cli-hub info <name>
cli-hub install <name>
# Manage installed CLIs
cli-hub update <name>
cli-hub uninstall <name>
cli-hub launch <name> [args...]
```

```
# Add marketplace & install (recommended)
/plugin marketplace add HKUDS/CLI-Anything
/plugin install cli-anything
# Build a CLI for any software with a codebase
/cli-anything <software-name>
```

```
# Install any generated CLI
cd <software>/agent-harness
pip install -e .
# Verify
which cli-anything-<software>
# Use
cli-anything-<software> --help
cli-anything-<software> # enters REPL
cli-anything-<software> --json <command> # JSON output for agents
```

```
# Run tests for a specific CLI
cd <software>/agent-harness
python3 -m pytest cli_anything/<software>/tests/ -v
# Force-installed mode (recommended for validation)
CLI_ANYTHING_FORCE_INSTALLED=1 python3 -m pytest cli_anything/<software>/tests/ -v -s
```

We welcome contributions! CLI-Anything is designed to be extensible:

**New software targets**— Use the plugin to generate a CLI for any software with a codebase, then submit your harness via.`cli-anything-plugin/PUBLISHING.md`

**Methodology improvements**— PRs to`HARNESS.md`

that encode new lessons learned**Plugin enhancements**— New commands, phase improvements, better validation**Test coverage**— More E2E scenarios, edge cases, workflow tests

**Requires strong foundation models**— CLI-Anything relies on frontier-class models (e.g., Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4) for reliable harness generation. Weaker or smaller models may produce incomplete or incorrect CLIs that require significant manual correction.**Relies on available source code**— The 7-phase pipeline analyzes and generates from source code. When the target software only provides compiled binaries that require decompilation, harness quality and coverage will degrade substantially.**May require iterative refinement**— A single`/cli-anything`

run may not fully cover all capabilities. Running`/refine`

one or more times is often needed to push the CLI's performance and coverage to production quality.

- Support for more application categories (CAD, DAW, IDE, EDA, scientific tools)
- Benchmark suite for agent task completion rates
- Community-contributed CLI harnesses for internal/custom software
- Integration with additional agent frameworks beyond Claude Code
- Support packaging APIs for closed-source software and web services into CLIs
- Produce SKILL.md alongside the CLI for agent skill discovery and orchestration

| Document | Description |
|---|---|
`cli-anything-plugin/HARNESS.md` |

`cli-anything-plugin/README.md`

`cli-anything-plugin/QUICKSTART.md`

`cli-anything-plugin/PUBLISHING.md`

Each generated harness also includes:

`<SOFTWARE>.md`

— Architecture SOP specific to that application`tests/TEST.md`

— Test plan and results documentation

If CLI-Anything helps make your software Agent-native, give us a star! ⭐

If you find CLI-Anything useful, please cite our technical report:

```
@misc{yang2026clianythingagentnativecomputeruse,
title={CLI-Anything: Towards Agent-Native Computer Use},
author={Yuhao Yang and Tianyu Fan and Chao Huang},
year={2026},
eprint={2606.03854},
archivePrefix={arXiv},
primaryClass={cs.HC},
url={https://arxiv.org/abs/2606.03854},
}
```

Apache License 2.0 — free to use, modify, and distribute.