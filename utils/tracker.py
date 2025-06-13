# Daily tracker input handler
# utils/tracker.py
import json
from datetime import datetime

def log_user_data(name, dob, result):
    data = {
        "timestamp": datetime.now().isoformat(),
        "name": name,
        "dob": dob,
        "result": result
    }
    with open("user_logs.json", "a") as f:
        f.write(json.dumps(data) + "\n")
