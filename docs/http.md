import random
from datetime import datetime

if "action" in execution['input']:
    print("Simulating pfSense API...")
    return {
        "status": "success",
        "data": {
            "id": f"fwrule_{random.randint(1000,9999)}",
            "action": execution['input']['action'],
            "src": execution['input'].get('src_ip', 'any'),
            "dst": execution['input'].get('dst_ip', 'any'),
            "protocol": execution['input'].get('protocol', 'tcp'),
            "timestamp": datetime.now().isoformat()
        }
    }
else:
    return {"error": "Missing action parameter"}
