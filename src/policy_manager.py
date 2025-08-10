# Modul untuk memetakan temuan ke benchmark CIS
import json

def map_to_cis(findings):
    with open("src/utils/cis_mapping.json", "r") as f:
        cis_mapping = json.load(f)
    cis_results = []
    for finding in findings:
        if finding["check_id"] in cis_mapping:
            cis_results.append(cis_mapping[finding["check_id"]])
    return cis_results