lint_dirs := src/schematize research/scripts tests

.PHONY: fix check check-types test all research-check

fix:
	uv run ruff check --fix $(lint_dirs)

check:
	uv run ruff check $(lint_dirs)

check-types:
	uv run mypy src/schematize

test:
	uv run coverage run -m pytest
	uv run coverage report -mi

all: check check-types test

research-check:
	uv run ruff check research/scripts tests/research
	uv run pytest tests/research
