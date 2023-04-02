sudo echo "deb http://mirror-osd.de.bosch.com/ubuntu focal main restricted universe multiverse" > /etc/apt/sources.list
sudo echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-security main restricted universe multiverse" >> /etc/apt/sources.list
sudo echo "deb http://mirror-osd.de.bosch.com/ubuntu focal-updates main restricted universe multiverse" >> /etc/apt/sources.list
# RUN echo "deb http://mirror-osd.de.bosch.com/osd focal main" >> /etc/apt/sources.list
sudo echo "deb http://mirror-osd.de.bosch.com/partner focal partner" >> /etc/apt/sources.list