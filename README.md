# Softalaproject repo for automated fridge management app
The application is containerized with Docker and can be run with Vagrant. The build is done with Django and Node. For now we use an SQLite database

## SW requirements:
Git bash (if you're using Windows): https://gitforwindows.org/
Docker or python.

## Start server:


Locally using python;

1. Start server

	python manage.py runserver

2. Open localhost or http://127.0.0.1/ on your host machine.
3. To stop python from running application ctrl + c

Starting with Docker-compose;

1. Build Docker image:

	docker-compose build

2. Start application:

	docker-compose up -d

3. Stop using application

	docker-compose down

Starting with Docker (container)

1. Build container

	docker build -t djangoapp .

2. Run container 

	docker container run -p 8000:8000 --name djangoapp djangoapp

3. To stop container ctrl + c
