# Write Number in Expanded Form
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0.
#
# If you liked this kata, check out part 2!! https://www.codewars.com/kata/write-number-in-expanded-form-part-2


# P:
    # Convert to string
    # For each digit that is non-zero: count the number of digits behind it (length - index position) and add that
        # many 0s. Store result in array
    # Repeat for each digit and join with ' + '


def expanded_form(num):
    digits = str(num)
    expanded_array = []
    for i in range(len(digits)):
        if digits[i] != '0':
            expanded_array.append(digits[i] + '0' * (len(digits)-i-1))
    return ' + '.join(expanded_array)