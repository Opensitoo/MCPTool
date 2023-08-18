#!/usr/bin/python3

import time

from utils.writefile.WriteFile import WriteFile
from utils.checks.Folder import check_folders

base = '''
################
# MCPTool Logs #
################

[>] General information

[#] Command: [0]
[#] Time and date: [1]

[>] Command information: 
[2]'''

save_server = '''
[IP] [0]
[MOTD] [1]
[Version] [2]
[Protocol] [3]
[Players] [4]/[5]
'''

save_server_with_bot = f'[Checker] [6]\n'

save_timed_out_server = '''
[TimedOut] [0]
'''

save_player = '[Player] [0]\n'
save_command = '[Player] [0] -> [1]'


class LogsManager:
    def __init__(self, command, file):
        self.command = command
        self.file = file

    def create(self, *data):
        check_folders('logs', f'logs/{self.command}')

        if self.command == 'checker':
            information = f'[#] File: {data[0]}\n'

        elif self.command == 'host':
            information = f'[#] Host: {data[0]}\n[#] Ports: {data[1]}\n[#] Scanning Method: {data[2]}\n'

        elif self.command == 'listening':
            information = f'[#] Server: {data[0]}\n\n'

        elif self.command == 'poisoning':
            information = f'[#] Server: {data[0]}\n\n[>] Captured commands:\n\n'

        elif self.command == 'rcon':
            information = f'[#] Server: {data[0]}\n[#]Password File: {data[1]}\n\n'

        elif self.command == 'scan':
            information = f'[#] Target: {data[0]}\n[#] Ports: {data[1]}\n[#] Scanning Method: {data[2]}\n'

        elif self.command == 'search':
            information = f'[#] Data: {data[0]}\n'

        logs = base.replace('[0]', self.command
                    ).replace('[1]', time.ctime()
                    ).replace('[2]', information)

        WriteFile(self.file, True, 'w+', logs)

    def write(self, type, *data):
        if type == 'save_command':
            information = save_command.replace('[0]', data[0]).replace('[1]', data[1])

        elif type == 'save_player':
            information = save_player.replace('[0]', data[0])
            information = information.replace('[lwhite]', '').replace('[lgreen]', '')

        elif type == 'save_server':
            information = save_server

            for num, i in enumerate(data):
                information = information.replace(f'[{str(num)}]', str(i))

        elif type == 'save_server_with_bot':
            for num, i in enumerate(data):
                information = save_server

                for num, i in enumerate(data):
                    information = information.replace(f'[{str(num)}]', str(i))

                information = f'{information}{save_server_with_bot.replace(f"[{str(num)}]", str(i))}'

        elif type == 'save_timed_out_server':
            information = save_timed_out_server.replace('[0]', data[0])

        WriteFile(self.file, False, 'a', information)