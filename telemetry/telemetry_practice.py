import time
import random
import string
import logging
from telemetry.telemetry import get_tracer

# Set up Python logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get tracer for spans
tracer = get_tracer()

def practice_telemetry(how_long):
    start_time = time.time()
    with tracer.start_as_current_span("baby_grogu_telemetry_with_logs"):
        try:
            how_long_int = int(how_long)
            logger.info("Starting to practice The Telemetry for %i second(s)", how_long_int)
            while time.time() - start_time < how_long_int:
                next_char = random.choice(string.punctuation)
                print(next_char, end="", flush=True)
                time.sleep(0.5)
            logger.info("Done practicing")
        except ValueError as ve:
            logger.error("I need an integer value for the time to practice: %s", ve)
            return False
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            return False
    return True

logger.info("Practicing telemetry for %i seconds.", how_long_int)
logger.info("Telemetry practice complete!")

# Example call
if __name__ == "__main__":
    practice_telemetry(5)
