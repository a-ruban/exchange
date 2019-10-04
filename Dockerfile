# Use an official Python runtime as a parent image
FROM python:3.7-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified from Pipfile
RUN apk add --no-cache gcc
RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev \
    postgresql-dev \
    python3-dev \
    musl-dev
RUN pip install pipenv
RUN pipenv install --system

# Make port 80 available to the world outside this container
EXPOSE 80