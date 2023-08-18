#!/usr/bin/python3

import subprocess
import time

from utils.minecraftserver.ServerData import mcstatus
from utils.managers.Settings import SettingsManager
from utils.gets.LoopArgument import get_loop_argument
from utils.gets.Language import language
from utils.color.TextColor import paint

sm = SettingsManager()
settings = sm.read('settings')


def kick_command(server, username, version, loop, proxy=None):
    """
    This command sends a bot with the specified name to 
    try to kick the player.

    :param server: IP address and port of the server
    :param username: Username that the bot will have
    :param version: Minecraft server version
    :param proxy: In the event that a user has entered a proxy, the bot will connect to the proxy.
    """

    try:
        if mcstatus(server) is None:
            paint(f'\n    {language["script"]["PREFIX"]}{language["commands"]["kick"]["INVALID_SERVER"]}')
            return

        paint(f'\n    {language["script"]["PREFIX"]}{language["commands"]["kick"]["STARTING_THE_ATTACK"]}')
        loop = get_loop_argument(loop)
        server = server.split(':')

        if loop:
            while True:
                time.sleep(4)

                if proxy is None:
                    subprocess.run(f'{settings["NODE_COMMAND"]} utils/scripts/Kick.js {server[0]} {server[1]} {username} {version} {settings["LANGUAGE"]}', shell=True)

                else:
                    proxy = proxy.split(':')
                    subprocess.run(f'{settings["NODE_COMMAND"]} utils/scripts/Kick.js {server[0]} {server[1]} {username} {version} {settings["LANGUAGE"]} {proxy[0]} {proxy[1]}', shell=True)

        elif proxy is not None:
            proxy = proxy.split(':')
            subprocess.run(f'{settings["NODE_COMMAND"]} utils/scripts/Kick.js {server[0]} {server[1]} {username} {version} {settings["LANGUAGE"]} {proxy[0]} {proxy[1]}', shell=True)

        else:
            subprocess.run(f'{settings["NODE_COMMAND"]} utils/scripts/Kick.js {server[0]} {server[1]} {username} {version} {settings["LANGUAGE"]}', shell=True)

    except KeyboardInterrupt:
        return