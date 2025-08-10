# Modul untuk parsing file input (Dockerfile, *.yaml, *.tf)
from pathlib import Path
import yaml

def parse_input(path):
    files = {"docker": [], "k8s": [], "terraform": []}
    for file in Path(path).rglob("*"):
        if file.name == "Dockerfile":
            files["docker"].append(file)
        elif file.suffix == ".yaml":
            with open(file, 'r') as f:
                if yaml.safe_load(f):  # Validasi YAML
                    files["k8s"].append(file)
        elif file.suffix == ".tf":
            files["terraform"].append(file)
    return files

