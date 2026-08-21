---
name: releazer
description: Turn shipped code into launch marketing — scan git history, PRs and diffs, then generate media pitches, social posts, ad campaigns, release notes and docs. Use when a developer just shipped a feature or release and wants it announced, needs launch PR, a changelog turned into a launch post, journalists to notice the product, or Google to index it — "launch marketing", "product launch", "announce my release", "PR for my repo".
version: 0.1.0
author: Axel Freeman (axelfreeman)
license: MIT
metadata:
  hermes:
    tags: [marketing, launch, public-relations, content, devtools, growth]
    related_skills: []
---

# Releazer Skill

Releazer turns the traces your coding agent already leaves behind — commits, PRs, diffs, changelogs, README edits — into launch marketing that real people can find and Google can index. It does not write product code; it markets what the code shipped.

## When to Use
- You just shipped a feature, fix, or release and want it to spread.
- You have a repo with real activity but zero marketing.
- You want journalists to notice the product and Google to index it.

Don't use for: writing product code, or internal-only changes with no external value.

## Prerequisites
- A git repo with commit history (the "traces").
- API keys — provide only the channels you actually want to use:
  - `GITHUB_TOKEN` — read commits/PRs, publish releases.
  - `DEVTO_API_KEY` — publish articles.
  - Google Ads MCP — paid campaigns (optional).
  - Any other channel the launch needs (social, media outlets, etc.).

## How to Run
Install once with a symlink so `git pull` updates it: `ln -s "$PWD" ~/.agents/skills/releazer` — or drop `SKILL.md` into your agent's skills directory.

After a release, point Releazer at the repo. It scans the traces, extracts what shipped, and produces a marketing package in exactly the formats the release needs.

## Procedure
1. **Scan traces** — run `python3 scripts/scan_traces.py` (in this repo), or `git log --oneline -20` + `git diff` manually. Completion: a plain-language list of what actually changed.
2. **Understand the product** — read the logic, not the release claims: work out how the product *actually* works. Then write the story: what shipped, who it's for, what it gives them.
3. **Rewrite to human language** — turn technical diffs into "what this means for you", stripping jargon.
4. **Triage importance** — full launch, or just a log entry? Small/dull changes accumulate quietly; meaningful ones get the full package.
5. **Generate the package** — in every format the release needs:
   - Media/PR: find relevant outlets, draft email + submission-form pitches.
   - Social: draft and schedule posts.
   - Paid: Google Ads / retargeting campaign, if budget exists.
   - Video/training: if the feature needs onboarding.
   - Docs + knowledge-base entry.
6. **Distribute** — send pitches, publish posts, launch campaigns, update docs.
7. **Verify** — confirm each channel actually went out and log the result.

## Pitfalls
- Market only what the traces actually show — never invent features.
- API keys are secrets; never commit them.
- A release with no external value will not get traction regardless of format — flag it instead of forcing a launch.

## Verification
- The generated story matches `git log` and the release diffs.
- Every publish action returned a success handle (URL, ID, or confirmation).
