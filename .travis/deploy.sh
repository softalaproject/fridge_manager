#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 .travis/id_rsa # Allow read access to the private key
ssh-add .travis/id_rsa # Add the private key to SSH

# Skip this command if you don't need to execute any additional commands after deploying.
ssh apps@$IP -p $PORT <<EOF
  pkill -f runserver
  cd $DEPLOY_DIR
  git fetch origin
  git reset --hard origin/dev
  pip3 install -r requirements.txt
  python3.6 restmanager/manage.py migrate
  python3.6 restmanager/manage.py runserver $IP2:8080 &
EOF
