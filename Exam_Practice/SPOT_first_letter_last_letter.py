'''
Write a function that accepts a string and outputs a list of strings.  The first string in the output list should be the concatenation of the first and last letter of the string.  Each subsequent string should 'move inwards' towards the center of the string.  

See the tests for more context and ask questions as necessary.

P:
input: string of arbitrary length
output: list of string pairs, containing the first and last letter of the string
Rules:
Explicit:
- None
Implicit:
- extra middle characters are included last and not paired
- no non-alpha strings, no integers, no leading or trailing spaces, case insensitive
E:
'lorem ipsum'
str[0] + str[-1] "lm"
str[1] + str[-2] "ou
...
str[4] + str[-5] "mi"
len(str) = 11
len(str) // 2 = 5
first index going up is zero, last index going up is len(str) // 2 - 1
down index is (-up_index - 1)
if len str is odd, add one extra string to list for middle character

D:
list of strings
input string

A:
- initialize an empty list of strings
- determine the length of the input string
- determine the middle index if any length // 2
- add indices of string to the list
    - for up_index in range (0, len(str) // 2) and 
        down_index = -up_index - 1)
        mini string = combined strings at above indices
    - add mini string to list of strings
    - add string at middle index to the list of strings
- return the list of strings

? - can I iterate over two ranges at once?
-> No
'''

def either_end(string):
    str_list = []
    length = len(string)
    if length % 2 != 0:
        middle_index = length // 2
    else:
        middle_index = False

    for index in range(0, length // 2):
        element = string[index] + string[-index - 1]
        str_list.append(element)

    if middle_index:
        str_list.append(string[middle_index])

    print(str_list)
    return str_list


# TESTS
string = 'lorem ipsum'
print(either_end(string) == ['lm', 'ou', 'rs', 'ep', 'mi', ' '])

string = 'helloworld'
print(either_end(string) == ['hd', 'el', 'lr', 'lo', 'ow'])
