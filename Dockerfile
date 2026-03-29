# Use Python 3.14 slim image
FROM python:3.14-slim

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast Python dependency installs
ENV UV_LINK_MODE=copy
ENV UV_INSTALL_DIR=/usr/local/bin
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/code/.venv/bin:${PATH}"

# Create non-root user before copying project files so we can avoid a slow recursive chown.
RUN adduser --disabled-password --gecos '' appuser \
    && chown appuser:appuser /code

# Copy lockfile metadata and install Python dependencies via uv
COPY --chown=appuser:appuser pyproject.toml uv.lock ./
USER appuser
RUN uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY --chown=appuser:appuser app ./app

# Expose port
EXPOSE 5050

# Run the application
CMD ["python", "-m", "app.app"]