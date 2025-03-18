'''
input: count integer
output: difference between square of sum of first count integers, and 
sum of squares of first count integers
- all positive, no zero input, no large numbers

- helper function to sum numbers
    recursive:
        sum = (n) + (n-1) + (n-2) + ... 1
- helper function to sum number squares
        sum = (n)**2 + (n-1)**2 + ... 1

'''

def sum_numbers(num):
    if num == 1:
        return 1
    
    return num + sum_numbers(num - 1)

def sum_squares(num):
    if num == 1:
        return 1
    
    return num**2 + sum_squares(num - 1)

def sum_square_difference(num):
    return sum_numbers(num)**2 - sum_squares(num)


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True