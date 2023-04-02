import socket
import threading
import datetime
import pickle
from Network.Common.Protocols.UDP_App import udp_server

if __name__=="__main__":
    udp_serv = udp_server()
    udp_serv.turn_on_server()
    
    
    

# while msg != "EXIT":
#     message, address = server.recvfrom(1024)
#     msg = message.decode('utf-8')
#     print(msg)
#     ret_msg = f"Hello Client {count}!"
#     server.sendto(ret_msg.encode('utf-8'), address)
#     print("SERVER TIME: ", datetime.datetime.now())
#     count += 1

