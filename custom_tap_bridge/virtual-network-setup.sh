#!/bin/sh
brctl addbr br-left
brctl addbr br-right
tunctl -t tap-left
tunctl -t tap-right
ifconfig tap-left 0.0.0.0 promisc up
ifconfig tap-right 0.0.0.0 promisc up
brctl addif br-left tap-left
ifconfig br-left up
brctl addif br-right tap-right
ifconfig br-right up
# Note:  you also need to have loaded br_netfilter module
# ('modprobe br_netfilter') to enable /proc/sys/net/bridge
# pushd /proc/sys/net/bridge
# for f in bridge-nf-*; do echo 0 > $f; done
# popd

# lxc-create now requires a template parameter, such as '-t ubuntu'
# lxc-create -n left -t ubuntu -f lxc-left.conf
# lxc-create -n right -t ubuntu -f lxc-right.conf

lxc-create -f lxc-left.conf -t download -n left -- -d fedora -r 36 -a amd64
lxc-create -f lxc-right.conf -t download -n right -- -d fedora -r 36 -a amd64

lxc file push -r udp_client_server/ left/
lxc file push -r udp_client_server/ right/
# Start both containers
# sudo chroot /var/lib/lxc/left/rootfs passwd
lxc-start -n left -d
lxc-start -n right -d

# for veth in $(ifconfig | grep "^veth" | cut -d' ' -f1)
# do
#     ifconfig $veth down
# done

echo "Container information:"
echo " "
lxc-ls -f
echo " "
echo "Network information:"
echo " "
brctl show
echo " "

#####################################
## Good to know for inside container:
# ip link show
# ip addr show dev eth0
# ip addr add 10.0.0.1/24 dev eth0
#####################################

## Following used for deletig veth -- don't use:

# echo "Deleting the following veth interfaces:"
# for veth in $(ip a | grep veth | cut -d' ' -f 2 | rev | cut -c2- | rev | cut -d '@' -f 1 )
# do
    
#     echo $veth
#     ip link set $veth down
#     ip link delete $veth  
# done
# echo "Container information:"
# echo " "
# lxc-ls -f
# echo " "
# echo "Network information:"
# echo " "
# brctl show
# echo " "
# ifconfig | grep "^veth" | cut -d' ' -f1

# ip addr add 10.0.0.1/24 dev eth0
