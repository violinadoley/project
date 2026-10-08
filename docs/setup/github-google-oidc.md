# GitHub Actions OIDC → Google Cloud (Workload Identity Federation)

**Status: MANUAL SETUP REQUIRED**

This repository deploy workflows authenticate with **short-lived credentials** via GitHub OIDC and Google Workload Identity Federation (WIF). Do **not** store a service account JSON key in GitHub unless you have documented an unavoidable exception.

Repeat the steps below for **staging** and **production** using **separate GCP projects** (recommended) or clearly separated resources in one project.

## Prerequisites

- GCP projects created (staging + production)
- Billing enabled (Cloud Run, Artifact Registry incur cost when used)
- `gcloud` CLI installed and authenticated as a human admin

Replace placeholders:

| Placeholder | Example | Where used |
|-------------|---------|------------|
| `STAGING_PROJECT_ID` | `myapp-staging-123` | Staging deploy |
| `PRODUCTION_PROJECT_ID` | `myapp-prod-456` | Production deploy |
| `REGION` | `asia-south1` | Artifact Registry + Cloud Run |
| `GITHUB_ORG` | `violinadoley` | WIF attribute condition |
| `GITHUB_REPO` | `AI-Builder-Cup-` | WIF attribute condition |

## 1. Enable APIs (each project)

```bash
gcloud config set project STAGING_PROJECT_ID
gcloud services enable \
  iamcredentials.googleapis.com \
  sts.googleapis.com \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  secretmanager.googleapis.com
```

Repeat for `PRODUCTION_PROJECT_ID`.

## 2. Create Artifact Registry repository (each project)

```bash
gcloud artifacts repositories create ai-hackathon \
  --repository-format=docker \
  --location=REGION \
  --description="API container images"
```

Note the repository name for GitHub variable `GCP_ARTIFACT_REPO_STAGING` / `_PRODUCTION` (e.g. `ai-hackathon`).

## 3. Create deploy service account (each project)

```bash
gcloud iam service-accounts create github-deploy \
  --display-name="GitHub Actions deploy"
```

Grant least privilege (adjust if you split frontend deploy):

```bash
SA="github-deploy@STAGING_PROJECT_ID.iam.gserviceaccount.com"
gcloud projects add-iam-policy-binding STAGING_PROJECT_ID \
  --member="serviceAccount:${SA}" \
  --role="roles/run.admin"
gcloud projects add-iam-policy-binding STAGING_PROJECT_ID \
  --member="serviceAccount:${SA}" \
  --role="roles/artifactregistry.writer"
gcloud projects add-iam-policy-binding STAGING_PROJECT_ID \
  --member="serviceAccount:${SA}" \
  --role="roles/iam.serviceAccountUser"
gcloud projects add-iam-policy-binding STAGING_PROJECT_ID \
  --member="serviceAccount:${SA}" \
  --role="roles/secretmanager.secretAccessor"
```

## 4. Create Workload Identity Pool + Provider (each project)

```bash
gcloud iam workload-identity-pools create github-pool \
  --location=global \
  --display-name="GitHub Actions"

gcloud iam workload-identity-pools providers create-oidc github-provider \
  --location=global \
  --workload-identity-pool=github-pool \
  --display-name="GitHub" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"
```

Restrict which repositories can authenticate:

```bash
gcloud iam workload-identity-pools providers update-oidc github-provider \
  --location=global \
  --workload-identity-pool=github-pool \
  --attribute-condition="assertion.repository=='GITHUB_ORG/GITHUB_REPO'"
```

Allow the GitHub identity to impersonate the deploy SA:

```bash
PROJECT_NUMBER=$(gcloud projects describe STAGING_PROJECT_ID --format='value(projectNumber)')
gcloud iam service-accounts add-iam-policy-binding "${SA}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/github-pool/attribute.repository/GITHUB_ORG/GITHUB_REPO"
```

## 5. Values for GitHub (repository Variables)

**Settings → Secrets and variables → Actions → Variables**

| Variable | Staging | Production |
|----------|---------|------------|
| `GCP_PROJECT_ID_STAGING` / `_PRODUCTION` | project id | project id |
| `GCP_REGION` | e.g. `asia-south1` | same |
| `GCP_ARTIFACT_REPO_STAGING` / `_PRODUCTION` | repo name | repo name |
| `GCP_WIF_PROVIDER_STAGING` / `_PRODUCTION` | full provider resource name | full provider resource name |
| `GCP_WIF_SERVICE_ACCOUNT_STAGING` / `_PRODUCTION` | `github-deploy@....iam.gserviceaccount.com` | same pattern |

Provider resource name format:

```text
projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github-pool/providers/github-provider
```

Obtain with:

```bash
gcloud iam workload-identity-pools providers describe github-provider \
  --location=global \
  --workload-identity-pool=github-pool \
  --format='value(name)'
```

## 6. GitHub Environments (MANUAL)

**Settings → Environments**

### `staging`

- Deployment branches: `develop` only
- Optional: required reviewers for first-time setup

### `production`

- Deployment branches: `main` only
- **Required reviewers** (recommended)
- Prevent concurrent production deploys (workflow uses `concurrency` group)

Secrets in environments should be **staging-specific** or **production-specific** — never share production Gemini keys with staging.

## 7. Secret Manager (each project)

```bash
echo -n "YOUR_GEMINI_API_KEY" | gcloud secrets create GEMINI_API_KEY --data-file=-
```

Cloud Run service account (runtime) also needs `secretAccessor` on this secret.

## 8. Verify

1. Push to `develop` after variables are set → **Deploy Staging** workflow runs.
2. Check Cloud Run service URL and workflow **Smoke test API** step.
3. Promote via PR `develop` → `main` → approve **Deploy Production**.

## Cost note

WIF and IAM are free. Cloud Run, Artifact Registry storage, and Gemini API usage incur charges when services run.
