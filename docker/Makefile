REPO=docker.lappsgrid.org
IMAGE=deiis/base
NAME=base
TGZ=deiis-rabbit.tgz

docker:
	if [ ! -e $(TGZ) ] ; then ./get-deiis-rabbit.sh ; fi
	docker build -t $(IMAGE) .

push:
	docker tag $(IMAGE) $(REPO)/$(IMAGE)
	docker push $(REPO)/$(IMAGE)

run:
	docker run -it --name $(NAME) $(IMAGE) /bin/bash

stop:
	docker rm -f $(NAME)

help:
	@echo
	@echo "GOALS"
	@echo
	@echo "docker - builds the image [default]"
	@echo "push   - pushes the image to $REPO"
	@echo "run    - runs the Docker container"
	@echo "stop   - stops a running Docker container"			
	@echo "help   - prints this help message"
	@echo
		