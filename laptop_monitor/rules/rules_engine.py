import time

global LAST_TRIGGER_TIME

def check_trigger(metrics):
    """
    Decide whether to trigger LLM based on rules.

    Args:
        metrics (dict): current system metrics

    Returns:
        bool: True if LLM should be triggered
    """

    #adding a cool down period. This avoinds spawning multiple threads if there is more than 1 spike
    LAST_TRIGGER_TIME = 0
    COOLDOWN = 60  # seconds

    current_time = time.time()     

    # Prevent frequent triggering
    if current_time - LAST_TRIGGER_TIME < COOLDOWN:
        return False

    cpu = metrics.get("cpu", 0)
    memory = metrics.get("memory", 0)

    # Simple thresholds (we will improve later)
    if cpu > 80:
        print("[RULE] High CPU detected")
        return True

    if memory > 85:
        print("[RULE] High Memory detected")
        return True

    return False
