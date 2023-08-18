#!/usr/bin/python3

import subprocess
import re
import os

from utils.managers.Settings import SettingsManager
from utils.checks.Encoding import check_encoding

sm = SettingsManager()
settings = sm.read('settings')

def nmap(target, ports, file):
    """ 
    Scan the specified target using Nmap 

    :param target: IP address
    :param ports: Ports Range
    :param file: Scan file
    :return: IP List
    """

    try:
        ip_list = []
        command = settings['NMAP_COMMAND'].replace('[0]', ports
                                         ).replace('[1]', file
                                         ).replace('[2]', target)

        subprocess.run(command, shell=True)

        with open(file, 'r', encoding=check_encoding(file)) as f:
            for line in f:
                ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)  # Search for an ip address in the line.
                ip = ' '.join(ip)
                ip = ip.replace('(', '').replace(')', '')

                port = re.findall('\d{1,5}\/tcp open', line)  # Search for an open port in the line.
                port = ' '.join(port)

                if not port:
                    if settings['SHOW_NMAP_FILTERED_PORTS']:
                        port = re.findall('\d{1,5}\/tcp filtered', line)
                        port = ' '.join(port)

                if '.' in ip:
                    current_ip = ip

                if 'tcp' in port:
                    port = port.replace('/tcp open', '').replace('/tcp filtered', '')
                    current_ip_backup = current_ip

                    try:
                        current_ip = current_ip.split(' ')
                        current_ip = current_ip[1]

                    except IndexError:
                        current_ip = current_ip_backup

                    ip_list.append(f'{current_ip}:{port}')

            return ip_list

    except KeyboardInterrupt:
        try:
            os.remove(file)

        except FileNotFoundError:
            pass

    return 'CtrlC'
