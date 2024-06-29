import os
import base64
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from requests import get
from jinja2 import Template
import pytz
from config import Config, head

# loading email credentials
print("---", Config.EMAIL_ID)
EMAIL_ID = json.loads(base64.b64decode(Config.EMAIL_ID).decode("ascii"))


tz_in = pytz.timezone('Asia/Kolkata')

def send_alert(subject, body):
    """
    Sends alert emails.
    """
    # print logs
    print(f"[{datetime.now(tz_in)}] Sending alert email...")
    server_ip = get('https://api.ipify.org').text

    current_time = datetime.now(tz_in).strftime("%Y-%m-%d %H:%M:%S")

    with open(os.path.join(head, 'templates/alert.html'), 'r') as template_file:
        html_template = Template(template_file.read())

    data = {
        "project_name": "HDFC",
        "env": body.get("env", "N/A"),
        "time": current_time,
        "ip": server_ip,
        "cpu_usage": body.get("cpu_usage", "N/A"),
        "mem_usage": body.get("mem_usage", "N/A"),
        "disk_usage": body.get("disk_usage", "N/A")
    }
    print("Data passed to template:", data)  # Debug print statement
    final_html = html_template.render(data=data)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = Config.EMAIL_ID['username']
    msg['To'] = "rahulkataria3355@gmail.com"
    msg['Cc'] = Config.STARTUP_MAIL_CC
    part2 = MIMEText(final_html, 'html')
    msg.attach(part2)

    try:  
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as mail:
            mail.ehlo()
            mail.starttls()
            mail.login(Config.EMAIL_ID['username'], Config.EMAIL_ID['password'])
            mail.sendmail(
                Config.EMAIL_ID['username'], 
                msg['To'].split(",") + msg['Cc'].split(","), 
                msg.as_string()
            )
    except Exception as ex:
        print(ex)
        return {"RESPONSE_TYPE": "E", "RESPONSE_MESSAGE": "Failed to send email", "error": str(ex)}

    return {"RESPONSE_TYPE": "I", "RESPONSE_MESSAGE": "Email sent successfully"}


