print("q1")

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

# variable scope and mutation - integers are immutable

print("q2")

'''
The problem here is that we are reassigning the string variable while 
iterating over it. So rather than looping through the original characters
of string, we're looping through a modified set of characters as string
is reassigned to new values. This demonstrates immutability of strings
and reassignment.

Strings are immutable, so we're adding the original string to the end of
the string the first time we execute the string = char + string code.

'''
def reverse_string(string):
    new_string = ""
    for char in string:
        new_string = char + new_string

    return new_string

def reverse_string_og(string):
    for char in string:
        string = char + string

    return string

print(reverse_string_og("hello"))

string = "abcde"
for char in string:
    print(char)
    string = ""

print("q3")

'''
The problem here is that we aren't updating the list with the multiplied
result. Lists are mutable so we can update an item in the list, we're just 
missing the assignment line. Instead we're reassigning the temporary variable
item to item *2, then doing nothing with it. We need to reassign it to the index
in the list where the original item came from using enumerate to get the index.
'''
def multiply_list(lst):
    for idx, item in enumerate(lst):
        lst[idx] = item * 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

print("q4")

'''
Calling dict[key] on a key that doesn't exist raises a KeyError. Instead
we could use the dict.get(key) method, which returns None or an optional
default value if the key doesn't exist.
'''

def get_key_value(my_dict, key):
    if my_dict.get(key):
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

print("q5")

'''
The 'in' keyword doesn't work directly for dictionaries as a whole. Instead
you have to check whether the key is in the dictionary.keys() DVO. Also, we
are returning whether the date is already taken, so the True and False conditions
are backwards.
'''
events = {
    "2023-08-13": "Python debugging exercises",
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    print(list(events.keys()))
    if date in list(events.keys()):
        return False

    return True

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

print("Test", "Python debugging exercises" in events)

'''
Well I was totally wrong. 'In' tests for the presence of a key in a dictionary.
No need to check the .keys DVO. 
'''
print("q6")

def append_to_list(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

'''
The problem is that the default object lst = [] is executed once at function
definition and stored in the function object's attributes. The default
is not re-called every function call. So lst already exists in the function's
namespace when the function is called a second time, and it is mutated.

The easiest change for this is to set the default value for lst to None 
and reassign lst to an empty list if the function is called without a lst 
argument.
'''

print("q7")
'''
Here we're shadowing the built-in Python sum function with the function name sum.
So when we call sum in the function, it calls the function itself.
This throws a TypeError as we are calling it with one argument rather than
the 2 expected. It can be fixed by remaning the function.
'''
def a_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(a_sum(numbers, 2) == 20)

print("q8")

'''
This is happening because a shallow copy of the list does not copy the
nested objects referenced by the items in the list. So when we mutate a
nested list, the inner reference still points to the same item and the change is
reflected in the original. It can be fixed by making a deep copy, which
recursively copies every mutable object referenced by the list.
'''
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

print("q9")

'''
This gives us an error that the set size changed during iteration. Because
sets are mutable, changing the set as we are iterating over it results in iterating
over the (current) new set rather than the original set. If the size is
changed, this results in an error - RuntimeError for sets and frozensets, and
less predictable error for lists and dictionaries. This can be fixed
by copying the set and mutating the copy while iterating over the original.
'''
data_set = {1, 2, 3, 4, 5}
data_copy = data_set.copy()
for item in data_set:
    if item % 2 == 0:
        data_copy.remove(item)
print(data_copy)

'''data_set = [1, 2, 3, 4, 5]
for item in data_set:
    if item % 2 == 0:
        print(item, data_set)
        data_copy.remove(item)
print(data_copy)'''

print("q10")

'''
We could instead just add the elements to the list only if they don't already
exist in the list.
'''
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

data_list = []
unique_data = [data_list.append(num) for num in data if num not in data_list]

print(data_list) # order not guaranteed