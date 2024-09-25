# Use a base Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose ports
EXPOSE 5000
EXPOSE 3000

# Add a script to start MLflow UI and the training script
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Run the start script
CMD ["/app/start.sh"]
