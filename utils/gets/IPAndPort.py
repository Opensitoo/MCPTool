#!/usr/bin/python3

# This script gets the ip address and port of the 
# specified minecraft server.

from utils.minecraftserver.ServerData import mcsrvstatus


def get_ip_port(server):
    """ 
    Get only ip and port of the server 
    
    :param server: Server domain
    :return: IP and Port or None
    """

    data = mcsrvstatus(server)

    return (data[0], data[1]) if data is not None else (None, None)