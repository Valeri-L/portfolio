# Dockerfile for the backend
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Expose the backend port
EXPOSE 8000

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.settings

# Run the Django development server (replace with `gunicorn` in production)
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
