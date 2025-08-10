# Skrip CLI utama untuk menjalankan audit
import argparse
from input_parser import parse_input
from audit_engine import run_audit
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="IaC and Container Security Audit")
    parser.add_argument("--path", required=True, help="Path to IaC/container files")
    parser.add_argument("--format", default="json", choices=["json", "text"])
    args = parser.parse_args()
    files = parse_input(args.path)
    results = run_audit(files)
    report = generate_report(results, args.format)
    print(report)

if __name__ == "__main__":
    main()
