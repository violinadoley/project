# Staging deployment

**AUTOMATED (after manual setup):** `.github/workflows/deploy-staging.yml` on push to `develop`.

**MANUAL SETUP REQUIRED:** GCP project, WIF, Artifact Registry, Secret Manager, GitHub `staging` environment. See [../setup/github-google-oidc.md](../setup/github-google-oidc.md).

## Flow

```text
merge PR → develop
  → CI (on PR)
  → Deploy Staging workflow
  → Build Docker image (tag = git SHA)
  → Push to Artifact Registry (staging project)
  → Deploy Cloud Run service: ai-hackathon-api-staging
  → scripts/smoke-api.sh
```

## Frontend staging

Frontend deploy to Firebase App Hosting / Hosting is **not fully automated in this starter**. Options:

1. Firebase CLI in a follow-up workflow (separate job, staging Firebase project)
2. Manual `firebase deploy` from CI artifact for demos

Document your chosen URL in GitHub environment variables when added.

## Configuration

Runtime env vars are set in the workflow. Adjust `AUTH_REQUIRED`, CORS, and Firebase IDs per staging project.

Never point staging at production Firestore.
