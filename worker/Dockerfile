FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend app
COPY worker/app /app/app

# Copy shared folder
COPY shared /app/shared

CMD ["python", "-m", "app.worker"]