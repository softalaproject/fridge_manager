# Softalaproject repo for automated fridge management app
This is a school project done by Haaga-Helia software development students for Eficode,
the application manages different floors and fridge contents on said floors. The user of the application can send direct messages to the companys internal Slack channel of the fridge status e.g. when it need's a fill up etc. <br>
The application is containerized with Docker. <br>
The build is done with Django.<br> 
Project uses SQLite for the database. <br>
There is a mobile version of this app wrapped with Cordova.


## Screenshots of the application running
1st image is the view for all the floors that the application is tracking.
![Floors](https://github.com/softalaproject/fridge_manager/blob/master/documents/screenshots/floors.jpg) 

2nd image is the single floor view, that displays all the fridges on that floor and their content status.
![Floor2](https://github.com/softalaproject/fridge_manager/blob/master/documents/screenshots/floor2.jpg) 

## SW requirements:
Git bash (if you're using Windows): https://gitforwindows.org/<br>
Docker or Python3.<br>
Make sure you have both .env files in right folders with appropriate values. Check [env documentation](https://github.com/softalaproject/fridge_manager/blob/master/documents/env_information.md) for details.
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
