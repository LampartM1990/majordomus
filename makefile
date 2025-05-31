.PHONY: dev prod clean logs shell \
    dev-build dev-up dev-down \
    prod-build prod-up prod-down

dev: dev-down dev-build dev-up logs
prod: prod-down prod-build prod-up logs

# Development environment
dev-build:
	docker compose --profile dev build --pull --no-cache

dev-up:
	docker compose --profile dev up -d --force-recreate --remove-orphans

dev-down:
	docker compose --profile dev down

dev-restart:
	docker compose --profile dev restart

# Production environment
prod-build:
	docker compose --profile prod build --pull --no-cache

prod-up:
	docker compose --profile prod up -d --force-recreate --remove-orphans

prod-down:
	docker compose --profile prod down

prod-restart:
	docker compose --profile prod restart

# Utils
logs:
	docker compose logs -f majordomus

shell:
	docker compose exec -it majordomus bash
