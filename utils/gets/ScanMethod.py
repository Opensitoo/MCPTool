#!/usr/bin/python3


def get_scan_method(method):
    """  
    Returns the scan method. 

    This function is made to simplify the code since the user can enter 
    the method by numbers or by its respective name.

    :param method: Scan Method
    :return: Scan Method
    """

    if method in ['0', 'nmap']:
        return 'nmap'

    if method in ['1', 'qubo', 'quboscanner']:
        return 'quboscanner'

    #if method == '2' or method == 'masscan':
    #    return 'masscan'