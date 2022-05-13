# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):
    if len(s) % 2 != 0: s += '_'
    output = []
    i=0
    while i < len(s):
        output.append(s[i:i+2])
        i += 2
    return output



solution("asdfadsf")   #['as', 'df', 'ad', 'sf']),
solution("asdfads")    #['as', 'df', 'ad', 's_']),
solution("")    #[]