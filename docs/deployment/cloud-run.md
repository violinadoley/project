# Cloud Run deployment (hackathon)

**AUTOMATED (after manual setup):** `.github/workflows/deploy.yml` on push to `develop`.

**MANUAL SETUP REQUIRED:** One GCP project, WIF, Artifact Registry, Secret Manager, GitHub `gcp` environment. See [../setup/github-google-oidc.md](../setup/github-google-oidc.md).

## Flow

```text
merge PR → develop
  → CI (on PR)
  → Deploy API workflow
  → Build Docker image (tag = git SHA)
  → Push to Artifact Registry
  → Deploy Cloud Run service: ai-hackathon-api
  → scripts/smoke-api.sh
```

## Frontend

Frontend deploy to Firebase Hosting is **not automated in this starter**. Options:

1. Firebase CLI in a follow-up workflow
2. Manual `firebase deploy` for demos

Set `NEXT_PUBLIC_API_URL` to your Cloud Run URL when you host the UI.

## Configuration

Runtime env vars are set in the workflow (`ENVIRONMENT=cloud`, `AUTH_REQUIRED=false` by default). Adjust `AUTH_REQUIRED`, CORS, and Firebase IDs for your demo.

Use a dedicated GCP / Firebase project for this app — do not point local dev at the same Firestore you use for demos unless intentional.

## Finding the URL (team-friendly)

Each deploy updates:

- GitHub **About → Website** → API root (browser shows one link: **Backend API (Swagger UI)**)
- Repository variable **`BACKEND_API_URL`** → full `/docs` URL for copy/paste

## Legacy service name

If you previously deployed `ai-hackathon-api-staging`, delete that Cloud Run service in the console after the first successful **Deploy API** run (the URL will change to `ai-hackathon-api`).
