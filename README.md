# PROJECT_NAME

## Overview

Production-quality **starter monorepo** for a Google-native AI hackathon project. It includes a Next.js dashboard, FastAPI backend with Gemini, Firebase-ready auth/data/storage hooks, Docker for Cloud Run, tests, and CI.

Replace placeholders (`PROJECT_NAME`, problem statement, domain logic) after your team selects a competition track.

## Problem

TODO: Add competition problem statement

## Solution

TODO: Describe the proposed AI solution

## Key Features

- Landing page and generic AI dashboard (text + file upload)
- Gemini integration via official `google-genai` SDK (model from env)
- Firebase Auth, Firestore, and Storage abstractions (stubs ready to extend)
- Optional auth (`AUTH_REQUIRED=false` for local dev)
- Structured API errors and JSON logging for Cloud Run
- Backend pytest suite and GitHub Actions CI

## Tech Stack

| Layer | Technologies |
|-------|----------------|
| Frontend | Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, Lucide |
| Backend | Python 3.11+, FastAPI, Uvicorn, Pydantic Settings |
| AI | Google Gemini (`google-genai`) |
| Data / Auth | Firebase (Auth, Firestore, Storage) |
| Deploy | Cloud Run (API), Firebase Hosting / App Hosting (UI) |

## Architecture

See [docs/architecture.md](docs/architecture.md) for diagrams and extension points (RAG, ADK, embeddings — **future**).

## MCP (Cursor agent tools)

See [docs/mcp.md](docs/mcp.md) for the team MCP setup (GitHub, Context7, Playwright, Google Cloud, Firebase, Sentry, Postman). Configuration lives in [`.cursor/mcp.json`](.cursor/mcp.json).

## Local Setup

```bash
git clone <your-repo-url>
cd ai-hackathon-starter
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local
# Add GEMINI_API_KEY to backend/.env
```

Or run `./scripts/dev.sh` for instructions.

## Environment Variables

**Backend** (`backend/.env`): `GEMINI_API_KEY`, `GEMINI_MODEL`, `FIREBASE_PROJECT_ID`, `FIREBASE_STORAGE_BUCKET`, `AUTH_REQUIRED`, `MAX_UPLOAD_SIZE_MB`, `CORS_ORIGINS`, etc. See [backend/.env.example](backend/.env.example).

**Frontend** (`frontend/.env.local`): `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_FIREBASE_*`, `NEXT_PUBLIC_AUTH_REQUIRED`. See [frontend/.env.local.example](frontend/.env.local.example).

## Running Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Running Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Health check: [http://localhost:8000/health](http://localhost:8000/health)

## Testing

```bash
cd backend && pytest -q
cd frontend && npm run lint && npm run typecheck
```

## Deployment

See [docs/deployment.md](docs/deployment.md) for Cloud Run, secrets, Firebase, and frontend hosting.

## Google Cloud Setup

1. Create a GCP project and enable Cloud Run, Cloud Build, Secret Manager.
2. Store `GEMINI_API_KEY` in Secret Manager.
3. Deploy the backend from `./backend` (Dockerfile included).

## Firebase Setup

1. Add Firebase to your GCP project.
2. Enable Authentication and (optionally) Firestore and Storage.
3. Configure web app env vars on the frontend and Admin SDK on Cloud Run.

## Gemini Setup

1. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. Set `GEMINI_API_KEY` and optionally `GEMINI_MODEL` (default `gemini-2.5-flash`).

## Project Structure

```
frontend/          Next.js App Router UI
backend/app/       FastAPI application
backend/tests/     Pytest suite
docs/              Architecture, development, deployment
scripts/           dev.sh, deploy.sh stub
.github/workflows/ CI
```

## Future Enhancements

- [ ] Competition-specific prompts and workflows
- [ ] Firestore-backed chat history and activity feed
- [ ] GCS upload in production
- [ ] RAG + Gemini embeddings + vector search
- [ ] Google ADK agentic tools
- [ ] Structured outputs and multimodal pipelines

## Competition Submission Checklist

- [ ] Correct problem statement selected
- [ ] Gemini/Gemma integration
- [ ] Functional prototype
- [ ] Cloud deployment
- [ ] Public demo URL
- [ ] 3-minute demo video
- [ ] Proposal PDF
- [ ] Documentation
- [ ] Category specified
- [ ] Impact clearly explained
- [ ] Scalability explained

## License

TODO: Add license if required by your hackathon.
