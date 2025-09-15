FROM python:3.11-slim

WORKDIR /app
EXPOSE 8011

CMD ["python", "-m", "http.server", "8011", "--bind", "0.0.0.0"]

