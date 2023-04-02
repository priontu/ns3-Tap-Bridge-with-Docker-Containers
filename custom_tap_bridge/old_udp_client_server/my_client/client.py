import socket
from datetime import datetime, time
import pickle
from Data_Packet_Manager.Data_Packet import Data_Packet
from Data_Packet_Manager.DPM import DPM

PORT = 24
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER ="10.0.0.2"
counter = 0

if __name__ == "__main__":
    print("Server: ", SERVER)
    print("Port: ", PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # input_val = input()
    packet_count = 0
    while packet_count < 10:
        packet = Data_Packet()
        pack_man = DPM()
        
        pack_man.set_dp(packet)
        packet = pack_man.prepare_for_send()
        data_string = pickle.dumps(packet)
        
        client.sendto(data_string.encode('utf-8'), (SERVER, PORT))
        time.sleep(1)


    # while input_val != "EXIT":
    #     my_str = f"Hello Server {counter}!"
    #     client.sendto(my_str.encode('utf-8'), (SERVER, PORT))
    #     packet = client.recvfrom(1024)
    #     print(packet[0].decode('utf-8'))
    #     counter += 1
    #     print("CLIENT TIME: ", datetime.datetime.now())
    #     input_val = input()