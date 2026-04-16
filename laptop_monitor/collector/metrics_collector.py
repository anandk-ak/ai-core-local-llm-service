import time
import psutil
import os

def get_top_processes(limit=3):
    """
    Get top CPU-consuming processes.

    This function performs a two-step CPU measurement:
    1. Initialize CPU counters
    2. Wait briefly
    3. Capture actual CPU usage
    """

    processes = []

    # Step 1: Initialize CPU counters for all processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Step 2: Wait a short time to measure CPU usage
    time.sleep(0.3)

    # Step 3: Collect actual CPU usage
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            current_pid = os.getpid()
            if proc.pid == current_pid:
                continue  # 👈 skip your own process, that is, monitor is excluded from this list

            process_info = proc.info

            cpu_usage = process_info['cpu_percent'] or 0.0

            processes.append({
                "name": process_info['name'] or "unknown",
                "cpu": cpu_usage
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Sort by CPU usage (highest first)
    processes = sorted(processes, key=lambda x: x['cpu'], reverse=True)

    return processes[:limit]

def get_metrics():
    """
    Collect system-level and process-level metrics.

    Returns:
        dict: System metrics + top processes
    """

    # Capture CPU usage (1-second interval for accuracy)
    cpu = psutil.cpu_percent(interval=1)

    # Memory usage percentage
    memory = psutil.virtual_memory().percent

    # Disk usage percentage
    disk = psutil.disk_usage('/').percent

    # Get top CPU-consuming processes
    top_processes = get_top_processes(limit=3)

    return {
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "top_processes": top_processes
    }
