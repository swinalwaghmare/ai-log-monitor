FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# COPY backend/requirements.txt .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend app
# COPY backend/app /app/app
COPY app /app/app

# Copy shared folder
# COPY shared /app/shared
COPY ../shared /app/shared


# Copy log generator
# COPY backend/log_generator.py /app/app/log_generator.py
COPY log_generator.py /app/app/log_generator.py


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]