# Write a method which takes an array of integers (positive and negative) and returns the longest contiguous sequence in this array, which total sum of elements equal 0.
#
# For example:
# maxZeroSequenceLength([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, -7, 2, -9, 16, 2, -11])
#
# Should return [92, -115, 17, 2, 2, 2], because this is the longest zero-sum sequence in the array.

# Start with entire list and search smaller lists via nested loops:
# Loop 1: for each element left -> right
# Loop 2: for each element right -> left
# Check if sum is 0. If yes, check if longest

from operator import add
from functools import reduce

def max_zero_sequence(arr):
    longest = []
    for i in range(len(arr)):    # Start from first
        for j in range(len(arr[i:]), 0, -1):    # Start from last
            if len(arr[i:j]) > 0 and reduce(add, arr[i:j]) == 0 and len(arr[i:j]) > len(longest):
                longest = arr[i:j]
                break
    return longest


max_zero_sequence([1, -2, 1])
max_zero_sequence([1, -2, 1, 12])
max_zero_sequence([4, 1, -2, 1, 12])
max_zero_sequence([25, -35, 12, 6, 92, -115, 17, 2, 2, 2, -7, 2, -9, 16, 2, -11])