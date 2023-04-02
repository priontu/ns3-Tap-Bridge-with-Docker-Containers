from Network.Common.Protocols.UDP_App import udp_client

if __name__=="__main__":
    udp_cl = udp_client()
    udp_cl.start_sending()