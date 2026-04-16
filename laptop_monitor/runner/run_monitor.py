# Import components from different layers
import time
from laptop_monitor.collector.metrics_collector import get_metrics
from laptop_monitor.prompts.prompt_builder import build_prompt
from laptop_monitor.client.ai_client import get_ai_insight
from laptop_monitor.storage.metrics_store import save_metrics
from laptop_monitor.rules.rules_engine import check_trigger



def run(interval=15):
    """
    Continuous monitoring loop.

    Args:
        interval (int): seconds between each cycle
    """

    print("Starting continuous laptop monitoring...\n")

    try:
        while True:

            # Step 1: Collect metrics
            metrics = get_metrics()

            # Step 2: Save metrics (history)
            save_metrics(metrics)

            # Step 3: Print basic info
            print("\n==============================")
            print("Metrics:", metrics)

            # Step 4: Rule-based trigger
            trigger = check_trigger(metrics)

            if trigger:
                print("[ACTION] Triggering AI analysis...")

                prompt = build_prompt(metrics)
        
                # Print the prompt for debugging
                print("\n=== [DEBUG] PROMPT SENT TO AI ===")
                print(prompt)

                insight = get_ai_insight(prompt)

                print("\n=== AI INSIGHT ===")
                print(insight)
            else:
                print("[ACTION] No trigger. Skipping AI call.")

            print("==============================\n")

            # Step 5: Wait before next cycle
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nStopping monitoring gracefully...")


if __name__ == "__main__":
    run(interval=15)
