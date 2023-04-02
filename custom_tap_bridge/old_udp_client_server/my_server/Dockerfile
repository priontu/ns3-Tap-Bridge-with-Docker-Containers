FROM ubuntu:20.04 AS builder

# ARG TARGETPLATFORM

# # RUN echo "TARGETPLATFORM : $TARGETPLATFORM"
# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal main restricted universe multiverse" > /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-security main restricted universe multiverse" >> /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-updates main restricted universe multiverse" >> /etc/apt/sources.list
# # RUN echo "deb http://mirror-osd.de.bosch.com/osd focal main" >> /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/partner focal partner" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y apt-transport-https

RUN apt-get update && \
    apt-get install -y net-tools iputils-ping tcpdump ethtool iperf iproute2 python3.8 python3-pip iputils-ping tcpdump
# RUN pip install -U setuptools
# RUN pip freeze
# RUN apt-get update && apt-get -y upgrade python3-pip
# COPY DateTime-5.1.tar.gz home/
# RUN tar xvf DateTime-5.1.tar.gz
# RUN python3 DateTime-5.1/setup.py install
# RUN apt-get install -y python-zope.datetime

RUN pip install DateTime
COPY server.py home/