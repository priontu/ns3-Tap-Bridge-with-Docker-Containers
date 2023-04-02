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

class tcp_client:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.packet_count = 0
        self.packet = Data_Packet()
        self.pack_man = DPM()
        self.data_string = None
        self.connection_established = False
        
    def start_client(self):
        self.client.connect((SERVER, PORT))
        self.connection_established = True
        
        # self.client.send("Hello Server!".encode('utf-8'))
        
  
  
    def start_sending(self, plan_to_send = 10):
        if self.connection_established == False:
            self.start_client()
            
        while self.packet_count < plan_to_send:
            self.pack_man.set_dp(self.packet)
            self.packet = self.pack_man.prepare_for_send(plan_to_send)
            self.data_string = pickle.dumps(self.packet)
            self.pack_man.print_attributes()
            self.client.send(self.data_string)
            self.packet_count += 1
            # time.sleep(1)
            
        self.packet_count = 0
    
class tcp_server:
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((SERVER, PORT)) 
        self.server.listen()
        self.dpm = DPM()
        self.client, address = self.server.accept()
        print(f"Connected to {address}")
    
    def turn_on_server(self):
        while True:
            # print(client.recv(1024).decode('utf-8'))
            data_string = self.client.recv(1024)
            # print("Done upto here!")
            packet = pickle.loads(data_string)
            self.dpm.set_dp(packet)
            packet = self.dpm.prepare_after_receive()
            self.dpm.print_attributes()
            
            if (packet.Received_Packet_Count >= packet.Expected_Count):
                break     
        
        self.client.close()
            
        