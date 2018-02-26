#!/usr/bin/env bash

docker ps -q -f "status=exited" | xargs docker rm


