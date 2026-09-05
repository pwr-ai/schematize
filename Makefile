lint_dirs := src/schematize tests
research_lint_dirs := research/scripts tests/research

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
	uv run ruff check $(research_lint_dirs)
	uv run pytest tests/research
