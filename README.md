# GEO Command Center (MVP Bootstrapped)

GEO Command Center is an **AI-readable Enterprise Knowledge Infrastructure** platform for:

- AI Brand Intelligence
- GEO Monitoring
- Consumer GEO Testing
- Knowledge Graph based publishing for LLM citation
- MCP-ready enterprise integration

## Current implementation stage

This commit starts implementation in the required order:

1. Supabase schema
2. Knowledge Graph core models and exports
3. GEO Core domain models and scoring primitives

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
├─ supabase/
│  ├─ migrations/
│  └─ seed.sql
├─ reports/
├─ .env.example
├─ docker-compose.yml
├─ Makefile
└─ README.md
```

## Next steps

- FastAPI backend resources for GEO runs / scores / knowledge entities
- Typer CLI commands (`geo init`, `geo seed`, `geo run`, `geo score`, `geo knowledge export`)
- FastMCP stdio server with required tools
