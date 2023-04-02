FROM ubuntu:20.04

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get update && \
    apt-get install -y net-tools iputils-ping tcpdump ethtool iperf iproute2 python3.8 python3-pip iputils-ping tcpdump

RUN pip install DateTime
RUN apt install -y libssl-dev python3-dev
# RUN pip install -e .
RUN pip install asgiref dnslib "flask<2.2" httpbin starlette "werkzeug<2.1" wsproto
RUN pip install aioquic

ADD net_applications home/net_applications