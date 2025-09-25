# Use official Python base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from current directory to container
COPY . .

# Install dependencies
RUN pip install flask

# Expose the port your app runs on
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]