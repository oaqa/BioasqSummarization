FROM docker.lappsgrid.org/deiis/base

COPY *.py /root/
COPY logging.ini /root

WORKDIR /root
ENTRYPOINT ["python", "service.py"]
