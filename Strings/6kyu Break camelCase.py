# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
#
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""


def solution(s):
    return ''.join([' ' + letter if letter.isupper() else letter for letter in s])

# Regex solution
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

# def solution(s):
#     letterList = re.split(r'([A-Z])', s)
#     for i in range(len(letterList)):
#         if letterList[i].isupper(): letterList[i] = ' ' + letterList[i]
#     return ''.join(letterList)

