# https://www.codewars.com/kata/628e6f112324192c65cd8c97
# The target dose for the oral medication Katamol has been calculated: d (in mg).
#
# The only options to prescribe the medication are pills of strength a (in mg) or b (in mg), so it may not be possible to prescribe the exact target dose.
#
# For a given target dose d, return the highest possible dose that can be made with any amount of pills a and/or b that does not exceed the target dose.
#
# Input: List of 3 integers, d,a,b representing the calculated target dose, the dose of pill a, and the dose of pill b (all in mg)
#
# Output: Integer value of the closest dose to the target that can be made with any amount of pills a and/or b without going above the target dose.
#
# Example:
#
# Input:
# 99,25,60
# Output:
# 85
# # 85 can be made with 1 * 25mg pill and 1* 60mg pill, no closer dose can be made that is less than or equal to 99
#
# Constraints:
#
# a <= d
#
# 2 <=d <=10000
#
# 1 <= a < b <5000

# P: target dose (d) as an integer, available pill sizes (a, b) as integers
    # a will always be smaller or equal to d.
    # b will always be larger than a
    # d will be less than 10,000
# R: The highest dose that can be achieved using different combinations of a and b that does not exceed d

# P:
    # First thought is to do nested loops:
        # Use b as the starting dose: add b until it exceeds d and record highest value
            # Replace the last b with a's until it exceeds d and record highest value
            # Decrease b's with each loop until there is only 1.
        # Next use a as starting dose and repeat above.

def prescribe(d,a,b):
    record = 0
    n_b = d // b    # Number of times b can fit into d
    n_a = d // a    # Number of times a can fit into d
    for i in range(0, n_b+1):
        for j in range(0, n_a+1):
            test_val = i*b + j*a
            print(f'{test_val} from i: {i} and j: {j}')
            if test_val > d:
                break
            elif test_val > record:
                record = test_val
    return record


def prescribe(d,a,b):
    return max(b*i + a*(d - b*i//a) for i in range(d//b+1))


# E:
prescribe(180,25,60)    # 180; 3x60
prescribe(99,25,40)    # 90; 1x40 + 2x25
prescribe(99,32,40)    # 96; 3x32
prescribe(99,25,60)    # 85; 1x60 + 1x25
prescribe(2575,400, 150)    # 2550; Can be made 3 different ways
prescribe(4540,9,15)    # 4539; 1x4539
prescribe(150,130,200)    # 4539; 1x4539


