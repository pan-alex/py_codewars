# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# Examples
# Valid arrays
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
#
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
#
# Invalid arrays
#
# If, for example, we change the first number to something else, comp is not returning true anymore:
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
#
# comp(a,b) returns false because in b 132 is not the square of any number of a.
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
#
# comp(a,b) returns false because in b 36100 is not the square of any number of a.
# Remarks
#
#     a or b might be [] or {} (all languages except R, Shell).
#     a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
#
# If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.
# Note for C
#
# The two arrays have the same size (> 0) given as parameter in function comp.


# P: 2 lists, a and b, containing numbers.
    # The numbers may be negative
    # Numbers may be repeated
# R:
    # Compare the contents of the two lists, and:
        # If a and b are "the same" return true
        # If not return false
        # "the same" means that the elements in b are equal to a**2, regardless of order
        # If either are None return false

# P:
    # Check that lists are not None
    # For each element in A (a), check that a*a is present in B. If so, remove that element from B and continue.

def comp(A, B):
    if None in (A, B): return False
    for a in A:
        if a**2 not in B: return False
        B.remove(a**2)
    return True


# More elegant solution
def comp(A, B):
    try:
        return sorted([i ** 2 for i in A]) == sorted(B)
    except:
        return False

# E:
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
comp(a1, a2) # True
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
comp(a1, a2) # False (first element is not 11**2
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
comp(a1, a2) # False (190**2 is not in a1. And 19*19 appears 3 times in a1 and only 2 times in a2)