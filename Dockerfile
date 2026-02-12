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
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# uv installs to ~/.local/bin by default; ensure it's on PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy requirements and install Python dependencies via uv
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Copy application code
COPY app ./app

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /code
USER appuser

# Expose port
EXPOSE 5050

# Run the application
ENTRYPOINT ["python"]
CMD ["app/app.py"]