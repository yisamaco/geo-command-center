# GEO Command Center (MVP Bootstrapped)

GEO Command Center is an **AI-readable Enterprise Knowledge Infrastructure** platform for:

- AI Brand Intelligence
- GEO Monitoring
- Consumer GEO Testing
- Knowledge Graph based publishing for LLM citation
- MCP-ready enterprise integration

## Current implementation stage

Completed in required order:

1. Supabase schema ✅
2. Knowledge Graph core models/exports ✅
3. GEO Core domain models/scoring ✅
4. Backend API (FastAPI) ✅
5. CLI (Typer) ✅
6. MCP Server (FastMCP stdio) ✅
7. Frontend (Refine React scaffold + API list pages) ✅
8. Browser Runner placeholder ✅
9. Reporting template + CLI report command ✅

## Repository layout

```text
geo-command-center/
├─ apps/
│  ├─ frontend/
│  ├─ backend/
│  ├─ cli/
│  ├─ mcp-server/
│  └─ browser-runner/
├─ packages/
│  ├─ geo-core/
│  ├─ knowledge-core/
│  ├─ shared/
│  └─ ui/
├─ scripts/
├─ supabase/
│  ├─ migrations/
│  └─ seed.sql
├─ reports/
├─ .env.example
├─ docker-compose.yml
├─ Makefile
└─ README.md
```

## MVP test-run checkpoint

You can start **test running from Step 4** (Backend API) because API endpoints exist.

Recommended first full smoke sequence:

1. `make db-up`
2. `make db-init`
3. `make db-seed`
4. Start backend: `make backend-dev`
5. In another shell, run: `make smoke-test`
6. (Optional) Start frontend: `make frontend-dev`

If the above passes, the MVP stack is runnable end-to-end for read/list flows.

## Next engineering focus

- Replace placeholder scoring/content generation with real evaluator modules
- Add frontend resource CRUD pages (knowledge entities/snippets/exports)
- Add integration tests for CLI + API + MCP tools
