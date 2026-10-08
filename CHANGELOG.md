# Changelog

All notable changes to this project are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows [Semantic Versioning](https://semver.org/) where applicable.

## [Unreleased]

### Added

- Git branching model (`main` / `develop`) and contributing guide
- Expanded CI: Ruff, mypy, security scans, AI eval framework tests, Playwright E2E
- Staging and production deploy workflows (OIDC/WIF — **manual GCP setup required**)
- Versioned AI layout under `backend/app/ai/`
- `ai-evals/` regression framework (placeholders)
- Health `/ready`, environment and version fields on `/health`
- Documentation: ADRs, runbooks, observability, cost control, OIDC setup guide

## [0.1.0] - 2026-03-28

### Added

- Initial hackathon starter monorepo (Next.js + FastAPI + Gemini + Firebase hooks)
- Basic CI and deployment documentation

[Unreleased]: https://github.com/violinadoley/project/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/violinadoley/project/releases/tag/v0.1.0
