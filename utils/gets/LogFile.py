#!/usr/bin/python3

from utils.checks.Folder import check_folders
from datetime import datetime


def create_file(command):
    """
    Create the file that will be used to store data

    :param command: Command name
    :return: File address
    """

    date = datetime.now()
    t = f'{date.day}-{date.month}-{date.year}_{date.hour}.{date.minute}.{date.second}'

    check_folders('logs', f'logs/{command}')
    return f'logs/{command}/{command.capitalize()}_{t}.txt'