# Modul untuk memetakan temuan ke benchmark CIS
import json

def map_to_cis(findings):
    with open("src/utils/cis_mapping.json", "r") as f:
        cis_mapping = json.load(f)
    cis_results = []
    for finding in findings:
        # finding: {tool: {result_dict}}
        for tool, result in finding.items():
            if not isinstance(result, dict):
                continue
            # Cek id temuan sesuai tool
            check_id = result.get("check_id") or result.get("id")
            if check_id and check_id in cis_mapping:
                cis_results.append(cis_mapping[check_id])
    return cis_results