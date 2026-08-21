#!/usr/bin/env python3
"""Releazer 67 — scan a repo's release traces into a structured digest.

Reads git history (commits, changed files, doc edits) and prints a
plain-text digest the agent feeds into the marketing playbook.

Usage:
    python3 scripts/scan_traces.py [--repo /path] [--since N]
"""
import argparse
import subprocess


def git(args, repo="."):
    r = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True)
    return r.stdout.strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", default=".")
    p.add_argument("--since", type=int, default=10, help="commits back to scan (default 10)")
    a = p.parse_args()

    log = git(["log", "--oneline", f"-{a.since}"], a.repo)
    stat = git(["diff", "--stat", f"HEAD~{a.since}..HEAD"], a.repo)
    changed = git(["diff", "--name-only", f"HEAD~{a.since}..HEAD"], a.repo)

    print("# Release traces\n")
    print("## Recent commits")
    print(log or "(no commits)")

    print("\n## Changed files (stat)")
    print(stat or "(no changes detected)")

    docs = [f for f in changed.splitlines()
            if f.lower().startswith(("changelog", "readme", "docs/"))]
    if docs:
        print("\n## Docs changed")
        print("\n".join(docs))

    print("\n## Next (for the agent)")
    print("Use the above to write the story: what shipped, who it's for, what it gives them.")


if __name__ == "__main__":
    main()
