import psutil
from datetime import datetime
from app.alerting import send_alert
from app.db import insert_metrics
from config import Config

def log_and_check_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_metrics(timestamp, cpu_usage, memory_usage, disk_usage)

    if cpu_usage > Config.CPU_THRESHOLD:
        print("----cpu----")
        send_alert('CPU Alert', {"cpu_usage": cpu_usage})
    if memory_usage > Config.MEMORY_THRESHOLD:
        print("----memory----")
        send_alert('Memory Alert', {"mem_usage": memory_usage})
    if disk_usage > Config.DISK_THRESHOLD:
        send_alert('Disk Alert', {"disk_usage": disk_usage})
