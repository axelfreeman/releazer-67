# Supported agents

Releazer 67 is agent-agnostic. `SKILL.md` is a universal format — any agent that loads skills runs the same marketing playbook with its own tools. No SDK, no lock-in.

Install with a **symlink** (not a copy), so one `git pull` updates every install at once.

## Top 5 — copy-paste install

```bash
git clone https://github.com/axelfreeman/releazer-67.git
```

| Agent | Install (symlink) |
|-------|-------------------|
| **Claude Code** | `mkdir -p ~/.claude/skills && ln -s "$PWD/releazer-67" ~/.claude/skills/releazer` |
| **Cursor** | `mkdir -p .cursor/skills && ln -s "$PWD/releazer-67" .cursor/skills/releazer` |
| **OpenAI Codex** | `mkdir -p ~/.codex/skills && ln -s "$PWD/releazer-67" ~/.codex/skills/releazer` |
| **Gemini CLI** | `mkdir -p ~/.gemini/skills && ln -s "$PWD/releazer-67" ~/.gemini/skills/releazer` |
| **Hermes** | `mkdir -p ~/.hermes/skills && ln -s "$PWD/releazer-67" ~/.hermes/skills/releazer` |

## Shared convention

Any tool that reads the shared directory can use it too:

```bash
mkdir -p ~/.agents/skills && ln -s "$PWD/releazer-67" ~/.agents/skills/releazer
```

Releazer is the marketing backend; the agent supplies the tools.
