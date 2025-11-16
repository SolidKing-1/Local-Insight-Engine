# Use official Python 3.13 slim image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install system dependencies & Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential curl && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the backend code
COPY . .

# Expose Flask port
EXPOSE 5000

# Default command (can be overridden by docker-compose)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
