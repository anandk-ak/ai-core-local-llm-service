# Import components from different layers
from laptop_monitor.collector.metrics_collector import get_metrics
from laptop_monitor.prompts.prompt_builder import build_prompt
from laptop_monitor.client.ai_client import get_ai_insight
from laptop_monitor.storage.metrics_store import save_metrics
from laptop_monitor.rules.rules_engine import check_trigger


def run():
    """
    Main execution flow:
    1. Collect system metrics
    2. Build AI prompt
    3. Get AI-generated insight
    4. Print results
    """

    # Step 1: Collect real-time metrics from system
    metrics = get_metrics()

    # and Save metrics to history
    save_metrics(metrics)

    # Step 2: Check if we should trigger AI
    trigger = check_trigger(metrics)

    if trigger:
        print("[ACTION] Triggering AI analysis...")

        # Step 4: Convert metrics into a structured prompt
        prompt = build_prompt(metrics)
        
        # 👉 NEW: Print the prompt for debugging
        print("\n=== [DEBUG] PROMPT SENT TO AI ===")
        print(prompt)

        # Step 5: Display the metrics
        print("\n=== METRICS ===")
        print(metrics)

        # Step 6: Send prompt to AI Core and get insight
        insight = get_ai_insight(prompt)
        print("\n=== AI INSIGHT ===")
        print(insight)
    else:
        # Step 5: Display the metrics
        print("\n=== METRICS ===")
        print(metrics)
        
        print("[DEBUG] [ACTION] No trigger. Skipping AI call.")


# Standard Python entry point
if __name__ == "__main__":
    run()
