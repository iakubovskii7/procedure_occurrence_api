# Use official Python image
FROM python:3.11-slim

# Install required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libffi-dev python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /code

# Copy files
COPY ./app /code/app
COPY poetry.lock /code/poetry.lock
COPY pyproject.toml /code/pyproject.toml

# Install dependencies
RUN python -m pip install --upgrade pip --no-cache-dir  \
    && pip install poetry \
     && poetry config virtualenvs.create false \
    && poetry install --without test --no-interaction --no-ansi --no-root

# Expose port
EXPOSE 8080

# Run the application
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]

