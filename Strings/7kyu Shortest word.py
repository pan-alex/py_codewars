# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.
def find_short(S):
    return min([len(s) for s in S.split(' ')])


# def find_short(s):
#     return min(map(len, s.split(' ')))