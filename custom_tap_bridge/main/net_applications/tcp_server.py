from Network.Common.Protocols.TCP_App import tcp_server

if __name__=="__main__":
    tcp_serv = tcp_server()
    tcp_serv.turn_on_server()