# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    numbers = [n for n in numbers if n >= 0]
    smallest = []
    for i in range(2):
        smallest.append(numbers.pop(numbers.index(min(numbers))))

    return sum(smallest)


def sum_two_smallest_numbers(numbers):
    numbers = [n for n in numbers if n >= 0]
    return sum(sorted(numbers)[:2])
