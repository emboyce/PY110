
def string_to_signed_integer(string):
    total = 0
    lookup = {str(num):num for num in range(0, 10)}

    for index, digit in enumerate(string[::-1]):
        if digit == "+":
            continue
        elif digit == "-":
            total *= -1
        else:
            total += lookup[digit] * 10**(index)
    
    return total





print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

'''
4321
4 x 10^3, index is 1, len is 4 (len - index + 1)
3 x 10^2, index is 3, len is 4`
2 x 10^0, index is 2, len is 4 
'''