import os

script_path = os.path.realpath(__file__)
head, tail = os.path.split(script_path)


class Config:
    # System thresholds
    CPU_THRESHOLD = int(os.getenv('CPU_THRESHOLD', 80))
    MEMORY_THRESHOLD = int(os.getenv('MEMORY_THRESHOLD', 80))
    DISK_THRESHOLD = int(os.getenv('DISK_THRESHOLD', 90))
    
    # SMTP settings
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'localhost')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 25))
    EMAIL_ID = os.getenv('EMAIL_FROM')
    EMAIL_TO = os.getenv('EMAIL_TO')
    STARTUP_MAIL_CC = os.getenv("STARTUP_MAIL_CC")
    
    # Database settings
    DB_NAME = os.getenv('DB_NAME', 'monitoring')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    DB_HOST = os.getenv('DB_HOST', 'db')
    DB_PORT = os.getenv('DB_PORT', '5432')
