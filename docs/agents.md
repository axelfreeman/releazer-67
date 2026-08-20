# Supported agents

Releazer 67 is agent-agnostic. `SKILL.md` is a universal format — any agent that loads skills runs the same marketing playbook with its own tools. No SDK, no lock-in.

## Top 5 — copy-paste install

| Agent | Install |
|-------|---------|
| **Claude Code** | `mkdir -p ~/.claude/skills/releazer && cp SKILL.md ~/.claude/skills/releazer/` |
| **Cursor** | `mkdir -p .cursor/skills/releazer && cp SKILL.md .cursor/skills/releazer/` |
| **OpenAI Codex** | `mkdir -p ~/.codex/skills/releazer && cp SKILL.md ~/.codex/skills/releazer/` |
| **Gemini CLI** | `mkdir -p ~/.gemini/skills/releazer && cp SKILL.md ~/.gemini/skills/releazer/` |
| **Hermes** | `mkdir -p ~/.hermes/skills/releazer && cp SKILL.md ~/.hermes/skills/releazer/` |

## Any other agent

Same pattern: drop `SKILL.md` into the agent's skills directory, point it at a repo after a release, and go.

Releazer is the marketing backend; the agent supplies the tools.
