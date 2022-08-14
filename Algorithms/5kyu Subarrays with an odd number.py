# Task
#
# Implement a function which takes an array of nonnegative integers and returns the number of subarrays with an odd number of odd numbers. Note, a subarray is a contiguous subsequence.

# Example
## Consider an input:
# # [1, 2, 3, 4, 5]) #
#
# The subarrays containing an odd number of odd numbers are the following:
# # [1, 2, 3, 4, 5]) #, [2, 3, 4]) #, [1, 2]) #, [2, 3]) #, [3, 4]) #, [4, 5]) #, [1]) #, [3]) #, [5]) #
#
# The expected output is therefore 9.
# Test suite
# # 100 random tests, with small arrays, 5 <= size <= 200, testing the correctness of the solution.
# # 10 performance tests, with arrays of size 200 000.
# # The expected output for an empty array is 0, otherwise the content of the arrays are always integers k such that 0 <= k <= 10000.
# # Expected time complexity is O(n)


# Enumerate every possible set of sequences... somehow
    # Loop through all and filter out even numbers. Check if length is odd. If yes, increment
# counter


# Currently unsolved; not optimized for very large (length = 200,000) arrays
import itertools

def solve(arr):
    subarrays = [arr[s:e] for s, e in itertools.combinations(range(len(arr)+1), 2)]
    count = 0
    for subarray in subarrays:
        count += len( list(filter(lambda x: x % 2 != 0, subarray)) ) % 2 != 0
    return count



# Examples
solve([]) #, 0),
solve([0]) #, 0),
solve([1]) #, 1),
solve([1, 1]) #, 2),
solve([2, 2]) #, 0),
solve([1, 1, 1]) #, 4),
solve([2, 1, 1]) #, 3),
solve([1, 2, 1]) #, 4),
solve([1, 1, 1, 1]) #, 6),
solve([1, 2, 1, 2, 1]) #, 9),
solve([1, 2, 3, 3, 2, 1]) #, 12),
solve([2, 3, 5, 5, 6, 8, 9, 1]) #, 20)
