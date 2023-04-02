FROM ubuntu:20.04



# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal main restricted universe multiverse" > /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-security main restricted universe multiverse" >> /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-updates main restricted universe multiverse" >> /etc/apt/sources.list
# # RUN echo "deb http://mirror-osd.de.bosch.com/osd focal main" >> /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/partner focal partner" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y apt-transport-https

# RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf
# RUN echo "nameserver 8.8.4.4" > /etc/reolv.conf

RUN apt-get update && \
    apt-get install -y net-tools iputils-ping tcpdump ethtool iperf iproute2 python3.8 python3-pip iputils-ping tcpdump

# RUN pip install numpy
# RUN pip install --no-cache-dir DateTime==4.8
# RUN apt-get update && apt-get install -y python-zope.datetime

# COPY DateTime-5.1.tar.gz home/
# # RUN chmod -R a+rwx home/
# # RUN tar xvf home/DateTime-5.1.tar.gz -C home/
# # RUN chmod -R a+rwx home/DateTime-5.1/src
# # RUN python3 home/DateTime-5.1/setup.py install
RUN pip install DateTime
COPY client.py home/