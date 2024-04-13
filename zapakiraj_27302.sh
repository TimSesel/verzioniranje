#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Napaka: Neustrezno število argumentov za ukaz zapakiraj"
    exit 1
fi

DOCKER_USERNAME=$1
REPONAME=$2

docker build . --file Dockerfile --tag "$DOCKER_USERNAME/$REPONAME:latest"