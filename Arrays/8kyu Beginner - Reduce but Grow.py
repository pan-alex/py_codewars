# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
#
import functools
import operator

def grow(arr):
    return functools.reduce(operator.mul, arr)