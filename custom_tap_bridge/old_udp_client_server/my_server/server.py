import socket
import threading
import datetime
import pickle
from Data_Packet_Manager.DPM import DPM
PORT = 24
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "10.0.0.2"

print("SERVER: ", SERVER)
print("PORT: ", PORT)
# SERVER = "172.29.46.232"

# print(SERVER)


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER, PORT))

msg = ""
count = 0

dpm = DPM()

while True:
    dt_str, address = server.recvfrom(1024)
    packet = pickle.loads(dt_str)
    dpm.set_dp(packet)
    packet = dpm.prepare_after_receive()
    dpm.print_attributes()
    
    

# while msg != "EXIT":
#     message, address = server.recvfrom(1024)
#     msg = message.decode('utf-8')
#     print(msg)
#     ret_msg = f"Hello Client {count}!"
#     server.sendto(ret_msg.encode('utf-8'), address)
#     print("SERVER TIME: ", datetime.datetime.now())
#     count += 1

