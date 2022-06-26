# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
#
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# P: String of words separated by '_' or '-'. Characters may be upper case or lower case. Input
# may be ''
# R:
    # Convert the string to camel case.
    # If the first character is uppercase, then retain it as uppercase.
    # If the string is empty, return an empty string
# P:
    # Check if string is empty and return empty string if so.
    # Split the string into list of words.
        # Make the first character of each word uppercase
        # Except for the first word: check if the input string is uppercase or lowercase

import re

def to_camel_case(text):
    if text == '': return ''
    words = re.split('-|_', text)
    camelCase = [words[0]] + [word[0].upper() + word[1:] for word in words[1:]]
    return ''.join(camelCase)


#:
to_camel_case('') # ''
to_camel_case("the_stealth_warrior") #, "theStealthWarrior",
to_camel_case("The-Stealth-Warrior") #, "TheStealthWarrior",
to_camel_case("A-B-C") #, "ABC"