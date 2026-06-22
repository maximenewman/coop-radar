# coop-radar

# Why?

The job market is tougher than ever right now, and applying late makes you one of many names.

The issue isn't that you don't have the qualifications, it might be that you didn't apply on time.

The result, your resume is ignored, and you are sent the generic email 

"unfortunately, we've moved on with another candidate, however, we appreciate your interest!"

**Coop-radar** acts as a bridge to solve this problem. No need to login to the usual job boards that have outdated jobs

or your school job board that does nothing to bridge the gap between you and the recruiters.

Instead use **Coop-radar**, and find fresh jobs immediately, and apply through employer websites in a matter of seconds.

With this, you are guaranteed to land your next coop

## Architecture

```
Source: Pitt CSC / Simplify new-grad + internship listing repo (public, structured)
        │  scheduled daily ingestion (Python)
        ▼
   AWS S3  raw/YYYY-MM-DD/listings.json   (immutable raw layer = data lake)
        │  transform: parse, normalize, dedup, tag role + location + status
        ▼
   Supabase Postgres  `jobs` table        (modeled, indexed warehouse)
        │  served via FastAPI
        ▼
   React frontend                         (filters, "new today" badge, apply link)
```

## Tech stack (FIXED — do not substitute)
- Ingestion + transform: **Python 3.11**, `boto3`, `requests`, `psycopg2` (or SQLAlchemy)
- Raw storage: **real AWS S3** (bucket via env vars / IAM user, S3-only perms)
- Warehouse: **Supabase Postgres** (connection string via env)
- API: **FastAPI**
- Frontend: **React** (Vite), plain fetch, minimal styling — clean and skimmable
- Deploy target: **Fly.io** (API + static frontend; ingestion runs as a scheduled job)
- Scheduler: a Python entrypoint runnable by cron / Fly scheduled machine