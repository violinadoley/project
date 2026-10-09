# PostHog (product analytics — optional)

PostHog complements **Cloud Logging / Sentry** (reliability) and **`ai-evals/`** (model quality). It answers: *Do people complete the workflow? Where do they drop off?*

It is **not** a source of truth for AI correctness or backend errors.

## Setup

1. Create a project at [PostHog](https://posthog.com/) (US or EU cloud).
2. Copy the **Project API key** (starts with `phc_`).
3. GitHub **Settings → Variables** (for deploy) and local `frontend/.env.local`:

| Variable | Required | Notes |
|----------|----------|--------|
| `NEXT_PUBLIC_POSTHOG_KEY` | Yes, to enable | Omit or leave empty to disable analytics entirely |
| `NEXT_PUBLIC_POSTHOG_HOST` | No | Default `https://us.i.posthog.com` (use EU host if applicable) |
| `NEXT_PUBLIC_APP_ENV` | No | `development` / `cloud` — sent on every event |
| `NEXT_PUBLIC_POSTHOG_ENABLED` | No | Set `false` to disable without removing the key |
| `NEXT_PUBLIC_POSTHOG_SESSION_REPLAY` | No | Default **off**. Set `true` only after masking review |

4. Redeploy frontend (`develop` push) or run `npm run dev` locally.

Use **separate PostHog projects** (or environments) for local vs production when possible. Set [billing limits](https://posthog.com/pricing) in PostHog.

## Events (starter)

| Event | When |
|-------|------|
| `workflow_started` | Dashboard loaded |
| `input_submitted` | AI message or file chosen (length/extension buckets only — **no prompt or file content**) |
| `ai_workflow_completed` | AI or upload succeeded (`duration_ms`) |
| `ai_workflow_failed` | Failure (`error_kind` message class, not stack traces) |
| `recommendation_reviewed` | AI response shown or upload succeeded |
| `action_approved` | User clicks **Accept result** (AI) |
| `feedback_submitted` | Thumbs up/down on AI response |

Properties: `workflow_type`, `environment`, plus buckets — see `frontend/lib/posthog/events.ts`.

## Privacy

- **Do not** send prompts, AI outputs, filenames, or document contents in analytics (UI masks replay with `data-ph-mask` where noted).
- Firebase **UID** only for `identify` when signed in — no email in events.
- Session replay stays **disabled** until you explicitly enable it and verify masking.

## Demo / AI Builder Cup

Use PostHog **funnels** (e.g. `workflow_started` → `input_submitted` → `ai_workflow_completed`) and completion rates in your final presentation as usage evidence — alongside Firestore activity and your eval framework for quality.
