#!/bin/sh
docker build -t left main/
docker build -t right main/

# docker run --name left --network none --privileged -itd ramansingh1984/dweb-base:dweb-base-ubuntu
# docker run --name right --network none --privileged -itd ramansingh1984/dweb-base:dweb-base-ubuntu

docker run --network none --privileged -itd --name left left
docker run --network none --privileged -itd --name right right

pid_left=$(docker inspect --format '{{ .State.Pid }}' left)
pid_right=$(docker inspect --format '{{ .State.Pid }}' right)

sudo brctl addbr br-left
sudo brctl addbr br-right

sudo tunctl -t tap-left
sudo tunctl -t tap-right

sudo ifconfig tap-left 0.0.0.0 promisc up
sudo ifconfig tap-right 0.0.0.0 promisc up

sudo brctl addif br-left tap-left
sudo ifconfig br-left up
sudo brctl addif br-right tap-right
sudo ifconfig br-right up

pushd /proc/sys/net/bridge
for f in bridge-nf-*; do echo 0 > $f; done
popd

echo $pid_left
sudo mkdir -p /var/run/netns
sudo ln -s /proc/$pid_left/ns/net /var/run/netns/$pid_left

sudo ip link add internal-left type veth peer name external-left
sudo brctl addif br-left internal-left
sudo ip link set internal-left up

sudo ip link set external-left netns $pid_left

sudo ip netns exec $pid_left ip link set dev external-left name eth0
sudo ip netns exec $pid_left ip link set eth0 address 12:34:88:5D:61:BD
sudo ip netns exec $pid_left ip link set eth0 up
sudo ip netns exec $pid_left ip addr add 10.0.0.1/16 dev eth0

sudo ln -s /proc/$pid_right/ns/net /var/run/netns/$pid_right
sudo ip link add internal-right type veth peer name external-right
sudo brctl addif br-right internal-right
sudo ip link set internal-right up
sudo ip link set external-right netns $pid_right

sudo ip netns exec $pid_right ip link set dev external-right name eth0
sudo ip netns exec $pid_right ip link set eth0 address 5A:34:88:5D:61:BD
sudo ip netns exec $pid_right ip link set eth0 up
sudo ip netns exec $pid_right ip addr add 10.0.0.2/16 dev eth0

# sudo docker cp udp_client_server/client.py left:/home/
# sudo docker cp setup_sources.sh left:/home/
# sudo docker cp udp_client_server/server.py right:/home/
# sudo docker cp setup_sources.sh right:/home/

# sudo docker exec left /bin/bash -c "chmod +x home/setup_sources.sh"
# sudo docker exec right /bin/bash -c "chmod +x home/setup_sources.sh"

# sudo docker exec left /home/setup_sources.sh
# sudo docker exec right /home/setup_sources.sh