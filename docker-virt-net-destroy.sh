ip link set br-left down
ip link set br-right down
sudo brctl delif br-left tap-left
sudo brctl delif br-right tap-right
brctl delbr br-left
brctl delbr br-right

sudo ifconfig tap-left down
sudo ifconfig tap-right down
sudo tunctl -d tap-left
sudo tunctl -d tap-right

ip link delete tap-left
ip link delete tap-right

ip link delete internal-left
ip link right internal-right

docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)

docker container ls -a