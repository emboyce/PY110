'''//You are asked to square every digit of a number.
// For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

/*
P
Given an integer, return a new integer with each digit squared

E
- each digit must be sqaured
- the return value is an integer
- all inputs are non-negative integers
- the biggest number we need to deal with is 99999999

D
I: integer
O: integer

Intermediate:
  - string: to convert from an integer to a series of digits, int = 123, str = '123', lst/arr = ['1', '2', '3']
  - list: of individual digits

A
High-level strategies
Caroline: split the integer into digits, square them, recombine into an integer

- split the integer into digits
    - convert the integer to a string
        - initialize a str_num variable
        - use the str() Python function
    - initialize a new list (digit_list)
    - iterate through the list
    - assign each string digit (str_digit) of the string number (str_num) to an element in the list
        - use a list comprehension
        - for each str_digit in str_num, assign as-is to list
            - can optionally wrap the conversion of the integer to a string into this list comprehension
- square each digit
    - initialize a new list (sqr_int_digit)
    - iterate through each digit in the new list (digit_list)
    - assign the square of the integer conversion of each digit (int_digit)*(int_digit) to a new list
- recombine the digits into an integer
    - initialize a new list (sqr_str_digit)
    - convert each squared int digit back to a string
    - combine the str digits back to a single string
    - convert that string back to an integer
- return the resulting integer


- create a list of the squared string values of the string conversion of the integer
    - convert the string digits to integers before squaring
    - then convert back to a string before storing in list
- recombine the list back into a single string
- convert that string to an integer
- return the integer


*/
'''
def square_digits(num):
    squared_list = [ str(int(digit)**2) for digit in str(num)]
    digits_squared = "".join(squared_list)
    return int(digits_squared)

print(square_digits(0) ==    0)
print(square_digits(64) ==   3616)
print(square_digits(1111) == 1111)
print(square_digits(2222) == 4444)
print(square_digits(3333) == 9999)
print(square_digits(3212) == 9414)
print(square_digits(1234) == 14916)
print(square_digits(77455754) == 4949162525492516)
print(square_digits(99999999) == 8181818181818181)