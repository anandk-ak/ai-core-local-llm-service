import json
import os
from datetime import datetime

# File where metrics will be stored
METRICS_FILE = "laptop_monitor/storage/metrics.json"

# Max number of records to keep (rolling window)
MAX_RECORDS = 1000

def save_metrics(metrics):
    """
    Save metrics to a JSON file with timestamp.

    Args:
        metrics (dict): System + process metrics
    """

    # Add timestamp to metrics
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        **metrics
    }

    # If file exists, load existing data
    if os.path.exists(METRICS_FILE):
        with open(METRICS_FILE, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupted file
                existing_data = []
    else:
        existing_data = []

    # Append new record
    existing_data.append(data)

    # Keep only last MAX_RECORDS entries
    if len(existing_data) > MAX_RECORDS:
        existing_data = existing_data[-MAX_RECORDS:]

    # Write back to file
    with open(METRICS_FILE, "w") as f:
        json.dump(existing_data, f, indent=2)
