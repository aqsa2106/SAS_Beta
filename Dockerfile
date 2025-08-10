# Dockerfile untuk menjalankan sistem dalam container
FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN curl -sSL https://get.snyk.io | bash
COPY src/ ./src
CMD ["python", "src/audit_iac.py", "--path", "/infra", "--format", "json"]