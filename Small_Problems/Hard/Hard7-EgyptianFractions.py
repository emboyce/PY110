'''
increment the denominator
if adding with that denominator is less than the number, store it
if it's equal to the number, exit
if it's more than the number, move to the next denominator

'''

from fractions import Fraction

def egyptian(rational):
    denom = 1
    running_total = 0
    test_total = 0
    output = []

    while True:
        test_total = running_total + Fraction(1, denom)
        if test_total < rational:
            output.append(denom)
            running_total = test_total
            denom += 1
        elif test_total == rational:
            output.append(denom)
            return output
        else:
            denom += 1

def unegyptian(denominators):
    return sum([Fraction(1, denom) for denom in denominators])

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))