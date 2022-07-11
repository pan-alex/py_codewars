# A list S will be given. You need to generate a list T from it by following the given process:
#     Remove the first and last element from the list S and add them to the list T.
#     Reverse the list S
#     Repeat the process until list S gets emptied.
# The above process results in the depletion of the list S. Your task is to generate list T without mutating the input List S.
# Example
# S = [1,2,3,4,5,6])
# T = [])

# S = [2,3,4,5]) => [5,4,3,2])
# T = [1,6])

# S = [4,3]) => [3,4])
# T = [1,6,5,2])

# S = [])
# T = [1,6,5,2,3,4])
# return T

# Note
#
#     size of S goes up to 10^6
#     Keep the efficiency of your code in mind.
#     Do not mutate the Input.


# P:
    # Mutating s is not allowed... Is making a copy allowed?
from collections import deque

def arrange(s):
    q = deque(s)
    return [q.pop() if 0 < i%4 < 3 else q.popleft() for i in range(len(s))]


# Other approach:
    # Loop through S.
        # Add to T: S[0] and S[1]
            # Set "invert" to True
        # Add to T: S[1], S[-2]
            # Set "invert" to False
        # If S is odd length, create condition to add middle value as singleton

import math

def arrange(s):
    T = []
    mid = len(s) // 2
    invert = 1    # 1 => no invert; -1 => invert list
    for i in range(math.ceil(len(s)/2)):
        if i != mid or len(s) % 2 == 0:
            x = [s[i], s[-(i+1)]]
            if invert < 1:
                x.reverse()
            T += x
        else:
            T.append(s[i])
        invert *= -1
    return T


# Examples
arrange([1, 2]) # [1, 2])),
arrange([4, 3, 2]) # [4, 2, 3])),
arrange([9, 7, -2, 8, 5, -3, 6, 5, 1]) # [9, 1, 5, 7, -2, 6, -3, 8, 5])),
arrange([1]) # [1])),
arrange([]) # [])),
arrange([2, 4, 3, 4]) # [2, 4, 3, 4])),