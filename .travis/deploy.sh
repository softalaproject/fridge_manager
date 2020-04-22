#!/bin/bash

eval "$(ssh-agent -s)" # Start ssh-agent cache
chmod 600 .travis/id_rsa # Allow read access to the private key
ssh-add .travis/id_rsa # Add the private key to SSH

# git config --global push.default matching
# git remote add deploy ssh://git@$IP:$PORT$DEPLOY_DIR
# git push deploy dev

# Skip this command if you don't need to execute any additional commands after deploying.
ssh apps@$IP -p $PORT <<EOF
  cd $DEPLOY_DIR
  git fetch origin
  git reset --hard origin/dev2
  docker-compose down
  python restmanager/manage.py makemigrations
  python restmanager/manage.py migrate
  docker-compose build
  docker-compose up -d
EOF
