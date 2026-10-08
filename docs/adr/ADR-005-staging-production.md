# ADR-005: Staging and production isolation

## Context

Direct-to-production development causes outages and data leaks.

## Decision

- `develop` → staging resources
- `main` → production resources
- Separate GCP/Firebase projects (recommended) and secrets

## Consequences

- Double setup cost, lower incident risk
- GitHub environments `staging` and `production` gate deploy credentials
