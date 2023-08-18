#!/usr/bin/python3


def get_loop_argument(argument):
    """  
    Returns the scan method. 

    This function is made to simplify the code since the user can enter 
    the method by numbers or by its respective name.

    :param argument: Loop Argument
    :return: Boolean value that checks if it is positive
    """

    return argument in ['y', 'yes']