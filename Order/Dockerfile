FROM docker.lappsgrid.org/deiis/base

#COPY logging.ini /root
COPY *.py /root/

WORKDIR /root
ENTRYPOINT ["python", "service.py"]
