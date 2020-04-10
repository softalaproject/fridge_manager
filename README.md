# Softalaproject repo for automated fridge management app
The application is containerized with Docker. <br>
The build is done with Django and Node.<br> 
Project uses SQLite for the database.

## SW requirements:
Git bash (if you're using Windows): https://gitforwindows.org/<br>
Docker or Python3.<br>
Make sure you have a .env file in fridge_manager/restmanager folder with appropriate values:<br>
SLACK_TOKEN<br>
DJANGO_TOKEN<br>
IP2<br>
Documentation regarding these values is found in documents/env information
## Start server:

Locally using python;

1. Start server

	python manage.py runserver

2. Open localhost or http://127.0.0.1/ on your host machine.

3. To stop hosting the server use ctrl + c in the python console window.

Starting with Docker-compose;

1. Build Docker image:

	docker-compose build

2. Start application:

	docker-compose up -d

3. Stop using application

	docker-compose down


## Bad Request 400
If you get Bad Request 400 when trying to access the server, <br>
please add your local internal IP (192.168.x.x) to the .env file located in fridge_manager/restmanager
