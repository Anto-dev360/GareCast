# Dockerfile – GareCast with Python 3.13

FROM python:3.12-slim

# Environement variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install required python libs
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Project copy
COPY . .

# Exposure of the port used by Streamlit
EXPOSE 8501

# Launch command
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
