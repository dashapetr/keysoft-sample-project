---
name: deps
description: Produce a dependency report for the repo.
context: fork                       # verbose work stays out of the main thread
allowed-tools: [Read, Grep, Bash, Write, mcp__github]   # a real list — brackets belong here
argument-hint: "[path]"                    # a string — quote it, or YAML reads it as a list
---
List dependencies, flag outdated ones, write deps-report.md.