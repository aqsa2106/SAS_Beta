# Skrip untuk otomatisasi tugas
install:
    pip install -r requirements.txt
test:
    pytest tests/
audit:
    python src/audit_iac.py --path tests/sample_files --format json


