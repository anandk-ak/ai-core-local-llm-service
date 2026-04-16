def check_trigger(metrics):
    """
    Decide whether to trigger LLM based on rules.

    Args:
        metrics (dict): current system metrics

    Returns:
        bool: True if LLM should be triggered
    """

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
