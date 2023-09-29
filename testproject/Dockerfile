# Use the official Python base image
FROM python:3.9.18-bookworm

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]