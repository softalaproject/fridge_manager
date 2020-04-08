# Dockerfile for django project

# Add a base image to build this image off of
FROM alang/django

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# define workdir
WORKDIR /code

#ENV DJANGO_APP=demo  # will start /usr/django/app/demo/wsgi.py

# copy requirements.txt and install
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy all files and folders
COPY . /code/

# Add a default port containers from this image should expose
#EXPOSE 8080
