# Environment variables for this project.

For running this project you need two .env files.
First .env file needs to be located in fridge_manager/restmanager folder and it's used for django's environment variables.
Second .env file needs to be located in fridge_manager/ folder and it's used for Docker-Compose's environment variables.

## .env for Django app:
    
    DJANGO_TOKEN='DJANGO secret key' 
    SLACK_TOKEN="Slack Bot User OAuth Access Token"
    IP2="IP-address of the hosting server or your local computers internal IP starting 192.168"

    DJANGO_SUPERUSER_PASSWORD = "password for django superuser"
    DJANGO_SUPERUSER_USERNAME = "username for django superuser"
    DJANGO_SUPERUSER_EMAIL = "email for django superuser"

    DB_NAME='DB_NAME <-- same value for both --> MYSQL_DATABASE'
    DB_USER='DB_USER <-- same value for both --> MYSQL_USER'
    DB_PASSWORD='DB_PASSWORD <-- same value for both --> MYSQL_PASSWORD'
    DB_HOST='mariadb-db'
    DB_PORT='3306'


## .env for Docker:

    MYSQL_ROOT_PASSWORD=mariadbroot
    MYSQL_DATABASE=DB_NAME <-- same value for both --> MYSQL_DATABASE
    MYSQL_USER=DB_USER <-- same value for both --> MYSQL_USER
    MYSQL_PASSWORD=DB_PASSWORD <-- same value for both --> MYSQL_PASSWORD
