.PHONY: db-up db-down db-init db-seed backend-dev frontend-dev smoke-test

db-up:
	docker compose up -d postgres

db-down:
	docker compose down

db-init:
	cd apps/cli && python -m geo_cli.main init

db-seed:
	cd apps/cli && python -m geo_cli.main seed

backend-dev:
	cd apps/backend && uvicorn app.main:app --reload --port 8000

frontend-dev:
	cd apps/frontend && npm run dev

smoke-test:
	python scripts/smoke_test.py
