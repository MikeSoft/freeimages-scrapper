# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the project code into the container
COPY . /app/

# print the current directory
RUN pwd
