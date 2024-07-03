# Use a slim Python image as the base
FROM python:3.9-slim

# Set working directory within the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire application code
COPY . .

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Command to run Gunicorn with your Flask application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
