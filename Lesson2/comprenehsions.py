lst = {'a', 'b', 'b'}
print(list(enumerate(lst)))
      
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

'''flattened_matrix = [ expression for sublist in outerlist
                        if outerlistcondition
                        for expression in sublist
                        if sublistcondition
                    ]
'''

flattened_matrix = [item for row in matrix
                         for item in row]
print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9])

print("q1")

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

ages = 0
for value in munsters.values():
    if value['gender'] == 'male':
        ages += value['age']
print(ages)

age_sum = sum([value['age'] for value in munsters.values() if value['gender'] == 'male'])
print(age_sum)

print("q2")

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
new_lst = []
for item in lst:
    new_lst.append(sorted(item))
print(new_lst)

two_lst = [sorted(item) for item in lst]
print(two_lst)

print("q3")
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
three_lst = [sorted(item, key=str) for item in lst]
print(three_lst)

print("q4")
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
d1 = {item[0]: item[1] for item in lst}
print(d1)

print("q5")
'''
sub-lists are ordered based on the sum of the odd values they contain
    the main list is sorted, the sub-lists stay the same
helper function to sum odd values
feed it into sorted
'''
lst1 = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odd(item):
    print(item)
    return sum([num for num in item if num % 2 != 0])

lst2 = sorted(lst1, key=sum_odd)

print(lst2)

'''
Why this works is hard to grok. Sorted with key is really weird. It acts 
on each element independently. So it's not working on the whole list, just
on the sub-lists one at a time...which is the desired behaviour
'''

print("q6")

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

''' Increase each number by 1
    The list contains 3 dictionary elements
    Output a new list where each value is incremented by 1 in the 3 dictionaries

'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
def increment_value(dicto):
    d2 = {key:dicto[key] + 1 for key in dicto.keys()}
    return d2
l2 = [increment_value(d) for d in lst]
print(l2, lst, sep="\n")

print('q7')
lst7 = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
lst7a = [[num for num in sublist if num % 3 == 0] for sublist in lst7]
print(lst7a)

lst7b = []
for sublist in lst7:
    sublist = [num for num in sublist if num % 3 == 0]
    lst7b.append(sublist)
print(lst7b)

print("q8")
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def color_size0(subdict_list):
    subdict_array = []
    for subdict in subdict_list:
        if subdict['type'] == 'fruit':
            subdict_array.append([color.capitalize() for color in subdict['colors']])
        elif subdict['type'] == 'vegetable':
            Size = subdict['size'].upper()
            subdict_array.append(Size)
    return subdict_array
        
def eat_list0(dict1):
    subdict_list = [dict1[key] for key in dict1.keys()]
    subdict_list = dict1.values()
    return color_size(subdict_list)
    

#print(eat_list(dict1))

def xform_dict(subdict):
    if subdict['type'] == 'fruit':
        return [color.capitalize() for color in subdict['colors']]
    else:
        return subdict['size'].upper()
    
new_dict = [xform_dict(subdict) for subdict in dict1.values()]
print(new_dict)
'''
Takeaways: I need more practice with .items and .values to make that second-nature
Nice job going back to the algorithem when I was getting lost in the weeds
Ok to revert to a loop to figure out the comprehension
'''
'''
dict1 = {'grape': {dict2}, 'carrot': {dict3},...}
first pull out the value for each key in dict1
    this will be a sub-dictionary
    value for subdict in dict
    value is dict1[key]
in the sub-dictionary, pull out the value of the key 'type' and 
    check if it's 'fruit' or 'vegetable'
    value will be sub-dict['type']
if it's fruit
    add capitalized versions of the strings in the list at the value
    of the key 'colors' to the new list
if it's vegetable
    add uppercased version of the string at the value of the key 'size'
    to the new list
'''
print('q9')
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
'''
P: return a list that contains only the dictionaries where all the numbers are even
Input: a list of dictionaries. In each dictionary, the values are lists of integers
Output: a list of dictionaries
Rules:
Ex - None
Im - no blank values. Each value is a list of one or more elements. 
Im - all elements are integers. Keys are letters.
Im - don't return any dictionaries when any element of any value list is odd
D/A:
a list of dictionaries to output
- look at each subdictionary
    for subdict in lst
- in the subdictionary, look at each set of values
    create a new list of values
- the list of values will be a list of integer filled sub-lists
- call a helper function over each element of the values list
    - if any element in any sub-list is odd, continue
        look at each number in each sub-list
        if odd, escape that dictionary
            return one
        otherwise return 0
- go back to main function and add the return value to yes_odds
    if yes_odds still 0 after checking all sublists
        add subdictionary to the new output list
'''
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def check_odd(sub_list):
    has_odds = 0
    for num in sub_list:
        if num % 2 == 1:
            has_odds += 1
    return has_odds

new_lst = []

for subdict in lst:
    yes_odds = 0
    values_list = list(subdict.values())
    for sub_list in values_list:
        yes_odds += check_odd(sub_list)
    if not yes_odds:
        new_lst.append(subdict)

print(new_lst)