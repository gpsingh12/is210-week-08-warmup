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
    lastnum, curnum = 0, 1
    list1 = [lastnum]
    while curnum < maxint:
        lastnum, curnum = curnum, lastnum + curnum
        list1.append(lastnum)
    return list1
