install:
	@poetry install

test:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build:
	check
	 @poetry build

.PHONY: install test lint selfcheck check build
