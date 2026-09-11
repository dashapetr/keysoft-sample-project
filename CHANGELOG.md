# Changelog

## [Unreleased] - since v.0.0.1

### Added
- CI workflow that generates a dependency report on pull requests and posts it as a PR comment (`.github/workflows/deps.yml`).

### Changed
- `deps` skill now posts its dependency report to the PR via the GitHub MCP server, in addition to writing `deps-report.md`.

### Fixed
- Moved the dependency-report workflow file into `.github/workflows/` so GitHub Actions actually picks it up.
- Restored missing trailing newline in `CLAUDE.md`.
