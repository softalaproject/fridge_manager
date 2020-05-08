# Environment variables for this project.

For running this project you need two .env files.
First .env file needs to be located in fridge_manager/restmanager/.env folder and it's used for django's environment variables.
Second .env file needs to be located in fridge_manager/ folder and it's used for Docker-Compose's environment variables.

## fridge_manager/restmanager/.env for Django app:
    
    DJANGO_TOKEN='DJANGO secret key' 
    SLACK_TOKEN="Slack Bot User OAuth Access Token"
    IP2="IP-address of the hosting server or your local computers internal IP starting 192.168"

    DJANGO_SUPERUSER_PASSWORD="password for django superuser"
    DJANGO_SUPERUSER_USERNAME="username for django superuser"
    DJANGO_SUPERUSER_EMAIL="email for django superuser"

    DB_NAME='mariadbdjango'
    DB_USER='mariadbuser'
    DB_PASSWORD='mariadbuser'
    DB_HOST='mariadb-db'
    DB_PORT='3306'


## fridge_manager/.env for Docker:

    MYSQL_ROOT_PASSWORD=mariadbroot
    MYSQL_DATABASE=same value as DB_NAME in the Django app .env
    MYSQL_USER=same value as DB_USER in the Django app .env
    MYSQL_PASSWORD=same value as DB_PASSWORD in the Django app .env
