# Development workflow

## Environments

| Environment | Where it runs | Data |
|-------------|---------------|------|
| Development | localhost | Dev Firebase / emulators / dev Gemini key |
| Staging | Cloud Run + staging Firebase | Staging project only |
| Production | Cloud Run + prod Firebase | Production project only |

## Daily flow

1. Pick or create GitHub Issue
2. `git checkout develop && git pull`
3. `git checkout -b feature/...`
4. Implement + tests
5. Open PR → `develop` → CI green → review → merge
6. Staging auto-deploys from `develop` (when GCP configured)
7. QA on staging
8. Release PR `develop` → `main` → approval → production deploy

## Emergency

Document any direct push to `main` in CHANGELOG and open a follow-up PR to sync `develop`.
