FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src/ ./src/

COPY assets assets

RUN uv sync --frozen --no-dev

RUN uv run playwright install chromium --with-deps

ENTRYPOINT ["uv", "run", "price-tracker"]
