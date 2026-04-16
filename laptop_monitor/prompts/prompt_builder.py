def build_prompt(metrics):
    """
    Build a prompt including system metrics + process insights.
    """

    # Format process list nicely for LLM readability
    process_text = "\n".join(
        [f"- {p['name']}: {p['cpu']}%" for p in metrics.get("top_processes", [])]
    )

    return f"""
You are a system monitoring expert.

Analyze the following laptop metrics and provide:
1. What is happening
2. Which processes are responsible
3. Possible causes
4. Recommendations

Metrics:
- CPU Usage: {metrics['cpu']}%
- Memory Usage: {metrics['memory']}%
- Disk Usage: {metrics['disk']}%

Top Processes:
{process_text}
"""
