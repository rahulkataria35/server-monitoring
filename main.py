import threading
import time
from app import create_app
from app.monitoring import log_and_check_metrics

# Create the Flask app
app = create_app()

# Define a function to monitor metrics
def monitor_metrics():
    """
    Monitor metrics indefinitely
    """
    while True:
        log_and_check_metrics()
        time.sleep(30)

# Entry point for Gunicorn
if __name__ == '__main__':
    # Create a daemon thread to run the monitor_metrics function
    monitor_thread = threading.Thread(target=monitor_metrics, daemon=True)
    monitor_thread.start()

    # Instead of running Flask directly, we'll use Gunicorn to serve the app
    # Use the following command to start the server:
    # gunicorn -w 4 -b 0.0.0.0:5000 main:app
