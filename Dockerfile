# Use official Python image
FROM python:3.11-alpine3.21

RUN apk add --no-cache g++ make libffi-dev musl-dev

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN python -m pip install --upgrade pip --no-cache-dir  \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Set environment variable for credentials
ENV GOOGLE_APPLICATION_CREDENTIALS="/database/operating-aria-445016-b8-237a8c866c96.json"

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
