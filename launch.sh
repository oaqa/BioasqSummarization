#!/usr/bin/env bash

if [ "$RABBIT_HOST" = "" ] ; then
	echo "Please set the RABBIT_HOST variable before starting the Docker containers."
	exit 1
fi

for container in tiler ranker expander order results ; do
	docker run -d -e RABBIT_HOST=$RABBIT_HOST --name $container docker.lappsgrid.org/deiis/$container
done