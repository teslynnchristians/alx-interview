#!/usr/bin/python3

"""
    Determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        Function that calculates the fewest number of operations
        needed to give the result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
