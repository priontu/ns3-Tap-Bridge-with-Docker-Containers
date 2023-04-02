#!/bin/sh
lxc-stop -n left -k
lxc-stop -n right -k
ifconfig br-left down
ifconfig br-right down
lxc-destroy -n left
lxc-destroy -n right
brctl delif br-left tap-left
brctl delif br-right tap-right
brctl delbr br-left
brctl delbr br-right
ifconfig tap-left down
ifconfig tap-right down
tunctl -d tap-left
tunctl -d tap-right
