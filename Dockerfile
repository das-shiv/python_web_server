# Using the python:alpine image as base image
FROM python:alpine

# Setting the working directory inside the container
WORKDIR /app

# Copying the app.py and server.py file to the working directory of container
COPY . /app

# Starting the python server with CMD
CMD ["python", "server.py"]
