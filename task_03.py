#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring added"""

import decimal


def lexicographics(to_analyze):
    """Function calculates the max, min and average of the input string.
       Arg:
           to_analyze(str): the input value of the function.
           text(str):split the input string into new line.
           maxcount(int): maximum no. of words in input.
           mincount(int): minimum no. of words in input.
           average(Decimal): average of input.
        Return:
                returns a tuple containing maxcount, mincount and average.
        Examples:
                lexicographics('Do not stop believing,
                             Hold on to that feeling')
                    (5, 4, Decimal('4'))
    """

    text = to_analyze.split('\n')
    list1 = []
    for item in text:
        myvar = len(item.split())
        myvar1 = list1.append(myvar)
        maxcount = max(myvar1)
        mincount = min(myvar1)
        average = decimal.Decimal(sum(list1)/decimal.Decimal(len(text)))
    return maxcount, mincount, average
