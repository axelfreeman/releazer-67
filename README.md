# Releazer 67

**You code. Releazer markets.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange.svg)]()
[![Type: AI Agent Skill](https://img.shields.io/badge/Type-AI_Agent_Skill-2563eb.svg)]()
[![Site](https://img.shields.io/badge/Site-releazer.online-2563eb.svg)](https://releazer.online)

Releazer 67 is an AI-agent skill that turns the traces your coding agent already leaves behind — commits, PRs, diffs, changelogs — into launch marketing that reaches real people and gets indexed by Google.

---

## The problem

You shipped something. The code is done. But a release nobody hears about might as well not exist. Most developers and indie hackers stop at "it works" — no PR, no posts, no docs, no Google footprint. Marketing stays a separate, manual job you never get to.

## The idea

Your code already contains the marketing — inside the algorithms, the features, the logic. Most developers ignore it because digging it out is hard. Every commit, PR, and diff is a trace of what you built. Releazer 67 reads those traces, understands how the product *actually* works, and turns it into a launch — automatically.

## How it works

1. **Scan** — reads your repo's traces: commits, PRs, diffs.
2. **Understand** — works out how the product *actually* works, not what the release claims.
3. **Rewrite** — technical diffs become "what this means for you."
4. **Triage** — small changes accumulate quietly; meaningful ones get a full launch.
5. **Generate & distribute** — in every format the release needs.

## What it generates

| Channel | What Releazer does |
|---------|--------------------|
| Media / PR | Finds relevant outlets, drafts email and submission-form pitches |
| Social | Auto-posts, triages importance, schedules the meaningful ones |
| Paid | Google Ads / retargeting campaign, when budget exists |
| Video / training | Onboarding videos when a feature needs them |
| Docs / knowledge base | Updates docs and the KB straight from the release |

## Install — runs in any agent

`SKILL.md` is a universal format. Install it with a **symlink** (not a copy), so one `git pull` updates every install at once. Works in Claude Code, Cursor, OpenAI Codex, Gemini CLI, Hermes — any agent that loads skills. No SDK, no lock-in.

```bash
git clone https://github.com/axelfreeman/releazer-67.git

# Shared convention — any tool that reads ~/.agents/skills/
mkdir -p ~/.agents/skills
ln -s "$PWD/releazer-67" ~/.agents/skills/releazer

# Claude Code (global)
mkdir -p ~/.claude/skills
ln -s "$PWD/releazer-67" ~/.claude/skills/releazer

# Cursor (project-scoped)
mkdir -p .cursor/skills
ln -s "$PWD/releazer-67" .cursor/skills/releazer
```

Releazer is the marketing backend; the agent supplies the tools.

## Get your beta key

Get it now at **[releazer.online/get-key](https://releazer.online/get-key)** — free, no credit card.

Beta key: **`RELEAZER-BETA-FREE`**

## Who it's for

- Developers and indie hackers who build in AI coding agents (Claude Code, Cursor, ...).
- Solo founders who want a marketing layer without hiring one.
- Anyone who ships code but never ships the story.

## Docs

- [Supported agents](docs/agents.md) — top 5 with copy-paste install commands
- [How it works](docs/how-it-works.md) — the pipeline in detail
- [Example](docs/examples.md) — a release turned into marketing
- [FAQ](docs/faq.md) — keys, security, pricing, and who it's NOT for
- [Changelog](CHANGELOG.md)

## Roadmap

- [x] `SKILL.md` + core workflow
- [x] `llms.txt` + `AGENTS.md` — AI-citation ready
- [x] Docs: agents, how-it-works, examples, FAQ
- [x] `releazer.online` — landing + key flow + lead capture
- [ ] MCP wrapper for one-command install
- [ ] Catalog listings (MCP directories, awesome-lists)

## License

MIT
