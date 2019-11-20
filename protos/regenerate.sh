#!/usr/bin/env bash

PROTO_DOCKER_PATH=/opt/herobattleground/protos

declare -a ProtosArray=("character")
 

for proto in ${ProtosArray[@]}; do
    # Generate Python pb files
    OUT_PATH=$PROTO_DOCKER_PATH/python PROTO_PATH=$PROTO_DOCKER_PATH PROTO_NAME=$proto docker-compose up generate-python
done
