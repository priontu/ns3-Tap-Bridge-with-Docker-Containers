import socket
import threading
import datetime

PORT = 24
SERVER = socket.gethostbyname(socket.gethostname())
print("SERVER: ", SERVER)
print("PORT: ", PORT)
# SERVER = "172.29.46.232"

# print(SERVER)


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))

msg = ""
count = 0

while msg != "EXIT":
    message, address = server.recvfrom(1024)
    msg = message.decode('utf-8')
    print(msg)
    ret_msg = f"Hello Client {count}!"
    server.sendto(ret_msg.encode('utf-8'), address)
    print("SERVER TIME: ", datetime.datetime.now())
    count += 1

