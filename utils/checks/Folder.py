#!/usr/bin/python3

import os


def check_folders(*folders):
    """ 
    Check if the following folders exist

    :param *folders: Folders 
    """

    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)
