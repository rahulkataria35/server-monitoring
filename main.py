from app import create_app
from app.monitoring import log_and_check_metrics
import threading
import time

# Define a function to monitor metrics
def monitor():
    """
    Monitor metrics indefinitely
    """
    while True:
        # Log and check metrics
        log_and_check_metrics()
        # Sleep for 30 sec before checking again
        time.sleep(30)

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Create a daemon thread to run the monitor function
    # This allows the thread to run in the background while the app runs
    threading.Thread(target=monitor, daemon=True).start()
    # Run the Flask app on host 0.0.0.0, port 5000, in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)