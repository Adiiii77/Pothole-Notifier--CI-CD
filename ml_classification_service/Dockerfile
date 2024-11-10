# Dockerfile for ml_classification_service
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002
CMD ["python", "app.py"]
