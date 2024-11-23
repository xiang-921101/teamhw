import time
from telemetry.telemetry import get_tracer
import logging

# Get tracer
tracer = get_tracer()

def baby_grogu_telemetry(how_long):
    """Simulates Baby Grogu level telemetry."""
    start_time = time.time()
    with tracer.start_as_current_span("baby_grogu_span"):
        try:
            how_long_int = int(how_long)
            print(f"Practicing telemetry for {how_long_int} seconds.")
            while time.time() - start_time < how_long_int:
                print("👾", end="", flush=True)
                time.sleep(0.5)
            print("\nTelemetry practice complete!")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    baby_grogu_telemetry(5)
