# GitHub labels and project board

## Labels (AUTOMATED)

These labels exist on **[violinadoley/project](https://github.com/violinadoley/project/labels)**:

| Label | Use |
|-------|-----|
| `frontend` | Next.js UI, Playwright |
| `backend` | FastAPI, Python, Docker |
| `ai` | Gemini, prompts, `ai-evals` |
| `infra` | CI/CD, GCP, Firebase deploy |
| `security` | Auth, secrets, IAM |
| `database` | Firestore, schema |
| `testing` | Tests and evals |
| `bug` | Regressions (default GitHub) |
| `documentation` | Docs-only work |
| `P0` / `P1` / `P2` | Priority |

Also use default GitHub labels (`enhancement`, `good first issue`, etc.) as needed.

---

## Project board (MANUAL — ~2 minutes)

GitHub CLI needs `read:project` / `project` scope to automate. Create in the UI:

1. Open the repo → **Projects** tab → **New project**
2. Template: **Board** (or **Team backlog**)
3. Name: **AI Builder Cup — Sprint**
4. Link repository: **project**

### Recommended columns

| Column | Meaning |
|--------|---------|
| Backlog | Not started |
| Ready | Spec clear, can pick up |
| In Progress | Active branch |
| Code Review | PR open |
| Staging | Merged to `develop`, QA on staging |
| Done | Merged/released |

### Workflow

1. Create an **Issue** for each task; add labels (`backend`, `P1`, …).
2. Add issue to project; move card across columns.
3. Link PR to issue (`Fixes #12`) so cards auto-update when supported.

### Optional CLI auth (for future automation)

```bash
gh auth refresh -h github.com -s read:project,project
gh project create --owner violinadoley --title "AI Builder Cup — Sprint" --format board
```

---

## Branch protection

Configured — see [github-branch-protection.md](./github-branch-protection.md).

## Project board (MANUAL — needs `project` scope on `gh`)

`gh` could not create the board without extra OAuth scopes. Either:

1. **UI (fast):** Repo → **Projects** → **New project** → Board → link **project** repo, columns: Backlog → Ready → In Progress → Code Review → Staging → Done  
2. **CLI:** Complete device login, then:
   ```bash
   gh auth refresh -h github.com -s read:project,project
   gh project create --owner violinadoley --title "Project — Sprint" --format board
   ```
