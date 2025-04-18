﻿# A51_Ishita-Shegaonkar_Final
Final Assignment: Dockerized Flask and Django Applications
This project contains two simple web applications developed with Flask and Django, containerized using Docker for easy deployment and scaling.

Both images have been built and pushed to Docker Hub and are publicly available.

📦 Docker Hub Repositories
Application	Repository	Docker Pull Command
Flask App	ishita1455/assignment3-flask	docker pull ishita1455/assignment3-flask:latest
Django App	ishita1455/assignment3-django	docker pull ishita1455/assignment3-django:latest


Follow these steps to run the applications locally using Docker:

1. Prerequisites
Ensure you have Docker installed and running.

2. Pull the Images
bash
Copy
Edit
docker pull ishita1455/assignment3-flask:latest
docker pull ishita1455/assignment3-django:latest
3. Run the Containers
Flask Application (Default Port: 5000):

bash
Copy
Edit
docker run -d -p 5000:5000 ishita1455/assignment3-flask:latest
Access it at http://localhost:5000.

Django Application (Default Port: 8000):

bash
Copy
Edit
docker run -d -p 8000:8000 ishita1455/assignment3-django:latest
Access it at http://localhost:8000.

🔍 Project Structure
Each application includes:

A Python application (app.py for Flask, manage.py and settings for Django).

A Dockerfile for containerization.

Minimal setup for running the app inside a container.

🧰 Technologies Used
Python 3.x

Flask (for lightweight web app)

Django (for full-stack web framework)

Docker (containerization)

Docker Hub (image repository)
