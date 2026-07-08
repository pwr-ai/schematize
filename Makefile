lint_dirs := src/schematize scripts tests

.PHONY: fix check check-types test all

fix:
	ruff check --fix $(lint_dirs)

check:
	ruff check $(lint_dirs)

check-types:
	mypy --install-types --non-interactive $(lint_dirs)

test:
	coverage run -m pytest
	coverage report -mi

all: check test
