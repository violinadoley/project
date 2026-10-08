# Firebase Hosting (free tier) — public frontend

**Cost:** Firebase **Spark (free)** plan includes Hosting for hackathon traffic. You still pay only if Gemini/Cloud Run usage exceeds free tiers elsewhere.

## Prerequisites

- Same GCP project as Cloud Run (`GCP_PROJECT_ID`)
- GitHub variables already used for API deploy (see [github-google-oidc.md](./github-google-oidc.md))
- **`PUBLIC_API_URL`** — Cloud Run base URL **without** trailing slash (e.g. `https://ai-hackathon-api-….run.app`)

## 1. Add Firebase to the GCP project

1. Open [Firebase Console](https://console.firebase.google.com/) → **Add project** → select your **existing** GCP project (`GCP_PROJECT_ID`).
2. Stay on the **Spark (free)** plan when prompted.
3. **Build → Hosting → Get started** (creates the default site `{projectId}.web.app`).  
   **Required** — deploy fails until this one-time step is done.
4. If deploy logs mention a missing site, confirm the site id matches your GCP project id (default).

## 2. Enable API + IAM for GitHub deploy

```bash
export PROJECT_ID=YOUR_GCP_PROJECT_ID
export SA="github-deploy@${PROJECT_ID}.iam.gserviceaccount.com"

gcloud config set project "$PROJECT_ID"
gcloud services enable firebasehosting.googleapis.com firebase.googleapis.com

gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:${SA}" \
  --role="roles/firebasehosting.admin"
```

## 3. GitHub repository variables

**Settings → Secrets and variables → Actions → Variables**

| Variable | Required | Example |
|----------|----------|---------|
| `PUBLIC_API_URL` | **Yes** | `https://ai-hackathon-api-….run.app` |
| `NEXT_PUBLIC_FIREBASE_*` | No | From Firebase **Project settings → Your apps → Web** (only if you want Google login in the UI) |
| `NEXT_PUBLIC_AUTH_REQUIRED` | No | `false` (default) |

Workflow: [`.github/workflows/deploy-frontend.yml`](../../.github/workflows/deploy-frontend.yml) on push to `develop`.

## 4. Verify

1. Merge to `develop` → **Deploy Frontend** and **Deploy API** run.
2. Open `https://YOUR_PROJECT_ID.web.app` → **Dashboard** → send a test message (hits Cloud Run via `NEXT_PUBLIC_API_URL`).
3. If the browser blocks requests, confirm **Deploy API** set `CORS_ORIGINS` to include `.web.app` and `.firebaseapp.com`.

## Local static preview

```bash
cd frontend
cp .env.local.example .env.local   # set NEXT_PUBLIC_API_URL to Cloud Run or localhost:8000
npm ci && npm run build && npm run preview
```
