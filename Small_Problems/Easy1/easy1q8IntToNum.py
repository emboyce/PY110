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
    - match...case
- remove digit from string. integer is complete when string is gone
    - could also do this with a list
'''
def value(digit, tens_count):
    match digit:
        case "1":
            return 1 * tens_count
        case "2":
            return 2 * tens_count
        case "3":
            return 3 * tens_count
        case "4":
            return 4 * tens_count
        case "5":
            return 5 * tens_count
        case "6":
            return 6 * tens_count
        case "7":
            return 7 * tens_count
        case "8":
            return 8 * tens_count
        case "9":
            return 9 * tens_count
        case "0":
            return 0 * tens_count
        case _:
            print("Error - not a digit")


def string_to_integer(string):
    tens_count = 1
    int_total = 0
    while len(string) > 0:
        digit = string[-1]
        int_total = int_total + value(digit, tens_count)
        string = string[0:-1]
        tens_count *= 10
    return int_total



print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True