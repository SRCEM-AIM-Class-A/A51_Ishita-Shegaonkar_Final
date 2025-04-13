# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Django development server port
EXPOSE 8000

# Set environment variable for Django
ENV PYTHONUNBUFFERED 1

# Run Django app (you can replace 'runserver' with another command if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
