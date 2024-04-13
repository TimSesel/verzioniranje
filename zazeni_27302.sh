#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Napaka: Neustrezno število argumentov za ukaz zazeni"
    exit 1
fi

DOCKER_USERNAME=$1
REPONAME=$2

docker pull "$DOCKER_USERNAME/$REPONAME:latest"
docker run -p 8888:5000 "$DOCKER_USERNAME/$REPONAME:latest"