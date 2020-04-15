#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 .travis/id_rsa # Allow read access to the private key
ssh-add .travis/id_rsa # Add the private key to SSH

git config --global push.default matching
git remote add deploy ssh://git@$IP:$PORT$DEPLOY_DIR
git push deploy dev

# Skip this command if you don't need to execute any additional commands after deploying.
ssh apps@$IP -p $PORT <<EOF
  pkill -f runserver
  cd $DEPLOY_DIR
  git fetch origin
<<<<<<< HEAD
  git pull origin dev
  pip3 install -r requirements.txt
  python3.6 restmanager/manage.py runserver $IP2:8080 &
=======
  git reset --hard origin/feature/docker
  docker-compose down
  docker-compose build
  docker-compose up -d

>>>>>>> parent of 82a60d3... Merge branch 'dev' into feature/docker
EOF
