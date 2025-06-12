import json
from datetime import datetime

def log_vulnerability(vuln_type, url, payload):
    log = {
        "timestamp": datetime.now().isoformat(),
        "type": vuln_type,
        "url": url,
        "payload": payload,
        "severity": "High" if vuln_type == "SQLi" else "Medium"
    }
    with open("scan_results.json", "a") as f:
        f.write(json.dumps(log) + "\n")
