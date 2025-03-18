{% if cookiecutter.use_docker == "yes" %}
# Stage 1: Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt
COPY . .

# Stage 2: Run
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /app .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
{% endif %}