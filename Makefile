.PHONY: format check test test-coverage

format:
	ruff check apiradar tests --fix --select I
	ruff format apiradar tests

check:
	ruff check apiradar tests
	ruff format --diff apiradar tests
	mypy --install-types --non-interactive apiradar tests
	poetry check

test:
	pytest -v --tb=short

test-coverage:
	pytest -v --tb=short --cov --cov-report=xml
