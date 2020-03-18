# Softalaproject repo for automated fridge management app
The application is containerized with Docker and can be run with Vagrant. The build is done with Django and Node. For now we use an SQLite database.

## SW requirements:

Virtualbox 6.0.x: https://www.virtualbox.org/wiki/Download_Old_Builds_6_0
Vagrant: https://www.vagrantup.com/downloads.html
Git bash (if you're using Windows): https://gitforwindows.org/
Some text editor, VSCode (https://code.visualstudio.com/) , notepad++ (https://notepad-plus-plus.org/), something else than Notepad
Todo:

## Starting vagrant:

Install first Virtualbox 6.0.x

Install vagrant after Virtualbox

And then run this command:

  vagrant up
Based on Ubuntu 18.04 Bionic server with docker-ce, docker-compose and minikube preinstalled

## Starting environment:

vagrant up
Stopping environment:

vagrant halt
Destroying environment:

vagrant destroy -f
Destroying and rebuilding environment:

vagrant destroy -f && vagrant up

Vagrant is automaticly installing python-pip and all python modules according to requirements.txt.

When development enviroment is up;

Navigate to django/restfull/

## Start server:

 python manage.py runserver 0.0.0.0:8000
Open localhost:8000 or http://127.0.0.1:8000/ on your host machine.

Starting with Docker;

if you are using Vagrant:

 cd /softala/django
Build Docker image:

 docker build -t djangoapp .
Run Docker container:

 docker container run -p 8000:8000 --name djangoapp djangoapp
