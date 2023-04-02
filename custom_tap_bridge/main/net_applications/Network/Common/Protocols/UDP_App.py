import socket
from datetime import datetime
import time
import pickle
from Network.Data_Management.Data_Packet import Data_Packet
from Network.Data_Management.Data_Packet_Manager import DPM
from Network.Common.Definitions import Bind_Info

sock_params = Bind_Info()
PORT = sock_params.port
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = sock_params.server
sock_params.print_bind_info()


class udp_client:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.packet_count = 0
        self.packet = Data_Packet()
        self.pack_man = DPM()
        self.data_string = None
        
    def start_sending(self, plan_to_send = 10):
        # input_val = input()
        while self.packet_count < plan_to_send:
            self.pack_man.set_dp(self.packet)
            self.packet = self.pack_man.prepare_for_send(expected_to_send = plan_to_send)
            self.data_string = pickle.dumps(self.packet)
            self.pack_man.print_attributes()
            self.client.sendto(self.data_string, (SERVER, PORT))
            self.packet_count += 1
            # time.sleep(1)
        self.packet_count = 0


class udp_server:
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((SERVER, PORT))
        self.dpm = DPM()
    
    def turn_on_server(self):
        while True:
            dt_str, address = self.server.recvfrom(1024)
            packet = pickle.loads(dt_str)
            self.dpm.set_dp(packet)
            packet = self.dpm.prepare_after_receive()
            self.dpm.print_attributes()



    # while input_val != "EXIT":
    #     my_str = f"Hello Server {counter}!"
    #     client.sendto(my_str.encode('utf-8'), (SERVER, PORT))
    #     packet = client.recvfrom(1024)
    #     print(packet[0].decode('utf-8'))
    #     counter += 1
    #     print("CLIENT TIME: ", datetime.datetime.now())
    #     input_val = input()