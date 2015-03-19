#!/usr/bin/env python 
# -*- coding: utf-8 -*
""" Fibonacci Sequence."""

def fibonacci(maxint):
    """Function generates a fibonacci sequence.
       Arg:
           maxint(int): Input value of the function. It is the upperbound
                        of while loop.
       Return:
            LIST(int): returns a list of integers called Fibonacci sequence.

        Examples:
                >>> fibonacci(10)
                    [0, 1, 1, 2, 3, 5, 8]
        
    """
    a, b = 0, 1
    LIST = [a]
    #print a
    while b < maxint:
        
        a, b = b, a + b
        
        LIST.append(a)
        #LIST.append(b)

    return LIST
    

