# Releazer 67

**You code. Releazer markets.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange.svg)]()
[![Type: AI Agent Skill](https://img.shields.io/badge/Type-AI_Agent_Skill-2563eb.svg)]()

Releazer 67 is an AI-agent skill that turns the traces your coding agent already leaves behind — commits, PRs, diffs, changelogs — into launch marketing that reaches real people and gets indexed by Google.

---

## The problem

You shipped something. The code is done. But a release nobody hears about might as well not exist. Most developers and indie hackers stop at "it works" — no PR, no posts, no docs, no Google footprint. Marketing stays a separate, manual job you never get to.

## The idea

Your code already tells the story. Every commit, PR, and diff is a trace of what you built. Releazer 67 reads those traces and turns them into a launch — automatically.

## How it works

1. **Scan** — reads your repo's traces: commits, PRs, diffs.
2. **Extract** — figures out what actually shipped.
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

## Install

Drop `SKILL.md` into your agent's skills directory, then point the agent at a repo after a release.

```bash
# Claude Code
mkdir -p ~/.claude/skills/releazer && cp SKILL.md ~/.claude/skills/releazer/

# Cursor
mkdir -p .cursor/skills/releazer && cp SKILL.md .cursor/skills/releazer/
```

## Get your beta key

Beta key: **`RELEAZER-BETA-FREE`**

The full key flow — a proper API-key server and lead capture — ships with the site at **releazer.online** (coming soon).

## Who it's for

- Developers and indie hackers who build in AI coding agents (Claude Code, Cursor, ...).
- Solo founders who want a marketing layer without hiring one.
- Anyone who ships code but never ships the story.

## Roadmap

- [x] `SKILL.md` + core workflow
- [x] `llms.txt` + `AGENTS.md` — AI-citation ready
- [ ] `releazer.online` — landing + key flow + lead capture
- [ ] MCP wrapper for one-command install
- [ ] Catalog listings (MCP directories, awesome-lists)

## License

MIT
