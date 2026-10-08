# Changelog

All notable changes to this project are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows [Semantic Versioning](https://semver.org/) where applicable.

## [Unreleased]

_Competition-specific features go here._

## [0.2.0] - 2026-10-08

### Added

- Firebase Hosting deploy workflow (`deploy-frontend.yml`) and setup guides
- Firestore activity logging, `GET /api/v1/activity`, dashboard Recent activity
- Cloud Run Firebase Admin env (`FIREBASE_PROJECT_ID`, `FIREBASE_STORAGE_BUCKET`); GCS uploads on `cloud` runtime
- Optional Google sign-in (client vars + Auth provider); Bearer tokens when signed in
- `scripts/sync-firebase-github-vars.sh`, `docs/setup/firebase-backend.md`
- MIT [LICENSE](LICENSE)
- **Starter template complete** — platform ready for competition-specific work

### Changed

- Single Cloud Run deploy workflow (`deploy.yml`, GitHub env `gcp`); removed staging/production split and `*_STAGING` variable names
- README and docs aligned with Firebase Hosting + full backend integration

### Fixed

- Cloud Run deploy env vars (CORS commas, `AUTH_REQUIRED` string in env-vars-file)

## [0.1.0] - 2026-03-28

### Added

- Initial hackathon starter monorepo (Next.js + FastAPI + Gemini + Firebase hooks)
- Git branching model (`main` / `develop`) and contributing guide
- Expanded CI: Ruff, mypy, security scans, AI eval framework tests, Playwright E2E
- Cloud Run deploy workflow (OIDC/WIF — **manual GCP setup required**)
- Versioned AI layout under `backend/app/ai/`
- `ai-evals/` regression framework (placeholders)
- Health `/ready`, environment and version fields on `/health`
- Documentation: ADRs, runbooks, observability, cost control, OIDC setup guide

[Unreleased]: https://github.com/violinadoley/project/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/violinadoley/project/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/violinadoley/project/releases/tag/v0.1.0
