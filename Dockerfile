
# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all scripts into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir langchain openai feedparser

# Set environment variables (you can override these during runtime)
ENV OPENAI_API_KEY=your_openai_api_key
ENV EMAIL_PASSWORD=your_email_password

# Default command: run all agents (can override in docker-compose)
CMD ["python", "Job_Hunter_Agent.py"]
