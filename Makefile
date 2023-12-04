.PHONY: tests
tests:
	@poetry run pytest ravApp -vv

.PHONY: up
up:
	@docker compose up -d

.PHONY: down
down:
	@docker compose down