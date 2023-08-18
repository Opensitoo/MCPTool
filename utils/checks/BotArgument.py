#!/usr/bin/python3

valid_arguments = ['yes', 'y', 'no', 'n']


def check_bot_argument(argument):
    """ 
    Check bot argument 
    
    :param argument: Bot Arguemnt
    :return: Boolean value that tells if the loop argument is valid
    """

    return argument in valid_arguments