---
name: changelog
description: Summarize commits since a tag into CHANGELOG.md.
context: fork                       # the verbose git log + diff reading stays in a fork;
                                    # only the finished summary returns to your main session
background: false                   # without this a fork runs in the BACKGROUND and its result
                                    # arrives later — it looks like nothing happened
allowed-tools: [Bash, Read, Write]  # a real list — brackets belong here
argument-hint: "[since-tag]"        # a string — unquoted, YAML reads [x] as a one-item list
---
Summarize the commits since the given tag (default: the latest tag).
Group them under Added / Changed / Fixed, write the result to CHANGELOG.md,
then return a 2-line summary — nothing else.
