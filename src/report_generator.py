# Modul untuk menghasilkan laporan JSON/teks


import json
from policy_manager import map_to_cis

def generate_report(results, format="json"):
    report = {"findings": [], "cis_compliance": []}
    for tool, result in results.items():
        report["findings"].append({tool: json.loads(result) if result else {}})
    report["cis_compliance"] = map_to_cis(report["findings"])
    return json.dumps(report, indent=2) if format == "json" else format_text(report)