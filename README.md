
# SAS_Beta

SAS_Beta adalah proyek open source untuk audit otomatis Infrastructure as Code (IaC) seperti Dockerfile, Kubernetes YAML, dan Terraform, serta pemetaan hasil audit ke benchmark CIS. Proyek ini mendukung integrasi CI/CD dengan GitHub Actions.

## Fitur Utama
- Audit otomatis file IaC (Dockerfile, YAML, Terraform) menggunakan Checkov & Trivy
- Pemetaan hasil audit ke CIS Benchmark
- Laporan dalam format JSON
- Integrasi GitHub Actions untuk CI/CD
- Struktur modular & mudah dikembangkan

## Struktur Folder
```
src/                # Kode utama (parser, engine, policy, report)
tests/              # Unit test & sample files
config/             # Konfigurasi audit & mapping CIS
reports/            # Output laporan audit
.github/workflows/  # Workflow GitHub Actions
```

## Instalasi & Persiapan
1. Clone repo ini:
	```bash
	git clone https://github.com/aqsa2106/SAS_Beta.git
	cd SAS_Beta
	```
2. Install Python & pip (minimal Python 3.8)
3. Install dependensi:
	```bash
	pip install -r requirements.txt
	```
4. (Opsional) Install Checkov & Trivy secara manual jika ingin audit lokal:
	```bash
	pip install checkov
	sudo apt-get install -y trivy  # atau ikuti petunjuk di https://aquasecurity.github.io/trivy/v0.18.3/installation/
	```

## Cara Menjalankan Audit (Lokal)
```bash
python src/audit_iac.py --path tests/sample_files --format json
```
Output akan tersimpan di `reports/audit_report.json`.

## Menjalankan di GitHub Actions (CI/CD)
1. Pastikan file `.github/workflows/main.yml` sudah ada di repo.
2. Setiap push/pull request ke repo akan otomatis menjalankan audit.
3. Hasil audit dapat diunduh dari tab **Actions** di GitHub.

## Kontribusi
Pull request & issue sangat terbuka! Silakan tambahkan fitur, perbaikan bug, atau dokumentasi.

## Lisensi
MIT License
