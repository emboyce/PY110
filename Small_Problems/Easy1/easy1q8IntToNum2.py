'''
P/E:
- input: a string of digits
- output: an integer numbr
Rules explicit:
- may not use any standard conversion functions
- don't worry about leading + or - signs
- assume all characters are numeric
Rules implicit:
- all integers are positive

D/A:
- data: 
    - counter to track integer position
    - integer running total
- for each digit, use the digit's position in the string to know what
power of ten we are multiplying by
    - 1, 10, 100...x10 each time
- then lookup the corresponding integer to multiply by, based on the
string value
    - create a dictionary with range
- remove digit from string. integer is complete when string is gone
'''

def string_to_integer(string):
    lookup = {str(num):num for num in range(0, 10)}
    tens_count = 1
    int_total = 0
    while len(string) > 0:
        digit = string[-1]
        int_total = int_total + tens_count*lookup[digit]
        string = string[0:-1]
        tens_count *= 10
    return int_total



print(string_to_integer("432991") == 432991)  # True
print(string_to_integer("570") == 570)    # True