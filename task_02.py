#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Module defining a function using
    simple if else statement
"""




def bool_to_str(bval):
    """Function takes one argument.
       Uses if else statement to return
       a string.
       Arg:
           bval(boolean): argument is assigned a boolean True value.
       Return:
           var(str): returns a string Yes if bval is True, otherwise
                     No.

        Examples:
                >>> bool_to_str(True)
                    'Yes'
                >>> bool_to_str(False)
                    'No'
    """

    bval == True
    if bval:
       var = 'Yes'
    else:
       var = 'No'

    return var
