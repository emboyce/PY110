'''
P:
Input: a list of dictionaries, in which the keys are letters and the
    values are lists of integers
Output: a list of only the dictionaries in which all integers are even
Rules:
- only integers, no empty dictionaries, no empty integer lists
E:
- if any integer in any list in the whole dictionary is odd, skip that dictionary
D:
- a list of even dictionaries
A:
- iterate through each dictionary in the list
    - for each dictionary, check each value
        - for each value, check whether all items in the integer list are even
- add only dictionaries where all integers are even to the new list

- initialize an empty dictionary
- use a list comprehension that goes through the list of dictionaries (lst)
- add a dictionary if it is returned by an output function all_even()

- all_even function
    - input: dictionary
    - output: that dictionary, but only if all values of that dictionary
        contain only even items in the list
    - combine the lists of values for all items in that dictionary
        - use a nested comprehension num for num in list for list in dictionary
        - output num % 2 for each element
    - test whether all items in the resulting list are zero (even)
        use all(list)
    - if yes return that dictionary, if not return False
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_even(dict_):
    all_ints = [(num % 2) == 0 for int_list in dict_.values()
                    for num in int_list]
    if all(all_ints):
        return True
    else:
        return False

lst_output = [dict_ for dict_ in lst if all_even(dict_)]
print(lst_output)

print("q10")
'''
P:
Input: nothing
Output: a UUID string in the format 8-4-4-4-12 where each char is hexadecimal
E:
Rules: each char should be random
D:
- import random
- a list of strings of the specific length that will be connected by '-'
    into an output string

- construct a list by generating groups of random hex strings
    - initialize a list of desired string lengths
    - use a list constructor
    - iterate over a list of [8, 4, 4, 4, 12]
    - add hex chars * the integer to the output list
- create a helper function that takes an integer as an argument and
    returns an random character the number of times of that integer
    -  initialize an empty string
    - initialize a hexchar string
    - for count in range(0,int)
        - add a char from hexchar at a random index between 0 and len(hexchar)
    - return the string

'''
import random

def hexer(int_):
    output = ""
    hexchars = "0123456789abcdef"
    hexlength = len(hexchars)
    for count in range(0, int_):
        output += hexchars[random.randrange(0, hexlength)]
    return output

def uuid():
    int_list = [8, 4, 4, 4, 12]
    hex_list = [hexer(int_) for int_ in int_list]
    return("-".join(hex_list))

print(uuid())

print("q11")
'''
list of values
    list of lists of words
        for char in word
            if char in VOWELS, add char to list
'''
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = [char for lst_ in dict1.values()
                       if lst_[0] == "the"
                       for cell in lst_
                       if len(cell) > 3
                       for char in cell
                       if char in 'aeiou']
print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']