import socket
import datetime

PORT = 24
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER ="193.167.100.100"
counter = 0

print("Server: ", SERVER)
print("Port: ", PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_val = input()


while input_val != "EXIT":
    my_str = f"Hello Server {counter}!"
    client.sendto(my_str.encode('utf-8'), (SERVER, PORT))
    packet = client.recvfrom(1024)
    print(packet[0].decode('utf-8'))
    counter += 1
    print("CLIENT TIME: ", datetime.datetime.now())
    input_val = input()