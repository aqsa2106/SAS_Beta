# Modul untuk mengorkestrasi alat-alat audit

import subprocess

def run_audit(files):
    results = {}
    for tool, cmd in [
        ("checkov", ["checkov", "-d", "{path}", "--framework", "all", "--output", "json"]),
        ("trivy", ["trivy", "config", "{path}", "--format", "json"]),
        # Tambahan untuk KICS, Terrascan, dll.
    ]:
        for file_type, file_list in files.items():
            for file in file_list:
                cmd_formatted = [arg.format(path=file) for arg in cmd]
                result = subprocess.run(cmd_formatted, capture_output=True, text=True)
                results[f"{tool}_{file}"] = result.stdout
    return results