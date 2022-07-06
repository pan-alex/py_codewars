# Task
#
# Imagine that you are standing near a lake and watching frog John trying to get to the other bank. You can see some stones in front of him, and you know that John can make short jumps and long jumps. But that's not it. You also know that John is a magic frog: he is afraid of water, so he can cross the lake only by stones. Luckily, he can understand your words. Can you help him to get to the other side of lake?
#
# You are given an array with coordinates of the stones ahead of John. Initially John is standing on a stone with coordinate 0. If he stands on a stone with coordinate x, he can jump to the stones with coordinates x + 1 (make a short jump), or x + 2 (make a long jump).
#
# Find the shortest path to the other side (to the last stone) and return the sequence of '1's and '2's, where '1' is a short jump and '2' is a long one. If there are several answers, return lexicographically smallest.
#
# String A is lexicographically smaller than string B either if A is a prefix of B (and A ≠ B), or if there exists such index i (0 ≤ i < min(x.length, y.length)), that Ai < Bi, and for any j (0 ≤ j < i) Aj = Bj. The lexicographic comparison of strings is implemented by operator < in modern programming languages.
# Input/Output
#
#     [input] integer array stones
#
# A sorted array of stones' coordinates. It is guaranteed that stones[0] = 0.
#
#     [output] a string
#
# A sequence of '1's and '2's describing the shortest path to the other bank. It's guaranteed that the answer exists.

def frogs_jumping(stones):
    path = ''
    i = len(stones) - 1    # Distance remaining, by index position
    while i > 0:
        # Do a 2-stone jump if:
        # distance > 1, and the distance between the current stone and 2nd closest stone is 2
        if i > 1 and (stones[i] - stones[i - 2]) == 2:
            dist = i_jump = 2    # i_jump is number of index positions to advance
        else:
            i_jump = 1
            # dist must be 1 or 2 as a solution is guaranteed
            dist = stones[i] - stones[i-1]
        i -= i_jump
        path += str(dist)
    return path[::-1]


# Example:
# For stones = [0,1,2,3,5,6], the output should be "1221".
# Here are all possible paths:
# "11121", not the shortest one;
# "2121", one of the shortest ones, but not the lexicographically smallest;
# "1221", the shortest and the lexicographically smallest.

frogs_jumping([0,1,2,3,5,6]) #, '1221'
frogs_jumping([0,2,4,6])# '222')
frogs_jumping([0,1,2,3])#'12')
frogs_jumping([0,1,2,3,4,5,6,7,9,10,11,13,15,16,17])#'122222222')
frogs_jumping([0,2,4,6,7,8,10,11,13,15,17,19,20,21,23])#'222221222222')
