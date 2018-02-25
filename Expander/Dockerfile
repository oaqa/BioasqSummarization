FROM deiis/base

RUN pip install pyquery

ADD metamap.tgz /usr/local/share
WORKDIR /usr/local/share/public_mm/bin
RUN echo "/usr/local/share/public_mm" | ./install.sh

ADD pymetamap.tgz /root
WORKDIR /root/pymetamap
RUN python setup.py install

COPY *.py /root/
COPY *.ini /root/
WORKDIR /root

ENTRYPOINT ["python", "service.py"]
