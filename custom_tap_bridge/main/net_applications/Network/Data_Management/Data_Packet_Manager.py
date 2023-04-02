from datetime import datetime
from Network.Data_Management.Data_Packet import Data_Packet
import sys

class DPM:
    def __init__(self) -> None:
        self.dp = None
        self.id_count = -1
        self.received_packet_count = 0
    
    def check_setting(self, source = "Source Unknown"):
        if type(self.dp) is not Data_Packet:
            print(f"{source}: Incorrect Input -- Provide Object of Type: Data_Packet.")
            quit()
    
    def set_dp(self, dp: Data_Packet):
        self.dp = dp
        
    def increment_ID(self):
        self.check_setting(source = "increment_ID")
        self.id_count += 1
        self.dp.Packet_ID = self.id_count
        return self.dp.Packet_ID
        
    def record_send_time(self):
        self.check_setting(source = "record_send_time")
        self.dp.Send_Time = datetime.now()
        return self.dp.Send_Time
        
    def record_receive_time(self):
        self.check_setting(source = "record_receive_time")
        self.dp.Receive_Time = datetime.now()
        return self.dp.Receive_Time
        
    def calculate_delay(self):
        self.check_setting(source = "calculate_delay")
        if (self.dp.Receive_Time is None):
            print("Error: Receive Time Not Set!")
            quit()
        if (self.dp.Send_Time == None):
            print("Error: Send time Not Set!")
            quit()
        self.dp.Detected_Delay = self.dp.Receive_Time - self.dp.Send_Time
        return self.dp.Detected_Delay
    
    def set_expected_count(self, count):
        self.dp.Expected_Count = count
    
    def set_packet_size(self):
        self.dp.Packet_Size = sys.getsizeof(self.dp) # first set size
        self.dp.Packet_Size = sys.getsizeof(self.dp) # then get size with size set
    
    def set_received_packet_count(self):
        self.dp.Received_Packet_Count = self.received_packet_count
        
    def prepare_for_send(self, expected_to_send):
        # self.check_setting()
        self.increment_ID()
        self.record_send_time()
        self.set_expected_count(expected_to_send)
        self.set_packet_size()
        return self.dp
    
    def prepare_after_receive(self):
        # self.check_setting()
        self.record_receive_time()
        self.calculate_delay()
        self.id_count = self.dp.Packet_ID
        self.received_packet_count += 1
        self.set_received_packet_count()
        return self.dp
    
    def print_attributes(self):
        print("Packet_ID: ", self.dp.Packet_ID)
        print("Send Time: ", self.dp.Send_Time)
        print("Receive Time: ", self.dp.Receive_Time)
        print("Detected Delay: ", self.dp.Detected_Delay)
        print("Expected Count: ", self.dp.Expected_Count)
        print("Received_Packet_Count: ", self.dp.Received_Packet_Count )
        print("Packet Size: ", self.dp.Packet_Size)
        print(" ")
        
        
    
    
        
    
        
    