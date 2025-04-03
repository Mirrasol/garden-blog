install:
	uv sync

run:
	uv run python manage.py runserver

lint:
	uv run ruff check

build:
	uv build