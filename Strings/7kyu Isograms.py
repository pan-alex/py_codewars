# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#
# Example: (Input --> Output)
#
# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)
#

# Make a dictionary for each letter in word that contains counts
# If any is > 1 then return false

def is_isogram(string):
    counts = {}
    for letter in string:
        if letter.lower() in counts:
            return False
        else:
            counts[letter.lower()] = 1
    return True


# More clever (cleverer?) solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))