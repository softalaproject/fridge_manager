# Dockerfile for django project

# Add a base image to build this image off of
FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# define workdir
WORKDIR /code

# copy requirements.txt and install
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy all files and folders
COPY . /code/
