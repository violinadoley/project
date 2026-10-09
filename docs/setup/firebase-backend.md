# Firebase backend (Firestore, Storage, Auth verification)

Use the **same GCP project** as Cloud Run (`GCP_PROJECT_ID`). The API uses the **Firebase Admin SDK** with Application Default Credentials on Cloud Run (no JSON key in GitHub).

## 1. Firebase console (one-time)

1. [Firebase Console](https://console.firebase.google.com/) → your project.
2. **Build → Firestore Database → Create database** → start in **production mode** (API uses Admin SDK; clients use your FastAPI routes, not direct Firestore reads). Deploy **`frontend/firestore.rules`** and **`frontend/storage.rules`** (deny all client access) via **Deploy Frontend** or `firebase deploy --only firestore:rules,storage` from `frontend/`.
3. **Build → Storage → Get started** — note the bucket name (often `YOUR_PROJECT_ID.firebasestorage.app`).
4. **Build → Authentication → Get started → Sign-in method → Google → Enable**.
5. **Project settings → Your apps → Add app → Web** — register a web app (required for client login). Copy **apiKey** and **appId** for GitHub variables below.

## 2. GCP APIs and Cloud Run service account

Replace placeholders with your values (`asia-south1`, project id, region).

```bash
export PROJECT_ID=YOUR_GCP_PROJECT_ID
export REGION=asia-south1

gcloud config set project "$PROJECT_ID"
gcloud services enable firestore.googleapis.com storage.googleapis.com identitytoolkit.googleapis.com

# Default runtime identity for Cloud Run (unless you set a custom SA on the service)
export PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
export RUN_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"

gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:${RUN_SA}" \
  --role="roles/datastore.user"

gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:${RUN_SA}" \
  --role="roles/storage.objectAdmin"
```

If Firestore is not created yet:

```bash
gcloud firestore databases create --location="$REGION" --type=firestore-native
```

## 3. GitHub Actions variables

**Settings → Secrets and variables → Actions → Variables**

| Variable | Required | Notes |
|----------|----------|--------|
| `NEXT_PUBLIC_FIREBASE_API_KEY` | **Yes** (for login) | Web app config |
| `NEXT_PUBLIC_FIREBASE_APP_ID` | **Yes** (for login) | Web app config |
| `NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID` | **Yes** (for login) | Web app config |
| `FIREBASE_STORAGE_BUCKET` | No | Defaults to `{GCP_PROJECT_ID}.firebasestorage.app` in deploy |
| `AUTH_REQUIRED` | No | `false` (default) — API open; tokens optional for activity attribution |
| `NEXT_PUBLIC_AUTH_REQUIRED` | No | `true` to block dashboard until sign-in (match `AUTH_REQUIRED` when locking down) |

Deploy workflows set `FIREBASE_PROJECT_ID`, `FIREBASE_STORAGE_BUCKET`, and derived `NEXT_PUBLIC_FIREBASE_*` fields from `GCP_PROJECT_ID` where possible.

Helper (after `firebase login` and web app exists):

```bash
./scripts/sync-firebase-github-vars.sh YOUR_GCP_PROJECT_ID
```

## 4. Verify

1. Push to `develop` → **Deploy API** + **Deploy Frontend**.
2. Open `https://YOUR_PROJECT_ID.web.app` → **Sign in with Google**.
3. Dashboard → sign in → AI message and file upload → **Recent activity** lists **your** entries only (anonymous callers get an empty feed).
4. Upload response includes `storage_key` when Storage IAM and bucket are correct.

## Optional: require login

Set `AUTH_REQUIRED=true` and `NEXT_PUBLIC_AUTH_REQUIRED=true`, redeploy both workflows. Unauthenticated API calls return 401.
