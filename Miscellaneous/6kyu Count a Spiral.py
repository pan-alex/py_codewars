# Your task is to return the amount of white rectangles in a NxN spiral. Your font may differ, if we talk of white rectangles, we talk about the symboles in the top row.
# Notes:
#
#     As a general rule, the white snake cannot touch itself.
#     The size will be at least 5.
#     The test cases get very large, it is not feasible to calculate the solution with a loop.
#
# Examples
#
# For example, a spiral with size 5 should look like this:
#
# ⬜⬜⬜⬜⬜
# ⬛⬛⬛⬛⬜
# ⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜
#
# And return the value 17 because the total amount of white rectangles is 17.
#
# A spiral with the size 7 would look like this:
#
# ⬜⬜⬜⬜⬜⬜⬜
# ⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜
#
# And return the value 31 because the total amount of white rectangles is 31.
#
# A spiral with the size 8 would look like this:
#
# ⬜⬜⬜⬜⬜⬜⬜⬜
# ⬛⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜⬜
#
# And return the value 39 because the total amount of white rectangles is 39.
#
# A spiral with the size 9 would look like this:
#
# ⬜⬜⬜⬜⬜⬜⬜⬜⬜
# ⬛⬛⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬛⬜⬛⬜
# ⬜⬛⬜⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜⬜⬜
#
# And return the value 49 because the total amount of white rectangles is 49.
#
# A spiral with the size 10 would look like this:
#
# ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
# ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬜⬛⬜⬛⬜
# ⬜⬛⬜⬛⬛⬜⬛⬜⬛⬜
# ⬜⬛⬜⬛⬛⬛⬛⬜⬛⬜
# ⬜⬛⬜⬜⬜⬜⬜⬜⬛⬜
# ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜
# ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#
# And return the value 59 because the total amount of white rectangles is 59.


# P:
    # The number of squares in the spiral corresponds to the sum of squares in the rings (but
    # alternating).
    # This rule applies for all rings except for the inner 1-2 rings.
        # If there is a ring of size 1x1, then it can be counted as 1 white square.
        # If the innermost ring (that is counted) is bigger than 1x1, it is counter as perimeter -1.
    # E.g., for size 5:
        # Ring 3 (outermost): 16 squares
        # Ring 2: 0
        # Ring 1: 1



def count_squares_in_perimeter(ring):
    if ring == 1: squares = 1
    elif ring <= 4: squares =(ring - 1) * 4 - 1    # eliminate 2x2 squares
    else: squares = (ring - 1) * 4    # if ring is bigger than 2, then it is not the last ring
    return squares


def spiral_sum(size):
    squares = 0
    # Each ring is 2 less than the previous one, and only count every other ring, so -4
    for ring in range(size, 0, -4):
        squares += count_squares_in_perimeter(ring)
    return squares

for size in range(500, 550):
    print(spiral_sum(size))


# The code above works but fails for extremely large numbers.
# Converting the above into an equation...

# Decided to run the pattern through a pattern detector and found the solution: OEIS A047838
def spiral_sum(size):
    return (size + 1)**2 // 2 - 1