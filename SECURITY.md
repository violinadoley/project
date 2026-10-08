# Security

## Reporting vulnerabilities

If you discover a security issue, **do not** open a public GitHub issue with exploit details.

Contact the maintainers privately (team email or direct message) with:

- Description and impact
- Steps to reproduce
- Affected environment (local / staging / production)

We will acknowledge and coordinate a fix before disclosure when appropriate.

## Secrets policy

Never commit:

- `.env`, `.env.local`, production credentials
- `service-account.json`, `credentials.json`
- Private keys (`.pem`, `.key`)

CI includes a basic check for tracked secret-like filenames. This is not a substitute for careful review.

## Authentication

- **Local:** `AUTH_REQUIRED=false` is acceptable for development only.
- **Staging / production:** Enable Firebase Auth and set `AUTH_REQUIRED=true` on the API when exposing public URLs.
- **GitHub Actions → GCP:** Use [Workload Identity Federation](docs/setup/github-google-oidc.md), not long-lived service account keys in GitHub.

## Dependencies

- Backend: `pip-audit`, `bandit` in CI
- Frontend: `npm audit` (high severity) — review failures

## Logging

Do not log passwords, tokens, API keys, or unnecessary PII. AI request logs should record metadata (model, prompt version, request ID) rather than full user content when possible.

## Production access

No direct SSH or manual edits on Cloud Run containers. Deploy via GitHub Actions from `main` with environment protection.

See [docs/security/README.md](docs/security/README.md) for checklists.
