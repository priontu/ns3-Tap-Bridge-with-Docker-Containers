from Network.Common.Protocols.TCP_App import tcp_client
if __name__=="__main__":
        tcp_cl = tcp_client()
        tcp_cl.start_client()
        tcp_cl.start_sending()