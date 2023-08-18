#!/usr/bin/python3


def check_domain(server):
    """ 
    Check if the entered server is a domain. Otherwise it is an IP address 
    
    :param server: Minecraft Server
    :return: Returns true if the server is a domain, false if it is an IP address.
    """

    return any(not i.isdigit() and i != ':' and i != '.' for i in server)
