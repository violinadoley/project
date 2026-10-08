# Production deployment

**AUTOMATED (after manual setup):** `.github/workflows/deploy-production.yml` on push to `main`.

**MANUAL SETUP REQUIRED:** Production GCP project, WIF, protected GitHub `production` environment, secrets.

## Guards

- Workflow runs only on `main` (plus explicit branch guard step)
- GitHub environment should require approval
- Concurrency group `deploy-production` prevents overlapping deploys
- Image tag = commit SHA (immutable traceability)

## Rollback

See [../runbooks/rollback.md](../runbooks/rollback.md).

## Frontend production

Deploy the Next.js app to your production Firebase project separately or extend the workflow. Set `CORS_ORIGINS` and `NEXT_PUBLIC_API_URL` to production URLs.
