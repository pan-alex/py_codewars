# Write a function insert_dash(num) that will insert dashes ('-') between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd digit.
#
# Note that the number will always be non-negative (>= 0).

# Loop over each digit. If the present digit + the next digit are odd, insert a -.
#

def insert_dash(num):
    num = list(str(num))
    odd = ['1', '3', '5', '7', '9']
    i = 1
    while i < len(num):
        if num[i-1] in odd and num[i] in odd:
            num.insert(i, '-')
            i -= 1
        i+= 1
    return ''.join(num)

# Alternative solution includes checking each digit and appending it to a new list. If there are 2 odds in a row then append a dash in between.

# Also a fancier solution
import re
def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))