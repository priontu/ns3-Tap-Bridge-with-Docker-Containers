import socket

class Bind_Info:
    def __init__(self) -> None:
        try:
            SERVER = socket.gethostbyname(socket.gethostname())
        except:
            SERVER = "10.0.0.2"
            
        self.server = SERVER
        self.port = 5050
    
    def print_bind_info(self):
        print("SERVER: ", self.server)
        print("PORT: ", self.port)